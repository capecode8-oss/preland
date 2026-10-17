#!/usr/bin/env python3
"""Generate missing cover scenes with Nano Banana 2 Lite (DeepInfra) from a canon face reference of the recurring character.

  python3 tools/carousel/cover_gen.py            # generate all scenes that are not generated yet
  python3 tools/carousel/cover_gen.py <id> ...   # (re)generate only these ids

Writes graded 1080x1350 jpgs to assets/covers/gen/ and assets/covers/manifest_gen.json (cover_bank.pick reads both).
Prompt method (2026 community practice): action instead of pose, gaze away from camera, slightly imperfect framing,
2-3 specific traits and props, natural skin texture, lens + light instead of "ultra realistic", explicit negatives,
fixed character block + canon face reference in every call.
"""
import base64, json, os, shutil, subprocess, sys, tempfile, threading
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cover_bank import grade, OUT, ROOT, W, H  # noqa: E402

MODEL = os.environ.get("COVER_GEN_MODEL", "nano-banana-2-lite")
GEN = OUT / "gen"
MANIFEST_GEN = OUT / "manifest_gen.json"
REF = OUT / "_ref" / "kira_face.jpg"
KEY = os.environ.get("DEEPINFRA_KEY") or open("/tmp/.dik").read().strip()

CHARACTER = ("The woman is the person in the reference photo: exactly the same face and age (early to mid 40s), "
             "dark brown wavy shoulder-length hair, natural skin with fine lines and a few freckles.")
STYLE = ("Candid photograph, 35mm lens, available light, natural skin texture, a few stray hairs, "
         "slightly imperfect framing as if grabbed quickly, warm natural color. "
         "Full-bleed photograph that continues naturally to all four edges: no borders, no white bars, no frames, no letterboxing. "
         "No text, no logos, no watermark, no airbrushed skin, no stock-photo smile.")

