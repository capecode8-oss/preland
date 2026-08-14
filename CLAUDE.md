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

## Хук — правила написания (CURIOSITY GAP формат)

**Структура — ровно 2 блока + CTA badge:**

- **Блок 1 (hook_lines[0–1]):** Конкретная деталь / открытие. Специфично, реально, без лишних слов.
  - Пример: "She Found A Second Phone In His Car."
- **Блок 2 (hook_lines[2–3]):** Твист / реверсал — переворачивает ожидание.
  - Пример: "The Messages Weren't From Another Woman."
- **CTA badge:** Скрывает развязку → заставляет читать caption.
  - Пример: "( The last message was worse ↓ )"

**Запрещено:**
- ❌ Нарративные 5–6 строк ("She walked to the kitchen and made coffee")
- ❌ Объяснять развязку в хуке
- ❌ Стрелки → в середине текста

**Разрешено:**
- ✅ Максимум 4 строки в hook_lines (2+2 структура)
- ✅ ≤8 слов на строку
- ✅ Конкретные детали (второй телефон, запертый ящик, чужое имя)
- ✅ CAPS на одном слове если нужно
- ✅ Curiosity gap — читатель ДОЛЖЕН открыть caption чтобы узнать конец

**Паттерны:** Pattern 01 (Specific Mystery), Pattern 05 (Reversal), Pattern 17 (Relationship Open Loop)

**Темы:** измена, второй телефон, скрытые сообщения, запертые вещи, чужое имя, утренние открытия

Тема выбирается ДО просмотра футажа; футаж — визуальная обёртка.

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
