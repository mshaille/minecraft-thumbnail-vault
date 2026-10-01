#!/usr/bin/env python3
"""Minecraft envanter efekt kutusu (ör. "Yükselme X / 00:21") -> şeffaf PNG.

Font, kutu ve ikon oyunun KENDİ dosyalarından (kurulu client .jar) okunur; repoda
Mojang dosyası tutulmaz. Efektin resmi adı için oyunun dil dosyasına bak
(ör. tr_tr.json -> "effect.minecraft.levitation" = "Yükselme").

  python3 tools/mc_effect_box.py --jar <client.jar> --name "Yükselme X" --time 00:21 \
      --icon levitation --scale 8 -o kutu.png
"""
import argparse, io, json, zipfile
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("--jar", required=True)
ap.add_argument("--name", required=True)
ap.add_argument("--time", default="")
ap.add_argument("--icon", default="levitation", help="textures/mob_effect/<icon>.png")
ap.add_argument("--scale", type=int, default=8)
ap.add_argument("-o", "--out", required=True)
a = ap.parse_args()

z = zipfile.ZipFile(a.jar)
img = lambda p: Image.open(io.BytesIO(z.read("assets/minecraft/textures/" + p))).convert("RGBA")

# --- font: bitmap provider'ları -> karakter başına (glif, ascent, ilerleme) ---
def providers(font_id):  # font/default.json "reference" ile include/*.json'a yönlendirir
    for p in json.loads(z.read(f"assets/minecraft/font/{font_id}.json"))["providers"]:
        if p.get("type") == "reference":
            yield from providers(p["id"].split(":")[1])
        else:
            yield p

glyphs = {}
for p in providers("default"):
    if p.get("type") != "bitmap" or p.get("filter", {}).get("uniform"):
        continue
    sheet = img(p["file"].split(":")[1]); rows = p["chars"]
    cw, ch = sheet.width // len(rows[0]), sheet.height // len(rows)
    k = p.get("height", 8) / ch
    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            if char in glyphs or char == "\u0000":
                continue
            g = sheet.crop((c * cw, r * ch, c * cw + cw, r * ch + ch))
            cols = [x for x in range(cw) if any(g.getpixel((x, y))[3] for y in range(ch))]
            w = (max(cols) + 1) if cols else 0
            if k != 1:
                g = g.resize((max(1, round(cw * k)), max(1, round(ch * k))), Image.NEAREST)
            glyphs[char] = (g, p["ascent"], int(0.5 + w * k) + 1)

def text_width(s):
    return sum(4 if ch == " " else glyphs[ch][2] for ch in s)

def draw_text(canvas, s, x, y, rgb):
    shadow = tuple(int(v * 0.25) for v in rgb)  # oyundaki yazı gölgesi: renk/4, +1,+1
    for color, off in ((shadow, 1), (rgb, 0)):
        cx = x
        for ch in s:
            if ch == " ":
                cx += 4; continue
            g, ascent, adv = glyphs[ch]
            mask = g.getchannel("A")
            canvas.paste(Image.new("RGBA", g.size, color + (255,)), (cx + off, y + off + 7 - ascent), mask)
            cx += adv

# --- kutu: effect_background (nine-slice, kenar 4), ikon 18x18, yazı x=28 ---
W = max(120, 28 + max(text_width(a.name), text_width(a.time)) + 7)
H = 32
bg = img("gui/sprites/container/inventory/effect_background.png"); b = 4
box = Image.new("RGBA", (W, H))
for (sx0, sx1, dx0, dx1) in ((0, b, 0, b), (b, 32 - b, b, W - b), (32 - b, 32, W - b, W)):
    for (sy0, sy1, dy0, dy1) in ((0, b, 0, b), (b, 32 - b, b, H - b), (32 - b, 32, H - b, H)):
        box.paste(bg.crop((sx0, sy0, sx1, sy1)).resize((dx1 - dx0, dy1 - dy0), Image.NEAREST), (dx0, dy0))
box.alpha_composite(img(f"mob_effect/{a.icon}.png"), (7, 7))
draw_text(box, a.name, 28, 6, (255, 255, 255))
if a.time:
    draw_text(box, a.time, 28, 16, (127, 127, 127))
box.resize((W * a.scale, H * a.scale), Image.NEAREST).save(a.out)
print(f"{a.out}: {W * a.scale}x{H * a.scale} (taban {W}x{H}, ölçek {a.scale})")
