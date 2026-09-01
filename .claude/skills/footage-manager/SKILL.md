---
name: footage-manager
description: Select a clip from the footage library for the current reel. Tracks usage history to prevent repeats. Run this FIRST — before writing the hook.
---

# Footage Manager
## Библиотека клипов @thekiramethod

---

## БИБЛИОТЕКА — полный список

### ✈️ TRAVEL клипы (32 штуки)
Путь: `/home/user/preland/footage/travel/`
Использовать когда продукт **SAFE** (Travel Safety Guide)

`1_3, 1_4, 1_5, 1_6, 1_7, 1_10, 1_12, 1_17, 1_20, 1_24, 1_25, 1_27, 1_29, 31_1, 31_3, 32_1, 32_3, 32_4, 32_5, 32_6, 32_7, 32_8, 32_9, 32_10, 32_11, 32_12, 32_13, 32_14, 32_15, 32_16, 32_17, 32_18`

### 🌙 GENERAL клипы (13 штук)
Путь: `/home/user/preland/footage/general/`
Использовать когда продукт **CALM** (3AM Calm Card) или relationship/health темы

`1_2, 1_8, 1_11, 1_14, 1_15, 1_16, 1_19, 1_23, 1_26, 1_28, 1_30, 31_2, 32_2`

❌ Удалены навсегда: `1_9`, `1_13`, `1_18`, `1_21`, `1_22`, `1_1`

---

## ЖУРНАЛ ИСПОЛЬЗОВАНИЯ

| Дата | Клипы |
|------|-------|
| Aug 13 | 1_11, 1_12, 1_14, 1_15 |
| Aug 19 | 1_19, 1_15, 1_23, 1_25, 1_18 |
| Aug 22 | 32_18, 32_13, 32_12, 32_6, 32_8, 32_9 |
| Aug 23 | 32_7, 32_4, 32_11, 32_14, 32_15 |
| Aug 24 | 32_7, 32_4, 32_5, 32_17, 32_1, 32_18, 32_9 |
| Aug 26 | 1_2, 32_7, 32_8, 32_15, 1_8, 32_13, 32_14, 32_16 |
| Aug 27 | 32_18, 32_6, 1_24, 32_5, 32_1 |
| Aug 25 | 32_10, 32_12, 32_16, 32_6, 32_8, 32_13 |
| Aug 26 | 1_3, 1_4, 1_5, 1_6, 1_7, 1_8, 1_10, 1_16 |
| Aug 27 | 32_11, 32_14, 32_15, 32_2, 1_1, 1_2 |
| Aug 27 | 31_2 |
| Sep 1 | 1_17, 32_4, 32_7 |

---

## ЖУРНАЛ ТЕМ (slug — повторять нельзя 14 дней)

| Дата | Slug / тема |
|------|-------------|
| Aug 13 | overhead-bin-theft, hotel-room-entry, cruise-balcony-entry, airport-helper-trap |
| Aug 19 | baggage-claim-swap, airport-atm-trap, cruise-port-scam, hotel-receptionist, rome-waiter |
| Aug 22 | border-officer-phone, crew-2am, bangkok-taxi, gate-agent-bump, eu-compensation, blue-zone-food |
| Aug 23 | luggage-theft-window, window-seat-xrays, fa-greeting-screening, airport-thief-target, doctor-radiation-story |
| Aug 24 | hotel-receptionist-v2, overhead-bin-theft-v2, cruise-port-scam-v2, airport-helper-trap-v2, baggage-claim-swap, airport-atm-trap |
| Aug 25 | gate-easy-target, taxi-uniform-scam, cruise-card-cloned, hotel-checkin-watched, restaurant-abroad-customs, cruise-cabin-nightclub |
| Aug 26 | adventure-tour-deposit-scam, japan-izakaya-hidden-cover, airline-damage-claim-window, vietnam-motorbike-price-switch, paris-bracelet-scam, paris-tourist-menu-prices, airplane-usb-port-data, rental-car-insurance-trap |
| Aug 27 | terminal-profiled-by-thief, cruise-lower-deck-midnight, cruise-waiter-room-charge, nyc-subway-swipe-scam, viewpoint-photo-handoff, italy-service-split-scam, marriage-warning-signs |
| Sep 1 | safari-lodge-overcharge, flight-upgrade-secret, hotel-minibar-trap |

---

## ПРАВИЛА — железные

