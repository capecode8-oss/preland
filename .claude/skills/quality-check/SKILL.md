---
name: quality-check
description: 7-point QA gate for every reel before scheduling in Videotool. Run after render, before push. Nothing publishes without passing all 7.
---

# Quality Check — 7-Point QA Gate
## @thekiramethod — финальный контроль перед публикацией

---

## ПРАВИЛО

**Ни один рилс не идёт в Videotool без прохождения всех 7 пунктов.**
Если хоть один ❌ — исправить и прогнать снова. Публиковать только когда все ✅.

---

## 7 ПУНКТОВ QA

### ✅ 1. ВИДЕО — технические параметры

Проверить через ffprobe или ffmpeg -i:

| Параметр | Требование | Как проверить |
|----------|------------|---------------|
| Размер | 1080×1920 | `ffprobe [file] 2>&1 \| grep Video` |
| Длительность | ровно 5.0s (±0.1s) | `ffprobe -v quiet -show_entries format=duration` |
| FPS | 30 fps | в выводе ffprobe |
| Кодек | H.264, yuv420p | в выводе ffprobe |
| Аудио | ПРИСУТСТВУЕТ (музыка из библиотеки) | есть audio stream aac в ffprobe |
| Размер файла | < 50MB (Videotool лимит) | `ls -lh [file]` |

```bash
ffprobe -v quiet -print_format json -show_streams /path/to/reel.mp4
```

❌ Если аудио ОТСУТСТВУЕТ → перерендерить с музыкой (обязательно!)
❌ Если аудио есть но не из нашей библиотеки → перерендерить с правильным треком
❌ Если размер файла > 50MB → `-crf 23` вместо `-crf 18`

---

### ✅ 2. ТЕКСТ — размер шрифта

Проверить что шрифт в превью JPG читаем:
- Минимум: **60px** (auto_font с max_size=100)
- Если строки хука слишком длинные → шрифт падает ниже 60px → ПЕРЕПИСАТЬ строки

Тест: открыть JPG-превью и прочитать с расстояния вытянутой руки. Если надо прищуриться — шрифт маленький.

❌ Шрифт < 60px → сократить строки до ≤6 слов → перерендерить

---

### ✅ 3. ТЕКСТ — позиция и оверлей (ЗЕЛЁНАЯ ЗОНА)

- Сплошная плашка (один прямоугольник, не отдельные на каждую строку) ✅
- `hook_y0 = 1550 - box_height` — текст внизу, выше Instagram UI ✅
- `cta_bottom ≤ 1550` — не перекрыто Instagram chrome ✅
- `center_x = 540 ± 2px` — отцентровано горизонтально ✅
- `box_w ≤ 860px` | текст внутри `≤ 760px` — не выходит за края экрана ✅
- Авто-перенос строк если строка > MAX_TEXT_W (встроено в render.py) ✅

❌ Отдельные плашки на каждую строку → перерендерить через render.py
❌ box_w > 860px → текст выйдет за края телефона → уменьшить строки
❌ cta_bottom > 1550 → перекрыто Instagram UI → сократить хук

---

### ✅ 4a. REPTILIAN BRAIN CHECK — 6 PRIMAL TRIGGERS

Перед QA пункта 4 — обязательный триггер-аудит:

| Проверка | Критерий | Порог |
|----------|----------|-------|
| Доминирующий триггер назван? | Команда указала T1/T2/T3/T4/T5/T6 | обязательно |
| T1 SURVIVAL THREAT активирован? | Есть угроза / потеря / опасность в первых 3 словах? | если не T1 — есть другой триггер |
| T5 CURIOSITY GAP работает? | Мозг не может закрыть луп — НЕВОЗМОЖНО не читать дальше? | обязательно |
| Нет "tips/advice" тона? | Нет "here's how", "you should", "pro tip" — только instinct hooks | обязательно |
| 0.3 сек тест пройден? | Тело реагирует ДО включения логики? | обязательно |

❌ Нет доминирующего триггера → хук переписать перед рендером
❌ Тон "полезный совет" вместо "угроза/тайна" → переписать
❌ Луп закрыт в хуке (payoff виден сразу) → переписать, оставить открытым

---

### ✅ 4. КОНТЕНТ — хук

