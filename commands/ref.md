---
description: Add an image to the reference library and analyze it (palette, checklist, small-size test)
argument-hint: <image path or URL> [why you like it]
---
**Rule: no laziness — aim for perfection.** Measure every element of the reference at ≥5× zoom with pixel profiles (stroke width/colour, inside/outside of edges, glow, shadow, colours, positions and sizes). Check every layer of an effect, not just the obvious one. Never stop at a plan; render the real draft, compare it side by side with the reference at full size and zoomed, re-measure, fix and re-render until it matches. Report every remaining difference honestly.

Use the `minecraft-thumbnail` skill, workflow **B (add a reference image)**.

Input: $ARGUMENTS

- Save the image under `references/images/` with an ASCII `ref-YYYY-MM-DD-short-name` file name.
- Run `tools/analyze_reference.py` on it, look at the original and the small/grey previews, then create the note from `templates/reference.md` and fill the 15-item checklist with concrete observations.
- Link observed techniques to `techniques/` notes and update `references/lessons.md`.
- If the image belongs to someone else, ask before committing it to a public repo.
- Reply in the user's language.
