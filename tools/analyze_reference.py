#!/usr/bin/env python3
"""Referans thumbnail analizi -> Obsidian'a yapıştırılabilir Markdown (sadece Pillow).

Vault kökünden çalıştır:
  python3 tools/analyze_reference.py references/images/ref-....png -o references/images/previews
"""
import argparse, os
from math import gcd
from PIL import Image, ImageStat

ap = argparse.ArgumentParser()
ap.add_argument("image")
ap.add_argument("-o", "--out", help="önizlemelerin kaydedileceği klasör (opsiyonel)")
ap.add_argument("-n", "--colors", type=int, default=6)
ap.add_argument("--rel", default="references", help="linklerin göreli olacağı not klasörü")
a = ap.parse_args()

im = Image.open(a.image)
rgb = im.convert("RGB")
w, h = im.size
kb = os.path.getsize(a.image) / 1024
q = rgb.resize((256, 144)).quantize(colors=a.colors)  # küçült = hızlı; alan oranları korunur
pal = q.getpalette()
cols = sorted(q.getcolors(), reverse=True)
total = sum(c for c, _ in cols)
lum = ImageStat.Stat(rgb.convert("L")).mean[0] / 2.55
sat = ImageStat.Stat(rgb.convert("HSV")).mean[1] / 2.55
notes = []
if abs(w / h - 16 / 9) > 0.01: notes.append("16:9 değil")
if w < 640: notes.append("genişlik < 640 px")
if kb > 2048: notes.append("> 2 MB (mobilden yüklenemez; masaüstü limiti 50 MB)")

print(f"## Teknik analiz: `{os.path.basename(a.image)}`\n")
print("| Özellik | Değer |\n|---|---|")
print(f"| Boyut | {w}x{h} px |")
print(f"| Oran | {w // gcd(w, h)}:{h // gcd(w, h)} ({w / h:.3f}; 16:9 = 1.778) |")
print(f"| Dosya | {kb:.0f} KB, {im.format} |")
print(f"| Ort. parlaklık | %{lum:.0f} |")
print(f"| Ort. doygunluk | %{sat:.0f} |")
print(f"| Kontrol | {', '.join(notes) or 'YouTube spec OK'} |")
print("\n### Baskın renkler\n")
for c, i in cols:
    r, gg, b = pal[i * 3:i * 3 + 3]
    print(f"- `#{r:02X}{gg:02X}{b:02X}` %{100 * c / total:.1f}")

if a.out:
    os.makedirs(a.out, exist_ok=True)
    stem = os.path.splitext(os.path.basename(a.image))[0]
    print("\n### Küçük boyut testi\n")
    for tag, size, img in (("120x68", (120, 68), rgb), ("168x94", (168, 94), rgb), ("320x180", (320, 180), rgb),
                           ("320x180_gri", (320, 180), rgb.convert("L"))):
        fn = f"{stem}_{tag}.png"
        img.resize(size, Image.LANCZOS).save(os.path.join(a.out, fn))
        print(f"![{tag}]({os.path.relpath(os.path.join(a.out, fn), a.rel)})")
