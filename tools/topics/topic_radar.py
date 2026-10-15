#!/usr/bin/env python3
"""Topic radar: pulls fresh health/women's-health stories and papers for carousel topic research.

Sources (all free, no keys): Google News RSS, PubMed E-utilities, Google Trends RSS.
Output: tools/topics/out/YYYY-MM-DD.md  (a digest to pick hooks from; facts still need source check).

Usage: python3 tools/topics/topic_radar.py
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (topic-radar)"}
OUT = Path(__file__).parent / "out"

# What our reader (women 35-65) is afraid of / curious about. Edit freely.
NEWS_QUERIES = [
    # broad, emotional, everyday topics first (the product is bridged in later, NOT used to filter topics)
    "scam warning police", "FBI warning families", "nurse says patients", "doctor warns everyday habit",
    "household item myth debunked", "food label changed ingredients", "grocery store trick",
    "safety tip every woman should know", "teens online parents warning", "retirees money mistake",
    "grandparents grandchildren study", "psychology habit study new", "relationship study new",
    "travel scam tourists warning", "cleaning myth experts", "sleep habit study new",
]
PUBMED_TERMS = [
    "menopause", "perimenopause", "women sleep", "visceral fat women",
    "caffeine health", "hot flashes", "midlife women cognition",
]


def get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def news(q):
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
        {"q": q + " when:7d", "hl": "en-US", "gl": "US", "ceid": "US:en"})
    root = ET.fromstring(get(url))
    for it in root.iter("item"):
        title = html.unescape(it.findtext("title", ""))
        src = it.findtext("source", "")
        yield title, src, it.findtext("link", ""), it.findtext("pubDate", "")


def norm(t):
    t = re.sub(r"\s+-\s+[^-]+$", "", t.lower())  # drop " - Outlet"
    return set(w for w in re.findall(r"[a-z]{4,}", t))


def cluster(items):
    """Group near-duplicate headlines; cluster size = how many outlets ran the story (virality proxy)."""
    clusters = []
    for it in items:
        w = norm(it["title"])
        for c in clusters:
            if len(w & c["words"]) / max(1, min(len(w), len(c["words"]))) >= 0.6:
                c["items"].append(it)
                c["words"] |= w
                break
        else:
            clusters.append({"words": set(w), "items": [it]})
    return clusters


def pubmed(term, days=14, n=5):
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "reldate": days, "datetype": "pdat",
                                "retmax": n, "sort": "date", "retmode": "json"})
    ids = json.loads(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + q))["esearchresult"]["idlist"]
    if not ids:
        return []
    s = json.loads(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" +
                       urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids), "retmode": "json"})))["result"]
    return [(s[i]["title"], s[i]["source"], s[i]["pubdate"], f"https://pubmed.ncbi.nlm.nih.gov/{i}/") for i in ids]


def main():
    OUT.mkdir(exist_ok=True)
    today = dt.date.today().isoformat()
    allnews, seen = [], set()
    for q in NEWS_QUERIES:
        try:
            for title, src, link, pub in news(q):
                if title in seen:
                    continue
                seen.add(title)
                allnews.append({"title": title, "src": src, "link": link, "pub": pub, "q": q})
        except Exception as e:
            print("news fail", q, e, file=sys.stderr)
    cl = sorted(cluster(allnews), key=lambda c: -len({i["src"] for i in c["items"]}))
    lines = [f"# Topic radar {today}", "", "## Stories covered by the most outlets (virality proxy)", ""]
    for c in cl[:15]:
        outlets = sorted({i["src"] for i in c["items"] if i["src"]})
        first = c["items"][0]
        lines.append(f"- **{first['title']}**  \n  outlets: {len(outlets)} ({', '.join(outlets[:5])})  \n  {first['link']}")
    lines += ["", "## Fresh PubMed papers (last 14 days)", ""]
    for t in PUBMED_TERMS:
        try:
            for title, src, pub, link in pubmed(t):
                lines.append(f"- [{t}] {title} | {src} {pub}  \n  {link}")
        except Exception as e:
            print("pubmed fail", t, e, file=sys.stderr)
    path = OUT / f"{today}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(path)
    print("\n".join(lines[:60]))


if __name__ == "__main__":
    main()
