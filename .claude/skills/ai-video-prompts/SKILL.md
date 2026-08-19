---
name: ai-video-prompts
description: Generate AI video prompts for @thekiramethod reels. Use when stock footage library has no matching clip OR when you want a custom visual that perfectly fits the hook's emotion. Run after kira-hooks — finalized hook required before generating visual. Output is ready-to-paste prompts for Veo 3, Kling, Runway, and Pika. The user generates the actual video themselves.
---

# AI Video Prompt System — KIRA
## Tools: Veo 3 ⭐ · Kling 2.1 · Runway Gen-4 · Pika 2.2
## Niche: Travel · Life Hacks · Food · Health · Money (USA, 35+)

---

## МИССИЯ

Когда в библиотеке `/home/user/preland/footage/` нет подходящего клипа — команда создаёт его.

Ты даёшь тему хука → NOVA + VIC генерируют промты → ты вставляешь промт в инструмент → получаешь клип → footage-manager логирует → kira-hooks body clearance → рендер.

**Аудит NOVA + VIC запускается ВНУТРИ — пользователь видит только финальные промты после их ✅.**

---

## КОМАНДА ВИДЕО-ПРОМТОВ

### 🤖 NOVA — AI Video Prompt Engineer (20 лет опыта)
*Пришла из кинопроизводства. Знает Kling, Runway, Pika от и до. Каждый промт — это сцена, эмоция и техника в одном предложении.*

Nova's background: 20 лет в кинопроизводстве (документалистика, реклама, клипы) → перешла в AI video в 2023, когда инструменты стали достаточно хорошими для реального контента. Тест 5000+ промтов. Знает что работает, что генерирует артефакты, что проходит без флага.

Nova's job: **Написать промты, по которым зритель не поймёт — это AI или реальная съёмка.**

Nova спрашивает:
- "Stock library `/footage/` — есть что-то близкое? Если да — зачем тратить генерации?"
- "Первый кадр: что зритель видит за 0.3 секунды ДО того как прочёл текст? Это и есть visual hook."
- "Эмоция хука: Fear / Awe / Injustice / Curiosity? Каждая требует разный visual language."
- "AI-риск артефактов: лицо крупным планом = ВЫСОКИЙ. Руки с предметами = СРЕДНИЙ. Среда без людей = НИЗКИЙ."
- "5-секундный seamless loop возможен? Финальный кадр должен перетекать в начальный без разрыва."
- "Text zone чистая? Человек в центре, верхняя 1/4 и нижняя 1/4 кадра свободны для overlay."

Nova's 20-летние правила (выжимка):
- `handheld` + `slightly shaky` + `natural light` + `documentary style` = реализм. Никогда "professional" или "studio".
- Описывай ЭМОЦИЮ сцены, не только её. "Nervous energy" > "person standing at counter".
- **Veo 3** (главный инструмент): нарративные ПРЕДЛОЖЕНИЯ, не keyword-список. Пять блоков: Camera → Scene → Subject+Action → Lighting → Style+Specs. Явно указывать "vertical frame, 9:16 portrait". Добавлять "no dialogue, no voiceover, ambient sound only" (Veo 3 генерирует аудио — для нас оно режется при рендере). Нет отдельного negative prompt — всё в основном тексте.
- Kling: comma-separated descriptors, cinematic precision. Лучший реализм после Veo 3.
- Runway: начинать с `[Camera motion]` (Slow push in / Pan right / Track forward). Лучший контроль движения.
- Pika: conversational natural language. Самая быстрая итерация для теста концепта.
- Negative prompt для Kling/Runway/Pika — ВСЕГДА: `text, watermark, logo, CGI, studio lighting, obvious AI artifacts, distorted hands, extra fingers, advertisement look`

---

### 🎬 VIC — Visual Director & Market Researcher
*Просматривает 5+ часов IG, TikTok, YouTube Shorts в день. Знает каждый визуальный тренд, каждое клише, каждый shot который работает ЭТУ неделю в travel, health, food, money нишах.*

VIC's job: **Убить любой визуал который видели 1000 раз. Одобрить только то, что останавливает скролл до того как прочтут текст.**

VIC спрашивает:
- "Visual pattern interrupt: если убрать ВЕСЬ текст — этот клип сам по себе заставит кого-то остановиться?"
- "Видел я этот shot в своей ленте за последние 48 часов? Если да → это обои, не хук."
- "Тренд этой недели поддерживает или мешает этому концепту?"
- "Атмосфера клипа СООТВЕТСТВУЕТ эмоции хука? Fear needs tension. Curiosity needs mystery. Awe needs scale."
- "Body clearance риск? Текст встанет сверху или снизу без перекрытия action zone?"

VIC's вердикт:
- 🔥 VISUAL VIRAL — "Останавливает скролл визуально, до текста. Генерировать немедленно."
- 🎬 VISUAL STRONG — "Сильный выбор. Подходит для этого хука."
- ⚠️ VISUAL WEAK — "Видел слишком часто. Правь промт: [конкретное изменение]."
- ❌ CHANGE CONCEPT — "Неправильный визуал для этого хука. Начни с: [альтернатива]."

