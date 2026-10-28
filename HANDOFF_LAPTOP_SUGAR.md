# Handoff для Claude Code на ноутбуке: ролик «What if you quit sugar» (low-poly 3D)

Репозиторий `capecode8-oss/preland`, ветка `claude/schedule-5-reels-metricool-ip1tp7`. Скиллы лежат в `.claude/skills/` (читать `motion-director`, `explainer-reel-builder`, `threejs-*`, `remotion-*`, `reel-script-engine`). Прототип сцены: `tools/reels/lowpoly_demo/apartment_sugar.html` (Three.js, квартира, 3 кадра). Правила проекта: `CLAUDE.md` (блок «ПРИОРИТЕТ ПРАВИЛ»).

## Текст для ElevenLabs (VOICE: простой язык, цифры прописью; каждый блок генерировать отдельно)
You can't really quit sugar for thirty days. It's hiding in four foods you'd never suspect. And number four is in your fridge right now.

Number four. Ketchup. Every squirt has about one spoon of sugar. One spoon. In ketchup.

Number three. A granola bar. Some have up to three spoons. Number two. Pasta sauce. One small bowl can have three.

And number one. Fruit yogurt. Some cups have four spoons or more. That's most of your day in one little cup. Doctors say women should stop at six.

Now add it up. A squirt of ketchup, a granola bar, and one yogurt. You passed six before lunch. So how do you really quit? Look at the label. Find the line that says added sugars. Take that number and divide it by four. That's your spoons.

Comment the word glow, and I'll message you what your body is trying to tell you.

## Текст для титров (SCREEN)
You can't really quit sugar for 30 days. It's hiding in four foods you'd never suspect. And #4 is in your fridge right now.

#4. Ketchup. Every squirt has about one spoon of sugar. One spoon. In ketchup.

#3. A granola bar. Some have up to three spoons. #2. Pasta sauce. One small bowl can have three.

And #1. Fruit yogurt. Some cups have four spoons or more. That's most of your day in one little cup. Doctors say women should stop at 6.

Now add it up. A squirt of ketchup, a granola bar, and one yogurt. You passed six before lunch. So how do you really quit? Look at the label. Find the line that says added sugars. Take that number and divide it by 4. That's your spoons.

Comment GLOW, and I'll DM you what your body is trying to tell you.

Структура: хук с темой («can't really quit… hiding in four foods») → обратный отсчёт 4–3–2–1, каждый номер открывает следующий → сложение «past six before lunch» → как реально считать по этикетке → CTA.
Графика: 3D-кухня, на каждом номере предмет выезжает на стойку и рядом растёт стопка ложек сахара (кетчуп 1, батончик до 3, соус до 3, йогурт 4+); справа счётчик «6 = limit», на сложении стопки превышают отметку 6.

Источники (вторичные, цифры зависят от бренда, поэтому в тексте «about / some / up to / can»): кетчуп около 4 г на столовую ложку, соус 8–12 г на полчашки, батончик 7–14 г, ароматизированный йогурт 17–33 г на порцию (блоги и новости, USDA FoodData Central не открывали); этикетка «Added Sugars» есть на американских упаковках; CDC 2017–2018: взрослые женщины в среднем 15 ч. л. добавленного сахара в день; лимит AHA 6 ч. л. для женщин; фруктовый йогурт 12–13 г добавленного сахара (≈ половина лимита 25 г), данные поиска уровня B, говорить «can»; AHA для женщин 25 г (6 ч. л.) добавленного сахара в день; 4 г сахара = 1 ч. л.; Wise et al. (Monell, AJCN 2015: 13 человек против 16; после 3 месяцев сниженного сахара еда казалась слаще, предпочитаемая сладость не изменилась). Выборка малая: на экране мелко «small study, 3 months».

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
