---
name: batch-processor
description: Produces 4-6 KIRA reels in one session. Runs full pipeline for each reel — hook audit, footage selection, render, QA, preview. Tracks progress and prevents errors across the batch. Use when creating multiple reels for one day.
---

# KIRA Batch Processor

## ПАЙПЛАЙН ОДНОЙ СЕССИИ — 4-6 РИЛСОВ

### Порядок для каждого рилса в batch:

```
1. FOOTAGE-MANAGER → выбрать клип (не повтор!)
2. KIRA-HOOKS → написать хук → аудит команды (7 человек) → PASSED
3. KIRA-CAPTIONS → написать капшен → аудит команды → PASSED
4. RENDER → ffmpeg рендер по спецификациям
5. QUALITY-CHECK → 7-пунктовый чеклист
6. JPG PREVIEW → показать пользователю
7. ОДОБРЕНИЕ → только потом следующий рилс
```

---

## ТРЕКЕР BATCH СЕССИИ

Заполнять по мере производства каждого рилса:

```
BATCH DATE: [дата]
GOAL: [N] рилсов

REEL 1:
  Clip: ___________
  Нища: ___________
  Hook: ___________
  Mike score: ______
  Red verdict: _____
  Output file: ______
  Preview: ✅/❌
  User approved: ✅/❌

REEL 2:
  Clip: ___________
  Нища: ___________
  Hook: ___________
  Mike score: ______
  Red verdict: _____
  Output file: ______
  Preview: ✅/❌
  User approved: ✅/❌

[продолжить до REEL N]

ИТОГ: [N]/[N] рилсов готово
ИСПОЛЬЗОВАННЫЕ КЛИПЫ СЕГОДНЯ: [список]
```

---

## ПРАВИЛА BATCH

### Обязательные:
- **Один хук на один клип** — не смешивать
- **Разные ниши в batch** — не делать 4 рилса про одно и то же
- **Одобрение после каждого превью** — не пропускать
- **Все клипы записаны** — в footage-manager журнал

### Рекомендованный микс для дня (4-6 рилсов):
- 1-2 Travel / Airport / Hotel
- 1-2 Health / Food / Pharmacy  
- 1 Money / Rights / Consumer
- 1 Home / Safety (если есть подходящий клип)

### Запрещено:
- Одинаковая формула хука в двух рилсах одного дня
- Одна и та же ниша 3 раза подряд в batch
- Публикация без JPG превью и одобрения

---

## БЫСТРЫЙ СТАРТ BATCH

Когда пользователь говорит "сделай [N] рилсов":

1. **Проверить footage-manager** — какие клипы доступны сегодня
2. **Предложить темы** — по 1 теме на рилс (разные ниши), показать список текстом
3. **Дождаться одобрения тем** — пользователь может изменить
4. **Производить один за другим** — каждый через полный pipeline
5. **После каждого** — JPG превью → одобрение → следующий

---

## NAMING CONVENTION

```
Формат файлов:
kira_[дата]_[номер]_[нища].mp4
kira_[дата]_[номер]_[нища]_preview.jpg

Примеры:
kira_aug17_1_travel.mp4
kira_aug17_2_pharmacy.mp4
kira_aug17_3_hotel.mp4

GitHub путь:
/home/user/preland/reels/[файл]
```

---

## ШАБЛОН ОТЧЁТА ПОСЛЕ BATCH

После завершения всего batch — показать пользователю:

```
🎬 BATCH ГОТОВ — [дата]

✅ REEL 1 — [тема/нища]
   Hook: "[первая строка хука]"
   Mike: 🟢 STRONG / 🔥 VIRAL
   Файл: kira_[дата]_1_[нища].mp4

✅ REEL 2 — [тема/нища]
   ...

📋 СЛЕДУЮЩИЙ ШАГ:
→ Добавь музыку и геотег (New York) в Metricool вручную
→ Расставь посты по расписанию (4-5 рилсов/день)
→ Первый пост — самый сильный хук по Mike score
```
