#!/usr/bin/env python3
"""Batch render — Aug 22 2026, 6 reels"""
import sys
sys.path.insert(0, "/home/user/preland")
from render import render_reel
import os

os.makedirs("/home/user/preland/footage/rendered", exist_ok=True)

DATE = "2026-08-22"

BATCH = [
    {
        "clip": "32_18",
        "slug": "baggage-claim-theft",
        "lines": ["Never Leave Your Bag On The Floor", "At Baggage Claim."],
        "cta": "( thieves have a 90-second window ↓ )",
    },
    {
        "clip": "32_12",
        "slug": "fake-taxi-airport",
        "lines": [
            "A driver at the airport exit had my name on a sign.",
            "I never booked a car service.",
            "He knew my hotel, my flight number, and my name.",
        ],
        "cta": None,
    },
    {
        "clip": "32_6",
        "slug": "hotel-two-keys",
        "lines": [
            "I checked into a hotel in Barcelona alone.",
            "The desk gave me one key card.",
            "Three people in the lobby now knew",
            "I was in that room by myself.",
        ],
        "cta": None,
    },
    {
        "clip": "32_13",
        "slug": "cruise-balcony-lock",
        "lines": [
            "My cruise cabin was entered through the balcony.",
            "I was at dinner. The sliding door was unlocked.",
            "What the crew told me — I wish I’d known before.",
        ],
        "cta": None,
    },
    {
        "clip": "32_8",
        "slug": "tokyo-restaurant-scam",
        "lines": [
            "A restaurant in Tokyo handed me a menu with no prices.",
            "I asked. The waiter said prices were on the other side.",
            "The bill for lunch came to $220.",
        ],
        "cta": None,
    },
    {
        "clip": "32_9",
        "slug": "usb-juice-jacking",
        "lines": ["Never Charge Your Phone", "At An Airport USB Station."],
        "cta": "( the FBI has a name for what happens ↓ )",
    },
]

for i, r in enumerate(BATCH, 1):
    print(f"\n[{i}/6] {r['slug']}")
    render_reel(r["clip"], r["slug"], r["lines"], cta=r["cta"], date=DATE)

print("\nDone.")
