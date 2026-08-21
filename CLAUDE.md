# ⛔ СТОП — ЧИТАЙ ПЕРВЫМ

## ОБЯЗАТЕЛЬНО перед любым хуком, рилсом или капшеном:
1. Вызвать `/kira-hooks` (или `/kira-captions`) → скилл загружается
2. Аудит команды **Jordan · Mike · Alex · Sam · Dana · Red · Tyler · Maya · NOVA · VIC · Rico** (11 человек) запускается ВНУТРИ, ДО показа пользователю
3. Mike ставит прогноз просмотров (минимум 🟢 STRONG). Red пытается убить хук (должен поставить ✅ SURVIVED)
4. Пользователь видит ТОЛЬКО финальный результат после того как все 11 ✅
5. Черновики, "варианты", "предложения" — не показывать. Никогда.

**АУДИТ = ВНУТРИ. Пользователь видит только готовое. Без исключений.**

---

# KIRA Project — Контент-продакшн команда

## МЫ — ПРОДАКШН КОМАНДА. Не просто аккаунт.

Каждый рилс и каждая карусель проходит через полный production pipeline.
Без исключений. Даже если кажется что "и так норм".

### Обязательный порядок для каждой единицы контента:

| Шаг | Скилл | Что делаем |
|-----|-------|------------|
| 0 | `footage-manager` | Выбрать клип (не повтор!) → записать в журнал |
| 0.5 | `ai-video-prompts` | Нет подходящего клипа? → Генерировать AI-видео под хук (Kling / Runway / Pika) |
| 1 | `niche-templates` | Взять шаблон по нише → адаптировать с конкретными цифрами |
| 2 | `kira-hooks` | Пишем хук → аудит команды (11 чел) → body clearance → рендер |
| 3 | `kira-captions` | Пишем капшен → аудит команды → выбираем CTA по теме |
| 4 | `quality-check` | 7-пунктовый QA gate → только после ✅ идём дальше |
| 5 | `metricool-ready` | Push MP4 → raw URL → запланировать в Metricool |
| 6 | `performance-tracker` | Записать рилс → через 24-72ч обновить метрики |

**Для batch (4-6 рилсов):** использовать `batch-processor` — трекает весь batch, один пайплайн для всех.

### Команда (Jordan · Mike · Alex · Sam · Dana · Red · Tyler · Maya · NOVA · VIC · Rico) — 11 человек.
Текст: Jordan, Mike, Alex, Sam, Dana, Red — аудируют хук и капшен.
Скролл-тест: Tyler [22M] и Maya [38F] листают ленту прямо сейчас — Tyler тестирует стоп-скролл, Maya тестирует DM-отправку.
Видео: NOVA (AI video prompts — Veo 3 primary + Kling fallback), VIC (visual director) — клип или AI-промт прямо в выводе.
Тренды: Rico (trend intelligence) — следит за конкурентами, выбирает свежий угол, пикает тему автономно если не указана.
Mike ставит прогноз просмотров (порог: 🟢 STRONG = 5K+). Red пытается убить хук. Rico проверяет: не было у конкурентов на этой неделе.
Если хоть один из 11 ставит ❌ — переписываем, не публикуем.

---

## Кто я и что делаю
Я (@thekiramethod) произвожу Instagram Reels для английского рынка (35+, США).
Тематика: **travel hacks, life hacks, food facts, health warnings, money traps** (универсальные темы).
❌ СТОП: отношения / измена / cheating drama — больше не делаем.
Ежедневно публикуем 4–5 рилсов через Metricool.

**Формат хуков — конкурент (maks.motivator) — ДВА ФОРМАТА:**

**Format A — Short Punch:** 2-3 строки, ≤6 слов/строку, CTA badge `( текст ↓ )`, шрифт 60px+
→ Для команд, предупреждений, фактов с цифрой. Пример: "Never Book This Cabin On A Cruise Ship"

