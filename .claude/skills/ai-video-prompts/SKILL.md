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
VEO 3 [7-LAYER]:
Shot on an iPhone held loosely at waist height by someone standing in the crowd — auto-exposure adjusting to the terminal's overhead fluorescents, slight electronic stabilization fighting the natural drift of a person shifting their weight. Inside a busy arrival baggage claim hall — scuffed linoleum floors reflecting cold institutional overhead fluorescent lights, rows of waiting passengers with luggage trolleys visible in background, the mechanical hum of the rotating carousel, bags of various sizes moving past in sequence. A pair of hands — a woman in her late 30s, travel-worn light blue sleeve visible, silver watch — reaches forward toward a black rolling suitcase as it passes on the moving belt, fingers slightly tense, the reach hesitant and uncertain. The specific nervous energy of someone who's not sure their bag actually made it. Cold overhead fluorescent lighting, slightly green-tinted, flat and institutional. Photorealistic. Vertical frame, 9:16 portrait orientation. Ambient airport sound only. No text, no watermarks.
```

**HOTEL — front desk dispute (Injustice):**
```
VEO 3 [7-LAYER]:
Shot on an iPhone held loosely at chest height by a bystander — slight auto-exposure adjusting, gentle drift before correcting. Inside the lobby of an ordinary mid-range hotel — reception counter with polished-but-not-luxurious marble surface, two monitors behind the desk, a small flower arrangement slightly wilting, soft warm light from recessed ceiling fixtures overhead, the sound of rolling luggage somewhere behind. A woman in her early 40s in a slightly wrinkled linen travel shirt and dark jeans stands at the counter — reading glasses pushed up on her head, a folded paper receipt in her left hand. She unfolds it slowly, runs her finger down the line items, stops — looks up at the receptionist with the specific quiet disbelief of someone realizing they've been charged for something they didn't use. One hand rests on the marble counter. The warm overhead light catches the surface of the paper. Photorealistic. Vertical frame, 9:16 portrait orientation. Ambient lobby sound only. No text, no watermarks.
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

## 🎯 NATURALISTIC LAYER SYSTEM — Что отделяет шаблон от вирусного

Инспирировано: @neurustik (8,962 лайков, 6,084 сохранений на одном промте — Seedance 2.0).
Подтверждено исследованиями 2026: специфичность промта = прямая корреляция с реализмом.

**Главная ошибка текущих промтов:** слишком общие. "Documentary-style footage with slight handheld movement" — это описание КАТЕГОРИИ, а не СЦЕНЫ. Veo 3 / Kling видят шаблон и рендерят шаблон.

**Правило neurustik:** Промт должен отвечать на 7 конкретных вопросов. Если хоть один пропущен — AI заполняет его "средним значением" = шаблонный вид.

---

### LAYER 1 — CAMERA IDENTITY (какая камера, кто снимает)

❌ СЛАБО: "handheld camera, documentary style"
✅ СИЛЬНО: "The camera was grabbed by someone who'd never held it before — strong unpredictable shake, constant minor reframing, subject sometimes drifting to the edge of the frame, autofocus hunting for a moment before locking"

**Шаблоны Camera Identity:**

```
[PHONE, современный, случайный очевидец]:
Shot on an iPhone held loosely at chest height by someone who picked it up to quickly film something — unsteady grip, auto-exposure adjusting to the light, slight electronic stabilization fighting against the hand movement

[DV CAMERA, 2000-2005, ностальгический]:
Shot on a consumer DV camcorder from around 2003 — strong handheld shake, constant reframing, autofocus lag, visible camera breathing, slight overexposure in bright areas, faded low-contrast image, digital noise, home video compression artifacts, no stabilization, no modern color grading

[SECURITY CAM / CCTV, статичная]:
Fixed security camera angle, high and slightly tilted downward, wide angle, slightly desaturated institutional color, minimal grain, static frame — the scene happens within the locked-off frame

[HANDHELD PROFESSIONAL, но не студийный]:
Slightly handheld documentary camera — enough movement to feel real, not enough to be distracting. The camera breathes with the cinematographer's body, subtle drift rather than shake
```

