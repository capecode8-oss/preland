---
name: kira-talking-head
description: Generate AI video prompts for KIRA talking head reels (Veo 3 / Kling / Runway / Pika). Use when the reel needs a speaking character — Kira in role (flight attendant, hotel staff, TSA, tourist). Accepts reference videos/images from user and generates remakes optimized for million-view reach. Run after kira-hooks — finalized hook required before generating visual.
---

# KIRA TALKING HEAD — AI VIDEO PROMPT SYSTEM

## Формат: говорящая голова с локацией и субтитрами
## Tools: Veo 3 ⭐ · Kling 2.1 · Runway Gen-4 · Pika 2.2
## Niche: Travel · Health · Food · Money (USA, 35+)

---

## ⚡ КРИТИЧЕСКОЕ — VEO 3 ЛИМИТ = 8 СЕКУНД

**Каждая генерация = максимум 8 секунд.**

Рилс 30 сек = **4 клипа × 8 сек** (последний можно обрезать до 6 сек при монтаже).

| Клип | Хронометраж | Задача |
|------|-------------|--------|
| Clip 1 | 0–8 сек | HOOK + VISUAL SHOCK — стоп-скролл за 0.3 сек |
| Clip 2 | 8–16 сек | REVEAL — объясняет, жестикулирует, показывает |
| Clip 3 | 16–24 сек | DETAIL + TENSION — конкретика, цифра, доказательство |
| Clip 4 | 24–30 сек | SOLUTION + CTA — "Comment SAFETY..." |

**Каждый промт = один клип = одна генерация = 8 сек.**
Генерируем по одному промту за раз, не весь рилс сразу.

---

## ⛔ ЖЕЛЕЗНОЕ ПРАВИЛО — КЛИП 1 = VISUAL + AUDIO ШОК ОДНОВРЕМЕННО

❌ ЗАПРЕЩЕНО: Кира стоит лицом к камере и говорит — статичная поза от пояса до головы
❌ ЗАПРЕЩЕНО: она начинает говорить через паузу или вступление
❌ ЗАПРЕЩЕНО: локация — нейтральный фон или не видна за первые 0.3 секунды

✅ ОБЯЗАТЕЛЬНО в Clip 1:
- **Визуальный шок** — Кира уже делает что-то в первом кадре (тянет руку, берёт предмет, смотрит куда-то с реакцией)
- **Локация видна** — аэропорт, самолёт, отель, ресторан — узнаётся мгновенно
- **Предмет в кадре** — то о чём она говорит уже в руках или прямо перед ней
- **Слова начинаются с кадра 1** — не через 2 секунды, а сразу
- **Провокация** — первое слово должно активировать амигдалу ("Never", "Stop", "I caught", "They took")

**Формула первого кадра:**
Кира (40% кадра) делает действие + локация (60%) видна + предмет разговора в руках → слова начинаются в первую секунду

---

## ЧЕМ ОТЛИЧАЕТСЯ ОТ B-ROLL РИЛСА

| B-Roll рилс | Talking Head рилс |
|-------------|-------------------|
| Footage из библиотеки | AI-генерированный персонаж с речью |
| Музыка (volume 0.8) | Оригинальный звук ТОЛЬКО — никакой музыки |
| Текстовая плашка поверх видео | НЕТ плашки — первые слова речи = хук |
| Субтитры: НЕТ | Субтитры: Montserrat Black Italic, y≈700px |
| `-map 1:a` из footage | `-map 1:a` из оригинального клипа |

⛔ ЗАПРЕЩЕНО при talking head: добавлять музыку поверх голоса, mute оригинального аудио

---

## ПЕРСОНАЖ — КИРА

**Кира** — женщина 40-45 лет, attractive, brown hair (ponytail или свободно), smart casual (blazer, кардиган, или форма по роли).

**Правило:** говорит от первого лица. НЕ просто лицо на камеру — всегда видно ГДЕ она и ЧТО происходит вокруг.