**Format B — Story Hook (ОСНОВНОЙ):** 3 строки полными предложениями, без CTA badge
→ Для личных историй с местом/человеком. Структура: SETUP → СОБЫТИЕ → CLIFF-HANGER
→ Пример: "A waiter in Rome brought me two different bills for the same table. The second one only appeared after I paid the first."

**Общее для обоих:** Kira рассказывает от первого лица ("I", "my", "a local told me") — НЕ "She/He". Конкретное место или цифра. Главный KPI: зритель пересылает другу.

## 🔑 КОДОВОЕ СЛОВО "ЗАПЛАНИРУЕМ" — ЖЕЛЕЗНОЕ ПРАВИЛО

Когда пользователь говорит **"запланируем рилсы"**, **"давай 5 рилсов"**, **"сделай batch"** — АВТОМАТИЧЕСКИ применять:

1. **Kira = рассказчик от первого лица** — "I found out", "A hotel receptionist told me", "My doctor showed me"
2. **Format B приоритет** — полные предложения, 3 строки, без CTA badge
3. **Три формулы-приоритета (maks.motivator стиль):**
   - `"I [did X] for [Y years]. A [person] told me [shocking fact]. I [changed] since."` — личная история
   - `"The first thing [person] looks for is not [obvious thing]. It's this."` — curiosity gap
   - `"Every [common thing] equals [shocking fact]. [Authority] know. No one tells you."` — insider reveal
4. **Клипы — только новые 32_x серия** (подобрать по теме, см. footage mapping в kira-hooks)
5. **Clips mapping (VERIFIED BY VISUAL PREVIEW — не менять без проверки скриншота):**
   - ✈️ САМОЛЁТ: 32_5 = window seat (иллюминатор, пассажирка)
   - 🏨 ОТЕЛЬ: 32_6 = reception (check-in стойка) | 32_7 = hotel room (номер, спальня)
   - ☕ КАФЕ: 32_8 = Asian cafe (Токио, город за окном)
   - 🛳️ КРУИЗ: 32_13 = cruise cabin (каюта, балкон) | 32_14 = cruise deck evening | 32_15 = cruise terrace | 32_16 = cruise deck railing | 32_17 = cruise deck Mediterranean port
   - 🧳 АЭРОПОРТ-ЗОНА ОЖИДАНИЯ: 32_1 = departure lounge (сидит) | 32_4 = departure lounge (другой ракурс) | 32_10 = departure lounge (= 32_4)
   - 🚶 АЭРОПОРТ-ДВИЖЕНИЕ: 32_9 = walking terminal | 32_11 = walking terminal (другой ракурс)
   - 🚪 АЭРОПОРТ-ВЫХОД: 32_12 = airport exit doors (автодвери наружу)
   - 🎒 БАГАЖ: 32_18 = baggage claim (багажная лента, чемоданы на карусели) ← ЕДИНСТВЕННЫЙ
   - 🚇 МЕТРО: 32_2 = subway (вагон метро)
   - 📸 СЕЛФИ: 32_3 = travel selfie (видовая точка, Рио)

   ⚠️ ПРАВИЛО: перед назначением клипа — всегда extract frame + read image визуально. Никогда не угадывать по названию.

---

## Правила футажей

- **Каждый день — новые клипы. Никаких повторов.**
- Нельзя повторять клип ни в тот же день, ни на следующий.
- Порядок клипов — рандомный, по кругу по всей библиотеке.
- Библиотека: 1_1 – 1_30, 31_1 – 31_3 (31 клип, удалены 1_9 и 1_13). Путь: `/home/user/preland/footage/`
- Использованные: 1_11, 1_12, 1_14, 1_15 (Aug 13); 1_19, 1_15, 1_23, 1_25, 1_18 (Aug 19).

---

## Размещение текста — ЖЕЛЕЗНОЕ ПРАВИЛО

⚠️ **Текст ВСЕГДА внизу. Лицо всегда свободно сверху. Без исключений. Никаких измерений.**

