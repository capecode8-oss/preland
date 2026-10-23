# VEO TEMPLATES (рабочие под Veo 3 / Flow). Брать отсюда, не изобретать заново.

## Правила
- 4 клипа по 10 с. Речь на клип 16–20 слов (22 уже мямлит), простые слова, без двоеточий и цитат внутри цитат, без пауз между предложениями.
- Клип 1 стартует с картинки Kira в этой же сцене и одежде (сгенерировать по LOOK + PLACE). Клипы 2–4 стартуют с последнего кадра предыдущего. Один голос, одинаковые блоки LOOK/PLACE/CAMERA в каждом промпте (не «замени блок»).
- Запрет субтитров ВНАЧАЛЕ и В КОНЦЕ промпта (титры ставит Remotion). Если Veo всё равно рисует или мямлит: 3–4 дубля, меньше слов, медленнее.
- Одежда эксперта: чёрный пиджак, белая рубашка, без стетоскопа, бейджей, логотипов.
- СЦЕНА ПОДБИРАЕТСЯ ПОД ТЕМУ и каждый раз разная (кухня и машина ниже это только примеры, не обязательные). Условия: место сразу узнаётся по теме, 3–4 живые детали, понятный источник света, реквизит темы в руках или рядом, не пастельно и не стерильно. Неон-фиолет можно как акцент, если подходит, но не обязателен.

## Как выбрать сцену (идеи, не список)
- Отель, дверь, номер: коридор или вход в номер, тёплая лампа, окно с городом.
- Такси, поездка: ночная улица у обочины или салон машины.
- Аэропорт, самолёт: зона вылета или кресло у иллюминатора, дневной свет из окна.
- Еда, вес, питание: кухня любого стиля (утренняя настоящая, кладовая, проход супермаркета), еда в руках.
- Кожа, старение: ванная с зеркалом и настоящими баночками, свет из окна.
- Мышцы, движение: угол дома с гантелями, рассветный свет или спортзал.
- Сон, усталость: спальня на рассвете, тумбочка.
- Деньги, быт: кухонный стол с бумагами и чашкой.
Описывать PLACE так: место + 3–4 конкретные детали + источник света + реквизит + одна цветовая нота.
- Жесты простые и привязаны к фразам. Пальцы: «exactly five fingers on each hand».

## Общие блоки
HEAD (первой строкой промпта):
IMPORTANT: absolutely no subtitles, no captions, no on-screen text of any kind anywhere in the video. The picture contains only the live-action scene, and the speech is audio only.

SPEECH (вторым блоком, подставить {SCRIPT}):
SPEECH, the most important part: the woman speaks this exact script, word for word, in clear American English, in one continuous take with no pauses between sentences, at a calm steady unhurried pace, every single word distinctly and clearly pronounced, close-miked clean voice, and she says nothing else: "{SCRIPT}"

LOOK:
A woman in her mid-40s with the same face as the reference image, dark brown shoulder-length wavy hair pulled neatly back with a few loose strands, polished makeup with soft glossy lips, small gold hoop earrings, a sharply tailored black blazer over a crisp white collared shirt with the sleeves rolled to mid-forearm, no badge, no logos, a composed expert look with calm authority.

TAIL (последней строкой):
Same low, calm, warm female voice as the previous clips. Audio is only her voice and {AMBIENCE}, no music, no other voices. Exactly five fingers on each hand, natural hand proportions, no morphing, the face, outfit and {PLACE_NAME} stay identical to the first frame.

No subtitles. No captions. No on-screen text.

## ПРИМЕР СЦЕНЫ A: тёмная неон-кухня (для еды, веса; использовать только если подходит теме)
CAMERA: Vertical 9:16 cinematic video, medium shot at the counter, slow gentle push-in, shallow depth of field.
PLACE: A dark, moody, high-end home kitchen at night. Polished black granite counter with glossy reflections, a dark marble backsplash lit by a violet-purple LED strip casting a soft neon purple glow with out-of-focus purple bokeh, {PROPS_ON_COUNTER}. Low-key lighting, deep violet shadows, warm soft glow on her face, natural skin tones (her skin is never purple). The background is out of focus and completely still.
AMBIENCE: a quiet kitchen room tone. PLACE_NAME: kitchen.
Порядок блоков: HEAD, SPEECH, CAMERA + LOOK, PLACE, GESTURES, TAIL.

## ПРИМЕР СЦЕНЫ B: ночная машина, Нью-Йорк, селфи (для такси и поездок; использовать только если подходит теме)
CAMERA: Vertical 9:16 selfie video, filmed as if she holds her phone at arm's length with her right arm extended toward the lens (the arm at the edge of the frame, no phone visible), wide front-camera look, slight natural handheld shake, mild phone-camera grain, her face upper center.
PLACE: She sits in a modern dark sedan at night, parked at a curb in Manhattan, a seat belt across her chest. Black leather seats, a soft violet-and-pink ambient glow along the dashboard and door panel warming her face, a glass sunroof above showing the glowing night sky between tall buildings. Outside the windows a rain-slick street with violet, magenta and cyan neon reflections, out-of-focus yellow taxi lights and city bokeh. Natural skin tones, soft rim light, cozy gentle glow.
AMBIENCE: a quiet car cabin with faint city traffic outside. PLACE_NAME: car.

## ПРИМЕР ЖЕСТОВ
«She jabs one finger toward the lens on the first sentence, shakes her head slowly on the second, and on the last sentence points one index finger downward toward the area below the frame and holds that pose until the end.»

## СЦЕНА C: ПОДКАСТ-СТУДИЯ — ФОРМАТ ПО УМОЛЧАНИЮ С Oct 23 2026 (решение владельца)
Кира сидит как эксперт в уютной подкаст-студии и живо говорит. Владелец монтирует в Remotion: Кира внизу, моушн-графика сверху. Поэтому КАМЕРА СТАТИЧНАЯ, кадр идентичен во всех клипах, голова в верхней половине кадра, микрофон снизу не закрывает рот.
CAMERA: Vertical 9:16, locked-off static tripod shot, no zoom, no push-in, no handheld shake, medium shot, her head and shoulders in the upper half of the frame, shallow depth of field.
PLACE: A cozy podcast studio. A teal-cyan blue wall with built-in shelves holding a snake plant, a trailing green pothos plant and a small ceramic vase, a tan velvet armchair back behind her, the edge of a large octagonal softbox glowing warm in the top-right corner. A large plain black broadcast microphone on a boom arm in the lower center foreground, below her chin, never covering her mouth, no logos. Warm soft key light on her face, cool cyan fill from the wall, natural skin tones. The background is completely still.
PERFORMANCE: She talks like a real person telling a friend something interesting: steady eye contact with the lens, natural blinking, small head nods and tilts, eyebrows that move with the words, smile on good news, serious look on warnings. She gestures with her right hand in the open space left of the microphone (open palms, counting on fingers, small pointing moves) in time with the words; left hand mostly out of frame; never touches the microphone; hands never cross in front of her face. Привязывать жесты к конкретным словам реплики.
SPEECH-добавка для этой сцены: «starting within a third of a second of the first frame and finishing right at the end of the clip» (без хвостов тишины, удобно резать).
AMBIENCE: a very quiet studio room tone. PLACE_NAME: studio.
Стартовый кадр (картинка с лицом Киры): та же студия, Кира за микрофоном, чёрный пиджак и белая рубашка, без текста и логотипов.
Если Veo тянет руки к микрофону: «her hands stay well to the left of the microphone».
Перед выдачей к каждому сценарию добавлять РАСКАДКУ ГРАФИКИ для Remotion (что показывать сверху в каждом клипе).