**VIC's rule: "Видео — это первый хук. Текст — второй. Если видео слабое — текст его не спасёт."**

---

## ПРАВИЛА ВИДЕО ДЛЯ НАШЕЙ НИШИ

### Rule 1 — Первый кадр = visual pattern interrupt
До текста, до хука — визуал должен создать паузу. "Что это?" или "Подождите, что происходит?"

Работает:
- Необычный ракурс на знакомую сцену (аэропорт снятый от пола)
- Движение к камере (человек идёт прямо на зрителя)
- Крупный план неожиданно близко (чек, таблетки, провод)
- Контраст (красивое место + тревожная деталь)

Не работает:
- Стандартный stock-footage вид (generic city skyline, empty office, sunset)
- Статика без движения и без субъекта
- Красиво, но понятно с первого взгляда — нет вопроса, нет остановки

### Rule 2 — Emotion match

| Формула хука | Эмоция | Нужный визуал |
|--------------|--------|----------------|
| Formula 1, 2 (Warning/Loss) | Страх, тревога | Темнее, closer shot, tension в сцене |
| Formula 3 (Command Interrupt) | Срочность, danger | Action, motion, urgency |
| Formula 4, 7 (Curiosity Gap) | Любопытство | Загадочная сцена, partially hidden info |
| Formula 5 (Injustice) | Злость, справедливость | Confrontational angle, clear subject |
| Formula 8, 9 (Health/Home) | Беспокойство, awe | Close-up objects, kitchen/clinical setting |

### Rule 3 — Text zones чистые
Человек / объект занимает ЦЕНТР кадра (y: 480–1440px). Верхняя 1/4 (y: 0–480px) и нижняя 1/4 (y: 1440–1920px) — чистые.

### Rule 4 — Выглядит как реальное видео на iPhone
НЕ "кинематографично". НЕ "студийное освещение".
Ключевые слова реализма: `handheld` / `slightly shaky` / `natural light` / `documentary style` / `shot on phone`

### Rule 5 — 10-second clip, seamless loop preferred
Оптимальная длина генерации — 10 секунд. Если клип короче — будет залуплен при рендере.
Для loop: используй движения которые зацикливаются естественно: конвейер, ходьба по коридору, медленный pan, волны, вращение.

---

## VEO 3 — ГЛАВНЫЙ ИНСТРУМЕНТ (Google DeepMind, 2025)

**Доступ:** Google VideoFX → labs.google.com/fx/tools/video-fx | Google Flow | Vertex AI API

**Почему Veo 3 первый:**
- Лучшая фотореалистичность среди всех инструментов (2025-2026)
- Лучшее движение людей — натуральные жесты, походка, мимика
- Нативное аудио (мы его режем `-an` при рендере — не мешает, не помогает)
- Вертикальный формат 9:16 поддерживается нативно
- Минимум AI-артефактов при правильном промте

**Duration в Veo 3:**
- VideoFX генерирует до 8 секунд за раз
- Для 10-секундного рилса: сгенерировать 8s → рендер залупит до 10s автоматически
- Альтернатива: Vertex AI API — там можно запросить duration через параметры

---

### ⭐ СТРУКТУРА ПРОМТА VEO 3 — 5 блоков (обязательный порядок)

Veo 3 понимает ПРЕДЛОЖЕНИЯ, не keyword-списки. Каждый блок — одно-два предложения.

```
БЛОК 1 — CAMERA (как снято)
Handheld close-up slowly pushing in toward [subject].
POV shot from [position] slowly moving forward.
Slow pan from left to right across [scene].
Wide shot gradually tightening to medium.

БЛОК 2 — SCENE (где, что за окружение)
Inside a crowded airport terminal with moving baggage carousel.
In a modern hotel lobby with marble counters and warm chandelier lighting.
In a home kitchen, under-sink cabinet just opened revealing cleaning supplies.

БЛОК 3 — SUBJECT + ACTION + EMOTION (кто, что делает, с какой эмоцией)
A woman in her mid-30s reaches toward the belt, her expression tense and cautious.
A pair of hands nervously holds a long paper receipt, fingers slightly trembling.
A traveler stands at a customs counter, looking worried as an officer examines documents.

БЛОК 4 — LIGHTING + ATMOSPHERE (свет и настроение)
Overhead fluorescent terminal lights cast a cool, slightly harsh institutional glow.
Warm morning window light enters from the left, soft and natural.
The atmosphere feels tense, slightly claustrophobic, urgent.

БЛОК 5 — STYLE + SPECS (стиль и технические требования)
Documentary-style footage with slight natural handheld camera movement. Photorealistic.
Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient sound only.
No text, no watermarks, no logos, no subtitles on screen.
```