**SOLID BOX placement (сплошная плашка):**
- Один прямоугольник на весь текст (не отдельные плашки на каждую строку)
- `BOTTOM_ANCHOR = 1550px` (выше Instagram UI — кнопки/имя канала закрывают ниже ~1680px)
- `hook_y0 = BOTTOM_ANCHOR - box_height`
- `MAX_BOX_W = 860px` | `MAX_TEXT_W = 760px` (safety margin 50px с каждой стороны)
- font: max_size=70, min_size=50, авто-перенос строк если строка > MAX_TEXT_W

❌ ЗАПРЕЩЕНО: ставить текст сверху, делать body clearance анализ, писать строки длиннее 6 слов
❌ ЗАПРЕЩЕНО: менять MAX_BOX_W > 860 — текст выйдет за края экрана
✅ ВСЕГДА: сплошная плашка внизу, авто-перенос строк, проверять превью перед пушем

---

## Рендер-спецификации (единый источник правды)

- Размер: 1080×1920
- Длительность: ровно 5.000s = 150 frames @ 30fps (loop если короче)
- Кодек: H.264, yuv420p, -an (без аудио), -crf 18, -preset fast
- FFMPEG: `/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2`
- Шрифт: `Montserrat-BlackItalic` — путь `/tmp/montserrat_extract/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf`
- Шрифт: auto_font(max_size=70, min_size=50), авто-перенос строк если > MAX_TEXT_W
- СТИЛЬ: СПЛОШНАЯ ПЛАШКА — один прямоугольник на весь текст, строки внутри с LINE_GAP=8px
- FILL: (255, 255, 255, 248), RADIUS: 18, PAD_X: 32, PAD_TOP/BOTTOM: 28
- CENTER_X: 540, **MAX_BOX_W: 860px** (НИКОГДА не увеличивать), **MAX_TEXT_W: 760px**
- BOTTOM_ANCHOR: 1550px (выше Instagram UI chrome)
- Всегда рендерить JPG-превью из финального MP4 и показывать перед публикацией

---

## Хук — правила написания (COMPETITOR FORMAT)

**Золотой стандарт:** maks.motivator — 8 доказанных формул в скилле `kira-hooks`.

**Структура:**
- **Первое лицо** ("I", "my friend", "A local told me") — обязательно
- **Конкретная цифра или место** ("$14,000", "Bali", "3×") — когда возможно
- **Max 3 строки** в hook_lines, ≤6 слов на строку
- **CTA badge:** одна фраза, скрывает payoff → всегда ↓

**5 обязательных вопросов перед финализацией:**
1. Tyler остановит скролл на первых 3 словах?
2. Перешлёт другу?
3. Чувствует что упускает что-то важное?
4. Есть конкретная цифра или место?
5. Первое лицо ("I/my") или прямое обращение ("you") — НЕ "she/he"?

Если хоть один ответ "нет" — переписать.

**Темы (ротировать):** airport hacks, hotel tricks, customs traps, food facts, health warnings, cruise secrets, EU flight compensation, gate bump, Blue Zone food.

❌ ЗАПРЕЩЕНО: отношения / измена / "she found" / "he asked" / "you won't believe"

---

## Metricool

- brand_id: 6476294
- Timezone: America/New_York
- Публиковать как Instagram Reel + TikTok (PUBLIC_TO_EVERYONE, нужен tiktokData.title)
- Музыку и геотег (New York) добавляет владелец вручную
- Caption: 1700–1900 символов, структура: second hook → context → detail → payoff → CTA → save line
- Все правила капшена и CTA банк — в скилле `kira-captions`

---

## GitHub / публикация

- Репо: `capecode8-oss/preland`, ветка: `claude/new-chat-fjz36a`
- MP4 пушить в репо → raw.githubusercontent.com URL → Metricool
- После изменений: commit + push обязательно

---

## Карусели (будущее — после 500 подписчиков)

Когда аккаунт достигнет 500 подписчиков — добавим карусели в формат публикаций.
Пока не делаем. Правила рендера карусели будут добавлены в отдельный скилл.
