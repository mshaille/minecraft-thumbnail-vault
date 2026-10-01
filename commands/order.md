---
description: Take a thumbnail order (requests + optional reference images) and build a plan with settings adapted to the references
argument-hint: <what is wanted> [reference image paths...]
---
**Rule: no laziness — aim for perfection.** Measure every element of the reference at ≥5× zoom with pixel profiles (stroke width/colour, inside/outside of edges, glow, shadow, colours, positions and sizes). Check every layer of an effect, not just the obvious one. Never stop at a plan; render the real draft, compare it side by side with the reference at full size and zoomed, re-measure, fix and re-render until it matches. Report every remaining difference honestly.

Use the `minecraft-thumbnail` skill, workflow **C (order)**. The full pipeline, the user's working preferences and known pitfalls are in `guides/order-workflow.md`.

**User preferences:** do not start designing before the reference arrives; renders usually come first (right panel, then left panel, then the reference), possibly as unnamed numbered files with duplicates. Leave out anything the user excludes (e.g. "no arrow for now"). In-game UI text must use the official translation and the game's own font (`tools/mc_effect_box.py`), never an invented one. Talk to the user in Turkish.

Order: $ARGUMENTS

1. Create `orders/YYYY-MM-DD-short-name/` with `brief.md` from `templates/order.md`, a `renders/` folder (`renders/left/`, `renders/right/` for split jobs) and a `refs/` folder. This folder is git-ignored, so client data never reaches the public repo. Fill "İstenenler" from the request.
1b. **Renders before the reference:** run `python3 tools/catalog_renders.py orders/<job>/renders/<panel>` and put its table into "Render'lar" (passes per character, bbox, nearness, duplicates). Rename the files meaningfully. Only catalogue; wait for the reference before any layout or effect decision.
2. **Pick the style** with `styles/README.md` (§1: brief keywords → style, then the reference decision tree). Choose one main style (S1–S11) and at most one secondary style, write them into `brief.md` with the reason. If the brief and references point to different styles, or nothing points anywhere, ask the user.
3. Copy any reference images into `refs/`, run (from the vault root) `python3 tools/analyze_reference.py orders/<job>/refs/<img> -o orders/<job>/refs/previews --rel orders/<job>` for each, and look at the images and previews.
4. Open the style card in `styles/`. It says which technique steps stay at default, change or are switched off, and which extra techniques (`techniques/style-catalog.md`, `character-pop.md`, `text-typography.md`, `action-effects.md`) are needed. Then, using `techniques/adapt-to-reference.md`, fill "Referanstan uyarlanan ayarlar": for every step whose value should change, give the video value, the style-card value, the value for this job, and the reason. With no references, start from `references/lessons.md` and the video defaults.
5. Check `guides/pitfalls.md` (policy, Mojang rules, licences) and `guides/common-mistakes.md` against the plan.
6. Write the bottom-to-top layer plan with exact settings and links to the technique notes.
7. **Do not stop at a plan.** If renders are present, write `orders/<job>/compose.py` with `tools/thumbkit.py` (NMS shading, depth fog, ambient/stroke/rim on characters, contact shadow, speed lines, 3D UI slab, split divider, export) and produce the actual draft (`thumbnail-*.png/jpg`).
8. Measure the draft against the reference: `python3 tools/compare.py orders/<job>/refs/<ref> orders/<job>/thumbnail-*.png -o /tmp/compare --crop … --profile … --color …` (side by side, zoomed crops, edge profiles, colour differences). Run the reference checklist again. Pay special attention to what surrounds the characters (all three edge layers), which layer is in front of which, whether UI boxes are flat or 3D, and the weight of speed lines. Fix and re-render until it matches, write the final values into `brief.md`, then show the user the draft and the reference side by side with every remaining difference and its reason.
9. List only the missing information that blocks the work (skins, scene, text, size), as short questions.
Reply in the user's language with a short summary and the path of `brief.md`.