**Veo 3 ЗАПРЕЩЕНО писать:**
- ❌ Keyword-списки через запятую (это для Kling, не Veo 3)
- ❌ "Ultra HD", "8K", "cinematic 4K" — это не помогает Veo 3
- ❌ "photorealistic render" — слово "render" триггерит CGI-look
- ❌ Отдельный negative prompt (нет такого поля в VideoFX) — пиши ограничения в тексте: "no text", "no watermarks"

**Veo 3 РАБОТАЕТ ЛУЧШЕ с:**
- ✅ "documentary-style footage" — включает реализм
- ✅ "slight natural camera movement" — естественное качание
- ✅ "ambient sound only, no dialogue" — чистый аудио-трек (нам не нужен, но подсказка Veo 3)
- ✅ описание эмоции персонажа — Veo 3 её воспроизводит в мимике
- ✅ "vertical frame, 9:16 portrait orientation" — вертикаль

---

### VEO 3 ПРИМЕРЫ ПО НИШАМ

**AIRPORT — luggage belt (Fear):**
```
VEO 3:
Handheld close-up shot slowly pushing in toward a moving airport baggage carousel. Inside a busy arrival terminal with overhead fluorescent lighting. A pair of hands nervously reaches forward toward a black suitcase as it passes on the moving belt, fingers slightly tense and hesitant. The cool, slightly harsh airport lighting creates an institutional, urgent atmosphere. Documentary-style footage with slight natural camera movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient airport sound only. No text, no watermarks, no logos on screen.
```

**HOTEL — front desk dispute (Injustice):**
```
VEO 3:
Medium shot slowly pushing in toward a hotel reception desk. Inside a hotel lobby with warm chandelier lighting and marble counter. A woman in her 40s stands at the desk holding a paper receipt, her expression frustrated and confused, gesturing toward the receptionist across the counter. The warm lobby lighting contrasts with the tension in her body language. Documentary-style footage with slight natural handheld movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient lobby sound only. No text, no watermarks, no logos.
```

**KITCHEN — cabinet reveal (Health Warning):**
```
VEO 3:
POV shot slowly pushing forward toward a kitchen cabinet as the door swings open. Inside a real home kitchen with warm natural light from a nearby window. A hand reaches into the cabinet revealing rows of spice jars and supplement bottles arranged on shelves. The warm, slightly cluttered kitchen environment feels familiar and domestic. The camera movement is slow and deliberate, as if discovering something unexpected. Documentary-style footage, slightly handheld. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient kitchen sound only. No text, no watermarks, no logos.
```

**PHARMACY — pill bottle (Health/Money):**
```
VEO 3:
Close-up shot slowly pushing in on a prescription medication bottle held in two hands. Inside a pharmacy or home bathroom, with neutral clinical overhead lighting. The hands carefully examine the label, turning the bottle slightly. The person's expression, partially visible, shows mild concern or realization. Clean, clinical atmosphere with no dramatic lighting. Documentary-style, slight natural camera movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient sound only. No text, no watermarks, no logos, no readable text on the bottle label.
```

**HOME DANGER — extension cord (Fear):**
```
VEO 3:
Macro close-up shot slowly pushing in toward an overloaded power extension strip on the floor. Inside a home living room or bedroom with warm indoor lamp lighting. Multiple thick power cords are plugged into a single strip, with a space heater cord prominently visible among them. The close framing and slow camera push creates a slightly ominous, cautionary atmosphere. Documentary-style footage with subtle handheld movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient room sound only. No text, no watermarks, no logos.
```

**MONEY — credit card payment (Injustice/Money):**
```
VEO 3:
Macro close-up shot slowly pushing in toward hands inserting a credit card into a payment terminal. Inside a retail store with neutral overhead lighting. The hands move with slight hesitation, the terminal screen visible. The framing is tight, focusing on the card and terminal, with the store environment softly blurred behind. A subtle sense of uncertainty in the hand movement. Documentary-style footage, natural camera movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient store sound only. No text, no watermarks, no logos, no readable text on screen.
```

**AIRPORT CUSTOMS — money confiscation (Fear + Injustice):**
```
VEO 3:
Medium static shot at an airport customs inspection counter. Inside an official customs area with cool institutional overhead fluorescent lighting. A customs officer in uniform reviews travel documents handed across the counter by a traveler standing opposite. The traveler's expression is tense and worried, watching carefully. The atmosphere is formal, slightly intimidating, institutional. Documentary-style footage with minimal camera movement. Photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient airport sound only. No text, no watermarks, no logos.
```

---

## ПРОМТ-ШАБЛОНЫ ПО НИШАМ

### ✈️ AIRPORT / FLIGHT