# id, products, tags, scene prompt (action + setting + light + shot). CHARACTER and STYLE are added automatically.
SCENES = [
    # ---------------- GLOW ----------------
    ("g_mirror_side", ["glow"], ["mirror", "face", "morning", "worried"],
     "Side-on shot of her leaning on both hands at a bathroom sink, studying her own face in the mirror, one eyebrow slightly raised, towel on her shoulder, soft morning window light on the tiles."),
    ("g_bed_3am", ["glow"], ["bedroom", "3am", "sleep", "tired"],
     "She sits on the edge of a rumpled bed with her feet on the rug, phone in her hand showing 3:07 in large digits, warm bedside lamp lighting the room clearly, blanket pushed aside, looking at the phone not the camera."),
    ("g_pill_label", ["glow"], ["supplements", "label", "reading", "hands"],
     "Close shot of her hands holding a supplement bottle at the kitchen counter, reading glasses pushed up into her hair, squinting at the small print on the label, bright daylight from the window."),
    ("g_doctor_waiting", ["glow"], ["doctor", "waiting", "clipboard"],
     "In a clinic waiting room she fills in a form on a clipboard, pen paused mid-line, glancing sideways toward a door out of frame, pale walls, daylight through a big window, chairs blurred behind her."),
    ("g_waistband", ["glow"], ["belly", "waist", "jeans"],
     "Shot from chin down, she stands in a bright bedroom pulling at the waistband of her denim jeans with a thumb, loose cotton shirt, morning light, her face is partly cropped by the top of the frame."),
    ("g_park_walk", ["glow"], ["walking", "park", "autumn"],
     "Caught mid-stride on a leafy park path in autumn, glancing down at her smartwatch, leaves blurred in motion at the edges, cardigan open, soft overcast daylight."),
    ("g_grocery_label", ["glow"], ["grocery", "label", "food"],
     "In a supermarket aisle she holds a cereal box at arm's length reading the nutrition label with narrowed eyes, shopping basket on her elbow, bright store lighting, colorful shelves softly blurred."),
    ("g_couch_laptop", ["glow"], ["tired", "laptop", "couch", "afternoon"],
     "Afternoon on the couch under a knitted blanket with a laptop on her knees, pinching the bridge of her nose with eyes closed, half-drunk cup of tea on the arm of the sofa, sunlight across the room."),
    ("g_tea_window", ["glow"], ["tea", "window", "calm", "morning"],
     "Over-the-shoulder view of her pouring tea into a mug at a window, steam rising, looking out at a garden, face in soft profile, sleepy hair, bright cool morning light."),
    ("g_car_breath", ["glow"], ["car", "stress", "breathing", "eyes-closed"],
     "Parked in her car in the afternoon sun, both hands on the steering wheel, eyes closed, taking a slow deep breath, shopping bags on the passenger seat, light flaring through the windshield."),
    ("g_cafe_friends", ["glow"], ["cafe", "friends", "window", "comparison"],
     "Photographed through a cafe window from the street: she sits alone at a small table with a half-smile watching a group of laughing friends at the next table, reflection of the street on the glass, daylight."),
    ("g_desk_clock_coffee", ["glow"], ["coffee", "caffeine", "clock", "desk"],
     "Close detail at a home desk: her hand wrapped around a coffee mug beside a small analog clock reading two o'clock, laptop and a notepad blurred behind, her face just visible at the edge of the frame looking at the screen."),
    ("g_temples_desk", ["glow"], ["headache", "desk", "stress", "tired"],
     "Messy bun, fingertips pressed to both temples at a cluttered home office desk, sticky notes and a mug in front of her, eyes shut, afternoon window light from the left."),
    ("g_fridge_open", ["glow"], ["fridge", "kitchen", "snack", "hesitation"],
     "She stands at an open refrigerator in a bright kitchen, one hand on the door, the other hovering undecided over a shelf, cool fridge light on her face, glancing at the camera with a guilty half-smile."),
    ("g_tub_phone", ["glow"], ["bathroom", "phone", "steps", "tired"],
     "Sitting on the edge of a bathtub in a white bathroom, scrolling a health app on her phone with a tired small smile, bathrobe, daylight from a frosted window."),
    ("g_back_stretch", ["glow"], ["yoga", "stretch", "back", "living-room"],
     "Mid-stretch on a yoga mat in a sunlit living room, one hand pressed to her lower back, wincing slightly, leggings and a loose tee, plants and a window behind her."),
    ("g_notebook_log", ["glow"], ["notebook", "writing", "log", "desk"],
     "Over-the-shoulder shot of her writing in a notebook, pen mid-sentence, looking up at a window with a thoughtful expression, handwritten dated list on the page, morning light, coffee untouched."),
    ("g_face_honest", ["glow"], ["face", "serious", "close"],
     "Close portrait with strong morning sun hitting one side of her face, hair messy, no makeup, an honest tired look straight into the camera, shallow depth of field, plain wall behind her."),
    ("g_lab_report", ["glow"], ["lab", "report", "reading", "kitchen"],
     "At a kitchen counter she follows one line of a printed lab report with her finger, reading glasses on, brows drawn together, folder and pen beside her, bright daylight."),
    ("g_morning_robe", ["glow"], ["morning", "robe", "stairs", "sleepy"],
     "Coming down a staircase in a robe, one hand on the banister, looking down at her feet, squinting in the morning sun from a hallway window, hair unbrushed."),
    # ---------------- SAFETY ----------------
    ("s_rental_walkaround", ["safety"], ["rental", "car", "phone", "filming"],
     "Crouching beside the front bumper of a white rental car in a sunny parking lot, filming a small scratch with her phone, keys in her other hand, sunglasses pushed up, midday light."),
    ("s_hotel_safe", ["safety"], ["hotel", "safe", "closet", "passport"],
     "In a hotel room closet she taps a code into a small in-room safe, passport in her other hand, glancing back over her shoulder toward the door, daylight through sheer curtains."),
    ("s_hotel_corridor", ["safety"], ["hotel", "corridor", "keycard", "luggage"],
     "Wide shot in a hotel corridor, she pulls a carry-on and checks a key card against the room numbers on the doors, mid-step, carpet runner leading away, warm light from wall sconces."),
    ("s_desk_passport", ["safety"], ["hotel", "reception", "passport", "counter"],
     "Her face in sharp profile as she slides a passport across a marble front-desk counter, the clerk's hand just entering the frame, brass bell and flowers blurred, bright lobby light."),
    ("s_vendor_bracelet", ["safety"], ["street", "vendor", "bracelet", "offer", "scam"],
     "POV from the vendor's side: a stranger's hand holds out a colorful woven bracelet toward her in a sunny Mediterranean old-town street, she steps back with a raised palm and a polite uncomfortable smile."),
    ("s_photo_offer", ["safety"], ["street", "photo", "phone", "offer", "scam"],
     "Over her shoulder: a friendly stranger's hands reach for her phone offering to take her picture in front of a famous fountain, she holds the phone against her chest hesitating, tourists blurred around, bright sun."),
    ("s_cruise_sanitizer", ["safety"], ["cruise", "buffet", "sanitizer", "doubt"],
     "At a cruise ship buffet entrance she stands by a wall hand-sanitizer dispenser with an empty plate in one hand, eyeing the dispenser doubtfully, white and blue ship interior, bright light."),
    ("s_port_hurry", ["safety"], ["cruise", "port", "watch", "hurry"],
     "On a sunny pier, she hurries toward a huge cruise ship while checking her wristwatch, tote bag swinging, shore-excursion crowd blurred behind, a little out of breath."),
    ("s_arrivals_tout", ["safety"], ["airport", "arrivals", "taxi", "tout"],
     "In an airport arrivals hall she walks past while looking at her phone, sharp in the foreground; behind her a man in a jacket gestures toward her bag offering a taxi, travelers blurred, bright terminal light."),
    ("s_rideshare_plate", ["safety"], ["rideshare", "plate", "curb", "phone"],
     "On a city curb she leans slightly to read a license plate and compares it to her phone screen before opening the car door, a silver sedan idling beside her, street trees, daylight."),
    ("s_security_tray", ["safety"], ["airport", "security", "tray", "laptop"],
     "At airport security she places a laptop into a gray tray while looking back at her bag behind her, conveyor belt and other travelers blurred, cool bright terminal light."),
    ("s_atm_cover", ["safety"], ["atm", "pin", "street", "money"],
     "Behind and beside her at a street ATM in a European old town, she shields the keypad with her left hand while typing with the right, coat collar up, a passer-by blurred behind, overcast daylight."),
    ("s_exchange_board", ["safety"], ["exchange", "rates", "money", "receipt"],
     "At a currency exchange booth she squints at a glowing rate board above the counter with a printed receipt in her hand, comparing numbers, slightly worried look, bright fluorescent light."),
    ("s_lobby_wifi", ["safety"], ["wifi", "lobby", "laptop", "hesitation"],
     "Seated in a hotel lobby armchair with a laptop, a framed free-WiFi sign blurred behind her, one finger hovering over the trackpad, wary sideways glance, soft window light."),
    ("s_metro_bag", ["safety"], ["metro", "crowd", "bag", "pickpocket"],
     "In a crowded metro car she hugs her crossbody bag in front of her with both arms, eyes scanning the faces around her, commuters blurred, wide angle, cool fluorescent light with a warm window glow."),
    ("s_bill_pen", ["safety"], ["restaurant", "bill", "pen", "money"],
     "At a restaurant table she taps a pen on one line of the printed bill, brows lowered, a waiter blurred in the background, plates and glasses on a checkered cloth, warm afternoon light."),
    ("s_passport_zip", ["safety"], ["passport", "pocket", "hands", "jacket"],
     "Close on her hands sliding a passport into an inner zip pocket of a travel jacket, face cropped at the lips, bright airport windows behind, quick motion slightly soft."),
    ("s_gate_delay", ["safety"], ["airport", "gate", "delay", "boarding-pass"],
     "Seated at a boarding gate holding a boarding pass, looking up at a departures screen with a delayed flight, tired expression, suitcase beside her, big terminal windows with daylight."),
    ("s_bed_contents", ["safety"], ["hotel", "bed", "documents", "phone", "photo"],
     "Top-down angle on a hotel bed: passport, cash and a necklace laid out on the white duvet, her hands photographing them with a phone, shadow of her head in the corner, bright daylight."),
    ("s_balcony_morning", ["safety"], ["hotel", "balcony", "morning", "calm"],
     "Leaning on a hotel balcony railing in the morning with a coffee cup, looking out over rooftops of an old town, relaxed, bathrobe, bright soft light, back and side of her face visible."),
    ("s_market_crowd", ["safety"], ["market", "crowd", "push", "street"],
     "Low angle in a packed tourist market, she pushes forward through the crowd holding her bag tight, vendors' hands waving goods around the frame edges, strong sun and awning shadows."),
    ("s_elevator_mirror", ["safety"], ["hotel", "elevator", "mirror", "tired"],
     "Reflection in a hotel elevator mirror: she leans against the wall, tired after travel, room key card between her fingers, brass doors and floor numbers, warm light."),
    ("s_curb_luggage", ["safety"], ["airport", "curb", "luggage", "taxi"],
     "At the airport curb a driver's hands lift her suitcase toward a taxi trunk while she looks at him suspiciously and keeps one hand on her bag strap, bright midday sun, cars blurred."),
]


