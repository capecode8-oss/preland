#!/usr/bin/env python3
"""
Smart Traveler's Cheat Sheet — Free Lead Magnet PDF
Premium minimal design, Montserrat fonts, ReportLab Platypus
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
pt = 1.0  # 1pt = 1 reportlab unit
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

# ─── FONTS ────────────────────────────────────────────────────────────────────
FONT_DIR = "/usr/share/fonts/truetype/montserrat"

pdfmetrics.registerFont(TTFont("Mont-Black",    f"{FONT_DIR}/Montserrat-Black.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Bold",     f"{FONT_DIR}/Montserrat-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Mont-SemiBold", f"{FONT_DIR}/Montserrat-SemiBold.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Regular",  f"{FONT_DIR}/Montserrat-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Light",    f"{FONT_DIR}/Montserrat-Light.ttf"))
pdfmetrics.registerFont(TTFont("Mont-Italic",   f"{FONT_DIR}/Montserrat-Italic.ttf"))

# ─── COLORS ───────────────────────────────────────────────────────────────────
C_GRAPHITE = colors.HexColor("#1A1F2C")
C_INDIGO   = colors.HexColor("#2A4365")
C_CREAM    = colors.HexColor("#F7FAFC")
C_RULE     = colors.HexColor("#E2E8F0")
C_COPPER   = colors.HexColor("#A85C2A")
C_MUTED    = colors.HexColor("#718096")
C_WHITE    = colors.white

MARGIN = 2.5 * cm
PAGE_W, PAGE_H = A4

# ─── HEADER / FOOTER CANVAS ───────────────────────────────────────────────────
class NumberedCanvas:
    """Two-pass canvas for page X of Y footers."""
    def __init__(self, filename, **kw):
        from reportlab.pdfgen import canvas
        self._pages = []
        self._doc_filename = filename
        self._kw = kw

    def beginForm(self, *args): pass
    def endForm(self, *args): pass

from reportlab.pdfgen import canvas as pdfcanvas

class MyDocTemplate(SimpleDocTemplate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._page_count = 0

    def handle_pageEnd(self):
        self._page_count = self.page
        super().handle_pageEnd()

    def afterPage(self):
        pass

def on_later_page(canvas, doc):
    """Header line + footer page number on pages 2+."""
    canvas.saveState()
    # Header rule
    canvas.setStrokeColor(C_RULE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, PAGE_H - MARGIN + 6*pt,
                PAGE_W - MARGIN, PAGE_H - MARGIN + 6*pt)
    # Header label
    canvas.setFont("Mont-Light", 7)
    canvas.setFillColor(C_MUTED)
    canvas.drawString(MARGIN, PAGE_H - MARGIN + 9*pt,
                      "THE SMART TRAVELER'S CHEAT SHEET  ·  @thekiramethod")
    # Footer page number
    canvas.setFont("Mont-Regular", 8)
    canvas.drawRightString(PAGE_W - MARGIN, MARGIN - 14*pt,
                           f"Page {doc.page}")
    canvas.restoreState()

def on_cover_page(canvas, doc):
    """Cover: no header/footer, draw full background."""
    canvas.saveState()
    # Thin bottom accent line
    canvas.setStrokeColor(C_COPPER)
    canvas.setLineWidth(1)
    canvas.line(MARGIN, MARGIN - 8*pt, PAGE_W - MARGIN, MARGIN - 8*pt)
    canvas.restoreState()

# ─── STYLES ───────────────────────────────────────────────────────────────────
def make_styles():
    s = {}
    s["cover_title"] = ParagraphStyle(
        "cover_title",
        fontName="Mont-Black",
        fontSize=38,
        leading=44,
        textColor=C_GRAPHITE,
        alignment=TA_CENTER,
        spaceAfter=16,
    )
    s["cover_sub"] = ParagraphStyle(
        "cover_sub",
        fontName="Mont-Light",
        fontSize=14,
        leading=20,
        textColor=C_INDIGO,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    s["cover_brand"] = ParagraphStyle(
        "cover_brand",
        fontName="Mont-Regular",
        fontSize=9,
        leading=14,
        textColor=C_MUTED,
        alignment=TA_CENTER,
    )
    s["section_label"] = ParagraphStyle(
        "section_label",
        fontName="Mont-SemiBold",
        fontSize=8,
        leading=12,
        textColor=C_COPPER,
        alignment=TA_LEFT,
        spaceAfter=4,
        spaceBefore=24,
        letterSpacing=1.4,
    )
    s["tip_num"] = ParagraphStyle(
        "tip_num",
        fontName="Mont-Black",
        fontSize=28,
        leading=32,
        textColor=C_RULE,
        alignment=TA_LEFT,
    )
    s["tip_head"] = ParagraphStyle(
        "tip_head",
        fontName="Mont-Bold",
        fontSize=13,
        leading=18,
        textColor=C_GRAPHITE,
        alignment=TA_LEFT,
        spaceAfter=5,
    )
    s["body"] = ParagraphStyle(
        "body",
        fontName="Mont-Regular",
        fontSize=10,
        leading=16,
        textColor=C_GRAPHITE,
        alignment=TA_LEFT,
        spaceAfter=10,
    )
    s["body_light"] = ParagraphStyle(
        "body_light",
        fontName="Mont-Light",
        fontSize=10,
        leading=16,
        textColor=C_GRAPHITE,
        alignment=TA_LEFT,
        spaceAfter=8,
    )
    s["callout_text"] = ParagraphStyle(
        "callout_text",
        fontName="Mont-SemiBold",
        fontSize=10,
        leading=15,
        textColor=C_INDIGO,
        alignment=TA_LEFT,
    )
    s["upsell_head"] = ParagraphStyle(
        "upsell_head",
        fontName="Mont-Black",
        fontSize=18,
        leading=24,
        textColor=C_WHITE,
        alignment=TA_CENTER,
        spaceAfter=10,
    )
    s["upsell_body"] = ParagraphStyle(
        "upsell_body",
        fontName="Mont-Light",
        fontSize=10,
        leading=16,
        textColor=C_WHITE,
        alignment=TA_CENTER,
        spaceAfter=14,
    )
    s["upsell_price"] = ParagraphStyle(
        "upsell_price",
        fontName="Mont-Black",
        fontSize=28,
        leading=34,
        textColor=C_COPPER,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    s["upsell_btn"] = ParagraphStyle(
        "upsell_btn",
        fontName="Mont-SemiBold",
        fontSize=11,
        leading=16,
        textColor=C_WHITE,
        alignment=TA_CENTER,
    )
    s["footer_note"] = ParagraphStyle(
        "footer_note",
        fontName="Mont-Light",
        fontSize=7.5,
        leading=11,
        textColor=C_MUTED,
        alignment=TA_CENTER,
    )
    return s

# ─── CALLOUT BOX ──────────────────────────────────────────────────────────────
def callout(text, style):
    """Left-accented callout box in cream background."""
    p = Paragraph(text, style["callout_text"])
    tbl = Table([[p]], colWidths=[PAGE_W - 2*MARGIN - 20*pt])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_CREAM),
        ("LEFTPADDING",  (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 14),
        ("TOPPADDING",   (0,0), (-1,-1), 12),
        ("BOTTOMPADDING",(0,0), (-1,-1), 12),
        ("LINEAFTER",    (0,0), (0,-1), 0, C_WHITE),  # no right line
        ("LINEBEFORE",   (0,0), (0,-1), 3, C_COPPER),
        ("BOX",          (0,0), (-1,-1), 0.5, C_RULE),
    ]))
    return tbl

# ─── TIP BLOCK ────────────────────────────────────────────────────────────────
def tip_block(num, category, headline, body_text, style):
    """One tip: big number + category label left, headline + body right."""
    num_para = Paragraph(str(num).zfill(2), style["tip_num"])
    cat_para = Paragraph(category.upper(), ParagraphStyle(
        "cat", fontName="Mont-SemiBold", fontSize=7, leading=10,
        textColor=C_COPPER, letterSpacing=1.2
    ))
    head_para = Paragraph(headline, style["tip_head"])
    body_para = Paragraph(body_text, style["body_light"])

    left_col  = [num_para, Spacer(1, 2), cat_para]
    right_col = [head_para, body_para]

    left_w  = 52
    right_w = PAGE_W - 2*MARGIN - left_w - 12

    tbl = Table(
        [[left_col, right_col]],
        colWidths=[left_w, right_w],
    )
    tbl.setStyle(TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (0,-1), 12),
    ]))

    rule = HRFlowable(width="100%", thickness=0.5, color=C_RULE,
                      spaceAfter=14, spaceBefore=14)
    return KeepTogether([tbl, rule])

# ─── UPSELL BLOCK ─────────────────────────────────────────────────────────────
def upsell_block(style):
    """Dark full-width upsell for paid product."""
    content = [
        Spacer(1, 20),
        Paragraph("Want the full picture?", style["upsell_body"]),
        Paragraph("The Solo Traveler's\nSafety Field Guide", style["upsell_head"]),
        Spacer(1, 6),
        Paragraph(
            "7 chapters. Hotels, airports, cruises, digital safety, money traps.\n"
            "Printable checklist inside — fits in your passport holder.",
            style["upsell_body"]
        ),
        Spacer(1, 10),
        Paragraph("$14.90", style["upsell_price"]),
        Spacer(1, 4),
        Paragraph(
            "thekiramethod.com/guide",
            ParagraphStyle("link", fontName="Mont-SemiBold", fontSize=10,
                           leading=14, textColor=C_COPPER, alignment=TA_CENTER)
        ),
        Spacer(1, 20),
    ]

    inner = Table([[content]], colWidths=[PAGE_W - 2*MARGIN])
    inner.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), C_GRAPHITE),
        ("LEFTPADDING",   (0,0), (-1,-1), 28),
        ("RIGHTPADDING",  (0,0), (-1,-1), 28),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return inner

# ─── BUILD PDF ────────────────────────────────────────────────────────────────
def build():
    out = "/home/user/preland/smart-traveler-cheat-sheet.pdf"
    doc = SimpleDocTemplate(
        out,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN + 10*pt,
        title="The Smart Traveler's Cheat Sheet",
        author="@thekiramethod",
    )

    S = make_styles()
    story = []

    # ══════════════════════════════════════════════════════
    # PAGE 1 — COVER
    # ══════════════════════════════════════════════════════
    story.append(Spacer(1, 5.5*cm))
    story.append(Paragraph("THE SMART TRAVELER'S", S["cover_title"]))
    story.append(Paragraph("CHEAT SHEET", ParagraphStyle(
        "ct2", fontName="Mont-Black", fontSize=38, leading=44,
        textColor=C_COPPER, alignment=TA_CENTER, spaceAfter=28
    )))
    story.append(HRFlowable(width=80, thickness=1.5, color=C_COPPER,
                             hAlign="CENTER", spaceAfter=28))
    story.append(Paragraph(
        "10 things most travelers learn the hard way.\nYou don't have to.",
        S["cover_sub"]
    ))
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("Airports · Hotels · Cruise Ships · Food · Money · Health",
                            ParagraphStyle("topics", fontName="Mont-Light", fontSize=9,
                                           leading=14, textColor=C_MUTED,
                                           alignment=TA_CENTER, spaceAfter=6)))
    story.append(Spacer(1, 5*cm))
    story.append(Paragraph("Free guide by @thekiramethod · 2026", S["cover_brand"]))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════
    # PAGE 2 — INTRO
    # ══════════════════════════════════════════════════════
    story.append(Spacer(1, 10))
    story.append(Paragraph("WHY THIS EXISTS", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(Paragraph(
        "Most travel advice is obvious. \"Keep your valuables safe.\" Okay, but <i>how</i>?",
        S["body"]
    ))
    story.append(Paragraph(
        "This cheat sheet is different. Every tip here is specific. You can use it on your next trip, starting today.",
        S["body"]
    ))
    story.append(callout(
        "These 10 things took me years of travel to learn. Some of them I learned the hard way. "
        "I'm putting them all in one place so you don't have to.",
        S
    ))
    story.append(Spacer(1, 16))

    # ══════════════════════════════════════════════════════
    # TIPS
    # ══════════════════════════════════════════════════════
    story.append(Paragraph("AIRPORTS", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(1, "Airport", "Thieves love baggage claim",
        "The second you pull your suitcase off the belt, your bag on the floor behind you is wide open. "
        "Professional teams work in pairs — one distracts, one grabs. "
        "Keep your carry-on on your shoulder. Every single time.",
        S))

    story.append(tip_block(2, "Airport", "The TSA checkpoint is the highest-theft moment in any airport",
        "You're removing shoes, emptying pockets, managing your laptop — "
        "and your phone and wallet are sitting in an open tray you can't see. "
        "Put valuables inside your zipped carry-on. Everything goes through as one unit, not scattered in three bins.",
        S))

    story.append(Paragraph("HOTELS", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(3, "Hotel", "Always ask for two key cards — even if you're alone",
        "When the front desk hands you one key, anyone nearby knows you're traveling solo. "
        "Two keys signals a companion without saying a word. "
        "It costs nothing and changes how people read you.",
        S))

    story.append(tip_block(4, "Hotel", "Request floors 3 to 6. Never the ground floor",
        "Ground floor rooms are easiest to access through windows and sliding doors. "
        "Above floor 6, most fire ladders can't reach. "
        "Floors 3–6 is the safety sweet spot every security expert recommends.",
        S))

    story.append(Paragraph("CRUISE SHIPS", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(5, "Cruise", "Lock your balcony door every time you leave",
        "Balcony-to-balcony access is how most in-cabin theft happens on cruise ships. "
        "Most passengers have no idea this is even possible. "
        "Every time you leave your cabin — the sliding door gets locked. No exceptions.",
        S))

    story.append(tip_block(6, "Cruise", "Leave your passport on the ship when you go ashore",
        "Carry a photocopy and your cruise card in port. "
        "If you get pickpocketed — and it happens more than cruise lines admit — "
        "you've lost a photocopy. Not your actual passport.",
        S))

    story.append(Paragraph("FOOD ABROAD", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(7, "Food", "Walk two blocks from the main square",
        "Restaurants right next to tourist attractions often have two menus — "
        "a tourist version and a local version. Walk two blocks. "
        "The food is better, cheaper, and made for people who eat there every week.",
        S))

    story.append(Paragraph("HEALTH", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(8, "Health", "Window seat on a long flight = extra radiation",
        "At cruising altitude you're above most of Earth's protective atmosphere. "
        "A transatlantic window seat gives you roughly a chest X-ray worth of radiation. "
        "For frequent flyers: aisle seat on long-haul cuts cumulative exposure significantly.",
        S))

    story.append(tip_block(9, "Health", "Never plug your phone into an airport USB port",
        "The FBI has issued repeated warnings about \"juice jacking\" — "
        "malware transferred through public USB ports while your device charges. "
        "Use your own wall charger. A USB port you don't own is a port you don't use.",
        S))

    story.append(Paragraph("MONEY", S["section_label"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=C_RULE, spaceAfter=14))

    story.append(tip_block(10, "Money", "Never bring your regular debit card abroad",
        "A stolen debit card is a direct line to your home bank account. "
        "Get a separate travel card with a low daily balance. "
        "If it's stolen, you've lost today's spending money — not your savings. "
        "Set it up once. Use it every trip.",
        S))

    # ══════════════════════════════════════════════════════
    # UPSELL
    # ══════════════════════════════════════════════════════
    story.append(Spacer(1, 10))
    story.append(upsell_block(S))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "Free for personal use · Not for redistribution · © 2026 @thekiramethod",
        S["footer_note"]
    ))

    doc.build(story,
              onFirstPage=on_cover_page,
              onLaterPages=on_later_page)
    print(f"Done → {out}")

if __name__ == "__main__":
    build()
