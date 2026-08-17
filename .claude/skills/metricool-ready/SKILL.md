---
name: metricool-ready
description: Prepares and schedules KIRA reels in Metricool. Generates correct API payload, pushes MP4 to GitHub, creates raw URL, schedules Instagram Reel + TikTok post. Run after quality-check passes and user approves JPG preview.
---

# KIRA Metricool Ready — Publish Pipeline

## ДАННЫЕ АККАУНТА (фиксированные)

```
brand_id: 6476294
Timezone: America/New_York
Платформы: Instagram Reel + TikTok
Visibility: PUBLIC_TO_EVERYONE
Музыка и геотег: добавляет пользователь вручную в Metricool
```

---

## ПАЙПЛАЙН ПУБЛИКАЦИИ

### Шаг 1 — Push MP4 в GitHub

```bash
# Файл должен быть в /home/user/preland/reels/
git add reels/FILENAME.mp4
git commit -m "Add reel: FILENAME"
git push -u origin claude/new-chat-fjz36a
```

**Raw URL формат:**
```
https://raw.githubusercontent.com/capecode8-oss/preland/claude/new-chat-fjz36a/reels/FILENAME.mp4
```

---

### Шаг 2 — Проверить caption

Капшен должен быть:
- Прошедший аудит команды (kira-captions скилл)
- 1200–1800 символов
- Структура: second hook → context → detail → payoff → CTA → save line
- CTA с конкретным payoff preview (не "click the link" — а что именно там)

---

### Шаг 3 — Создать TikTok title

TikTok требует отдельный заголовок (≤ 150 символов):
- Взять первую строку хука
- Или адаптировать — более прямолинейно
- Без эмодзи в начале

---

### Шаг 4 — Запланировать через Metricool

**Оптимальное время публикации (America/New_York):**

| Слот | Время ET | Рейтинг |
|------|----------|---------|
| Утро | 7:00-8:00 AM | ⭐⭐⭐ |
| День | 12:00-1:00 PM | ⭐⭐ |
| Вечер | 6:00-9:00 PM | ⭐⭐⭐⭐ |
| Ночь | 9:00-11:00 PM | ⭐⭐⭐⭐⭐ |

**Для 4-5 рилсов в день — распределить по слотам:**
```
Рилс 1: 7:30 AM (утренняя аудитория)
Рилс 2: 12:00 PM (обеденный перерыв)
Рилс 3: 5:30 PM (конец рабочего дня)
Рилс 4: 8:00 PM (прайм-тайм)
Рилс 5: 10:00 PM (ночная аудитория)
```

**Рекомендация:** Самый сильный хук (Mike: VIRAL) → 8-10 PM слот.

---

### Шаг 5 — Вызов Metricool API

Использовать инструмент `mcp__Metricoll__createScheduledPost` или `createScheduledPostForReview`.

**Структура запроса:**
```json
{
  "brandId": 6476294,
  "publishDate": "2026-08-17T20:00:00",
  "timezone": "America/New_York",
  "networks": {
    "instagram": {
      "text": "[CAPTION ЗДЕСЬ]",
      "reelUrl": "https://raw.githubusercontent.com/capecode8-oss/preland/claude/new-chat-fjz36a/reels/FILENAME.mp4",
      "shareAsReel": true
    },
    "tiktok": {
      "text": "[CAPTION ЗДЕСЬ]",  
      "videoUrl": "https://raw.githubusercontent.com/capecode8-oss/preland/claude/new-chat-fjz36a/reels/FILENAME.mp4",
      "title": "[TIKTOK TITLE ≤150 символов]",
      "privacyLevel": "PUBLIC_TO_EVERYONE"
    }
  }
}
```

---

## ЧЕКЛИСТ ПЕРЕД ПУБЛИКАЦИЕЙ

```
□ MP4 запушен в GitHub
□ Raw URL рабочий (проверить в браузере)
□ Caption прошёл kira-captions аудит
□ TikTok title готов (≤150 символов)
□ Время публикации выбрано (приоритет: вечер/ночь)
□ JPG превью одобрено пользователем
□ Quality-check: все 7 пунктов ✅
□ Клип записан в footage-manager журнал
```

---

## ЧАСТЫЕ ОШИБКИ

| Ошибка | Решение |
|--------|---------|
| Raw URL не работает | Проверить что push прошёл успешно |
| Видео не принято Metricool | Проверить: H.264, yuv420p, 1080×1920, ≤100MB |
| TikTok отклонил | title обязателен, max 150 символов |
| Время в UTC | Конвертировать из ET: ET+5 = UTC (зима), ET+4 = UTC (лето) |

---

## ПОСЛЕ ПУБЛИКАЦИИ

1. Записать в performance-tracker журнал (дата, клип, нища, формула)
2. Через 24ч и 72ч — проверить метрики (views, shares, saves)
3. Если рилс 10× лучше других → скопировать формулу немедленно
4. Обновить footage-manager журнал использованных клипов
