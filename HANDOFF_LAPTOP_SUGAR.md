# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст для ElevenLabs (VOICE: цифры прописью, без аббревиатур; генерировать КАЖДЫЙ блок отдельно, склеить в редакторе)
What happens if you quit sugar for thirty days? Everyone says you'll lose weight, stop craving it, and glow. Scientists checked. Only one of those came close.

Let's start with weight. In one eight week test, people ate food with less sugar. Their weight didn't change.

Now, cravings. In another test, people ate way less sugar for three months. Everything tasted sweeter. But they wanted the same sweet stuff. Their mouth changed. Their wanting didn't.

And the glow? We couldn't find one test that proves it in thirty days. Not one. So what actually works? Know your number. The average woman eats fifteen spoons of sugar a day. Doctors say six. Check any label, divide the sugar by four, and see where you land.

Comment the word glow, and I'll D M you what your body's been trying to tell you.

## Текст для титров на экране (SCREEN: цифры и GLOW как в дизайне; тайминг слов брать из готового аудио через Whisper или forced alignment, текст титров брать отсюда и сопоставлять по порядку слов: «thirty»=«30», «fifteen»=«15», «six»=«6», «D M»=«DM», «the word glow»=«GLOW»)
What happens if you quit sugar for 30 days? Everyone says you'll lose weight, stop craving it, and glow. Scientists checked. Only one of those came close.

Let's start with weight. In one eight-week test, people ate food with less sugar. Their weight didn't change.

Now, cravings. In another test, people ate way less sugar for three months. Everything tasted sweeter. But they wanted the same sweet stuff. Their mouth changed. Their wanting didn't.

And the glow? We couldn't find one test that proves it in 30 days. Not one. So what actually works? Know your number. The average woman eats 15 spoons of sugar a day. Doctors say 6. Check any label, divide the sugar by 4, and see where you land.

Comment GLOW and I'll DM you what your body's been trying to tell you.

Структура: хук с темой и петлёй → проверка трёх обещаний (weight, craving, glow) → «what actually works» → CTA.

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
