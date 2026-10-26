# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст для ElevenLabs (VOICE: простой язык для 15-летнего, цифры прописью; генерировать КАЖДЫЙ блок отдельно, склеить в редакторе)
What happens if you quit sugar for thirty days? People promise three things. You get thin. You stop wanting sweets. Your skin glows. Scientists tested all three. None worked the way people say.

First, getting thin. People ate less sugar for eight weeks. Their weight didn't move.

Next, wanting sweets. People ate way less sugar for three months. Food tasted sweeter to them. But they still wanted sweets just as much. Your mouth changes. Your wanting doesn't.

Last, glowing skin. We looked. We found no test that shows it. Not one. So what really helps? Know your sugar. The average woman eats about fifteen spoons a day. Doctors say six. Look at any food label. Take the sugar number and divide it by four. That's your spoons.

Comment the word glow, and I'll message you what your body is trying to tell you.

## Текст для титров (SCREEN: цифры и GLOW как в дизайне; тайминг слов из готового аудио (Whisper), текст из этой версии, сопоставление по порядку слов: «thirty»=«30», «the word glow»=«GLOW», «message you»=«DM you»)
What happens if you quit sugar for 30 days? People promise three things. You get thin. You stop wanting sweets. Your skin glows. Scientists tested all three. None worked the way people say.

First, getting thin. People ate less sugar for 8 weeks. Their weight didn't move.

Next, wanting sweets. People ate way less sugar for 3 months. Food tasted sweeter to them. But they still wanted sweets just as much. Your mouth changes. Your wanting doesn't.

Last, glowing skin. We looked. We found no test that shows it. Not one. So what really helps? Know your sugar. The average woman eats about 15 spoons a day. Doctors say 6. Look at any food label. Take the sugar number and divide it by 4. That's your spoons.

Comment GLOW, and I'll DM you what your body is trying to tell you.

Структура: хук с темой и петлёй (три обещания, «none worked») → проверка по очереди (weight, wanting sweets, glowing skin) → «what really helps» → CTA.

Источники: CDC 2017–2018: взрослые женщины в среднем 15 ч. л. добавленного сахара в день; лимит AHA 6 ч. л. для женщин; фруктовый йогурт 12–13 г добавленного сахара (≈ половина лимита 25 г), данные поиска уровня B, говорить «can»; AHA для женщин 25 г (6 ч. л.) добавленного сахара в день; 4 г сахара = 1 ч. л.; Wise et al. (Monell, AJCN 2015: 13 человек против 16; после 3 месяцев сниженного сахара еда казалась слаще, предпочитаемая сладость не изменилась). Выборка малая: на экране мелко «small study, 3 months».

## Раскадровка (на экране крупно тот же текст, что в озвучке: титры по словам)
| Время | Сцена | Движение и графика |
|---|---|---|
| 0–9 | Квартира вечером, на стойке сладости, над героем заголовок «What happens if you quit sugar for 30 days?» и три карточки WEIGHT / CRAVING / GLOW, которые по очереди проверяются | Титры по словам, наезд 6%, герой задумчиво смотрит на пончик, затем выкидывает его в урну |
| 9–18 | Две тарелки пудинга: слева «kept eating sugar», справа «quit for 3 months». На правой метка «tastes SWEETER» | Шкала сладости справа растёт, слева ровная. Подпись «small study» |
| 18–27 | Шкала «FAVORITE LEVEL OF SWEET»: у обеих групп стрелка на одной отметке. Герой пожимает плечами. Затем крупно «?» | Шкала не двигается на слове «didn't change», пауза 0.3 с перед вопросом |
| 27–38 | Крупно этикетка, 4 г = 1 ложка, ряд из 6 ложек | Ложки наполняются по одной на «count», счёт 1…6 |
| 38–45 | Утро, голубое небо, яблоки, улыбка | Плашка `COMMENT GLOW`, стрелка вниз; нижняя треть пустая под Киру |

## Правила
- 1080×1920, 30 fps, MP4 H.264. Текст сверху в зоне y 140–520, Montserrat Bold (файл `products/Montserrat-Bold.ttf`), ≤8 слов на экран. Герой в зоне y 600–1350.
- Не писать на экране обещаний про кожу, энергию, вес. Никаких цен и слова «free».
- Анимация: ease in/out, антиципация, звуки из `tools/reels/sfx_synth.py`. Голос владелец накладывает сам, под него подогнать тайминг.
- Сначала один кадр на каждый блок, потом контактный лист, потом полный рендер. На ноутбуке запускать Chromium с GPU (без SwiftShader) для скорости.
- Результат: `reels/sugar_whatif_3d.mp4` и 4 кадра-скриншота. Закоммитить и запушить в ту же ветку.
