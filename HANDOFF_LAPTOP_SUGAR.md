# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст озвучки (English, 117 слов, ≈44 с; хук произносится голосом И дублируется титрами; не менять слова)
Структура Triple Loop: хук открывает петлю «что НЕ изменилось», блок 2 даёт первую выдачу и «It isn't», блок 3 закрывает петлю и открывает вывод, блок 4 польза, блок 5 CTA.

One fruit yogurt can use up half of a woman's sugar for the whole day. So researchers cut people's sugar way down for three months. Then one thing about them didn't change at all.

First, their food started tasting sweeter. Same pudding, sweeter, compared to people who ate normally. Sounds like a win. It isn't.

Because how sweet they wanted their food? Exactly the same. Three months, no change. So the wanting is not how you measure this.

Measure the label instead. Four grams of sugar is one teaspoon. Six teaspoons is the daily limit for women. Count to six.

Comment GLOW and I'll DM you the guide to what your body's been trying to tell you.

Источники: фруктовый йогурт 12–13 г добавленного сахара (≈ половина лимита 25 г), данные поиска уровня B, говорить «can»; AHA для женщин 25 г (6 ч. л.) добавленного сахара в день; 4 г сахара = 1 ч. л.; Wise et al. (Monell, AJCN 2015: 13 человек против 16; после 3 месяцев сниженного сахара еда казалась слаще, предпочитаемая сладость не изменилась). Выборка малая: на экране мелко «small study, 3 months».

## Раскадровка (на экране крупно тот же текст, что в озвучке: титры по словам)
| Время | Сцена | Движение и графика |
|---|---|---|
| 0–9 | Квартира вечером, на стойке сладости, над героем заголовок «Half your sugar. One yogurt.» | Титры по словам, наезд 6%, герой задумчиво смотрит на пончик, затем выкидывает его в урну |
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
