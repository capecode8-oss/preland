---
name: explainer-reel-builder
description: Build animated explainer reels from code (no AI video model) for @thekiramethod: kinetic captions, vector infographics, cutaway diagrams, low-poly 3D counters, timelines, subscribe/CTA end cards. Use when the owner sends a reference video or idea in the "motion-graphics explainer" style (dark infographic, 3D counter, cutaway physics, schematic with word-by-word captions) or asks for a fact reel, counter reel, or "how it works" reel. AUTO-TRIGGER: apply without being asked; read references/style-cards.md first.
---

# EXPLAINER REEL BUILDER (код вместо видеомодели)

Работает в облачной среде Claude Code (браузерная версия): Node, Chromium (headless), FFmpeg, Java и Python есть. Десктоп не нужен.

## Конвейер (каждый раз, без вопросов к владельцу)
1. **Референс**: нарезать кадры (1 кадр/с, для быстрых сцен 2–3/с), записать каждую сцену с таймкодом, словарь сцен, палитру, шрифты, ритм (см. `reel-growth-playbook`: «ремейк рилса конкурента»).
2. **Сценарий и факты**: как в `reel-script-engine` (хук первыми словами, петли, простые слова, CTA со словом). Все медицинские и числовые утверждения проверять поиском, источники в ответе. Нет источника, не говорим.
3. **Раскадровка**: таблица «сцена, секунды, что рисуем, подпись» (≈2–3 с на сцену, 2–4 слова на подпись).
4. **Сборка**: HTML + SVG/CSS/Canvas (плоская графика) или Three.js (низкополигональное 3D) с детерминированным временем `t`; кадры снимает headless Chromium (`--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`), FFmpeg собирает MP4. Three.js ставится через npm. Рендер 3D на CPU медленный (оценка 15–40 минут на 24 с в 1080×1920).
5. **Проверка**: контактный лист кадров глазами (текст в безопасной зоне y 270–1520, 1080×1920, ничего не обрезано).
6. **Звук (SFX)**: эффекты синтезируются кодом, `python3 tools/reels/sfx_synth.py` (whoosh, tick, pop, ding, riser, impact, typing; готовые WAV в `assets/sfx/`), микшируются на смены сцен и счётчики через ffmpeg `adelay`+`amix` под музыку (громкость SFX ниже музыки). Реалистичные звуки (стекло, шаги, ткань) синтезом не делаем: брать лицензированные библиотеки или сервис SFX, файл присылает владелец.
6b. **Музыка и голос**: музыка из `music/` (правило музыки из CLAUDE.md, без затухания) или озвучка, присланная владельцем (mp3). Синтезатора речи в среде нет, распознавания речи тоже нет: тайминги слов берём из сценария или из файла таймингов, который экспортирует сервис озвучки.
7. **Выдача**: MP4 в `reels/`, commit + push, `SendUserFile`, планирование как обычно.

## Правила
- Оригинальный дизайн под нашу нишу (здоровье женщин 35+), не копия чужих ассетов и текстов.
- «Страшилки» и обещания лечения не используем; любая «схема» с добавками и лекарствами требует оговорки «не медицинская рекомендация» и проверки по источникам.
- Подписи слов: белые, ключевое слово подсвечено цветом; нижняя граница текста не ниже y=1520.
- Каждая новая правка владельца записывается в журнал замечаний `reel-growth-playbook`.
