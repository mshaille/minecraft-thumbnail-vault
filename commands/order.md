---
description: Take a thumbnail order (requests + optional reference images) and build a plan with settings adapted to the references
argument-hint: <what is wanted> [reference image paths...]
---
Use the `minecraft-thumbnail` skill, workflow **C (order)**.

Order: $ARGUMENTS

1. Create `orders/YYYY-MM-DD-short-name/` with `brief.md` from `templates/order.md` and a `refs/` folder. This folder is git-ignored, so client data never reaches the public repo. Fill "İstenenler" from the request.
2. Copy any reference images into `refs/`, run (from the vault root) `python3 tools/analyze_reference.py orders/<job>/refs/<img> -o orders/<job>/refs/previews --rel orders/<job>` for each, and look at the images and previews.
3. Using `techniques/adapt-to-reference.md`, fill "Referanstan uyarlanan ayarlar": for every step whose value should change, give the video value, the new value for this job, and the reason. With no references, start from `references/lessons.md` and the video defaults.
4. Write the bottom-to-top layer plan with exact settings and links to the technique notes.
5. List only the missing information that blocks the work (skins, scene, text, size), as short questions.
Reply in the user's language with a short summary and the path of `brief.md`.
