import os
import json
import hmac
import hashlib
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = os.environ["WEBHOOK_VERIFY_TOKEN"]
PAGE_ACCESS_TOKEN = os.environ["INSTAGRAM_PAGE_ACCESS_TOKEN"]
APP_SECRET = os.environ["META_APP_SECRET"]

KEYWORDS = ["calm"]
PRODUCT_URL = "https://thekiramethod.com/"
GRAPH_API_URL = "https://graph.facebook.com/v21.0"


async def send_message(recipient_id: str, message: dict):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{GRAPH_API_URL}/me/messages",
            params={"access_token": PAGE_ACCESS_TOKEN},
            json={"recipient": {"id": recipient_id}, "message": message},
            timeout=10.0,
        )
        return resp.json()


async def send_first_dm(user_id: str):
    """Step 1 — Opening DM with quick-reply button (as in screenshot 1)."""
    message = {
        "text": (
            "Got you — your free **Calm Guide** is ready \U0001f319\n\n"
            "Tap below and I’ll send you the link."
        ),
        "quick_replies": [
            {
                "content_type": "text",
                "title": "Send me the FREE Calm Guide",
                "payload": "SEND_GUIDE",
            }
        ],
    }
    return await send_message(user_id, message)


async def send_second_dm(user_id: str):
    """Step 2 — DM with link button (as in screenshot 2)."""
    message = {
        "attachment": {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Your Free Calm Guide \U0001f319",
                        "subtitle": (
                            "Simple steps to calm your mind — saved in one quick phone guide.\n\n"
                            "No email. No checkout. Just open it below."
                        ),
                        "buttons": [
                            {
                                "type": "web_url",
                                "url": PRODUCT_URL,
                                "title": "Get the Free Guide",
                            }
                        ],
                    }
                ],
            },
        }
    }
    return await send_message(user_id, message)


def contains_keyword(text: str) -> bool:
    return any(kw in text.lower() for kw in KEYWORDS)


def verify_signature(body: bytes, signature: str) -> bool:
    expected = "sha256=" + hmac.new(
        APP_SECRET.encode(), body, hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)


@app.get("/webhook")
async def verify_webhook(request: Request):
    """Meta webhook verification challenge."""
    params = dict(request.query_params)
    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return PlainTextResponse(params["hub.challenge"])
    raise HTTPException(status_code=403, detail="Invalid verify token")


@app.post("/webhook")
async def handle_webhook(request: Request):
    """Handle incoming Instagram comment and messaging events."""
    body = await request.body()
    signature = request.headers.get("x-hub-signature-256", "")

    if not verify_signature(body, signature):
        raise HTTPException(status_code=403, detail="Invalid signature")

    data = json.loads(body)

    for entry in data.get("entry", []):
        # --- Comment trigger ---
        for change in entry.get("changes", []):
            if change.get("field") == "comments":
                value = change.get("value", {})
                comment_text = value.get("text", "")
                commenter_id = value.get("from", {}).get("id")

                if commenter_id and contains_keyword(comment_text):
                    await send_first_dm(commenter_id)

        # --- Button click (quick reply postback) ---
        for messaging in entry.get("messaging", []):
            sender_id = messaging.get("sender", {}).get("id")
            postback = messaging.get("postback", {})
            quick_reply = messaging.get("message", {}).get("quick_reply", {})

            payload = postback.get("payload") or quick_reply.get("payload")
            if sender_id and payload == "SEND_GUIDE":
                await send_second_dm(sender_id)

    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "running"}