**Luggage belt — тревога / theft warning (Fear):**
```
KLING:
Close-up of moving airport baggage claim belt, multiple suitcases passing, a pair of hands nervously reaching toward a bag, fluorescent terminal overhead lighting, slightly handheld camera movement, tense worried atmosphere, documentary style, photorealistic, no text no watermarks, 10 seconds vertical 9:16

RUNWAY:
[Slow push in] Crowded airport baggage carousel, bags circulating, person's hands visible reaching forward with anxious energy, cool fluorescent overhead lights, authentic documentary feel, photorealistic, no logos

PIKA:
Airport baggage belt with suitcases moving past in both directions, someone reaching out to grab their bag, slight nervous energy in the movement, real airport terminal, natural fluorescent lighting, handheld documentary feel, no text
```

**Customs — money confiscation (Fear + Injustice):**
```
KLING:
Medium shot of airport customs desk, official in uniform reviewing travel documents, traveler standing across looking tense and worried, cool institutional overhead lighting, slight handheld motion, tense confrontational atmosphere, documentary style, photorealistic, no text

RUNWAY:
[Static] Two-shot at customs counter, officer examining passport and forms, traveler with concerned expression, blue-tinted official lighting, real-life documentary, photorealistic

PIKA:
Airport customs checkpoint, traveler handing documents to officer at counter, subtle nervous body language, institutional lighting, authentic travel documentary style, no watermarks
```

**Flight crew single-file (Curiosity Gap):**
```
KLING:
Flight crew in matching uniforms walking in tight single-file formation through busy airport terminal corridor, rolling carry-on bags, view from behind, wide concourse with natural daylight from windows, slow follow shot, documentary style, photorealistic, no text

RUNWAY:
[Track forward] Flight attendants walking in formation down terminal hallway, uniform attire, bags rolling, shot from behind, natural terminal lighting, observational documentary feel
```

**Gate area — bump / compensation (Injustice/Money):**
```
KLING:
Close-up of airport departure board showing GATE CHANGED status, person's face partially visible looking up with frustrated expression, warm terminal lighting, slightly handheld, realistic travel documentary, photorealistic, no text no logos

RUNWAY:
[Slow push up] Airport gate departure display, status updating, passenger reaction visible, terminal ambient light, authentic travel content style
```

### 🏨 HOTEL

**Front desk dispute (Injustice):**
```
KLING:
Person at luxury hotel front desk holding a paper receipt and looking confused/frustrated, receptionist behind marble counter, warm hotel lobby lighting, medium two-shot, subtle confrontational atmosphere, handheld documentary, photorealistic, no text

RUNWAY:
[Slow push in] Hotel reception desk interaction, guest examining bill with concern, elegant lobby background, warm chandelier light, realistic hotel scenario

PIKA:
Hotel check-in counter, guest and receptionist in conversation, guest looking at receipt with visible frustration, warm ambient hotel lobby lighting, authentic documentary style
```

**Hotel room reveal (Curiosity):**
```
KLING:
POV shot of key card being inserted into hotel door lock, door swinging open to reveal hotel room interior, warm lamp lighting inside contrasting with corridor, slightly shaky handheld, realistic first-person travel documentary, photorealistic, no text

RUNWAY:
[Push forward] Hotel room door opening from outside, key card contact, room interior revealed, realistic hotel lighting
```

### 💰 MONEY / CONSUMER

**Credit card dispute (Injustice + Money):**
```
KLING:
Close-up of hands inserting credit card into payment terminal, terminal screen visible, natural retail store lighting, macro-style tight focus, slight tension in the movement, photorealistic, handheld, documentary style, no text no logos

RUNWAY:
[Macro push in] Credit card terminal with amount displayed, hands approaching with slight nervous energy, sharp focus, warm retail lighting, realistic

PIKA:
Hands inserting credit card into payment reader at checkout, close-up shot, real store environment lighting, subtle anxious energy in hands, no text or watermarks
```

**Receipt with big number (Surprise + Injustice):**
```
KLING:
Close-up of hands unfolding a long paper receipt, clearly showing the bottom total area, expression of mild shock partially visible, warm indoor lighting from above, handheld slight motion, photorealistic, documentary style, no text

RUNWAY:
[Slow push in] Long paper receipt being unfolded in hands, total visible at bottom, surprised reaction from person holding it, warm light
```

**GoodRx / pharmacy savings (Money + Awe):**
```
KLING:
Close-up of prescription medication bottle on pharmacy counter, pharmacist hands and register visible in background slightly blurred, neutral pharmacy lighting, tight focus on bottle, documentary style, photorealistic, no text no logos

RUNWAY:
[Macro push in] Prescription bottle on white pharmacy counter, blurred pharmacy environment behind, clinical fluorescent lighting, realistic pharmaceutical setting

PIKA:
Pharmacy counter with prescription medicine bottles, clinical white lighting, realistic pharmacy environment, handheld documentary style
```

### 🍎 FOOD / HEALTH