**Одежда по роли (ротировать):**
- Стюардесса: `navy flight attendant uniform, red neckerchief, silver wings pin`
- Отельный сотрудник: `hotel staff blazer, name badge on lapel`
- TSA/Security: `dark uniform, lanyard with badge, airport security checkpoint`
- Туристка-Кира: `smart casual blazer, travel bag visible`
- Врач/медик: `white lab coat, stethoscope around neck`
- Шеф-повар: `chef whites, kitchen behind`

---

## ВИЗУАЛЬНЫЙ СТАНДАРТ — ТОЧНЫЙ СТИЛЬ

**Образец:** стюардесса в форме сидит в кресле самолёта, руками показывает на подлокотник/карман кресла, субтитр: "The dirtiest spot in your row"

**Что делает этот формат правильно:**
- Локация понятна за 0.3 секунды (самолёт, отель, аэропорт)
- Руки показывают на предмет разговора — не просто говорит, а демонстрирует
- Взгляд чуть в сторону от камеры — как будто объясняет пассажиру рядом, не лекция
- Форма/одежда соответствует роли (стюардесса = форма, отельный сотрудник = бейдж и т.д.)

❌ Запрещено: говорящая голова на весь экран, нейтральный фон, студия, взгляд строго в объектив всё время
✅ Обязательно: локация видна, предмет разговора в кадре или в руках, Кира в действии

**Формула кадра:** Кира (40% кадра) + локация (60%) + предмет/объект в руках или рядом

---

## СТРУКТУРА РИЛСА = 4 КЛИПА × 8 СЕК = 32 СЕК (обрезать до 30 при монтаже)

### CLIP 1 — VISUAL + AUDIO HOOK (0–8 сек) ← САМЫЙ ВАЖНЫЙ
**Задача: остановить скролл за 0.3 секунды визуально И аудиально одновременно**

- Кира уже в действии с первого кадра — тянет руку, берёт предмет, реагирует
- Локация: узнаётся мгновенно (аэропорт, самолёт, отель)
- Предмет разговора: физически в кадре или в руках
- Слова начинаются немедленно — первые 3 слова = хук
- Взгляд: в камеру на 1-2 секунды, потом на предмет — как будто показывает другу
- Энергия: не лекция, а "ты не поверишь что я только что увидела/узнала"

**Промт-ключи для Clip 1:**
```
"She is already mid-action as the clip begins — not posed, already doing it"
"Her first word lands before the viewer has time to process the frame"
"The object she's discussing is physically in frame, in her hands or directly in front of her"
"Slightly breathless urgency — like telling someone something important, not performing"
```

### CLIP 2 — INSIDER REVEAL (8–16 сек)
- Другой ракурс или шаг ближе к камере
- Жестикулирует, указывает на предмет, показывает конкретно
- Говорит быстрее — как рассказывает подруге, не читает текст
- Цифра или конкретный факт ("90,000 items a year", "$340 they charged me")

### CLIP 3 — DETAIL + PROOF (16–24 сек)
- Демонстрирует что именно происходит
- Руки в кадре — показывает действие правильно vs неправильно
- Максимум конкретики — место, предмет, механика

### CLIP 4 — SOLUTION + CTA (24–30 сек)
- Чуть ближе к камере, уверенный тон
- Показывает руками как делать правильно
- Последние слова: `"Comment SAFETY and I'll send you 44 more situations like this."`
- Смотрит прямо в камеру на финальной фразе

---

## ПРАВИЛА ПРОМТИНГА ПОД 8-СЕКУНДНЫЕ КЛИПЫ

**Каждый промт пишется под ОДИН клип = одно непрерывное действие за 8 секунд.**

❌ Не пиши "she then does X" — одно действие, не последовательность сцен
✅ Пиши как кино-момент: что происходит прямо сейчас, в движении

