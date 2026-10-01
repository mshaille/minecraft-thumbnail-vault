---
description: Check a finished thumbnail against current YouTube specs and the 15-item checklist
argument-hint: <image path> [order folder or reference note to compare with]
---
Use the `minecraft-thumbnail` skill.

Input: $ARGUMENTS

1. Run `python3 tools/analyze_reference.py <image> -o /tmp/thumbnail-check` (from the vault root) and read the output.
2. Look at the image and its 168x94 and grey previews.
3. Report: spec problems (size, ratio, file size; see `techniques/12-export.md`), then the 15-item checklist from `references/README.md` as a table, then the three most valuable fixes with links to technique notes.
4. If an order folder is given, also check every item in its `brief.md` and compare with its `refs/` images side by side (palette, brightness, saturation, 168x94). If a reference note is given, compare with it.
Do not save anything into the vault unless the user asks. Reply in the user's language.
