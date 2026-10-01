---
description: Take a thumbnail order (requests + optional reference images) and build a plan with settings adapted to the references
argument-hint: <what is wanted> [reference image paths...]
---
Use the `minecraft-thumbnail` skill, workflow **C (order)**.

Order: $ARGUMENTS

1. Create `orders/YYYY-MM-DD-short-name/` with `brief.md` from `templates/order.md` and a `refs/` folder. This folder is git-ignored, so client data never reaches the public repo. Fill "İstenenler" from the request.
2. **Pick the style** with `styles/README.md` (§1: brief keywords → style, then the reference decision tree). Choose one main style (S1–S11) and at most one secondary style, write them into `brief.md` with the reason. If the brief and references point to different styles, or nothing points anywhere, ask the user.
3. Copy any reference images into `refs/`, run (from the vault root) `python3 tools/analyze_reference.py orders/<job>/refs/<img> -o orders/<job>/refs/previews --rel orders/<job>` for each, and look at the images and previews.
4. Open the style card in `styles/`. It says which technique steps stay at default, change or are switched off, and which extra techniques (`techniques/style-catalog.md`, `character-pop.md`, `text-typography.md`, `action-effects.md`) are needed. Then, using `techniques/adapt-to-reference.md`, fill "Referanstan uyarlanan ayarlar": for every step whose value should change, give the video value, the style-card value, the value for this job, and the reason. With no references, start from `references/lessons.md` and the video defaults.
5. Check `guides/pitfalls.md` (policy, Mojang rules, licences) and `guides/common-mistakes.md` against the plan.
6. Write the bottom-to-top layer plan with exact settings and links to the technique notes.
7. List only the missing information that blocks the work (skins, scene, text, size), as short questions.
Reply in the user's language with a short summary and the path of `brief.md`.