**Kitchen cabinet spices (Health Warning):**
```
KLING:
Kitchen cabinet door opening to reveal rows of spice jars and supplement bottles arranged on shelves, person's hand reaching in selecting a jar, warm kitchen window natural lighting, slight handheld motion, realistic modern kitchen setting, photorealistic, no text

RUNWAY:
[Slow reveal pan left] Open kitchen cabinet interior, various spice bottles arranged on shelves, hand reaching in, warm natural light from nearby window, realistic

PIKA:
Kitchen cabinet opening to show collection of spice jars, warm kitchen lighting from window, person reaching in to get a jar, realistic home setting, no watermarks
```

**Medication / prescription (Health Fear):**
```
KLING:
Close-up of hands holding a prescription medication bottle, examining the label carefully, pharmacy or bathroom counter surface visible, neutral clinical lighting, slight handheld motion, documentary style, photorealistic, no text no logos

RUNWAY:
[Macro push in] Prescription bottle in hands, label visible but text blurred, slight movement, clinical overhead lighting, realistic

PIKA:
Person holding prescription pill bottle and reading label carefully, bathroom or kitchen counter, natural indoor lighting, handheld documentary feel
```

**Olive oil (Food Fact + Awe):**
```
KLING:
Close-up of multiple olive oil bottles lined up on grocery store shelf, person's hand reaching to pick one, examining the label, supermarket aisle fluorescent lighting, slight handheld camera sway, documentary style, photorealistic, no text

RUNWAY:
[Slow pan across] Supermarket shelf with olive oil bottles, hand reaching in to pick one and check label, cool retail fluorescent lighting, observational documentary
```

**Coffee timing (Health Habit):**
```
KLING:
Close-up of coffee mug being filled from coffee maker early morning, dark kitchen with warm window light beginning, steam rising, person's hands visible, slightly shaky handheld, warm morning atmosphere, documentary style, photorealistic, no text

RUNWAY:
[Slow push in] Morning coffee ritual, mug being filled, soft morning window light, steam wisps, realistic home kitchen setting
```

### 🏠 HOME DANGER

**Cleaning products (Fear + Danger):**
```
KLING:
Under-kitchen-sink cabinet door opening, revealing cleaning product bottles crammed together including spray bottles and jugs, person's hand reaching in, fluorescent kitchen light overhead, slightly handheld, tense curiosity atmosphere, documentary style, photorealistic, no text

RUNWAY:
[Slow push in] Under-sink cabinet interior revealed, cluttered cleaning bottles of different brands visible, cool overhead kitchen light, slight sense of concern in the reveal

PIKA:
Kitchen under-sink cabinet opening to show cleaning supplies, bottles visible, realistic home setting, natural kitchen lighting
```

**Extension cord / space heater (Fear + Danger):**
```
KLING:
Close-up of multiple power cords plugged into a single overloaded extension strip on floor, space heater cord prominently visible, warm indoor room lighting, macro-style tight focus, subtle tension, documentary style, photorealistic, no text

RUNWAY:
[Macro push in] Overloaded extension strip on floor, multiple thick cords, space heater cord visible, warm lamp light, realistic danger scenario
```

**Bleach products (Extreme Fear):**
```
KLING:
Close-up of two common cleaning spray bottles side by side on counter, both labels partially visible, kitchen counter setting, fluorescent overhead lighting, tight shot with slight handheld, documentary style photorealistic, no text

RUNWAY:
[Static close-up] Two cleaning product bottles on kitchen counter, slightly ominous framing, cool fluorescent light, realistic kitchen setting
```

### ⚖️ RIGHTS / CONSUMER LAW

**Security deposit / landlord (Rights + Money):**
```
KLING:
Close-up of person writing a check at a table, official-looking document partially visible underneath, warm indoor desk lighting, slightly handheld, focused documentary style, photorealistic, no text or logos

RUNWAY:
[Slow push in] Hands writing check at desk, rental agreement document visible beneath, warm lamp light, documentary feel, realistic

PIKA:
Person signing or writing a check at a home desk, document on table, warm natural room light, realistic everyday scenario
```

**Airline bump compensation (Money + Awe):**
```
KLING:
Airport gate area, overhead announcement board showing flight status, stressed passengers waiting in chairs, one person approaching gate agent desk, warm-cool terminal mixed lighting, wide observational shot, documentary style, photorealistic, no text

RUNWAY:
[Slow pan] Airport gate waiting area, passengers and departure board visible, traveler approaching agent at desk, authentic travel documentary atmosphere
```

---

## NEGATIVE PROMPT (универсальный — вставлять во все инструменты)

```
text, watermark, logo, subtitle, caption, overlay text, animation, cartoon, CGI, rendered look, 3D render, studio lighting, artificial lighting, ring light, professional filming setup, obvious AI artifacts, uncanny valley effect, distorted hands, extra fingers, floating objects, perfect symmetry, advertisement look, stock footage aesthetic, Getty watermark, Shutterstock watermark, iStock look
```

---

## АУДИТ — ВНУТРИ (пользователь не видит черновики)

NOVA пишет 2–3 варианта промтов внутри.
VIC оценивает каждый: 🔥 VIRAL / 🎬 STRONG / ⚠️ WEAK / ❌ CHANGE.
Mike проверяет: этот тип визуала работает в нашей нише с аудиторией 35+?
Red пытается убить концепт: "Видел 100 раз? Чем отличается?"