**Для Clip 1 — обязательная фраза в промте:**
```
"The clip begins mid-action — she is already [действие], not posed or waiting."
"Her first words begin within the first second of the clip."
```

**Динамика вместо статики — замены:**
| ❌ Статично | ✅ Динамично |
|-------------|--------------|
| "she holds a tray" | "she tilts the tray toward camera as she speaks, the phone sliding slightly inside it" |
| "she looks at camera" | "she glances up from the tray directly into the lens for exactly one beat, then back down" |
| "she explains" | "she taps the edge of the seat pocket with two fingers as she speaks — fast, matter-of-fact" |
| "she stands at the desk" | "she leans forward on both hands on the counter, voice dropped, like sharing a secret"

---

## ПРОМПТ-ФОРМУЛА VEO 3 — TALKING HEAD

```
Vertical 9:16. Woman 40s, brown hair in ponytail,
[ОДЕЖДА ПО РОЛИ]. [ЛОКАЦИЯ — конкретно].
She gestures toward [ПРЕДМЕТ] while explaining.
Slightly off-axis gaze — talking to someone just
off camera, not directly into lens.
She says: "[ТОЧНЫЕ СЛОВА]"
Photorealistic, cinematic, natural lighting. 10 seconds.
```

### Базовый шаблон (5 блоков):
```
БЛОК 1 — CAMERA
Handheld close-up at chest height, slight natural drift, auto-exposure adjusting.

БЛОК 2 — SCENE (локация конкретно)
Inside [конкретная локация с деталями среды].

БЛОК 3 — CHARACTER + ACTION
A woman in her early 40s, brown hair in a ponytail, [одежда по роли].
She [действие — не стоит, а делает]. Her gaze is slightly off-axis —
she's explaining to someone just off camera, not performing for a lens.

БЛОК 4 — LIGHTING
[Физический источник света + направление + атмосфера].

БЛОК 5 — SPECS
She says: "[ТОЧНЫЕ СЛОВА ХУКА]"
Photorealistic, documentary-style, natural camera movement.
Vertical frame, 9:16 portrait orientation.
No text, no watermarks, no logos.
```

---

## ЛОКАЦИИ ПОД TRAVEL-ТЕМАТИКУ

| Тема | Локация для промта |
|------|-------------------|
| Самолёт | economy seat, window behind, tray table or seat pocket in frame |
| Аэропорт досмотр | security conveyor belt, grey trays, scanner arch behind |
| Отель | front desk behind her / hotel room door / bed with luggage |
| Круиз | deck railing, ocean behind, balcony cabin door |
| Ресторан | table with menu/bill, candle, европейский интерьер |
| ATM | руки у экрана, улица за спиной |
| Паспортный контроль | customs counter, officer booth behind |
| Аптека | pharmacy shelf, medication bottles around |

---

## 7 NATURALISTIC LAYERS — КИРА ВЕРСИЯ

Каждый промт проходит 7 слоёв. Пропущенный слой = AI заполняет "средним значением" = шаблонный вид.

**LAYER 1 — CAMERA IDENTITY**
```
Shot on an iPhone held loosely at chest height — slight auto-exposure adjusting,
electronic stabilization fighting natural hand drift, occasional minor reframing.
```

**LAYER 2 — ENVIRONMENT TEXTURE (3-4 конкретных детали среды)**
❌ "inside an airport terminal"
✅ "inside a busy mid-size regional airport — scuffed linoleum floors, molded plastic chairs with worn armrests, departure boards clicking through updates, a Starbucks visible through the crowd"

**LAYER 3 — CHARACTER SPECIFICITY**
❌ "a woman in her 40s"
✅ "A woman in her early 40s, brown hair pulled back in a neat ponytail, navy flight attendant uniform with a small silver wings pin and a red neckerchief tied at the collar"

**LAYER 4 — ACTION SEQUENCE (движение, не статика)**
❌ "woman explaining something"
✅ "She pauses mid-reach, turns her head slightly toward the camera, and says — her voice low, like she's telling a secret to the person sitting next to her"

