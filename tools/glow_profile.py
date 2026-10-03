#!/usr/bin/env python3
"""Parlama (glow/bloom) halesini ölç: renkli öğenin (trim, büyü, lav) çevresinde, uzaklığa göre renk taşması.

Referansta ve taslakta ayrı ayrı çalıştır, oranları karşılaştır. Görsel 1280x720'ye ölçeklenir.
Çekirdek = bölgede skoru en yüksek %5'in --core katından yüksek pikseller (iki görselde aynı tanım; mutlak eşik
taslaktaki parlak haleyi de çekirdek sayıp sonucu bozar). Oran = (halka skoru − zemin) / (çekirdek − zemin);
zemin = 12 px uzaktaki halka.

  python3 tools/glow_profile.py ref.jpg --color g --region 570,200,1250,520
  python3 tools/glow_profile.py taslak.png --color r --region 570,200,1250,520
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter

ap = argparse.ArgumentParser()
ap.add_argument('img'); ap.add_argument('--color', choices='rgb', required=True, help='parlayan öğenin baskın kanalı')
ap.add_argument('--region', default='0,0,1280,720'); ap.add_argument('--core', type=float, default=0.75)
a = ap.parse_args()
r = np.asarray(Image.open(a.img).convert('RGB').resize((1280, 720), Image.LANCZOS)).astype(float)
c = 'rgb'.index(a.color); o = [i for i in range(3) if i != c]
score = r[..., c] - r[..., o].mean(-1)
x0, y0, x1, y1 = map(int, a.region.split(',')); reg = np.zeros(score.shape, bool); reg[y0:y1, x0:x1] = True
m = reg & (score > a.core * np.percentile(score[reg], 95))
cur, prev, rings = Image.fromarray((m * 255).astype(np.uint8)), m, {}
for d in range(1, 13):
    cur = cur.filter(ImageFilter.MaxFilter(3)); dil = np.asarray(cur) > 0; rings[d] = score[dil & ~prev & reg].mean(); prev = dil
core, base = score[m].mean(), rings[12]
print(f'öğe piksel {m.sum()}  çekirdek renk {tuple(int(v) for v in r[m].mean(0))}  çekirdek L {(r[m] @ [0.299, 0.587, 0.114]).mean():.0f}')
print('uzaklık (px @1280) → hale oranı:', '  '.join(f'{d}: {(rings[d] - base) / (core - base):.2f}' for d in (1, 2, 3, 4, 6, 8, 10)))