Только после VIC 🎬 STRONG+ и Red ✅ SURVIVED — показать пользователю.

---

## OUTPUT FORMAT — финальный вывод

```
AI VIDEO BRIEF — [тема хука]
Hook emotion: [Fear / Awe / Injustice / Curiosity]
Visual concept: [одна фраза — что зритель видит в первые 0.3 секунды]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⭐ VEO 3 (главный — labs.google.com/fx/tools/video-fx):
[Готовый промт — 5 блоков предложениями, вставить напрямую]
↳ Duration: запросить максимум (8s) → рендер залупит до 10s
↳ No separate negative prompt — ограничения уже в тексте

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 KLING 2.1 (если Veo 3 недоступен — лучший реализм):
[Готовый промт — comma-separated descriptors]

🎬 RUNWAY GEN-4 (лучшее движение камеры):
[Camera: тип движения] + [готовый промт]

⚡ PIKA 2.2 (быстрый тест концепта):
[Готовый промт — natural language]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚫 NEGATIVE PROMPT (только для Kling / Runway / Pika — НЕ для Veo 3):
text, watermark, logo, subtitle, CGI, studio lighting, obvious AI artifacts, uncanny valley, distorted hands, extra fingers, advertisement look, stock footage aesthetic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TECH SPECS:
- Duration: 10 seconds | Resolution: 1080×1920 (9:16 вертикальное)
- Veo 3 generates 8s max → loop to 10s in render (-stream_loop -1)
- После генерации: footage-manager → залогировать как custom clip
- Затем: kira-hooks body clearance → рендер

TEAM: NOVA ✅ | VIC 🎬 [VIRAL/STRONG] | Mike 🟢 | Red ✅ SURVIVED
```

---

## 🎭 SPECTACLE MODE — Визуальный спектакль (новый стиль)

### Что такое Spectacle Mode

Инспирировано @evanrosenman (156M / 128M / 106M views).

**Принцип:** Видео = первый хук. Текст не нужен чтобы остановить скролл. Зритель видит что-то **физически невозможное** — но моментально понятное. Мозг кричит "подождите, что?!" раньше чем текст прочитан.

**Documentary Mode** (текущий): реалистично, мог быть снят на iPhone  
**Spectacle Mode** (новый): физика нарушается чтобы ВИЗУАЛИЗИРОВАТЬ правду хука

Разница:
| Documentary | Spectacle |
|------------|-----------|
| "Человек у стойки отеля с квитанцией" | "Долларовые купюры буквально вылетают из стены когда он прикасается к полотенцу" |
| 65-78% hold rate | Потенциал 80%+ |
| Хук = текст + видео вместе | Видео ЭТО и есть хук |
| Подходит для всех форматов | Убийца для Formula 3, 5, 9 (Command / Injustice / Pattern Interrupt) |

---

### Правила промтинга для Spectacle Mode (Veo 3)

**Ключевой принцип:** Сохранять реалистичную среду — и вводить ОДНО невозможное событие. Контраст реальности и нереальности = шок.

**Формула:**
```
Реальная обычная сцена + одно физически невозможное явление которое ПОКАЗЫВАЕТ правду хука + slow motion чтобы дать зрителю время обработать увиденное
```

**Запрещено в Spectacle Mode:**
- ❌ CGI-вид, картунность, мультяшность — это убивает эффект
- ❌ Слишком много невозможных элементов — один эффект, максимум
- ❌ Нарратив от первого лица — показываем ФАКТ, не персонажа
- ❌ Слова "magical" или "fantasy" — это уводит в сказку

**Работает:**
- ✅ "as if demonstrating the invisible force" — невидимая сила стала видимой
- ✅ "in slow motion" — даёт мозгу время осознать невозможное
- ✅ "photorealistic environment" — обычная среда усиливает шок невозможного
- ✅ "the effect happens naturally, as if this is normal physics" — не подчёркивать трюк
- ✅ Деньги, газ, свет, тепло — это всё можно визуализировать "невидимыми" силами

---

### VEO 3 SPECTACLE ПРИМЕРЫ ПО НИШАМ

**HOTEL — towel charge ($40 вылетает из кармана):**
```
VEO 3 SPECTACLE:
Slow-motion close-up shot inside a hotel bathroom as a guest's hand gently touches a neatly folded white towel on the rack. At the moment of contact, several dollar bills visibly peel off the countertop nearby and float upward into the air, as if drawn by an invisible magnetic force, disappearing off-screen. The hotel bathroom environment is photorealistic and ordinary — warm lighting, marble tiles, nothing unusual except the floating currency. The movement of the money is slow, deliberate, inevitable. Documentary-style footage with natural handheld movement, photorealistic. Vertical frame, 9:16 portrait orientation. No dialogue, no voiceover, ambient bathroom sound only. No text, no watermarks.
```

