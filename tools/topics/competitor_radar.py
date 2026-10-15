#!/usr/bin/env python3
"""Competitor outlier radar via Apify (apify/instagram-scraper).

Reads APIFY_TOKEN from the environment (never store it in the repo).
For each account: pulls the latest N posts, computes the account's median likes, and lists posts that are
>= MIN_RATIO x the median with >= MIN_LIKES. Output: tools/topics/out/competitors_YYYY-MM-DD.md (+ .json).

Note: public data has likes/comments/date/caption only. Shares (sends) are NOT available.
Cost: roughly $1.5-2.3 per 1,000 posts (check the actor's Pricing tab).

Usage: APIFY_TOKEN=... python3 tools/topics/competitor_radar.py [posts_per_account]
"""
import datetime as dt
import json
import os
import statistics as st
import sys
import urllib.request
from pathlib import Path

ACCOUNTS = [
    "elevatemindhq", "mikestartegy1", "withmilaofficial", "seva.gorobets",
    "neiro_gleb", "fit_grandma_rose_", "maks.motivator",
]
MIN_RATIO, MIN_LIKES = 3.0, 1000
OUT = Path(__file__).parent / "out"


def run(accounts, n):
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN in the environment.")
    body = json.dumps({
        "directUrls": [f"https://www.instagram.com/{a}/" for a in accounts],
        "resultsType": "posts", "resultsLimit": n, "addParentData": False,
    }).encode()
    req = urllib.request.Request(
        "https://api.apify.com/v2/acts/apify~instagram-scraper/run-sync-get-dataset-items?timeout=280&memory=2048",
        data=body, method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    posts = run(ACCOUNTS, n)
    OUT.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    slim = [{k: p.get(k) for k in ("ownerUsername", "type", "likesCount", "commentsCount", "timestamp", "url", "caption", "shortCode")}
            for p in posts]
    (OUT / f"competitors_{today}.json").write_text(json.dumps(slim, ensure_ascii=False, indent=1), encoding="utf-8")
    by = {}
    for p in slim:
        by.setdefault(p["ownerUsername"], []).append(p)
    lines = [f"# Competitor outliers {today}", "", "## Accounts", ""]
    scored = []
    for acc, ps in by.items():
        likes = [p["likesCount"] for p in ps if isinstance(p["likesCount"], int) and p["likesCount"] >= 0]
        if not likes:
            lines.append(f"- {acc}: {len(ps)} posts, no public like counts")
            continue
        med = st.median(likes)
        lines.append(f"- {acc}: {len(ps)} posts, median {med:.0f} likes, max {max(likes)}")
        for p in ps:
            lk = p["likesCount"]
            if isinstance(lk, int) and med > 0 and lk >= MIN_LIKES and lk / med >= MIN_RATIO:
                scored.append((lk / med, p, med))
    lines += ["", f"## Outliers (>= {MIN_RATIO:g}x account median and >= {MIN_LIKES} likes)", ""]
    for ratio, p, med in sorted(scored, key=lambda x: -x[0])[:30]:
        cap = (p["caption"] or "").replace("\n", " ")[:260]
        lines.append(f"- **{p['ownerUsername']}** | {p['likesCount']} likes ({ratio:.0f}x) | {p['commentsCount']} comments | {(p['timestamp'] or '')[:10]} | {p['type']}  \n  {cap}  \n  {p['url']}")
    path = OUT / f"competitors_{today}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(path)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
