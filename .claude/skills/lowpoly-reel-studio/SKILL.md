---
name: lowpoly-reel-studio
description: Build any short vertical (1080x1920) explainer reel as a low-poly 3D animation from code for @thekiramethod, with voiceover, word-by-word subtitles and sound effects. Use for ANY topic (What if, hidden facts, countdowns, myth checks) whenever the owner supplies a script/voiceover and wants a 3D low-poly video. Contains the scene kit (hero, room, props, lights, easing), the job template, the render scripts for Windows/GPU and the QA checklist. Topic-independent.
---

# Lowpoly Reel Studio (topic-independent)

Goal: turn ANY voiceover script into a 55-60 s low-poly 3D reel that stops the scroll and is understood by a 15-year-old. You (Claude Code) write the scene code, the owner supplies voice files and the script.

## Read first (in this order)
1. `.claude/skills/motion-director/SKILL.md` (composition, 12 animation principles, camera, color, review checklist)
2. `templates/scene_kit.js` (reusable Three.js kit, already tested) and `references/workflow.md`
3. `.claude/skills/threejs-*` (fundamentals, geometry, lighting, materials, animation) when you need details
4. `references/windows_render.md` for rendering and `references/qa.md` before showing anything

## Inputs you need from the owner (ask once, only if missing)
- The voiceover text (blocks) and the audio files (one per block, or one merged file)
- The topic in one line and, if given, the on-screen text version (digits instead of spelled-out numbers)
Everything else you decide yourself using the job template `templates/job_template.json`.

## Workflow
1. **Fill the job template**: copy `templates/job_template.json` to `job.json`, put the blocks and a shot list. Each shot = one block (or part of a block), each beat is tied to a WORD of the voiceover (the trigger word), never to a guessed second.
2. **Word timing**: transcribe each audio block with faster-whisper (`word_timestamps=True`) into `words.json`. If unavailable, measure block length with ffprobe and spread words by character count.
3. **Assets**: import `scene_kit.js`. Use `makeRoom`, `makeLights`, `makeHero` (5 expressions), `sugarSpoon/can/glassJar` as examples. Build NEW props for the topic with `mesh`, `box`, `mat` (flat shading, 6-10 segments, 5-7 colors per scene). One recognizable silhouette per prop.
4. **One still per shot** (`render_still.js`), contact sheet, show the owner, WAIT for approval.
5. **Animate** with a deterministic `update(t)` function (no real-time clocks), use `prog()` and `ease` from the kit, anticipation before actions, a visual event every 2-3 seconds.
6. **Subtitles** word by word from `words.json` (see `references/workflow.md`), SFX from `tools/reels/sfx_synth.py` on the trigger-word frames.
7. **Render** on the GPU (`render_frames.js`), ffmpeg to MP4, mix voice (-16 LUFS) and quiet SFX, no music.
8. **QA** with `references/qa.md`, push or save to `reels/<slug>.mp4`, report what differs from the plan.

## Hard rules
- Never change a word of the voiceover. No invented facts or numbers. No health-result promises, no prices, never the word "free", no hashtags, no music.
- Keep text and key action inside y 270-1520 px, x 108-972 px (Instagram UI).
- Language on screen: plain English for a 15-year-old, max 8 words per screen.
- First 2 seconds: the topic is obvious and something moves.
- Show the contact sheet before the full render.