**CUSTOMS — money confiscation (купюры засасывает из чемодана):**
```
VEO 3 SPECTACLE:
Slow-motion medium shot of a traveler opening their suitcase at an airport customs counter. As the lid opens, dollar bills begin to rise slowly from inside the bag on their own, floating upward in a steady stream, as if being pulled by an invisible vacuum toward the customs officer across the counter. The traveler watches with visible shock, unable to stop the movement. The airport customs area is completely realistic — fluorescent lighting, official uniforms, standard counter. Only the money moves impossibly. Documentary-style footage, natural camera movement, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient airport sound only. No text, no watermarks.
```

**BLEACH + WINDEX — toxic gas visible (яд становится видимым):**
```
VEO 3 SPECTACLE:
Slow-motion close-up shot on a kitchen counter as two common cleaning spray bottles are placed next to each other. A faint, sickly green-tinted mist begins to rise slowly from the gap between the two bottles, spreading across the counter surface and drifting upward into the kitchen air. The kitchen is completely ordinary — warm natural window light, familiar counter surface. Only the gas is unusual, visible, and spreading. The effect is subtle and deeply unsettling. Documentary-style footage, slight natural handheld movement, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient kitchen sound only. No text, no watermarks.
```

**EXTENSION CORD — heat becomes visible (жар становится видимым):**
```
VEO 3 SPECTACLE:
Macro close-up slow-motion shot of an overloaded power extension strip on a living room floor with a space heater plugged in. Gradually, a faint orange-red glow begins to emanate from inside the cord itself, pulsing slightly, intensifying with each second, as if the heat building inside is becoming visible through the plastic. The surrounding room is completely normal — carpet, furniture, warm lamp light. Only the cord glows with internal heat. The effect grows slowly, making it more unsettling. Documentary-style, handheld, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient room sound only. No text, no watermarks.
```

**SPICE — potency draining in sunlight (специя тускнеет на глазах):**
```
VEO 3 SPECTACLE:
Macro close-up slow-motion shot of a spice jar sitting on a sunny kitchen windowsill. As the sunlight hits the jar directly, the color of the spice inside visibly fades — starting from the edges touching the glass, spreading inward, the vibrant red or orange slowly becoming pale and grey over several seconds. The kitchen environment is warm, real, everyday. Only the spice changes, draining of color in real time. Documentary-style footage, slightly handheld, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient kitchen sound only. No text, no watermarks.
```

**AIRLINE BUMP — cash appears at gate (деньги материализуются из посадочного):**
```
VEO 3 SPECTACLE:
Slow-motion close-up of hands holding a boarding pass at an airport gate. As the flight status board behind shows CANCELLED or DELAYED, the boarding pass in the hands slowly transforms — dollar bills begin to appear underneath it, one by one, as if the cancelled ticket is converting directly into cash in real time. The gate area is completely realistic — fluorescent terminal lighting, departure board, gate agent desk in background. Only the money materializing is impossible. Documentary-style, natural camera movement, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient terminal sound only. No text, no watermarks.
```

**FRIDGE — bacteria visual (невидимое становится видимым):**
```
VEO 3 SPECTACLE:
Slow-motion POV shot of a refrigerator door swinging open. As the light inside illuminates the food shelves, a faint shimmer or heat-haze effect rises from the food containers, visualizing the warmth — the temperature that should not be there. Leftovers and fresh food sit normally on shelves, but the rising heat shimmer creates a subtle, unsettling glow above each item. The fridge is completely realistic and ordinary. Documentary-style, handheld, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient fridge hum only. No text, no watermarks.
```

**PHARMACY — price difference (таблетка раздваивается):**
```
VEO 3 SPECTACLE:
Macro close-up slow-motion shot of a single white pill on a pharmacy counter. Gradually, the pill splits into two identical pills side by side — one stays surrounded by a small stack of dollar bills, the other sits alone with just coins beside it. The two pills are identical. The price difference is visible in the objects surrounding them. The counter surface is a real pharmacy — clinical, fluorescent-lit, clean. The split happens slowly and inevitably, like a demonstration. Documentary-style, natural handheld, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient pharmacy sound only. No text, no watermarks.
```

---

---

### 🚢 CRUISE — SPECTACLE ПРОМТЫ

**#1 — Giant storm wave (Fear · Formula 3 Command Interrupt):**
```
VEO 3 SPECTACLE:
Wide slow-motion shot from the stern of a massive cruise ship, camera low and slightly shaking as if held by someone gripping a railing. The open ocean stretches ahead, and on the horizon an enormous dark wave — fifteen to twenty meters high — rises slowly and moves toward the ship. Inside the ship through the portholes, warm yellow cabin lights glow, completely unaware. The contrast between the cozy interior light and the approaching wall of black water is the visual hook. The wave moves slowly, inevitably, filling the frame. The sky is dark grey, the ocean surface rough. Documentary-style footage with strong natural camera shake from wind and swell, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient ocean and wind sound only. No text, no watermarks, no dialogue.
```
Hook fit: "Never Book This Cabin / In A Storm"  
Mike: 🔥 VIRAL — Maya шлёт мужу перед круизом

