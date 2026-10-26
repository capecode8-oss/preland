# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст озвучки (English, ≈120 слов, ≈45 с; хук произносится голосом И дублируется титрами; не менять слова)
Структура Triple Loop: хук открывает петлю «что изменилось и что нет», на 3-м блоке новая петля «что тогда показывает прогресс», в 4-м закрывается, 5-й это призыв.
1. (0–9 с, HOOK + INTENSIFIER) What happens when you quit sugar for three months? Researchers tested it. One thing changed. One didn't. And it's not what you'd bet.
2. (9–18 с, первая выдача + «but there's a catch») First, food tastes sweeter. After three months, people rated puddings sweeter than the group that kept eating normally. Sounds like a win. But there's a catch.
3. (18–27 с, вторая выдача + REHOOK) What they wanted didn't change. Their favorite level of sweet stayed exactly the same. So if cravings don't tell you how you're doing, what does?
4. (27–38 с, закрытие петли + польза) The label. Four grams of sugar is one teaspoon. The heart association says six teaspoons a day is the most for women. Divide the grams by four and count.
5. (38–45 с, CTA) Comment GLOW and I'll DM you the guide to what your body's been trying to tell you.

Источники: AHA для женщин 25 г (6 ч. л.) добавленного сахара в день; 4 г сахара = 1 ч. л.; Wise et al. (Monell, AJCN 2015: 13 человек против 16; после 3 месяцев сниженного сахара еда казалась слаще, предпочитаемая сладость не изменилась). Выборка малая: на экране мелко «small study, 3 months».

## Раскадровка (на экране крупно тот же текст, что в озвучке: титры по словам)
| Время | Сцена | Движение и графика |
|---|---|---|
| 0–9 | Квартира вечером, на стойке сладости, над героем заголовок «What happens when you quit sugar for 3 months?» | Титры по словам, наезд 6%, герой задумчиво смотрит на пончик, затем выкидывает его в урну |
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
