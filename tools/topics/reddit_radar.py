#!/usr/bin/env python3
"""Reddit radar via Apify (practicaltools/apify-reddit-api): top posts of the week from topic subreddits.

Reddit's own API needs approval and unauthenticated .json is blocked (403), so we go through Apify.
Reads APIFY_TOKEN from the environment (never store it in the repo). Cost: about $2 per 1,000 posts.
Each subreddit runs as its own call, because one bad subreddit name fails the whole run.
Posts are TOPIC SEEDS only: verify facts by search, rewrite in our words, never repost text or usernames.

Usage: APIFY_TOKEN=... python3 tools/topics/reddit_radar.py [posts_per_sub] [day|week|month]
Output: tools/topics/out/reddit_YYYY-MM-DD.md (+ .json)
"""
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SUBS = {  # sub -> kind (fact = checkable, story = personal/unverified)
    "todayilearned": "fact", "Damnthatsinteresting": "fact", "interestingasfuck": "fact", "BeAmazed": "fact",
    "LifeProTips": "fact", "YouShouldKnow": "fact", "TravelHacks": "fact", "travel": "fact",
    "relationship_advice": "story", "survivinginfidelity": "story",
}
OUT = Path(__file__).parent / "out"


def run(sub, n, period, token):
    body = json.dumps({"startUrls": [{"url": f"https://www.reddit.com/r/{sub}/"}], "sort": "top", "time": period,
                       "maxItems": n, "skipComments": True, "skipCommunity": True}).encode()
    req = urllib.request.Request(
        "https://api.apify.com/v2/acts/practicaltools~apify-reddit-api/run-sync-get-dataset-items?timeout=200",
        data=body, method="POST", headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=230) as r:
        return json.loads(r.read())


def main():
    token = os.environ.get("APIFY_TOKEN") or sys.exit("Set APIFY_TOKEN in the environment.")
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    period = sys.argv[2] if len(sys.argv) > 2 else "week"
    rows = []
    for sub, kind in SUBS.items():
        try:
            for p in run(sub, n, period, token):
                rows.append({"sub": sub, "kind": kind, "title": p.get("title"), "up": p.get("upVotes") or 0,
                             "comments": p.get("numberOfComments") or 0, "url": p.get("url"),
                             "body": (p.get("body") or "")[:400], "video": p.get("isVideo")})
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print("fail", sub, e, file=sys.stderr)
    OUT.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    (OUT / f"reddit_{today}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    lines = [f"# Reddit radar {today} (top {period})", ""]
    for r in sorted(rows, key=lambda r: -r["up"])[:60]:
        lines.append(f"- [{r['kind']}] r/{r['sub']} | {r['up']} up | {r['comments']} comments  \n  {r['title']}  \n  {r['url']}")
    path = OUT / f"reddit_{today}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(path, len(rows))


if __name__ == "__main__":
    main()