---

**#2 — Hidden fees fly from ticket (Injustice · Formula 5):**
```
VEO 3 SPECTACLE:
Slow-motion close-up of hands holding a glossy cruise line brochure showing a price of $800. As the fingers hold the brochure steady, coins and dollar bills begin to peel away from behind the pages one by one, rising upward into the air in a slow steady stream, as if hidden charges are physically escaping the fine print. The bills float upward and disappear off-screen. In the background, a blurred living room with warm lamp light — someone at home planning a vacation. The brochure remains in hand, unchanged on the surface, as the money continues to rise. The effect is inevitable and impossible to stop. Documentary-style handheld footage, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient room sound only. No text, no watermarks.
```
Hook fit: "My $800 Cruise / Cost $1,400 Before Boarding"  
Mike: 🔥 VIRAL — конкретные цифры + Injustice = Formula 5 = 3M views formula

---

**#3 — Private island reveal (Curiosity + Injustice · Formula 4/7):**
```
VEO 3 SPECTACLE:
Slow cinematic drone-style shot beginning at water level, looking at a picture-perfect tropical beach with white sand and palm trees — the cruise line's "private island." Passengers in the foreground on the ship deck point and photograph it with excitement. Then the camera slowly, continuously rises upward and pulls back, revealing more and more of the island from above. As the altitude increases, the manufactured nature becomes visible: identical beach loungers in perfect grid formation, a large commercial dock, logistics trucks on a hidden road behind the treeline, corporate infrastructure. The island looks less natural and more like a theme park operation from above. The passengers below remain excited and unaware. The rise is slow and relentless. Photorealistic, natural daylight, slight natural lens movement. Vertical frame, 9:16 portrait orientation. Ambient ocean and crowd sound only. No text, no watermarks.
```
Hook fit: "A Local Told Me / What That 'Private Island' Actually Is"  
Mike: 🟢 STRONG → 🔥 VIRAL potential — тайна + путешествие = Maya мгновенно пересылает

---

### КОГДА ИСПОЛЬЗОВАТЬ Spectacle vs Documentary

| Formulas | Spectacle Mode | Documentary Mode |
|----------|---------------|-----------------|
| Formula 3 — Command Interrupt | ✅ ПЕРВЫЙ ВЫБОР | Запасной |
| Formula 5 — Injustice | ✅ ПЕРВЫЙ ВЫБОР | Запасной |
| Formula 9 — Pattern Interrupt + Stat | ✅ ПЕРВЫЙ ВЫБОР | Запасной |
| Formula 2 — Specific Loss | ✅ Работает | ✅ Работает |
| Formula 1 — Personal Warning | ✅ Работает | ✅ Первый выбор |
| Formula 4 — Insider Observation | ❌ Слабее | ✅ ПЕРВЫЙ ВЫБОР |
| Formula 7 — Location Danger | ❌ Слабее | ✅ ПЕРВЫЙ ВЫБОР |
| Formula 8 — Body Self-Sabotage | ✅ Работает | ✅ Работает |

**VIC решает:** если VIC ставит 🔥 VISUAL VIRAL на Spectacle концепт — берём Spectacle. Если сомнения — Documentary безопаснее.

---

## КОГДА ИСПОЛЬЗОВАТЬ

| Ситуация | Действие |
|----------|----------|
| Есть подходящий клип в `/footage/` | → `footage-manager` выбирает. Этот скилл не нужен. |
| Клип не подходит по теме | → `/ai-video-prompts` с темой хука |
| Все доступные клипы уже использованы сегодня | → `/ai-video-prompts` |
| Хук требует сцену которой нет в стандартной библиотеке | → `/ai-video-prompts` |
| AI клип сгенерирован → тест body clearance ✅ | → Рендер через kira-hooks |
| AI клип сгенерирован → body clearance ❌ | → Другой промт или modify shot composition |

---

## AI ARTIFACT RISK GUIDE

| Тип сцены | Риск | Решение |
|-----------|------|---------|
| Лицо крупным планом | 🔴 ВЫСОКИЙ | Избегать. Или: partial face, side angle, out of focus |
| Руки с предметами | 🟡 СРЕДНИЙ | Добавить: "hands clearly holding [object], correct finger count" |
| Руки без предметов | 🟡 СРЕДНИЙ | Минимизировать рук в кадре. Или: hands blurred in background |
| Среда без людей | 🟢 НИЗКИЙ | Безопасно. Объекты, пространства, предметы = минимальный риск |
| Люди на среднем плане | 🟢 НИЗКИЙ | Работает хорошо с `documentary style` + `natural light` |
| Текущая вода, огонь, дым | 🟡 СРЕДНИЙ | Специфичны для Kling. В Pika могут выглядеть artificial. |