- Первое лицо: "I", "my", "A local" — НЕ "She/He" ✅
- ≤ 3 строки в hook_lines ✅
- ≤ 6 слов на каждой строке ✅
- Есть конкретная цифра или место ✅
- Нет запрещённых слов: "you won't believe", "the truth about", "She found" ✅
- CTA badge присутствует, скрывает payoff, заканчивается ↓ ✅

---

### ✅ 5. КОНТЕНТ — дубликат

- Этот хук/тема не публиковались последние 3 дня ✅
- Этот клип не использовался сегодня и вчера ✅ (см. footage-manager журнал)
- Проверить: не повторяем ли тему которую опубликовали менее 3 дней назад

---

### ✅ 6. КАПШЕН — структура и длина

- Длина: 1800–1900 символов ✅
- Структура: second hook → context → detail → payoff → CTA → save line ✅
- CTA из банка kira-captions ✅
- Хештеги: 5-8 штук, релевантные нише ✅
- TikTok title заполнен (< 150 символов) ✅

```
Проверить длину: echo -n "[caption text]" | wc -c
```

---

### ✅ 7. ПРЕ-РЕНДЕР ПРЕВЬЮ — обязательно ДО рендера MP4

**Железное правило: хук показывается на РЕАЛЬНОМ кадре footage. Никогда на чёрном фоне или заглушке.**

```bash
# Шаг 1 — извлечь кадр из выбранного клипа
FFMPEG="/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
$FFMPEG -y -ss 2 -i /home/user/preland/footage/[CLIP].mp4 \
  -vframes 1 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  /tmp/preview_bg.jpg
```

```python
# Шаг 2 — PIL overlay
from PIL import Image, ImageDraw, ImageFont
bg = Image.open("/tmp/preview_bg.jpg").resize((1080, 1920))
draw = ImageDraw.Draw(bg, "RGBA")
FONT_PATH = "/usr/share/fonts/truetype/montserrat/Montserrat-BlackItalic.ttf"
lines = [hook_line_1, hook_line_2, hook_line_3]  # CAPS на ключевых словах
MAX_TEXT_W = 760; PAD_X = 40; PAD_Y = 32; LINE_GAP = 10; BOTTOM_ANCHOR = 1520
font_size = 72
while font_size > 36:
    font = ImageFont.truetype(FONT_PATH, font_size)
    widths = [font.getbbox(l)[2]-font.getbbox(l)[0] for l in lines]
    if max(widths) <= MAX_TEXT_W: break
    font_size -= 2
# Нарисовать белую плашку + текст → сохранить /tmp/hook_preview.jpg
bg.save("/tmp/hook_preview.jpg", quality=92)
```

Шаг 3 — `SendUserFile(["/tmp/hook_preview.jpg"])` → ждать одобрения пользователя.

❌ Чёрный фон / заглушка / placeholder = СТОП, перегенерировать с реальным footage
❌ Текст за пределами MAX_TEXT_W=760px = СТОП, уменьшить font_size или переписать хук
✅ Только после одобрения превью → рендер финального MP4

---

### ✅ 8. ФАЙЛ — готов к пушу

- MP4 файл существует по пути `/home/user/preland/footage/rendered/` ✅
- JPG-превью из реального footage одобрен пользователем ✅
- Имя файла: `YYYY-MM-DD_[topic-slug].mp4` (без пробелов) ✅
- Нет watermarks, нет AI-артефактов в превью ✅

---

## ИТОГОВЫЙ ВЫВОД

```
QA GATE — [дата] | [topic]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Пре-рендер превью на реальном footage ✅ / ❌  ← ПЕРВЫЙ ШАГ
2. Видео-параметры           ✅ / ❌
3. Музыка присутствует       ✅ / ❌
4. Шрифт ≥60px               ✅ / ❌
5. Текст-позиция (safe zone) ✅ / ❌
6. Хук-правила               ✅ / ❌
7. Нет дубликата             ✅ / ❌
8. Капшен 1800-1900с         ✅ / ❌
9. Файл готов к пушу         ✅ / ❌
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
РЕЗУЛЬТАТ: ✅ PASS — идти в videotool-ready (все 9 пунктов ✅)
           ❌ FAIL — исправить пункт [N], повторить QA
```