**LAYER 5 — LIGHT SOURCE (физический, named)**
✅ "Warm overhead cabin reading lights from above, casting a narrow pool of warm light on her face and uniform, the rest of the seat in soft shadow"

**LAYER 6 — TECHNICAL IMPERFECTIONS**
Добавлять 2-3 из:
- `slight auto-exposure adjusting`
- `autofocus briefly hunting before locking on her face`
- `slight natural camera breathing`
- `the frame drifts slightly right before correcting`
- `natural motion blur on hand gestures`

**LAYER 7 — EMOTIONAL ATMOSPHERE**
❌ "she looks concerned"
✅ "the specific low-voice urgency of someone sharing a secret they probably shouldn't — not dramatic, not performative, just real"

---

## VEO 3 ПРИМЕРЫ — TALKING HEAD

**СТЮАРДЕССА — самолёт (тема: грязь на борту):**
```
Shot on an iPhone held loosely at chest height by someone sitting two rows back —
slight auto-exposure adjusting to the cabin's overhead LED strip lights, natural drift
before electronic stabilization corrects. Inside an economy cabin mid-flight —
overhead bins closed and latched, window shades at half-mast, the ambient hum of
engines, a few passengers with neck pillows visible softly blurred in the background.
A woman in her early 40s, brown hair pulled back in a neat ponytail, navy flight
attendant uniform with a small silver wings pin and red neckerchief, sits in the
jump seat at the rear of the cabin, leaning slightly forward, elbows on knees.
She gestures toward the seat pocket in front of her as she speaks — her gaze
slightly off-axis, addressing someone just left of camera, the tone low and direct,
like sharing something real. The warm narrow beam of an overhead reading light
falls across her face and uniform. Autofocus briefly hunts before locking on her face.
She says: "Nobody cleans that pocket between flights. I stopped putting anything in
it my first month on the job."
Photorealistic, documentary-style footage, natural camera movement.
Vertical frame, 9:16 portrait orientation.
No text, no watermarks, no logos, no subtitles.
```

**ОТЕЛЬНЫЙ СОТРУДНИК — стойка регистрации (тема: скидки):**
```
Shot on an iPhone held loosely at waist height by a guest waiting nearby —
slight auto-exposure adjusting to the lobby's warm recessed lighting, the frame
drifting slightly before correcting. Inside the lobby of an ordinary mid-range hotel —
a marble-effect reception counter with two monitors visible behind it, a small wilting
flower arrangement to one side, warm amber light from ceiling fixtures overhead,
the sound of rolling luggage somewhere in the background.
A woman in her early 40s, brown hair loose at the shoulders, hotel staff navy blazer
with a silver name badge on the lapel, stands behind the counter. She leans forward
slightly on both hands, voice dropped, as if what she's about to say isn't something
guests usually know. Her gaze is off-axis — she's looking at the guest across the
counter, not at the camera.
She says: "If you ask for a quiet room when you check in — we usually upgrade you
for free. Most people never ask."
Warm recessed ceiling light catches the surface of the marble counter.
Photorealistic, documentary-style footage, slight natural handheld movement.
Vertical frame, 9:16 portrait orientation.
No text, no watermarks, no logos, no subtitles.
```

**TSA АГЕНТ — досмотр (тема: запрещённые предметы):**
```
Shot on an iPhone held at chest height — strong natural handheld movement,
auto-exposure adjusting to the harsh overhead fluorescents, the frame occasionally
drifting before correcting. Inside an airport security checkpoint — grey plastic trays
stacked at the end of the conveyor belt, the scanner arch visible behind, other
travelers moving through in soft blur.
A woman in her early 40s, brown hair in a tight ponytail, dark TSA uniform
with a badge lanyard, stands beside the conveyor belt. She rests one hand on
the belt edge, turns slightly toward the camera — the tone is direct, matter-of-fact,
the way someone explains something they've had to say a hundred times but means it.
She says: "Your laptop in a bag — we see it as a red flag. I pull those people
every single time."
Cold overhead fluorescent lighting, slightly institutional, flat and even.
Autofocus briefly adjusts before locking on her face.
Photorealistic, documentary-style footage.
Vertical frame, 9:16 portrait orientation.
No text, no watermarks, no logos, no subtitles.
```