def trim_borders(img, max_trim=40):
    """Cut thin black/white letterbox borders the model sometimes adds, then rescale back to W x H."""
    import numpy as np
    a = np.asarray(img.convert("L")).astype(float)

    def edge(vals):
        k = 0
        while k < max_trim and (vals[k] < 14 or vals[k] > 247):
            k += 1
        return k
    t, b = edge(a.mean(axis=1)), edge(a.mean(axis=1)[::-1])
    l, r = edge(a.mean(axis=0)), edge(a.mean(axis=0)[::-1])
    if t or b or l or r:
        img = img.crop((l, t, img.width - r, img.height - b)).resize((W, H), Image.LANCZOS)
    return img


def ensure_ref():
    if REF.exists():
        return
    REF.parent.mkdir(parents=True, exist_ok=True)
    ff = shutil.which("ffmpeg")
    if not ff:
        import imageio_ffmpeg
        ff = imageio_ffmpeg.get_ffmpeg_exe()
    tmp = tempfile.mktemp(suffix=".jpg")
    subprocess.run([ff, "-y", "-loglevel", "error", "-ss", "1", "-i", str(ROOT / "footage/general/face_3.mp4"), "-vframes", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB")
    im.resize((768, int(768 * im.height / im.width))).save(REF, quality=92)


def _uri():
    buf = BytesIO()
    Image.open(REF).convert("RGB").save(buf, "JPEG", quality=92)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def gen_one(spec, uri, retries=2):
    sid, products, tags, scene = spec
    prompt = f"{CHARACTER} {scene} {STYLE}"
    for a in range(retries + 1):
        try:
            r = requests.post(f"https://api.deepinfra.com/v1/inference/google/{MODEL}",
                              headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
                              json={"prompt": prompt, "image": uri, "aspect_ratio": "4:5"}, timeout=300)
            if r.status_code != 200:
                raise RuntimeError(r.text[:200])
            j = r.json()
            s = j["images"][0]
            img = Image.open(BytesIO(base64.b64decode(s.split(",")[-1]))).convert("RGB")
            img = trim_borders(img.resize((W, H), Image.LANCZOS))
            img = grade(img)
            GEN.mkdir(parents=True, exist_ok=True)
            img.save(GEN / f"{sid}.jpg", quality=92)
            cost = (j.get("inference_status") or {}).get("cost") or 0
            return dict(id=sid, file=f"gen/{sid}.jpg", source=f"generated:{MODEL}", products=products, tags=tags, prompt=scene), cost
        except Exception as e:
            err = e
    print("FAILED", sid, err)
    return None, 0


def main(ids):
    if not os.environ.get("ALLOW_IMAGE_GEN"):
        raise SystemExit("Image generation is disabled (saves money). Set ALLOW_IMAGE_GEN=1 only when the owner explicitly asks.")
    ensure_ref()
    uri = _uri()
    done = {m["id"]: m for m in json.loads(MANIFEST_GEN.read_text())} if MANIFEST_GEN.exists() else {}
    todo = [s for s in SCENES if (s[0] in ids if ids else s[0] not in done)]
    print(len(todo), "scenes to generate with", MODEL)
    total = 0.0
    lock = threading.Lock()
    with ThreadPoolExecutor(max_workers=4) as ex:
        for entry, cost in ex.map(lambda s: gen_one(s, uri), todo):
            if entry:
                with lock:
                    done[entry["id"]] = entry
                    total += cost
    order = {s[0]: i for i, s in enumerate(SCENES)}
    MANIFEST_GEN.write_text(json.dumps(sorted(done.values(), key=lambda m: order.get(m["id"], 999)), indent=1), encoding="utf-8")
    print(f"ok: {len(done)} generated in manifest, cost this run ${total:.3f}")


if __name__ == "__main__":
    main(set(sys.argv[1:]))