---

### LAYER 2 — ENVIRONMENT TEXTURE (среда с деталями, не название места)

❌ СЛАБО: "inside an airport terminal"
✅ СИЛЬНО: "inside a busy mid-size regional airport — scuffed linoleum floors reflecting fluorescent overhead lights, rows of molded plastic chairs with worn armrests, departure boards clicking through updates, a Starbucks visible through the crowd in background"

**Правило:** Назови 3-4 конкретных детали среды. Imperfections читаются как реальность.

```
[HOTEL BATHROOM реалистичный]:
Ordinary mid-range hotel bathroom — slightly yellowed grout between white tiles, chrome faucet with minor water stains, used soap bar at the edge of the sink, white towels folded on a chrome rail, the kind of bathroom that could be in any Marriott or Hilton

[KITCHEN реалистичный]:
A real lived-in home kitchen — magnets and papers on the fridge, a dish drying rack with a few plates, soft yellow morning light from a window above the sink, a half-finished coffee mug on the counter, the kind of kitchen a family actually uses

[CRUISE SHIP DECK реалистичный]:
The stern deck of a mid-size cruise ship — white painted metal railing with some rust streaks where the paint has chipped, deck chairs stacked and strapped down, salt-air haze softening the horizon, institutional exterior lighting fixtures mounted every few meters along the deck wall

[AIRPORT CUSTOMS]:
A real customs inspection area — long counter with visible wear marks, institutional overhead fluorescent lights casting a slightly green-tinted light on everything, official blue CUSTOMS sign in background, security cameras mounted on the ceiling, the floor slightly scuffed from years of rolling luggage
```

---

### LAYER 3 — CHARACTER SPECIFICITY (если человек в кадре)

❌ СЛАБО: "a woman in her 40s holding a receipt"
✅ СИЛЬНО: "a woman in her early 40s in a faded navy blue cotton t-shirt tucked into light-wash jeans, reading glasses pushed up on her head, holding a folded paper receipt, her expression shifting from confusion to quiet frustration, one hand on the counter for balance"

**Правило @neurustik:** один оригинальный персонаж, неизменные лицо/кожа/фигура/одежда на протяжении всего ролика. Конкретные детали одежды = характер.

**AI-риск:** лица крупным планом = высокий риск артефактов. Использовать partial face, side angle, hands+body, или blur.

```
[TRAVELER — средний возраст, аэропорт]:
A woman in her late 30s in light-wash jeans and a slightly wrinkled linen shirt — the kind of outfit someone wore on a long flight, slightly travel-tired, rolling carry-on handle visible at her side

[MAN — деловой путешественник]:
A man in his mid-40s in a rumpled business-casual button-down, laptop bag strap over one shoulder, the slightly defeated posture of someone who's been traveling all day

[WOMAN — домашняя сцена]:
A woman in her early 40s in a soft grey oversized cardigan and dark jeans, at home, hair in a loose bun, the kind of person who's organized but currently mildly worried about something
```

---

### LAYER 4 — ACTION SEQUENCE (последовательность, не статика)

❌ СЛАБО: "woman holding a receipt at the hotel desk"
✅ СИЛЬНО: "she unfolds the paper receipt slowly, scans it top to bottom, stops partway down — her eyes go back to the same line — she looks up at the receptionist with an expression halfway between confusion and frustration, says nothing yet"

**Правило:** Опиши что происходит В ЭТОТ МОМЕНТ — не состояние, а движение. Multi-step = жизнь. Single state = stock photo.

---

### LAYER 5 — LIGHT SOURCE (физический, named, направленный)

❌ СЛАБО: "warm lighting"
✅ СИЛЬНО: "warm incandescent light from a floor lamp to camera left, casting a soft golden glow across the left half of the scene, the right side falling into cooler shadow from the window behind"

**Правило:** всегда называй физический источник света (ceiling fluorescent, window, floor lamp, phone screen glow, car headlights) + его направление (from the left, from below, backlit, overhead).

---

### LAYER 6 — TECHNICAL IMPERFECTIONS (несовершенства = аутентичность)

