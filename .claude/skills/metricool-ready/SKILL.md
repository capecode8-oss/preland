---
name: metricool-ready
description: Push rendered MP4 to GitHub repo, get raw URL, schedule in Metricool as Instagram Reel + TikTok. Run after quality-check passes.
---

# Metricool Ready
## Push → Raw URL → Schedule · @thekiramethod

---

## ПАРАМЕТРЫ (вшиты навсегда)

- **brand_id**: `6476294`
- **Timezone**: `America/New_York`
- **Платформы**: Instagram Reel + TikTok (PUBLIC_TO_EVERYONE)
- **Музыка**: вшита в MP4 при рендере (библиотека music/1–30.mp3) — владелец может заменить вручную в Instagram если нужно
- **Геотег (New York)**: добавляет владелец вручную после публикации
- **Репо**: `capecode8-oss/preland`, ветка: `claude/new-chat-fjz36a`

---

## ШАГ 1 — PUSH MP4 В РЕПО

```bash
# Убедиться что файл существует
ls -lh /home/user/preland/footage/rendered/[filename].mp4

# Добавить в git и запушить
git add footage/rendered/[filename].mp4
git commit -m "reel: [topic-slug] [date]"
git push -u origin claude/new-chat-fjz36a
```

---

## ШАГ 2 — ПОЛУЧИТЬ RAW URL

После успешного пуша — raw URL формируется автоматически:

```
https://raw.githubusercontent.com/capecode8-oss/preland/claude/new-chat-fjz36a/footage/rendered/[filename].mp4
```

Проверить доступность:
```bash
curl -I "https://raw.githubusercontent.com/capecode8-oss/preland/claude/new-chat-fjz36a/footage/rendered/[filename].mp4"
# Ожидаем: HTTP/2 200
```

---

## ШАГ 3 — ЗАПЛАНИРОВАТЬ В METRICOOL

Использовать инструмент `mcp__Metricool__createScheduledPost`.

**Лучшее время для публикации (America/New_York):**
- 7:00 AM — утро (завтрак, телефон в руках)
- 12:00 PM — обед
- 6:00 PM — вечер после работы
- 9:00 PM — прайм (Майя листает перед сном)

**Обязательные поля:**

```json
{
  "brandId": 6476294,
  "networks": ["instagram", "tiktok"],
  "text": "[CAPTION — 1700-1900 символов из kira-captions]",
  "mediaUrls": ["https://raw.githubusercontent.com/...mp4"],
  "publishAt": "2026-MM-DDTHH:MM:00-05:00",
  "instagramData": {
    "type": "REEL"
  },
  "tiktokData": {
    "title": "[TikTok title ≤150 символов — первая строка хука]",
    "privacyLevel": "PUBLIC_TO_EVERYONE"
  }
}
```

❌ Без `tiktokData.title` — TikTok не запланируется
❌ `publishAt` должен быть в будущем
❌ URL должен быть прямой ссылкой на MP4, не на страницу GitHub

---

## ШАГ 4 — ПОДТВЕРЖДЕНИЕ

После успешного создания поста:

```
✅ METRICOOL SCHEDULED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Тема: [topic]
Время: [дата время ET]
Платформы: Instagram Reel + TikTok
Post ID: [id из ответа Metricool]
Raw URL: [url]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Владелец добавляет: геотег New York вручную (музыка уже в видео)
```

---

## ЧАСТЫЕ ОШИБКИ

| Ошибка | Причина | Решение |
|--------|---------|---------|
| 404 на raw URL | GitHub не успел обработать пуш | Подождать 30-60 секунд, попробовать снова |
| TikTok не публикуется | Нет `tiktokData.title` | Добавить title |
| "Media URL not accessible" | Приватный репо или неверный URL | Проверить что репо публичный |
| Время в прошлом | Неверный timezone | Использовать `-05:00` (ET) или `-04:00` (EDT) |
