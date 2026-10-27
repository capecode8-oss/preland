---
name: neon-body-reel-studio
description: Build short vertical (1080x1920) explainer reels in the calm "neon glowing body silhouette" style (dark navy background, soft glowing outlines of women and men, glowing organs, rulers and counters, word-by-word karaoke subtitles) from code for @thekiramethod. Use for body, health, age, men-vs-women, "what happens to your body" topics when the owner gives a voiceover script. Topic-independent. Renders as SVG + CSS in Chromium, fast, no GPU needed.
---

# Neon Body Reel Studio (topic-independent)

Visual identity: calm deep-navy night, soft neon outlines, never scary. NO saturated red. Warning = soft coral, women = rose, men = cyan, good news = mint, key numbers = amber.

## Read first
1. `references/style_bible.md` (palette, layout, motion language, shot patterns)
2. `templates/neon_kit.js` (tested: `frame, bokeh, body, organ, ruler, karaoke, prog, ease`) and `templates/job_template.json`
3. `.claude/skills/motion-director/SKILL.md` (composition, 12 animation principles, review checklist)
4. `.claude/skills/lowpoly-reel-studio/references/windows_render.md` and `qa.md` (render and QA are the same)

## Workflow
1. Get the voiceover text + audio files from the owner. Fill `job.json` from the template; every beat is tied to a spoken WORD.
2. Word timing: faster-whisper (`word_timestamps=True`) -> `words.json`; fallback: ffprobe durations + character spread.
3. Build `scene.html` that imports `neon_kit.js` and exposes `window.update(t)` (pure function of t, no real-time clocks). Draw each frame as one SVG via `frame(...)`.
4. One still per shot, contact sheet, show the owner, WAIT for approval.
5. Render frames with Playwright (`window.update(t)` then screenshot), ffmpeg to MP4, mix voice (-16 LUFS) + quiet SFX (tools/reels/sfx_synth.py), no music.
6. QA with `references/qa.md`, save `reels/<slug>.mp4`.

## Hard rules
- Never change a word of the voiceover. No invented facts or numbers; numbers on screen come from the script.
- No red as a main color, no gore, no scary imagery. No health-result promises, prices, "free", hashtags, music.
- Text and key visuals inside y 270-1520, x 108-972. ONE text system at a time: big title for the first 3 s OR karaoke subtitles, never two duplicates of the same words.
- First 2 seconds: the question is on screen and something glows or moves.
