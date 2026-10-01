#!/usr/bin/env python3
"""Taslağı referansla ölçerek karşılaştır (ÜŞENGEÇLİK YOK kuralının aracı).

Çıktılar: tam boy alt alta görüntü, büyütülmüş kesit çiftleri, piksel profilleri ve bölge renk farkları.
Koordinatlar karşılaştırma ölçeğinde (varsayılan 1280x720, referansın boyutu).

  python3 tools/compare.py ref.webp taslak.png -o /tmp/kars \
      --crop 1100,200,1180,300=1110,250,1190,350 \
      --profile 255,1160,1178=300,1150,1168 \
      --color 1180,255=1175,300
"""
import argparse
from pathlib import Path
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('ref'); ap.add_argument('draft'); ap.add_argument('-o', '--out', required=True)
ap.add_argument('--size', default=None, help='GxY; varsayılan referans boyutu')
ap.add_argument('--crop', action='append', default=[], help='rx0,ry0,rx1,ry1=dx0,dy0,dx1,dy1')
ap.add_argument('--profile', action='append', default=[], help='ry,rx0,rx1=dy,dx0,dx1 (yatay piksel satırı)')
ap.add_argument('--color', action='append', default=[], help='rx,ry=dx,dy (tek nokta, 5x5 ortalama)')
ap.add_argument('--zoom', type=int, default=5)
a = ap.parse_args()

ref = Image.open(a.ref).convert('RGB')
size = tuple(map(int, a.size.split('x'))) if a.size else ref.size
ref = ref.resize(size, Image.LANCZOS); draft = Image.open(a.draft).convert('RGB').resize(size, Image.LANCZOS)
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
R, D = np.asarray(ref).astype(int), np.asarray(draft).astype(int)
nums = lambda s: [int(v) for v in s.split(',')]

full = Image.new('RGB', (size[0], size[1] * 2 + 10), (255, 0, 255)); full.paste(ref, (0, 0)); full.paste(draft, (0, size[1] + 10))
full.save(out / 'tam.png'); print(f"tam boy (üst referans, alt taslak): {out / 'tam.png'}")

if a.crop:
    tiles = []
    for c in a.crop:
        r, d = (nums(x) for x in c.split('='))
        for im, b in ((ref, r), (draft, d)):
            t = im.crop(b); tiles.append(t.resize((t.width * a.zoom, t.height * a.zoom), Image.NEAREST))
    W = sum(t.width for t in tiles) + 12 * len(tiles); c = Image.new('RGB', (W, max(t.height for t in tiles)), (255, 0, 255)); x = 0
    for t in tiles: c.paste(t, (x, 0)); x += t.width + 12
    c.save(out / 'kesitler.png'); print(f"kesitler (her çift: referans, taslak; {a.zoom}x): {out / 'kesitler.png'}")

for p in a.profile:
    (ry, rx0, rx1), (dy, dx0, dx1) = (nums(x) for x in p.split('='))
    print(f"\nprofil REF  y={ry}: " + ' '.join(str(tuple(int(v) for v in R[ry, x])) for x in range(rx0, rx1)))
    print(f"profil TAS  y={dy}: " + ' '.join(str(tuple(int(v) for v in D[dy, x])) for x in range(dx0, dx1)))

for c in a.color:
    (rx, ry), (dx, dy) = (nums(x) for x in c.split('='))
    rc = R[ry - 2:ry + 3, rx - 2:rx + 3].reshape(-1, 3).mean(0); dc = D[dy - 2:dy + 3, dx - 2:dx + 3].reshape(-1, 3).mean(0)
    print(f"renk ref {tuple(int(v) for v in rc.round())}  taslak {tuple(int(v) for v in dc.round())}  fark {tuple(int(v) for v in (dc - rc).round())}")

lum = lambda X: (X @ [0.299, 0.587, 0.114]) / 2.55
print(f"\nort. parlaklık ref %{lum(R.reshape(-1, 3)).mean():.0f}  taslak %{lum(D.reshape(-1, 3)).mean():.0f}")
