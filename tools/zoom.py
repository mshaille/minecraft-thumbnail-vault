#!/usr/bin/env python3
"""Izgaralı büyütülmüş kesit: referansta konum/ölçü okumak için (ÜŞENGEÇLİK YOK kuralının aracı).

Çizgiler 20 px'te bir (100'lerde koyu), etiketler görüntünün kendi koordinatlarında.

  python3 tools/zoom.py ref.jpg 540 180 1000 560 -z 3 -o /tmp/kesit.png
"""
import argparse
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

ap = argparse.ArgumentParser()
ap.add_argument('img'); ap.add_argument('box', nargs=4, type=int, metavar=('x0', 'y0', 'x1', 'y1'))
ap.add_argument('-z', '--zoom', type=int, default=3); ap.add_argument('--step', type=int, default=20)
ap.add_argument('--contrast', type=float, default=1.0); ap.add_argument('-o', '--out', required=True)
a = ap.parse_args()
x0, y0, x1, y1 = a.box; z = a.zoom
im = ImageEnhance.Contrast(Image.open(a.img).convert('RGB').crop(a.box)).enhance(a.contrast)
im = im.resize(((x1 - x0) * z, (y1 - y0) * z), Image.NEAREST); d = ImageDraw.Draw(im); f = ImageFont.load_default(14)
for v in range((x0 // a.step + 1) * a.step, x1, a.step):
    X = (v - x0) * z; d.line([(X, 0), (X, im.height)], fill=(255, 0, 0) if v % 100 == 0 else (255, 130, 130))
    d.text((X + 2, 2), str(v), fill=(255, 255, 0), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
for v in range((y0 // a.step + 1) * a.step, y1, a.step):
    Y = (v - y0) * z; d.line([(0, Y), (im.width, Y)], fill=(255, 0, 0) if v % 100 == 0 else (255, 130, 130))
    d.text((2, Y + 2), str(v), fill=(255, 255, 0), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
im.save(a.out); print(a.out, im.size)
