#!/usr/bin/env python3
"""Carousel renderer (Hook Atlas standard). kind=fact|split, 7 slides, 1080x1350.
Usage: CAROUSEL_DATA=data.json python3 gen_atlas_five.py [slug ...]"""
import base64, json, sys, requests
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import os
HERE = Path(__file__).resolve().parent
API_KEY = os.environ.get("DEEPINFRA_KEY") or open("/tmp/.dik").read().strip()
W, H = 1080, 1350
BG, DARK, ACCENT = (252, 249, 245), (22, 18, 14), (180, 110, 60)
WHITE, ORANGE = (255, 255, 255), (255, 140, 0)
GREEN, RED = (30, 120, 50), (170, 30, 30)
GREEN_BG, RED_BG = (226, 244, 228), (248, 226, 224)
MARGIN = 72
BEBAS = str(HERE / "fonts" / "BebasNeue-Bold.otf")
MBLACK = "/usr/share/fonts/truetype/montserrat/Montserrat-Black.ttf"
MBOLD = "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf"
COVER_W = 972 - 108
OUT_BASE = Path(os.environ.get("CAROUSEL_OUT", HERE.parents[1] / "carousels" / "2026" / "10"))


def lf(p, s):
    return ImageFont.truetype(p, s)


def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]


def lh(d, f):
    b = d.textbbox((0, 0), "Ag", font=f)
    return b[3] - b[1]


def wrap(d, text, f, mw_):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if tw(d, t, f) <= mw_:
            cur = t
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def fit(d, text, path, max_w, max_h, start=84, stop=36):
    for s in range(start, stop - 1, -2):
        f = lf(path, s)
        lines = wrap(d, text, f, max_w)
        h = len(lines) * (lh(d, f) + 14)
        if h <= max_h and all(tw(d, l, f) <= max_w for l in lines):
            return f, lines
    f = lf(path, stop)
    return f, wrap(d, text, f, max_w)


def dots(d, idx, total):
    r, gap = 11, 26
    for i in range(total):
        x = W // 2 - (total * gap) // 2 + i * gap + gap // 2
        if i == idx:
            d.ellipse([x - r, 1265 - r, x + r, 1265 + r], fill=ACCENT)
        else:
            d.ellipse([x - r, 1265 - r, x + r, 1265 + r], outline=ACCENT, width=3)
    f = lf(MBOLD, 28)
    d.text(((W - tw(d, "@thekiramethod", f)) // 2, 1300), "@thekiramethod", font=f, fill=ACCENT)


def chip(d, x, y, text, fill, size=28):
    f = lf(MBLACK, size)
    w = tw(d, text, f)
    d.rounded_rectangle([x, y, x + w + 48, y + lh(d, f) + 28], radius=8, fill=fill)
    d.text((x + 24, y + 12), text, font=f, fill=WHITE)
    return y + lh(d, f) + 28


def flux(prompt):
    full = prompt + ", bright natural light, vibrant colors, cinematic, photorealistic, 4k"
    r = requests.post(
        "https://api.deepinfra.com/v1/inference/black-forest-labs/FLUX-1-schnell",
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"prompt": full, "width": 1080, "height": 1350, "num_inference_steps": 4},
        timeout=90)
    return Image.open(BytesIO(base64.b64decode(r.json()["images"][0].split(",")[1]))).convert("RGB").resize((W, H))


def video_frame(path, t=2.0, top=60):
    import subprocess, shutil, tempfile
    ff = shutil.which("ffmpeg")
    if not ff:
        import imageio_ffmpeg
        ff = imageio_ffmpeg.get_ffmpeg_exe()
    tmp = tempfile.mktemp(suffix=".jpg")
    subprocess.run([ff, "-y", "-loglevel", "error", "-ss", str(t), "-i", str(path), "-vframes", "1", tmp], check=True)
    im = Image.open(tmp).convert("RGB")
    sc = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * sc) + 1, int(im.height * sc) + 1))
    top = max(0, min(top, im.height - H))
    left = (im.width - W) // 2
    return im.crop((left, top, left + W, top + H))


def cover(bg, lines, save):
    img = bg.copy()
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for i in range(750):
        od.rectangle([(0, H - 750 + i), (W, H - 750 + i + 1)], fill=(0, 0, 0, int(230 * i / 750)))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img)
    f = None
    for s in range(160, 71, -4):
        f = lf(BEBAS, s)
        if all(tw(d, l, f) <= COVER_W for l in lines):
            break
    hs = [lh(d, f) for l in lines]
    y = 1290 - (sum(hs) + 14 * (len(lines) - 1))
    for i, l in enumerate(lines):
        x = (W - tw(d, l, f)) // 2
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if dx or dy:
                    d.text((x + dx, y + dy), l, font=f, fill=(0, 0, 0))
        d.text((x, y), l, font=f, fill=ORANGE if i == len(lines) - 1 else WHITE)
        y += hs[i] + 14
    img.save(save, "JPEG", quality=95)


