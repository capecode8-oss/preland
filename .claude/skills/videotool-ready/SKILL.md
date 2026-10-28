---
name: videotool-ready
description: Push the finished MP4 and caption to the repo, check the raw URL, schedule the reel in Videotool (Instagram). Run after the owner returns the finished video and the caption passes the checks.
---

# Videotool Ready (актуально с Oct 25 2026)

## Параметры
- Инструмент: `mcp__VIDEO_Tool__createScheduledPost` (поля: `video_url`, `caption`, `scheduled_time_iso` в UTC, `platform`, `skip_music`). Других полей нет.
- Платформа: `instagram`. TikTok и YouTube владелец загружает вручную.
- `skip_music: true` на talking head (музыку не добавлять). Флаг не всегда срабатывает: напомнить владельцу проверить пост.
- Время: America/New_York. Сегодня EDT = UTC−4 (до 1 ноября 2026), потом EST = UTC−5. Окна из `getBestTimeToPost`: 12:00, 15:00, 18:00, 20:00, 21:00 ET. Между постами минимум 3 часа. Перед планированием вызвать `getScheduledPosts` (status scheduled), чтобы не занять тот же слот.
- Репо: `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`.

## Шаги
1. Просмотреть кадры видео (контактный лист ffmpeg), проверить длину и звук. Файл сохранить как `reels/<slug>.mp4`, подпись как `reels/<slug>.caption.txt`.
2. Подпись: 1700–1900 знаков, считать `wc -m`; без хэштегов, слов «free» и цены; первая строка не повторяет хук ролика; мост GLOW по ротации (последний использован: №3 на посте #389, следующий №1); блок CTA по теме. Прогнать через `stop-slop`.
3. `git add reels/... && git commit && git push -u origin <ветка>`.
4. Проверить `curl -sI https://raw.githubusercontent.com/capecode8-oss/preland/<ветка>/reels/<slug>.mp4` → `HTTP/2 200`.
5. `createScheduledPost`. Ответ `{id}` записать в `performance-tracker`.
6. Сообщить владельцу: время ET, ID поста, что музыку проверить вручную, TikTok вручную.

## Частые ошибки
- 404 на raw URL: подождать 30–60 с и повторить.
- Время в прошлом: проверить `date -u` и пересчитать из ET.
- Правка или удаление уже созданного поста через API не работает по заявлению владельца: владелец удаляет вручную, мы создаём заново. Поэтому финальную проверку подписи делать ДО создания поста.
