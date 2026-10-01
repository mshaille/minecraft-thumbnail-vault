---
description: Take a thumbnail order (requests + optional reference images) and build a plan with settings adapted to the references
argument-hint: <what is wanted> [reference image paths...]
---
**Rule: no laziness — aim for perfection.** Measure every element of the reference at ≥5× zoom with pixel profiles (stroke width/colour, inside/outside of edges, glow, shadow, colours, positions and sizes). Check every layer of an effect, not just the obvious one. Never stop at a plan; render the real draft, compare it side by side with the reference at full size and zoomed, re-measure, fix and re-render until it matches. Report every remaining difference honestly.

Use the `minecraft-thumbnail` skill, workflow **C (order)**.

Order: $ARGUMENTS

1. Create `orders/YYYY-MM-DD-short-name/` with `brief.md` from `templates/order.md` and a `refs/` folder. This folder is git-ignored, so client data never reaches the public repo. Fill "İstenenler" from the request.
2. **Pick the style** with `styles/README.md` (§1: brief keywords → style, then the reference decision tree). Choose one main style (S1–S11) and at most one secondary style, write them into `brief.md` with the reason. If the brief and references point to different styles, or nothing points anywhere, ask the user.
3. Copy any reference images into `refs/`, run (from the vault root) `python3 tools/analyze_reference.py orders/<job>/refs/<img> -o orders/<job>/refs/previews --rel orders/<job>` for each, and look at the images and previews.
4. Open the style card in `styles/`. It says which technique steps stay at default, change or are switched off, and which extra techniques (`techniques/style-catalog.md`, `character-pop.md`, `text-typography.md`, `action-effects.md`) are needed. Then, using `techniques/adapt-to-reference.md`, fill "Referanstan uyarlanan ayarlar": for every step whose value should change, give the video value, the style-card value, the value for this job, and the reason. With no references, start from `references/lessons.md` and the video defaults.
5. Check `guides/pitfalls.md` (policy, Mojang rules, licences) and `guides/common-mistakes.md` against the plan.
6. Write the bottom-to-top layer plan with exact settings and links to the technique notes.
7. **Do not stop at a plan.** If renders are present, write `orders/<job>/compose.py` with `tools/thumbkit.py` (NMS shading, depth fog, ambient/stroke/rim on characters, contact shadow, speed lines, 3D UI slab, split divider, export) and produce the actual draft (`thumbnail-*.png/jpg`).
8. Put the draft and the reference side by side and run the reference checklist again. Pay special attention to what surrounds the characters, which layer is in front of which, and whether UI boxes are flat or 3D. Fix and re-render until it matches, then show the user the draft and the reference.
9. List only the missing information that blocks the work (skins, scene, text, size), as short questions.
Reply in the user's language with a short summary and the path of `brief.md`.