Это самый быстрый способ убрать AI-look. Добавлять 2-3 из этого списка:

```
CAMERA SHAKE:        strong handheld shake / slight tremor / unpredictable micro-movements
FOCUS:               autofocus lag / rack focus / slightly out of focus foreground
EXPOSURE:            slight overexposure in bright areas / lens flare / auto-exposure adjusting
GRAIN:               light film grain / digital noise / slight compression artifacts
COLOR:               slightly desaturated / faded washed-out tones / no modern color grading / low contrast
FRAME:               constant minor reframing / subject drifts to frame edge / accidental dutch angle
MOTION BLUR:         natural motion blur on fast movements
BREATHING:           the lens breathes slightly as it adjusts focal length
```

---

### LAYER 7 — EMOTIONAL ATMOSPHERE (настроение = "nervous energy" > "tense scene")

❌ СЛАБО: "tense atmosphere"
✅ СИЛЬНО: "the specific nervous energy of someone who suspects they've been cheated but isn't sure yet"

```
INJUSTICE:    the specific quiet outrage of someone realizing they were cheated
FEAR:         the held-breath stillness of someone about to discover something wrong
CURIOSITY:    the leaning-in concentration of someone who just noticed something they can't explain
AWE:          the frozen wide-eyed moment when something is bigger than expected
RELIEF:       the exhale-and-shoulders-drop of someone who just solved a problem
```

---

### BEFORE / AFTER — Апгрейд промта

**НАШИ СТАРЫЕ ПРОМТЫ (шаблонные):**
```
Medium shot slowly pushing in toward a hotel reception desk. Inside a hotel lobby with warm chandelier lighting and marble counter. A woman in her 40s stands at the desk holding a paper receipt, her expression frustrated and confused, gesturing toward the receptionist across the counter. Documentary-style footage with slight natural handheld movement. Photorealistic. Vertical frame, 9:16 portrait orientation.
```

**NEURUSTIK-LEVEL (7 слоёв):**
```
Shot on an iPhone held loosely at chest height by a bystander — slight auto-exposure adjusting, gentle electronic stabilization fighting the grip, the camera drifts slightly right before correcting. Inside the lobby of an ordinary mid-range hotel — a reception counter with polished but not luxurious marble surface, two monitors behind the desk, a small flower arrangement wilting slightly, soft warm light from recessed ceiling fixtures overhead. A woman in her early 40s in a slightly wrinkled linen travel shirt and dark jeans stands at the counter — reading glasses pushed up on her head, a folded paper receipt in her left hand. She unfolds it slowly, runs her finger down the line items, stops — looks up at the receptionist with the specific quiet disbelief of someone realizing they've been charged for something they didn't use. The receptionist behind the counter has the calm, practiced expression of someone who's had this conversation before. The warm overhead light catches the surface of the paper. Vertical frame, 9:16 portrait orientation. Ambient lobby sound only. No text, no watermarks, no dialogue.
```

**Разница:** 70 слов → 190 слов. Каждое из 7 слоёв заполнено.

---

### QUICK REFERENCE — Словарь реализма (вставлять напрямую в промты)

**Camera shake levels:**
- лёгкий: "slight natural handheld drift, camera breathes with the operator's body"
- средний: "moderate handheld shake, constant minor reframing, subject occasionally drifts toward frame edge"
- сильный (DV-стиль): "strong unpredictable handheld shake, autofocus hunting, subject sometimes drifts out of frame, constant reframing"

**Light sources (добавлять в каждый промт):**
- кухня: "warm window light from the left, soft and directional, casting a gentle shadow to the right"
- аэропорт: "cold institutional overhead fluorescent lights, slightly green-tinted, casting flat even shadows"
- отель-лобби: "warm recessed ceiling fixtures supplemented by a floor lamp in the corner"
- улица-день: "overcast daylight, soft and directionless, no strong shadows"
- вечер-дом: "single warm floor lamp to camera left, the rest of the room falling into cool shadow"

**Texture words (добавлять к локациям):**
worn / scuffed / slightly yellowed / water-stained / chipped paint / faded / salt-air corroded / smudged / lived-in / slightly cluttered / fingerprint-marked