1. **Никаких повторов клипов** — нельзя использовать клип если он уже был сегодня или вчера
2. **Никаких повторов тем** — нельзя брать тему (slug) если она была в последние 14 дней. Смотреть ЖУРНАЛ ТЕМ перед брейнштормом.
3. **Ротация** — идти по библиотеке рандомно, не зацикливаться на первых клипах
4. **Batch** — если делаем 4-6 рилсов сразу, все клипы и все темы должны быть разными
5. **После выбора** — записать клип В ЖУРНАЛ ИСПОЛЬЗОВАНИЯ и slug В ЖУРНАЛ ТЕМ с сегодняшней датой

---

## КАК ВЫБРАТЬ КЛИП — ОБЯЗАТЕЛЬНЫЙ ПОРЯДОК

### ШАГ 1 — VISUAL PREVIEW (железное правило, без исключений)

**Никогда не выбирать клип по названию или старому маппингу. Всегда смотреть визуально.**

Для каждого кандидата:
```bash
FFMPEG="/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
$FFMPEG -y -ss 1 -i /home/user/preland/footage/[CLIP_ID].mp4 -vframes 1 -vf "scale=320:568" /tmp/preview_[CLIP_ID].jpg
```
Затем — Read `/tmp/preview_[CLIP_ID].jpg` и посмотреть что на кадре.

### ШАГ 2 — СОВПАДЕНИЕ С ТЕМОЙ ХУКА

После просмотра превью — выбрать клип где **визуал прямо связан с темой хука**:
- Хук про самолёт/перелёт → клип должен показывать самолёт/иллюминатор/аэропорт
- Хук про отель → клип должен показывать ресепшн/номер/коридор
- Хук про круиз → клип должен показывать палубу/каюту/море
- Хук про багаж → клип должен показывать багажную ленту/чемоданы
- Если тема и визуал не совпадают → брать следующий кандидат

### ШАГ 3 — ПРОВЕРИТЬ ЖУРНАЛ (не повторять)

Посмотреть журнал — убрать клипы использованные сегодня и вчера.

### БЫСТРЫЙ СПРАВОЧНИК 32-й серии (верифицирован визуально Aug 21 2026)

| Клип | Визуал |
|------|--------|
| 32_1 | Аэропорт — зал ожидания (сидит с чемоданом, табло) |
| 32_2 | Метро/сабвей (вагон) |
| 32_3 | Селфи с видовой точки (Рио-де-Жанейро) |
| 32_4 | Аэропорт — зал ожидания (другой ракурс, табло) |
| 32_5 | Самолёт — иллюминатор (window seat, пассажирка) |
| 32_6 | Отель — ресепшн (check-in стойка, две женщины) |
| 32_7 | Отель — номер (спальня, женщина в белом) |
| 32_8 | Кафе в Азии (Токио, город за окном) |
| 32_9 | Аэропорт — идёт с чемоданом по терминалу |
| 32_10 | Аэропорт — зал ожидания (= как 32_4) |
| 32_11 | Аэропорт — идёт по терминалу (другой ракурс) |
| 32_12 | Аэропорт — выход наружу (автоматические двери) |
| 32_13 | Круиз — каюта с балконом (вид на море) |
| 32_14 | Круиз — балкон/палуба (вечер, дusk) |
| 32_15 | Круиз — ресторан/терраса на палубе |
| 32_16 | Круиз — палуба (перила, открытый океан) |
| 32_17 | Круиз — палуба (средиземноморский порт, город) |
| 32_18 | Багажная лента — baggage claim (карусель, чемоданы) |

⚠️ Этот справочник — только для быстрой ориентации. Всё равно делать visual preview перед финальным выбором.

---

## ВЫВОД ФОРМАТА

```
📦 FOOTAGE MANAGER
Доступно сегодня: [N клипов] (исключены: [список])
Выбран: [ID клипа] — [краткое описание визуала]
Путь: /home/user/preland/footage/[ID].mp4
Журнал обновлён: [дата] → [ID]
```

---

## КОГДА НЕТ ПОДХОДЯЩЕГО КЛИПА

Если ни один из доступных клипов не подходит под тему хука:
→ Сообщить: `Нет подходящего клипа → NOVA генерирует Veo 3 промт в kira-hooks`
→ Клип в журнал НЕ записывать (нечего записывать пока нет видео)
→ После генерации AI-видео — записать дату генерации и тему вместо ID клипа
