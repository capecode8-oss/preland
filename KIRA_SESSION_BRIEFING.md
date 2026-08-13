# KIRA Session Briefing — прочитай перед любым действием

## Контекст

Ты продолжаешь работу по проекту KIRA Method Instagram (@thekiramethod).
Вся документация, скиллы и правила уже в этом репозитории на ветке `claude/reels-carousel-principles-bcnylv`.

**Первым делом переключись на рабочую ветку:**
```bash
git checkout claude/reels-carousel-principles-bcnylv
git pull origin claude/reels-carousel-principles-bcnylv
```

## Что уже сделано

### Aug 13 — 3 рилса готовы к публикации в Metricool
| Время (NY) | Файл | JSON каптшен |
|------------|------|--------------|
| 15:00 | `content/reels/renders/reel_1_13_skydive.mp4` | `content/reels/2026-08-13_skydive-sorry-mom_1_13.json` |
| 18:00 | `content/reels/renders/reel_1_26_positano.mp4` | `content/reels/2026-08-13_positano-red-dress_1_26.json` |
| 21:00 | `content/reels/renders/reel_1_20_hawaii.mp4` | `content/reels/2026-08-13_helicopter-hawaii_1_20.json` |

### Aug 14 — 5 рилсов готовы (измена/отношения)
| Время (NY) | Файл | JSON |
|------------|------|------|
| 09:00 | `reel_1_16_coastal_drive.mp4` | `2026-08-14_coastal-drive-phone_1_16.json` |
| 12:30 | `reel_1_14_passenger_coastal.mp4` | `2026-08-14_wrong-thread_1_14.json` |
| 16:00 | `reel_31_1_backseat_night.mp4` | `2026-08-14_anniversary-receipt_31_1.json` |
| 19:30 | `reel_31_2_train_night.mp4` | `2026-08-14_one-bag-train_31_2.json` |
| 23:00 | `reel_1_9_taxi_night.mp4` | `2026-08-14_cab-call_1_9.json` |

## Metricool

- Бренд: **thekiramethod**
- brand_id: **6476294**
- Timezone: **America/New_York**
- Коннектор уже подключён. Используй Metricoll MCP инструменты.
- После планирования запиши post_id в соответствующий JSON файл.
- Музыку добавляет владелец вручную через Metricool web planner → Instagram presets → Add audio.

## Правила рендера (кратко)

- Canvas 1080×1920, 5.000s, H.264, no audio
- Шрифт: `04_VISUAL_LIBRARY/fonts/reels/Montserrat-BoldItalic.ttf`
- Хук: минимум 4 строки (лучше 5-6), структура: Setup → Escalation → Stakes → Pivot → Open loop
- CAPS на одном эмоциональном слове
- Белый rounded_rectangle (radius=14) за текстом, центр x=540px ±2px
- Box width никогда не превышает 1060px — длинные строки разбивать
- Лицо: извлечь 5 кадров (t=0.25, 1.25, 2.50, 3.75, 4.75s), взять UNION, +70px отступ
- CTA badge — отдельный белый бокс ниже хука, y < 1600px

## Ключевые файлы

- Бренд: `kira_pack/01_BRAND/KIRA_ACCOUNT_CONTEXT.md`
- Воркфлоу рилсов: `kira_pack/04_AUTOMATION/REELS_FOOTAGE_RENDER_AND_METRICOOL_WORKFLOW.md`
- Хуки: `kira_pack/02_PATTERN_LIBRARY/BROAD_REELS_TOPIC_AND_HOOK_SYSTEM.md`
- CTA ротация: `kira_pack/02_PATTERN_LIBRARY/REELS_CAPTION_OPEN_CTA_ROTATION.md`

## Ниша и CTA

- Контент: женский лайфстайл, нервная система, сон, отношения, измена/брак (broad)
- Ключевое слово: **CALM** → триггерит DM → "3AM Calm Card" (бесплатный гайд)
- Каждый каптшен заканчивается: "Comment CALM. I'll send you The 3AM Calm Card..."

## Задача прямо сейчас

Запланируй в Metricool 3 рилса на 13 августа (15:00, 18:00, 21:00 NY).
Файлы MP4 лежат локально в `content/reels/renders/` на ветке выше.
