#!/usr/bin/env python3
"""
Free Travel Safety Card — one-page PDF
Style: matches thekiramethod.com (cream bg, dark text, minimal)
"""
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

pt = 1.0

# ── Fonts ──────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/montserrat"
pdfmetrics.registerFont(TTFont("Druk",         "/tmp/DrukWideBold.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Bold",    f"{FONT_DIR}/Montserrat-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mont-SemiBold",f"{FONT_DIR}/Montserrat-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Regular", f"{FONT_DIR}/Montserrat-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Light",   f"{FONT_DIR}/Montserrat-Light.ttf"))

# ── Palette ─────────────────────────────────────────────────────────────────
C_CREAM   = HexColor("#f8f6f0")   # exact site background
C_INK     = HexColor("#1a1a1a")   # near-black text
C_NAVY    = HexColor("#1C2A34")   # dark navy accent (headers, rule)
C_COPPER  = HexColor("#a85c2a")   # copper accent (kicker / highlight)
C_RULE    = HexColor("#d4cfc6")   # soft divider line

# ── Page ────────────────────────────────────────────────────────────────────
OUT = "/home/user/preland/traveler-safety-card.pdf"
W, H = A5  # 419.5 × 595.3 pt (~148×210mm)
MARGIN_X = 32 * pt
MARGIN_TOP = 36 * pt
MARGIN_BOT = 28 * pt
COL_W = W - MARGIN_X * 2

TIPS = [
    {
        "num": "01",
        "title": "Baggage Claim",
        "body": (
            "Thieves work in pairs and time your distraction. "
            "Keep your carry-on between your legs — never on the floor. "
            "Watch the belt, not your phone, until your bag is in your hand."
        ),
    },
    {
        "num": "02",
        "title": "Airport Taxi",
        "body": (
            "A driver with your name on a sign is not proof they're legitimate. "
            "Only ride cars you booked yourself through a verified app before landing. "
            "Screenshot the driver name and plate before you walk out."
        ),
    },
    {
        "num": "03",
        "title": "Hotel Check-In",
        "body": (
            "One key card tells everyone nearby you're traveling alone. "
            "Always ask for two keys — the desk assumes a companion is coming. "
            "If your room number is said out loud, ask to be moved."
        ),
    },
    {
        "num": "04",
        "title": "Cruise Cabin",
        "body": (
            "The main latch doesn't fully lock your balcony door. "
            "Find the small flip lock at the top of the sliding door frame. "
            "Check it every time you leave the cabin. Takes 3 seconds."
        ),
    },
    {
        "num": "05",
        "title": "USB Charging",
        "body": (
            "Public USB ports open a data channel — not just power. "
            "Use a USB data blocker ($7, fits on a keychain) or a wall outlet. "
            "If your phone asks 'Trust this device?' — always tap No."
        ),
    },
]


