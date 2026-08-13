# KIRA Reels — Footage, Text Rendering, and Metricool Workflow

## Goal

Turn an owner-supplied archive of AI footage into ready-to-publish Instagram Reels, prevent same-day footage repetition, apply the approved Kira text treatment, attach verified captions, and schedule approved posts through Metricool.

## Input Contract

The owner supplies a ZIP archive containing source footage. Preserve the archive and ingest supported video files into a dedicated footage pool. During import:

1. Record filename, file hash, duration, dimensions, frame rate, codec, and audio presence.
2. Detect exact duplicates by content hash even when filenames differ.
3. Flag corrupt, extremely short, low-resolution, landscape, or badly cropped assets.
4. Never overwrite the source footage.

Planned library:

- `04_VISUAL_LIBRARY/kira_reels_footage/`
- `04_VISUAL_LIBRARY/kira_reels_footage/footage_inventory.csv`
- `04_VISUAL_LIBRARY/kira_reels_footage/footage_usage.csv`

Owner footage pool: `I:\instagram 2026\KIRA\video footages`. Treat this directory as the authoritative source pool. Do not require descriptive filenames; numbered filenames are valid.

## Daily No-Repeat Contract

Use the intended publication date as the uniqueness boundary.

- Select one eligible footage asset randomly from the unused pool for that publication date.
- Exclude every content hash already reserved for another Reel on the same date.
- Reserve the asset in `footage_usage.csv` before final rendering.
- Never assign one source clip to two Reels sharing a publication date, even when the clip has been renamed or re-encoded.
- Reuse on another date is allowed unless the owner later sets a longer cooldown.
- If the date has no unused eligible footage, stop and request additional footage rather than silently repeat.

## Visual Classification and Selection

Source filenames carry no semantic meaning. The owner may name clips `001.mp4`, `002.mp4`, and so on. Never choose footage because a filename contains a topic word.

**Topic-first rule:** complete audience-demand research, choose the topic, verify the promised payoff, and approve the hook before browsing the footage pool for an asset. Footage is a visual wrapper, not a source of subject ideas. Never create elephant content merely because elephants are visible, airplane content merely because a plane is visible, or any other topic solely to match a clip.

During ingestion:

1. Assign a stable internal `clip_id`.
2. Calculate SHA-256 for exact-duplicate detection.
3. Extract representative frames from the beginning, middle, and end.
4. Record who is visible, shot type, action, setting, facial emotion, visual mood, dominant colors, motion level, and the safest text region.
5. Assign `topic_tags` and a `similarity_group` for visually near-identical clips from the same scene, outfit, or generation batch.
6. Reject or flag clips with visual artifacts, unreadable composition, face distortion, unsafe cropping, or insufficient text space.

Selection order:

1. Start with an independently researched and verified Reel topic, hook, and caption promise.
2. Match that topic's emotional tone to compatible visual tags without implying the footage documents the event.
3. Exclude exact hashes already used on the intended date.
4. Avoid repeating the same `similarity_group` on the same date when enough alternatives exist.
5. Check the selected frame against the headline placement so text does not cover the face or key action.
6. Randomize only among the remaining compatible clips.

Do not pair cheerful celebration footage with grief, danger, betrayal, or abuse merely because the clip is unused. Semantic and emotional fit outrank randomness.

Suggested usage ledger columns:

`publication_date,reel_id,source_filename,sha256,reserved_at,status,output_filename,metricool_post_id`

## Text Treatment

Match the owner-approved reference style:

- bold italic black text;
- compact white rounded rectangle behind each line group;
- high contrast with minimal shadow;
- center the headline in a vertically suitable safe region;
- mathematically center the complete headline block and the separate CTA badge on the horizontal axis at `x = 540 px`; never offset either block slightly left or right;
- natural two- or three-line wrapping;
- smaller separate white CTA badge below the headline;
- no generic Instagram template decorations.

Approved exact font: [`../04_VISUAL_LIBRARY/fonts/reels/Montserrat-BoldItalic.ttf`](../04_VISUAL_LIBRARY/fonts/reels/Montserrat-BoldItalic.ttf). Load this file directly during rendering; do not substitute a system font in final output.

CTA badge source:

- Load `02_PATTERN_LIBRARY/REELS_CAPTION_OPEN_CTA_ROTATION.md`.
- Randomly reserve one entry from its 30-item bank in `04_VISUAL_LIBRARY/kira_reels_footage/cta_usage.csv` before rendering.
- For the planned six Reels per publication date, all six badges must be different.
- Classify the headline/caption relationship first, then randomize only inside the logically eligible group. Prefer unused eligible badges across dates; semantic fit overrides exhausting the entire bank.
- `(read the caption)` remains approved, but it is only one rotating option.

