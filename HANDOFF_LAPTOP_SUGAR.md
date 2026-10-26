# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст озвучки (English, ≈100 слов, ≈40 с, не менять слова; факты проверены, источники ниже)
1. (0–9 с) Day one, you throw out every donut. Day three, you're digging through the trash. So what does quitting sugar actually do?
2. (9–19 с) The heart association says six teaspoons a day is the most a woman should have. Read a label and divide the grams by four. That's your teaspoons.
3. (19–29 с) Now the strange part. In one small study, people cut sugar for three months. Their food started tasting sweeter. But what they wanted didn't change.
4. (29–40 с) So if it's hard, don't beat yourself up. Comment GLOW and I'll DM you the guide to what your body's been trying to tell you.

Источники: AHA для женщин 25 г (6 ч. л.) добавленного сахара в день; 4 г сахара = 1 ч. л.; Wise et al. (Monell, AJCN 2015: 13 человек против 16, после 3 месяцев еда казалась слаще, предпочитаемая сладость не изменилась). Исследование малое, на экране подпись «small study».

## Раскадровка
| Время | Сцена | Движение и графика |
|---|---|---|
| 0–9 | Квартира вечером (тёплая лампа, окно, оранжевое небо). Стойка со сладостями. Герой выбрасывает пончики в урну, затем на «day three» тянется к урне | Наезд камеры на 6%, заголовок «What if you quit sugar?» сверху, подпись «Day 1», потом «Day 3» |
| 9–19 | Крупно этикетка и 6 ложек сахара в ряд | Цифра «÷ 4» на экране, ложки наполняются на слове «teaspoons» |
| 19–29 | Две шкалы: «TASTE» растёт, «WANT» ровная линия | Подпись «small study, 3 months». Герой пробует печенье, брови вверх |
| 29–40 | Утро, голубое небо, яблоки и вода, улыбка | Плашка `COMMENT GLOW`, стрелка вниз. Нижняя треть кадра (y>1360) пустая: туда Remotion кладёт Киру |

## Правила
- 1080×1920, 30 fps, MP4 H.264. Текст сверху в зоне y 140–520, Montserrat Bold (файл `products/Montserrat-Bold.ttf`), ≤8 слов на экран. Герой в зоне y 600–1350.
- Не писать на экране обещаний про кожу, энергию, вес. Никаких цен и слова «free».
- Анимация: ease in/out, антиципация, звуки из `tools/reels/sfx_synth.py`. Голос владелец накладывает сам, под него подогнать тайминг.
- Сначала один кадр на каждый блок, потом контактный лист, потом полный рендер. На ноутбуке запускать Chromium с GPU (без SwiftShader) для скорости.
- Результат: `reels/sugar_whatif_3d.mp4` и 4 кадра-скриншота. Закоммитить и запушить в ту же ветку.
