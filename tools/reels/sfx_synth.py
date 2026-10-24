#!/usr/bin/env python3
"""Procedural sound effects for reels (no samples, no network): whoosh, tick, pop, ding, riser, impact, typing.
Usage: python3 tools/reels/sfx_synth.py [outdir]  ->  WAV (44.1 kHz mono) per effect + _demo.mp3 with all in a row.
Needs numpy and ffmpeg."""
import sys, wave, subprocess, os
import numpy as np
SR = 44100
rng = np.random.default_rng(7)

def t(d): return np.arange(int(SR * d)) / SR
def env_exp(x, tau): return np.exp(-x / tau)
def norm(x, peak=0.8): return x / (np.max(np.abs(x)) + 1e-9) * peak
def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); s = 0.0
    for i, v in enumerate(x): s = (1 - a) * v + a * s; y[i] = s
    return y
def sweep_lowpass(x, f0, f1):
    n = len(x); y = np.zeros(n); s = 0.0
    for i in range(n):
        fc = f0 + (f1 - f0) * i / n; a = np.exp(-2 * np.pi * fc / SR); s = (1 - a) * x[i] + a * s; y[i] = s
    return y

def whoosh(d=0.6):
    x = t(d); n = rng.standard_normal(len(x)); y = sweep_lowpass(n, 300, 5000) - sweep_lowpass(n, 100, 800)
    return norm(y * np.sin(np.pi * np.clip(x / d, 0, 1)) ** 2)
def tick():
    x = t(0.06); return norm(np.sin(2 * np.pi * 1800 * x) * env_exp(x, 0.006) + 0.3 * rng.standard_normal(len(x)) * env_exp(x, 0.002))
def pop():
    x = t(0.12); f = 700 * np.exp(-x * 22) + 150; return norm(np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(x, 0.03))
def ding():
    x = t(1.2); y = sum(a * np.sin(2 * np.pi * f * x) for f, a in [(1318, 1), (2637, 0.35), (3951, 0.12)]); return norm(y * env_exp(x, 0.35))
def riser(d=1.6):
    x = t(d); f = 200 + 1600 * (x / d) ** 2
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.5 + sweep_lowpass(rng.standard_normal(len(x)), 400, 6000) * 0.8
    return norm(y * (x / d) ** 1.5)
def impact():
    x = t(0.9); f = 90 * np.exp(-x * 5) + 40
    low = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(x, 0.25); nz = lowpass(rng.standard_normal(len(x)), 1800) * env_exp(x, 0.08)
    return norm(low + 0.6 * nz)
def typing(n=14):
    out = np.zeros(int(SR * (n * 0.09 + 0.2)))
    for i in range(n):
        k = tick() * (0.6 + 0.4 * rng.random()); p = int(SR * (i * 0.09 + rng.random() * 0.02)); out[p:p + len(k)] += k
    return norm(out)

EFFECTS = {"whoosh": whoosh, "tick": tick, "pop": pop, "ding": ding, "riser": riser, "impact": impact, "typing": typing}

def save(path, y):
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "assets/sfx"; os.makedirs(out, exist_ok=True)
    gap = np.zeros(int(SR * 0.5)); demo = []
    for name, fn in EFFECTS.items():
        y = fn(); save(f"{out}/{name}.wav", y); demo += [y, gap]
    save(f"{out}/_demo.wav", np.concatenate(demo))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{out}/_demo.wav", "-b:a", "128k", f"{out}/_demo.mp3"], check=True)
    print("ok", list(EFFECTS))
