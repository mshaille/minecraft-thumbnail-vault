---
description: Check a finished thumbnail against current YouTube specs and the 15-item checklist
argument-hint: <image path> [order folder or reference note to compare with]
---
**Rule: no laziness — aim for perfection.** Measure every element of the reference at ≥5× zoom with pixel profiles (stroke width/colour, inside/outside of edges, glow, shadow, colours, positions and sizes). Check every layer of an effect, not just the obvious one. Never stop at a plan; render the real draft, compare it side by side with the reference at full size and zoomed, re-measure, fix and re-render until it matches. Report every remaining difference honestly.

Use the `minecraft-thumbnail` skill.

Input: $ARGUMENTS

1. Run `python3 tools/analyze_reference.py <image> -o /tmp/thumbnail-check` (from the vault root) and read the output.
2. Look at the image and its 168x94 and grey previews.
3. Report: spec problems (size, ratio, file size; see `techniques/12-export.md`), then the 15-item checklist from `references/README.md` as a table, then the three most valuable fixes with links to technique notes.
4. If an order folder is given, also check every item in its `brief.md` and compare with its `refs/` images: run `python3 tools/compare.py <ref> <image> -o /tmp/thumbnail-check/compare` with `--crop`, `--profile` and `--color` on the key spots (character edges, sky, ground, UI box), then look at `tam.png` and `kesitler.png`. Report palette, brightness, saturation, 168x94 and the measured differences. If a reference note is given, compare with it.
Do not save anything into the vault unless the user asks. Reply in the user's language.
