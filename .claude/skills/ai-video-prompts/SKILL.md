---
name: ai-video-prompts
description: Generate AI video prompts for @thekiramethod reels. Use when stock footage library has no matching clip OR when you want a custom visual that perfectly fits the hook's emotion. Run after kira-hooks — finalized hook required before generating visual. Output is ready-to-paste prompts for Kling, Runway, and Pika. The user generates the actual video themselves.
---

# AI Video Prompt System — KIRA
## Tools: Kling 2.1 · Runway Gen-4 · Pika 2.2
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
- Kling: comma-separated descriptors, cinematic precision. Лучший реализм.
- Runway: начинать с `[Camera motion]` (Slow push in / Pan right / Track forward). Лучший контроль движения.
- Pika: conversational natural language. Самая быстрая итерация.
- Negative prompt — ВСЕГДА: `text, watermark, logo, CGI, studio lighting, obvious AI artifacts, distorted hands, extra fingers, advertisement look`

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

### Rule 5 — Seamless 5-second loop
Финальный кадр визуально переходит в начальный. Используй движения которые зацикливаются естественно: конвейер, ходьба по коридору, медленный pan, волны.

---

## ПРОМТ-ШАБЛОНЫ ПО НИШАМ

### ✈️ AIRPORT / FLIGHT

**Luggage belt — тревога / theft warning (Fear):**
```
KLING:
Close-up of moving airport baggage claim belt, multiple suitcases passing, a pair of hands nervously reaching toward a bag, fluorescent terminal overhead lighting, slightly handheld camera movement, tense worried atmosphere, documentary style, photorealistic, no text no watermarks, 5 seconds seamless loop

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

🎯 KLING 2.1 (лучший реализм):
[Готовый промт — вставить напрямую в Kling]

🎬 RUNWAY GEN-4 (лучшее движение камеры):
[Camera: тип движения] + [готовый промт]

⚡ PIKA 2.2 (быстрая итерация):
[Готовый промт — вставить напрямую в Pika]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚫 NEGATIVE PROMPT (для всех инструментов):
text, watermark, logo, subtitle, CGI, studio lighting, obvious AI artifacts, uncanny valley, distorted hands, extra fingers, advertisement look, stock footage aesthetic

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TECH SPECS:
- Duration: 5 seconds | Resolution: 1080×1920 (9:16 вертикальное)
- После генерации: footage-manager → залогировать как custom clip
- Затем: kira-hooks body clearance → рендер

TEAM: NOVA ✅ | VIC 🎬 [VIRAL/STRONG] | Mike 🟢 | Red ✅ SURVIVED
```

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