Production safe zones must account for Instagram interface overlays. Keep essential text away from the extreme top, bottom, and right edge.

### Hook Text Length — Read-Time Engagement Rule

**Principle:** Every additional line a viewer reads keeps them on the Reel longer. Instagram's algorithm measures completion rate and watch time. A hook that takes 3–5 seconds to read fully aligns with the 5-second loop and maximises re-watch loops before the viewer can swipe away.

**Minimum hook length:** 4 lines. Preferred: 5–6 lines.

**Structure (mini-narrative arc):**

1. **Setup** — one clear, concrete situation. (e.g. "She carried the same red dress on every trip for 10 YEARS.")
2. **Escalation** — deepen the detail or add a complication. (e.g. "Left it in the suitcase every time.")
3. **Stakes / Pattern** — show the repeated behaviour or cost. (e.g. "Her daughter said 4 words.")
4. **Pivot / Tease** — hint at a turning point without revealing it. (e.g. "She finally put it on.")
5. *(Optional)* **Open loop** — a line that cannot be resolved without reading the caption.

**Rules:**

- Each line must be short enough to read in ≈ 0.5 s (≤ 10 words per line at 48 px Montserrat Bold Italic).
- Use CAPS on one high-emotion word per hook to create a visual anchor (e.g. YEARS, THIS, TOO OLD).
- Do not summarise the caption; create a gap between the hook and the answer that only the caption closes.
- Never pad with filler lines. Every line must earn its place by adding curiosity, stakes, or surprise.
- The CTA badge ("Read caption below ↓") is a separate smaller box, always placed below the hook block, always inside the Instagram-safe vertical zone (y < 1600 px on a 1920 px canvas).

**Algorithm rationale:** More lines → longer read time → higher watch-time signal → Instagram treats the Reel as high-retention content → wider organic distribution. Three short lines that a viewer reads in 1 s underperform five tight lines that require 3–4 s even when the copy quality is identical.

### Mandatory Horizontal Centering

- The headline container, every wrapped line group, and the CTA badge must share the exact horizontal center axis at `x = 540 px` on a 1080 × 1920 canvas.
- Vertical placement remains flexible and must respect the face, key action, readability, and Instagram UI safe zones.
- Center text inside each white rounded rectangle and center the rectangle itself on the canvas.
- Different line widths are allowed, but their individual white backgrounds must remain centered around the same axis.
- Do not use optical or asymmetric horizontal offsets. A block shifted even slightly left or right fails QA.
- Validate every rendered text-block bounding box numerically before export: `abs((left + right) / 2 - 540) <= 2 px`.

### Mandatory Face and Subject Clearance

Text must never cover Kira's face, eyes, mouth, hairline, or the story's key visual action.

Before generating the overlay:

1. Extract and inspect representative frames near `0.25`, `1.25`, `2.50`, `3.75`, and `4.75` seconds of the final five-second cut.
2. Mark the union of Kira's head/face positions across all inspected frames, not only the middle frame.
3. Expand that protected region by at least 70 px on every side so the white badge does not visually touch the face or hair.
4. Choose the safest composition from top-center, upper-left, upper-right, middle-left, middle-right, or lower-center while respecting Instagram UI safe zones.
5. Adjust wrapping, headline size, CTA size, `start-y`, and `center-x` to fit the chosen area.
6. Render a multi-frame QA preview with the final overlay and confirm zero intersection before exporting the MP4.
7. Confirm numerically that both headline and CTA horizontal bounding-box centers equal `540 px` within a maximum tolerance of `2 px`.

Hard rejection rule: if no readable vertically suitable placement exists while keeping the text horizontally centered and clear of the face or key action, use another footage asset. Do not shift the text left or right, shrink it below comfortable mobile readability, or accept partial overlap.

## Render Contract

- Canvas: 1080 × 1920 px (9:16)
- Final duration: exactly 5.000 seconds for every Reel
- Output: MP4
- Video codec: H.264
- Pixel format: yuv420p
- Audio: no audio stream in the rendered master. Always discard the source clip's original sound with `-an`; the owner adds Instagram-native music during manual publication.
- Trim or loop the source non-destructively to exactly 5.000 seconds. Reject an export whose measured duration differs from 5.000 seconds rather than rounding it in the report.
- Scale and crop intentionally; never stretch footage.
- Export a still preview and validate text fit before approving the full batch.
- Validate face clearance on multiple time points because the subject may move during the five-second cut.

## Content Contract

Before rendering, load:

- `01_BRAND/KIRA_ACCOUNT_CONTEXT.md`
- `02_PATTERN_LIBRARY/BROAD_REELS_TOPIC_AND_HOOK_SYSTEM.md`
- `02_PATTERN_LIBRARY/AUTHORITY_STAKES_OPEN_LOOP_HOOKS.md` and its four owner-supplied screenshot references
- `02_PATTERN_LIBRARY/REELS_5_SECOND_LOOP_DEEP_CAPTION.md` when relevant
- `02_PATTERN_LIBRARY/REELS_CAPTION_OPEN_CTA_ROTATION.md`
- `02_PATTERN_LIBRARY/REELS_FINAL_CAPTION_CTA_SYSTEM.md`
- `07_AGENTS/REELS_CONTENT_AGENT.md`

Every Reel requires a verified hook, full caption, final `CALM` CTA, source record, and truth classification. The `CALM` block must appear at the very end of the Metricool caption, include the link-in-bio alternative, and use wording not already assigned to another Reel on the same publication date. Do not fabricate experts, quotes, events, outcomes, or a sleep connection merely to fit a footage asset.

## Metricool Handoff

The configured remote MCP server is:

`https://ai.metricool.com/mcp`

After the Codex client restarts and Metricool OAuth succeeds:

1. Identify the correct Metricool brand and connected Instagram creator/business profile.
2. Create a scheduled Reel with the approved MP4, caption, date, time, and Instagram settings.
3. Return and store the Metricool post ID and direct planner link when available.
4. Leave the post reviewable before publication until the owner explicitly approves an automatic publishing policy.
5. Record scheduling state in the usage ledger.

## Music

Metricool's web planner supports adding authorized Meta-library music and original audio to scheduled Instagram Reels when the Instagram account is connected through Facebook Login. This feature has been available since May 18, 2026. The connected Kira brand is `thekiramethod` (`brand_id: 6476294`, timezone `America/New_York`).

### Default Kira Music Route

Owner-selected policy: `METRICOOL_NEUTRAL_AUDIO_AUTOPUBLISH`.

1. Render the exact 5.000-second MP4 without any audio stream. Discard the footage's original sound.
2. Create the Reel with its caption and intended time in Metricool.
3. In the authenticated Metricool web planner, open `Instagram presets > Add audio`.
4. Select a licensed neutral instrumental, ambient, cinematic, or lofi track that matches the story. Avoid lyrics, comedy cues, aggressive drops, or emotionally contradictory music.
5. Prefer an immediate musical cue because Metricool starts audio at second zero.
6. Enable `Auto-publish`, save, and verify the scheduled state.
7. Record the exact track title and artist in `04_VISUAL_LIBRARY/kira_reels_footage/music_usage.csv`.

The owner authorizes autonomous selection of neutral authorized music and automatic scheduling/publication. Maintain reviewable records and do not reuse one track across the six Reels on the same publication date.

The currently exposed Metricool MCP `create_scheduled_post` schema has no audio-selection field. Use MCP for brand data, timing, and post creation when possible, then use the authenticated Metricool web planner for audio selection and final Auto-publish verification.

### Daily Music Rotation

- Six Reels on one publication date must not use the same audio track.
- Match sound to the emotional mechanism: tense, warm, reflective, urgent, mysterious, or uplifting.
- Prefer a track with an immediate musical cue because Metricool starts audio at second zero and the Reel lasts only five seconds.
- Record the title, artist, audio type, selection route, mood, and status before publication.
- Do not choose random music that contradicts the story merely to avoid repetition.

### Local Audio Alternative

If the owner supplies an owned or royalty-free MP3/WAV file, FFmpeg may mix it into the MP4 automatically. Use this route only when rights are clear. A locally baked track will normally publish as original audio and may not receive the discovery benefit of an Instagram/Meta audio page.

Current limitations documented by Metricool include:

- available tracks are limited to those Meta permits for third-party publishing;
- audio starts at second zero and cannot currently be trimmed or offset;
- there is no combined final video-plus-audio preview;
- the feature is web-only;
- unavailable tracks require manual publication or a different authorized track.

If the requested song is not available in Metricool, choose another authorized track or disable Auto-publish and complete the Reel manually in Instagram through Metricool's notification workflow.

## Required Owner Inputs Before Autonomous Scheduling

- footage ZIP archive;
- approval of the first rendered overlay sample using the stored Montserrat Bold Italic font;
- Metricool OAuth and the intended brand/account;
- publication frequency, timezone, permitted days, and time windows;
- whether posts remain drafts for approval or may auto-publish;
- music policy: approved tracks/vibes and whether manual review is required.

External publishing must remain review-first until these controls are explicitly set.