**ТУРИСТКА-КИРА — ресторан (тема: счёт-ловушка):**
```
Shot on an iPhone held loosely at table level by someone sitting across —
slight auto-exposure adjusting to warm candlelight, natural camera drift.
Inside a mid-range European restaurant — white tablecloth with minor wine stain,
a bread basket with a few remaining pieces, a candle casting warm golden light,
other tables softly visible behind.
A woman in her early 40s, brown hair loose at the shoulders, a fitted dark blazer
over a simple top, holds an open menu in one hand and taps a specific line item
with her index finger. She glances up directly toward camera — for just a moment —
then back at the menu, her expression somewhere between amused and irritated.
She says: "The cover charge is buried here. It's on every table in Rome.
You're paying it whether you eat anything or not."
Warm candlelight from the table, cooler ambient restaurant lighting from above.
Natural motion blur on her hand gesture.
Photorealistic, documentary-style footage.
Vertical frame, 9:16 portrait orientation.
No text, no watermarks, no logos, no subtitles.
```

---

## СУБТИТРЫ — ТЕХНИЧЕСКИЕ ТРЕБОВАНИЯ

⚠️ Talking head рилс = субтитры ОБЯЗАТЕЛЬНО. Плашки НЕТ.

| Параметр | Значение |
|----------|----------|
| Шрифт | Montserrat Black Italic |
| Цвет | белый + чёрный outline 3px |
| Позиция | уровень груди, y≈700px на 1280px |
| Размер | 52-60px |
| Строка | по 3-5 слов, синхронно с речью |
| Музыка | ❌ ЗАПРЕЩЕНО — только оригинальный звук |

**FFMPEG субтитры:**
```bash
$FFMPEG -i input_talking_head.mp4 \
  -vf "subtitles=subs.srt:force_style='FontName=Montserrat-BlackItalic,
       FontSize=56,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,
       Outline=3,Bold=1,Italic=1,Alignment=2,MarginV=580'" \
  -c:v libx264 -c:a copy -crf 18 -preset fast \
  output_with_subs.mp4
```

---

## РЕЖИМ РЕМЕЙКА — РАБОТА С РЕФЕРЕНСАМИ

Когда пользователь кидает видео/скриншот/ссылку на вирусный рилс:

**Порядок работы:**
1. Проанализировать: что именно останавливает скролл (камера, одежда, локация, первые слова, движение рук)
2. Извлечь формулу (не копировать — адаптировать под Киру и нашу нишу)
3. NOVA пишет 2-3 варианта промта через 7 layers
4. VIC оценивает: 🔥 VIRAL / 🎬 STRONG
5. Показать пользователю только победителя

**Что анализировать в референсе:**
- Дистанция камеры (close-up / medium / wide)
- Одежда персонажа (что говорит о роли/доверии)
- Что в руках (предмет разговора)
- Направление взгляда (в камеру / чуть в сторону)
- Локация (насколько видна)
- Первые 3 слова (хук уже в речи или строится паузой)
- Темп речи (медленно/быстро)
- Эмоция (страх / инсайд / возмущение / любопытство)

---

## ЧТО ОСТАНАВЛИВАЕТ СКРОЛЛ В 2026 (research Sep 2026, USA)

Instagram смотрит на 1.0-секундный сигнал удержания — первые 24 кадра решают охват.

**Работает:**
- Prediction violation: визуал нормальный → речь говорит "это опасно" → мозг не может пролистнуть
- Identity threat: "They chose ME" / "You already did this" — личная причастность
- Physical insider: flight attendant / TSA / hotel housekeeper знает то что ты нет
- Действие в первом кадре — Кира уже что-то делает когда видео начинается
- Fast cuts каждые 3-4 секунды

