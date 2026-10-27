# Workflow details

## Shot design (each shot)
- ONE hero object, big, centered. Hero face acts the emotion (neutral, tempted, effort, happy, shock).
- Every spoken claim gets a visual proof: a counter that fills, a scale that tips, a clock, a label. The viewer should understand with the sound off.
- Open loop between shots: end a shot on a question the next shot answers (countdown, "wait", reveal).
- Hard cuts on new ideas, slow dolly (5-8%) on the key word, one whip-pan per video at most.

## Beat table (put in job.json)
{ "on_word": "fridge", "action": "dolly to fridge, door opens", "sfx": "ding" }
Find the frame: frame = round(words[block][index].start * fps). Use the FIRST occurrence after the previous beat.

## Subtitles (word by word)
- Montserrat Bold 78 px, white with 8 px black stroke, active word #FFD24A scale 1.12, 3-4 words per phrase, 2 lines max, baseline y 1230, inside safe zones.
- Text source: the on-screen version of each block (digits, GLOW), timing from words.json, matched by order of words (spelled number -> digit).
- Implement as DOM overlay in the same page (position absolute) so one screenshot per frame captures everything.

## Frame loop skeleton (render_frames.js)
for f in 0..total-1: await page.evaluate(t => window.update(t), f/fps); await page.screenshot({path: frames/%05d.jpg});
Then: ffmpeg -framerate 30 -i frames/%05d.jpg -i voice.wav -i sfx.wav -filter_complex "[1:a][2:a]amix=inputs=2:weights=1 0.35,loudnorm=I=-16" -c:v libx264 -crf 18 -pix_fmt yuv420p out.mp4

## Sound effects
tools/reels/sfx_synth.py has whoosh, tick, pop, ding, riser, impact. Add squirt/rattle/buzzer the same way with numpy. SFX 10-14 dB under the voice, 0.3 s of silence before the key reveal.

## Reuse
Keep one apartment (the "house" of the series) and change props and expression. New topic = new props + new beat table, the kit stays.