**Emotion phrases:**
- "the specific nervous energy of someone who suspects something is wrong"
- "the quiet held-breath stillness before a difficult conversation"
- "the frozen wide-eyed moment of seeing something unexpectedly large"
- "the specific quiet frustration of someone who's been cheated and knows it"
- "the exhale-and-shoulders-drop of someone who just found the solution"

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
7 NATURALISTIC LAYERS (среда, камера, текстура, свет, несовершенства) + одно физически невозможное явление + slow motion
```

Spectacle Mode требует ВСЕ 7 слоёв из NATURALISTIC LAYER SYSTEM — иначе невозможное событие выглядит как CGI на фоне шаблона. Только когда среда максимально реальная — невозможное событие даёт максимальный шок.

**Запрещено в Spectacle Mode:**
- ❌ CGI-вид, картунность, мультяшность — убивает эффект
- ❌ Слишком много невозможных элементов — один эффект, максимум
- ❌ Слова "magical" или "fantasy" — уводит в сказку
- ❌ "photorealistic render" — слово "render" триггерит CGI-look

**Работает:**
- ✅ "as if demonstrating the invisible force" — невидимая сила стала видимой
- ✅ "in slow motion" — даёт мозгу время осознать невозможное
- ✅ "the effect happens naturally, as if this is simply how physics works here"
- ✅ Деньги, газ, свет, тепло, цвет — всё это визуализируется "невидимыми" силами
- ✅ TEXTURE WORDS в среде (worn / scuffed / lived-in) — усиливают реализм фона

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
VEO 3 SPECTACLE [7-LAYER]:
Shot as if a passenger grabbed a phone and braced it against the railing — strong unpredictable shake from wind and swell, auto-exposure fighting the dark sky, the frame drifting slightly before correcting. The stern deck of a mid-size cruise ship at dusk — white painted metal railing with visible salt-air rust streaks where paint has chipped, deck chairs strapped and stacked against the wall, institutional exterior light fixtures mounted along the wall casting a cold flat glow. The open ocean stretches behind the ship. On the horizon, an enormous dark green wall of water — fifteen to twenty meters high — rises slowly and continuously, its foam-crested peak beginning to curl. Through the portholes along the ship's side, warm amber cabin lights glow steadily, completely unaware of what rises behind them. The contrast between the ordinary, warm domesticity of those lit windows and the scale of the approaching wave is the visual hook. The wave moves slowly and inevitably, its surface textured with whitecaps and foam. The sky above it is a deep bruised violet-grey, the water below it black and churning. Slow-motion, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient wind and ocean sound only. No text, no watermarks, no dialogue.
```
Hook fit: "Never Book This Cabin / On A Cruise Ship"
Mike: 🔥 VIRAL — Maya шлёт мужу перед круизом

---

**#2 — Hidden fees fly from brochure (Injustice · Formula 5):**
```
VEO 3 SPECTACLE [7-LAYER]:
Shot on an iPhone resting on a coffee table at a low angle — slight natural drift as if the phone wasn't perfectly propped, slight auto-exposure adjusting to the room light. Inside a real lived-in home living room — a coffee table with a half-finished glass of water and a notepad with handwritten trip notes, a couch visible in background, warm floor lamp light to the left casting a golden pool, the rest of the room in soft shadow. A pair of hands — a woman in her late 30s, light blue nail polish, casual rings — holds open a glossy cruise brochure showing a bold printed price of $800 against a tropical sea background. As the fingers hold the brochure open and still, individual coins and folded dollar bills begin to silently peel away from behind the pages one by one, rising slowly upward into the warm air above the table as if drawn by an invisible current, each bill rotating gently and catching the floor lamp light as it lifts. The brochure remains unchanged on the surface, face-up and bright. More money continues to rise. The effect feels inevitable and impossible to stop. Slow-motion, photorealistic. Vertical frame, 9:16 portrait orientation. Ambient room silence only. No text, no watermarks.
```
Hook fit: "My $800 Cruise / Cost Me $1,400"
Mike: 🔥 VIRAL — конкретные цифры + Injustice + визуал деньги буквально улетают

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