def draw_card(c):
    # Background
    c.setFillColor(C_CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    y = H - MARGIN_TOP

    # ── Top kicker ──────────────────────────────────────────────────────────
    c.setFont("Mont-SemiBold", 7.5 * pt)
    c.setFillColor(C_COPPER)
    kicker = "FREE 1-PAGE GUIDE  ·  KIRA METHOD"
    c.drawCentredString(W / 2, y, kicker)
    y -= 14 * pt

    # ── Thin top rule ────────────────────────────────────────────────────────
    c.setStrokeColor(C_RULE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, y, W - MARGIN_X, y)
    y -= 18 * pt

    # ── Hero title ───────────────────────────────────────────────────────────
    c.setFont("Druk", 22 * pt)
    c.setFillColor(C_NAVY)
    c.drawCentredString(W / 2, y, "THE TRAVELER'S")
    y -= 26 * pt
    c.drawCentredString(W / 2, y, "SAFETY CARD")
    y -= 10 * pt

    # ── Subtitle ─────────────────────────────────────────────────────────────
    c.setFont("Mont-Regular", 8.5 * pt)
    c.setFillColor(C_INK)
    sub = "5 things to check before you trust any situation abroad."
    c.drawCentredString(W / 2, y, sub)
    y -= 18 * pt

    # ── Rule ─────────────────────────────────────────────────────────────────
    c.setStrokeColor(C_RULE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, y, W - MARGIN_X, y)
    y -= 20 * pt

    # ── Tips ─────────────────────────────────────────────────────────────────
    NUM_W   = 28 * pt
    GAP     = 8 * pt
    TEXT_W  = COL_W - NUM_W - GAP
    LINE_H  = 11 * pt
    TITLE_SIZE = 10 * pt
    BODY_SIZE  = 8 * pt
    BLOCK_GAP  = 14 * pt

    for tip in TIPS:
        # Number
        c.setFont("Mont-Bold", 18 * pt)
        c.setFillColor(C_RULE)
        c.drawString(MARGIN_X, y - 4 * pt, tip["num"])

        # Title
        tx = MARGIN_X + NUM_W + GAP
        c.setFont("Mont-Bold", TITLE_SIZE)
        c.setFillColor(C_NAVY)
        c.drawString(tx, y, tip["title"])
        y -= LINE_H * 1.1

        # Body — manual word wrap
        words = tip["body"].split()
        c.setFont("Mont-Regular", BODY_SIZE)
        c.setFillColor(C_INK)
        line = ""
        for word in words:
            test = (line + " " + word).strip()
            if c.stringWidth(test, "Mont-Regular", BODY_SIZE) <= TEXT_W:
                line = test
            else:
                if line:
                    c.drawString(tx, y, line)
                    y -= LINE_H * 0.9
                line = word
        if line:
            c.drawString(tx, y, line)
            y -= LINE_H * 0.9

        y -= BLOCK_GAP

        # Divider (except after last)
        if tip != TIPS[-1]:
            c.setStrokeColor(C_RULE)
            c.setLineWidth(0.3)
            c.line(MARGIN_X, y + 6 * pt, W - MARGIN_X, y + 6 * pt)
            y -= 8 * pt

    # ── Bottom rule ──────────────────────────────────────────────────────────
    y = MARGIN_BOT + 42 * pt
    c.setStrokeColor(C_RULE)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, y, W - MARGIN_X, y)
    y -= 13 * pt

    # ── CTA box ──────────────────────────────────────────────────────────────
    c.setFont("Mont-SemiBold", 7.5 * pt)
    c.setFillColor(C_COPPER)
    c.drawCentredString(W / 2, y, "SAVE THIS CARD BEFORE YOUR NEXT TRIP")
    y -= 11 * pt

    c.setFont("Mont-Regular", 7.5 * pt)
    c.setFillColor(C_INK)
    c.drawCentredString(W / 2, y, "thekiramethod.com  ·  @thekiramethod")
    y -= 18 * pt

    # ── Upsell CTA ───────────────────────────────────────────────────────────
    c.setStrokeColor(C_COPPER)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, y, W - MARGIN_X, y)
    y -= 13 * pt

    c.setFont("Mont-SemiBold", 7.5 * pt)
    c.setFillColor(C_COPPER)
    c.drawCentredString(W / 2, y, "WANT THE FULL TRAVEL SAFETY GUIDE?")
    y -= 11 * pt

    c.setFont("Mont-Regular", 7.5 * pt)
    c.setFillColor(C_INK)
    c.drawCentredString(W / 2, y, "47 countries · 8 chapters · instant download  →  $14.90")
    y -= 10 * pt

    c.setFont("Mont-SemiBold", 7 * pt)
    c.setFillColor(C_NAVY)
    url = "thekiramethod.com/guide"
    c.drawCentredString(W / 2, y, url)


def main():
    c = canvas.Canvas(OUT, pagesize=A5)
    draw_card(c)
    c.showPage()
    c.save()
    size = os.path.getsize(OUT) / 1024
    print(f"✅  {OUT}  ({size:.0f} KB)")


if __name__ == "__main__":
    main()
