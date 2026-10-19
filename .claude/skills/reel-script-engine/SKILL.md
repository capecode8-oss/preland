---
name: reel-script-engine
description: Write the spoken script and the closing call-to-action for every @thekiramethod reel (talking head, voiceover, caption opening). Use BEFORE any Veo prompt or caption. Enforces a hook that stops the scroll, open loops that keep people to the end, plain language, fact-checked claims, and a value-based keyword CTA (SAFETY / GLOW / CALM). Applies automatically, the owner should not have to re-explain it.
---

# REEL SCRIPT ENGINE — сценарий, удержание, призыв

Читать ПЕРЕД любым диалогом, Veo-промптом и капшеном. Не спрашивать владельца про формат: применять по умолчанию.
Всегда читать вместе со скиллом `reel-growth-playbook` (алгоритм Instagram с уровнем доказательности, рост подписчиков, протокол команды, журнал замечаний владельца) и его `references/fact-bank.md` (проверенные факты).
Источники по CTA: вендорские блоги про comment-to-DM (Manychat и др.), цифры конверсии там не независимые, поэтому правила ниже это тактики для теста, не доказанные факты.

## 1. Роль
Пиши как сильный редактор, контент-мейкер и маркетолог одновременно. Цель текста: человек не может оторваться, досматривает до конца, понимает суть за 5 секунд даже в 15 лет, получает конкретную пользу и сам хочет написать кодовое слово.

## 2. Каркас: 4 клипа по 10 секунд (≈40 с), ≈20–22 слова на клип, речь одним потоком без пауз
| Клип | Роль | Что делает |
|------|------|-----------|
| 1 | HOOK | Первые 3 слова: противоречие, угроза или узнавание («Your Uber driver says your name. That proves nothing.»). До 15 слов. Открывает КОНКРЕТНУЮ петлю («Here's the one check that does»), не туман. |
| 2 | SCENE + WHY | Мини-сцена «ты в ней» и причина простыми словами. Новый поворот (re-hook). |
| 3 | FIX | Конкретные 2–3 шага, число, жест руками («all three»). Решение проблемы из хука. |
| 4 | PAYOFF + CTA | Закрыть петлю, потом призыв по формуле ниже. |

Эмоциональная дуга: тревога, ясность, облегчение. Подача через историю с героем («я/ты»), не лекция. Финал содержит момент «это про меня».

## 3. Обязательные проверки до выдачи (если хоть одна не пройдена, переписать)
1. **Пересказ:** 15-летний пересказывает суть одним предложением (проблема → решение).
2. **Логика:** нет дыр. Пример ошибки из практики: «you say yes and he's got your name», хотя водитель сам назвал имя.
3. **Факты:** каждое утверждение про здоровье/безопасность проверено через WebSearch, без выдуманной статистики, ссылки в ответе. Нет источника: смягчить («имя легко узнать»), не придумывать цифру.
4. **Язык:** слова из разговора, без терминов (не «кортизол», не «капсид»).
5. **Адресат пересылки:** можно назвать, кому отправят (дочери, маме, подруге).
6. **Ценность:** в ролике есть польза до CTA (шаг, правило, цифра), CTA не первая причина смотреть.

## 4. CTA по формуле (последние ≈10 секунд, ≤22 слов)
Пять элементов, все в одной связке:
1. **Назови ценность, не файл:** «45 situations like this», не «my guide» и не «a PDF».
2. **Тизер содержимого:** 1–2 конкретные вещи изнутри («hotels, airports, cruise ships»). Брать только то, что реально есть в продукте.
3. **Одно простое слово ЗАГЛАВНЫМИ + что произойдёт:** «Write SAFETY and I'll send it.» Одно действие, не два.
4. **Связь с болью ролика:** CTA продолжает проблему, не прыгает в сторону.
5. **В подписи (не в речи):** FOLLOW первым («так оно придёт в основные сообщения»), блок из CLAUDE.md.

### Банк CTA (ротировать, одинаковый не ставить два раза подряд)
SAFETY:
- «Doesn't match? Don't get in. My guide has 45 situations like this: hotels, airports, cruise ships. Write SAFETY and I'll send it.»
- «Midnight knock, a stranger's car, a hotel room that feels wrong. I wrote down what to do in 45 situations. Write SAFETY.»
- «Before your next trip, get all 45. Hotels, airports, cruise ships, step by step. Write SAFETY and I'll send it.»
GLOW:
- «Feel like your skin is aging faster than it should? My guide explains why, in plain words. Write GLOW and I'll send it.»
- «Tired, bloated, and nobody can tell you why? Four short guides on what your body is saying. Write GLOW.»
CALM: «Wake up at 3AM for no reason? There are four things to try tonight. Write CALM and I'll send them.»

### Запрещено в CTA
free / gift / price / «link in bio» для GLOW и CALM / «send the link» / «I have even more like this in my guide» (общая фраза, владелец отклонил) / хэштеги / обещания, которых нет в продукте («recipes», если бот шлёт гайды) / выдуманная срочность.
Бот шлёт ссылку на Lava.top preland, поэтому обещаем «guide», а не бесплатный файл.

## 5. Правила Veo (после проблем с субтитрами и пропуском слов)
- Каждый клип: один блок диалога целиком, «exact script, word for word, one continuous take, no pauses between sentences, says nothing else».
- Без двоеточий и цитат внутри цитат в реплике. ≤22 слов на клип.
- В начале промпта «IMPORTANT: absolutely no subtitles, no captions, no on-screen text of any kind», в конце «No subtitles. No captions. No on-screen text.» (титры потом ставит Remotion). Если Veo всё равно рисует, генерировать ещё дубль.
- В каждом клипе повторять одинаковые блоки LOOK, PLACE, CAMERA, VOICE. Стартовый кадр следующего клипа это последний кадр предыдущего. Одежда эксперта: чёрный пиджак и белая рубашка, без стетоскопа и бейджей.
- Звук только голос и тихий фон, без музыки.

## 6. Тест и учёт
Два рилса за неделю с разными кодовыми словами или CTA, сравнить комментарии на 1000 охвата и DM. Результат записать в performance-tracker.

## 7. Как показывать результат
Выдавать владельцу: текст по клипам и готовые промпты. Командный аудит и «фокус-группа» это моя симуляция, не реальные люди, подавать одной строкой и честно.
