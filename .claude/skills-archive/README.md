# Архив скиллов (Oct 25 2026)
Убраны из активных скиллов, потому что дублируют или противоречат текущему пайплайну (`reel-script-engine` + `reel-growth-playbook` + `references/veo-templates.md`, `kira-carousel-playbook`). Ничего не удалено, история в git. Вернуть: `git mv .claude/skills-archive/<имя> .claude/skills/<имя>`.
- instagram-carousel: чужой общий HTML-шаблон 420x525 Poppins, противоречит нашим каруселям 1080x1350 (`kira-carousel-playbook`, `tools/carousel`).
- find-skills: служебный, не используется.
- niche-templates: «placeholder stats», риск выдуманных цифр, противоречит правилу «факты только проверенные».
- batch-processor: учёт партии старого B-roll формата 5 с.
- kira-talking-head: старые промпты Veo, требует субтитры; заменён Сценой C в `veo-templates.md`.
- ai-video-prompts: Kling/Runway/Pika и 7 слоёв, дублирует `veo-templates.md`.