def fact(idx, total, tag, text, loop, save, soft=False):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 8)], fill=ACCENT)
    y = chip(d, MARGIN, 48, tag, ACCENT)
    d.rectangle([(MARGIN, y + 24), (W - MARGIN, y + 27)], fill=ACCENT)
    top = y + 70
    bottom = 1010 if (loop or soft) else 1150
    f, lines = fit(d, text, MBLACK, W - 2 * MARGIN, bottom - top)
    step = lh(d, f) + 14
    cy = top + max(0, (bottom - top - len(lines) * step) // 2)
    for l in lines:
        d.text(((W - tw(d, l, f)) // 2, cy), l, font=f, fill=DARK)
        cy += step
    if loop:
        lf2 = lf(MBLACK, 40)
        ll = wrap(d, loop, lf2, W - 2 * MARGIN)
        ly = 1030
        for l in ll:
            d.text(((W - tw(d, l, lf2)) // 2, ly), l, font=lf2, fill=ACCENT)
            ly += lh(d, lf2) + 10
    if soft:
        f3 = lf(MBLACK, 30)
        t = soft if isinstance(soft, str) else "SAVE THIS BEFORE YOUR NEXT TRIP"
        w = tw(d, t, f3)
        by = 1150
        d.rounded_rectangle([(W - w) // 2 - 28, by, (W + w) // 2 + 28, by + 70], radius=35, outline=ACCENT, width=3)
        d.text(((W - w) // 2, by + 17), t, font=f3, fill=ACCENT)
    dots(d, idx - 1, total)
    img.save(save, "JPEG", quality=95)


def split(idx, total, myth, reality, save, soft=False):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(0, 0), (W, 8)], fill=ACCENT)
    top_y, mid, bot_y = 40, 650, 1150 if not soft else 1100
    d.rectangle([(0, 8), (W, mid)], fill=RED_BG)
    d.rectangle([(0, mid), (W, bot_y)], fill=GREEN_BG)
    yb = chip(d, MARGIN, top_y + 8, "TOURISTS THINK", RED, 26)
    f, lines = fit(d, myth, MBLACK, W - 2 * MARGIN, mid - yb - 60, start=62, stop=34)
    step = lh(d, f) + 12
    y = yb + 30 + max(0, (mid - yb - 60 - len(lines) * step) // 2)
    for l in lines:
        d.text((MARGIN, y), l, font=f, fill=DARK)
        y += step
    yb2 = chip(d, MARGIN, mid + 24, "CREW KNOW", GREEN, 26)
    f, lines = fit(d, reality, MBLACK, W - 2 * MARGIN, bot_y - yb2 - 50, start=56, stop=32)
    step = lh(d, f) + 12
    y = yb2 + 24 + max(0, (bot_y - yb2 - 50 - len(lines) * step) // 2)
    for l in lines:
        d.text((MARGIN, y), l, font=f, fill=DARK)
        y += step
    if soft:
        f3 = lf(MBLACK, 30)
        t = "SAVE THIS BEFORE YOUR NEXT CRUISE"
        w = tw(d, t, f3)
        d.rounded_rectangle([(W - w) // 2 - 28, 1128, (W + w) // 2 + 28, 1198], radius=35, outline=ACCENT, width=3)
        d.text(((W - w) // 2, 1145), t, font=f3, fill=ACCENT)
    dots(d, idx - 1, total)
    img.save(save, "JPEG", quality=95)


PRODUCTS = {
    "SAFETY": dict(title=["THE TRAVEL", "SAFETY GUIDE"], word="SAFETY",
                   sub="45 real situations: airports, hotels, cruise ships. Exactly what to do in each.",
                   bridge="That was 1 of 45 situations I wrote down across 47 countries.",
                   dm="I'll DM you the guide."),
    "GLOW": dict(title=["THE GLOW", "HEALTH BUNDLE"], word="GLOW",
                 sub="4 short books + 4 tools. What your body has been trying to tell you.",
                 bridge="This is what I found after years of thinking it was just aging.",
                 dm="I'll DM you the Health Bundle."),
}


def cta2(closing, save, product="SAFETY"):
    P = PRODUCTS[product]
    img=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(img)
    d.rectangle([(0,0),(W,8)],fill=ACCENT)
    f,lines=fit(d,closing,MBLACK,W-2*MARGIN,230,start=60,stop=40)
    y=70
    for l in lines:
        d.text(((W-tw(d,l,f))//2,y),l,font=f,fill=DARK); y+=lh(d,f)+14
    y+=22
    f2=lf(MBOLD,34)
    for l in wrap(d,P["bridge"],f2,W-2*MARGIN-40):
        d.text(((W-tw(d,l,f2))//2,y),l,font=f2,fill=(110,95,80)); y+=lh(d,f2)+10
    cy0=y+50; cy1=1190
    d.rounded_rectangle([MARGIN,cy0,W-MARGIN,cy1],radius=26,fill=ACCENT)
    cx=W//2
    ft=lf(MBLACK,64); fs=lf(MBOLD,36); pf=lf(MBLACK,66); sf=lf(MBOLD,34)
    sub=wrap(d,P["sub"],fs,W-2*MARGIN-80)
    def layout(draw,yy):
        for l in P["title"]:
            if draw: d.text((cx-tw(d,l,ft)//2,yy),l,font=ft,fill=WHITE)
            yy+=lh(d,ft)+14
        yy+=14
        for l in sub:
            if draw: d.text((cx-tw(d,l,fs)//2,yy),l,font=fs,fill=(255,245,230))
            yy+=lh(d,fs)+12
        yy+=44
        t1,t2="COMMENT",P["word"]; w1,w2=tw(d,t1,pf),tw(d,t2,pf); gap=24; tot=w1+gap+w2; ph=lh(d,pf)+60
        if draw:
            d.rounded_rectangle([cx-tot//2-50,yy,cx+tot//2+50,yy+ph],radius=ph//2,fill=WHITE)
            tx=cx-tot//2; ty=yy+28
            d.text((tx,ty),t1,font=pf,fill=DARK); d.text((tx+w1+gap,ty),t2,font=pf,fill=ACCENT)
        yy+=ph+36
        for l in ["Follow first so it lands in your inbox.",P["dm"]]:
            if draw: d.text((cx-tw(d,l,sf)//2,yy),l,font=sf,fill=WHITE)
            yy+=lh(d,sf)+12
        return yy
    h=layout(False,0)
    layout(True,cy0+(cy1-cy0-h)//2)
    print("  content h",h,"card h",cy1-cy0)
    dots(d,6,7); img.save(save,"JPEG",quality=95)



def preflight(path, kind):
    img = Image.open(path).convert("RGB")
    bad = []
    if kind == "cover":
        l, r = 108, 972
    else:
        l, r = 60, 1020
    px = img.load()
    for x in list(range(0, l)) + list(range(r, W)):
        for y in range(20, 1240, 3):
            p = px[x, y]
            if kind == "cover":
                continue
            if kind == "split":
                if p not in (RED_BG, GREEN_BG, BG):
                    bad.append((x, y))
                    break
            elif sum(abs(p[i] - BG[i]) for i in range(3)) > 40:
                bad.append((x, y))
                break
    return bad


CAROUSELS = json.load(open(os.environ.get("CAROUSEL_DATA", HERE / "atlas_five.example.json")))


def build(c):
    slug = c["slug"]
    out = OUT_BASE / slug
    out.mkdir(parents=True, exist_ok=True)
    total = 7
    print(f"\n== {slug}")
    bg = video_frame(HERE.parents[1] / c["cover_video"], c.get("cover_t", 2.0), c.get("cover_top", 60)) if c.get("cover_video") else flux(c["flux"])
    cover(bg, c["cover"], out / "slide_01.jpg")
    for i, s in enumerate(c["slides"]):
        n = i + 2
        p = out / f"slide_0{n}.jpg"
        if c["kind"] == "split":
            split(n, total, s["myth"], s["real"], p, s.get("soft", False))
        else:
            fact(n, total, s["tag"], s["text"], s.get("loop"), p, s.get("soft", False))
    cta2(c["cta_hook"], out / "slide_07.jpg", c.get("product", "SAFETY"))
    (out / "caption.txt").write_text(c["caption"], encoding="utf-8")
    for n in range(2, 8):
        kind = "split" if (c["kind"] == "split" and n < 7) else "fact"
        b = preflight(out / f"slide_0{n}.jpg", kind)
        print(f"  slide_0{n}", "OK" if not b else f"OVERFLOW at {b[:2]}")
    print(f"  caption chars: {len(c['caption'])}")


if __name__ == "__main__":
    only = sys.argv[1:]
    for c in CAROUSELS:
        if not only or c["slug"] in only:
            build(c)
