# KIRA Project — Постоянные правила для Claude Code

## Кто я и что делаю
Я (@thekiramethod) произвожу Instagram Reels для английского рынка (35+, США).
Тематика: отношения, измена, брак. Ежедневно публикуем 4–5 рилсов через Metricool.

---

## Обязательные файлы — читать перед любым действием

| Файл | Когда читать |
|------|--------------|
| `/workspace/kira_pack/KIRA_PACK_UPDATED/04_AUTOMATION/REELS_FOOTAGE_RENDER_AND_METRICOOL_WORKFLOW.md` | Перед любым рендером или планированием |
| `/workspace/kira_pack/KIRA_PACK_UPDATED/02_CONTENT_SYSTEM/viral_pattern_library.md` | Перед написанием хуков |
| `/workspace/kira_pack/KIRA_PACK_UPDATED/02_CONTENT_SYSTEM/viral-reels-prompt-v2.original.md` | Перед написанием хуков |
| KIRA_FACE_CLEARANCE_PROTOCOL (загружен в сессии) | Перед каждым рендером |

---

## Правила футажей

- **Каждый день — новые клипы. Никаких повторов.**
- Нельзя повторять клип ни в тот же день, ни на следующий.
- Порядок клипов — рандомный, по кругу по всей библиотеке.
- Библиотека: 1_1 – 1_30, 31_1 – 31_3 (35 клипов). Использованные: 1_9, 1_11, 1_12, 1_13, 1_14, 1_15 (Aug 13).

---

## Face Clearance Protocol (обязательно)

1. Извлечь 5 кадров: t = 0.25, 1.25, 2.50, 3.75, 4.75s
2. UNION bbox лица по всем 5 кадрам → +70px сверху и снизу = forbidden zone
3. Текст должен быть ПОЛНОСТЬЮ выше forbidden_top ИЛИ ПОЛНОСТЬЮ ниже forbidden_bottom
4. Если нет места — брать другой клип
5. QA: center=540±2px, box_w≤1060px, cta_bottom≤1600px

---

## Рендер-спецификации

- Размер: 1080×1920
- Длительность: ровно 5.000s (loop если короче)
- Кодек: H.264, yuv420p, -an (без аудио)
- FFMPEG: `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2`
- Шрифт: LiberationSans-BoldItalic (Montserrat в репо повреждён)
- Hook: 48px, CTA badge: 42px
- FILL: (255, 255, 255, 245), RADIUS: 14, PAD_X: 28, PAD_Y: 18

---

## Хук — правила написания

- 4–6 строк, ≤10 слов в строке
- CAPS на одном ключевом слове
- Структура: Setup → Escalation → Stakes → Pivot → Open loop
- Паттерны: Pattern 06 (Human Secret), Pattern 17 (Relationship Open Loop), Pattern 05 (Reversal)
- Тема выбирается ДО просмотра футажа; футаж — визуальная обёртка

---

## Metricool

- brand_id: 6476294
- Timezone: America/New_York
- Публиковать как Instagram Reel
- Музыку и геотег (New York) добавляет владелец вручную
- Caption: 1600–1800 символов, структура: second hook → context → escalation → payoff → detail → CALM CTA
- CALM CTA: `Comment CALM. I'll send you The 3AM Calm Card -- a free one-page guide with 4 steps for when you wake up and can't settle. Also available from the link in bio.`

---

## GitHub / публикация

- Репо: `capecode8-oss/preland`, ветка: `claude/new-chat-fjz36a`
- MP4 пушить в репо → raw.githubusercontent.com URL → Metricool
- После изменений: commit + push обязательно