**Убивает охват:**
- Статичная говорящая голова без движения фона
- Вступление ("Hey guys, today...")
- Пауза в первые 3 секунды
- Нейтральный фон

---

## OUTPUT FORMAT — 4 КЛИПА × 8 СЕК

```
TALKING HEAD REEL — [тема хука]
Hook emotion: [Fear / Awe / Injustice / Curiosity]
Character role: [роль]  |  Location: [локация]
Opening line: "[первые слова — первая секунда клипа 1]"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLIP 1 — VISUAL + AUDIO HOOK (0–8 сек)
⚡ Задача: стоп-скролл за 0.3 сек — визуально И аудиально
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VEO 3:
[Промт Clip 1 — 7 layers — действие с первого кадра]
↳ Duration: 8s | The clip begins mid-action
↳ Her first words land within second 1

🎯 KLING (fallback): [comma-separated]
🎬 RUNWAY: [Camera motion] + промт

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLIP 2 — INSIDER REVEAL (8–16 сек)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VEO 3:
[Промт Clip 2 — другой ракурс, жестикуляция, цифра]
↳ Duration: 8s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLIP 3 — DETAIL + PROOF (16–24 сек)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VEO 3:
[Промт Clip 3 — демонстрация правильно vs неправильно]
↳ Duration: 8s

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLIP 4 — SOLUTION + CTA (24–30 сек)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VEO 3:
[Промт Clip 4 — ближе к камере, уверенный тон, CTA]
↳ Duration: 8s (обрезать до 6s при монтаже)
↳ Final words: "Comment SAFETY and I'll send you 44 more."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚫 NEGATIVE PROMPT (только для Kling / Runway / Pika — НЕ для Veo 3):
text, watermark, logo, CGI, studio lighting, ring light, AI artifacts,
distorted hands, extra fingers, advertisement look, static waist-up pose,
direct unbroken eye contact throughout, neutral background, green screen

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUBTITLES: Montserrat Black Italic · 56px · white + black outline 3px · y≈700px
AUDIO: Оригинальный голос только — NO music
EDIT: 4 клипа склеить → обрезать до 30 сек → добавить субтитры
TEAM: NOVA ✅ | VIC 🔥 VIRAL / 🎬 STRONG | Mike 🟢 | Red ✅ SURVIVED
```

---

## НЕГАТИВНЫЕ ПРОМТЫ ДЛЯ TALKING HEAD (Kling / Runway / Pika)

```
text, watermark, logo, subtitle, CGI, studio lighting, ring light,
professional filming setup, obvious AI artifacts, uncanny valley,
distorted hands, extra fingers, advertisement look, static pose,
direct unbroken eye contact with camera, neutral background, green screen,
empty studio, speaking directly to lens for entire duration
```

---

## КОГДА ИСПОЛЬЗОВАТЬ ЭТОТ СКИЛЛ

| Ситуация | Действие |
|----------|----------|
| Рилс требует говорящего персонажа с речью | → `kira-talking-head` |
| Пользователь кидает референс-видео | → Анализ + ремейк под Киру |
| Нужен insider reveal от конкретной роли (TSA, стюардесса, chef) | → `kira-talking-head` |
| B-roll рилс без речи | → `ai-video-prompts` (обычный скилл) |
| Нет подходящего footage клипа для b-roll | → `ai-video-prompts` |

---

## ПОСЛЕ ГЕНЕРАЦИИ

1. Пользователь генерирует клип в Veo 3 / Kling
2. Footage-manager логирует как `talking_head_[тема]_[дата]`
3. Субтитры: подготовить `.srt` файл синхронно с речью
4. Рендер: `-map 1:a` из оригинального клипа — никакой музыки
5. Quality-check → videotool-ready → push
