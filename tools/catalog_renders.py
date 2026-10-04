#!/usr/bin/env python3
"""Render geçişlerini tanı ve eşleştir (Markdown tablo).

- Birebir kopyaları atar (piksel hash).
- Geçiş türü: önce dosya adı (nms/dms/no-shader); yoksa DMS = gri tonlu; kalan iki renkli geçişten
  'birim normal oranı − doku' skoru yüksek olan NMS (tek başına eşik güvenilmez: ör. balkabağı skini birim normal gibi görünür).
- Aynı karakterin geçişleri aynı şeffaflık sınırını (bbox) paylaşır; şeffaflığı olmayanlar arka plandır.
- Karakter DMS'inin ortalama grisi yakınlığı verir (beyaz = yakın).
- Bütün karakter geçişlerinde ortak opak pikseller = uygulamanın ayıramadığı nesne (ör. kupa): uyarılır, bbox'lardan çıkarılır.

  python3 tools/catalog_renders.py <klasör veya dosyalar...>
"""
import hashlib, sys
from pathlib import Path
import numpy as np
from PIL import Image

files = [p for a in sys.argv[1:] for p in (sorted(Path(a).iterdir()) if Path(a).is_dir() else [Path(a)])
         if p.suffix.lower() in {'.png', '.webp', '.jpg', '.jpeg'}]
def name_hint(n):
    n = n.lower().replace('_', '-')
    return 'dms' if 'dms' in n else 'nms' if 'nms' in n else 'shadersiz' if ('no-shader' in n or 'noshader' in n) else None

common = None                                                    # şeffaf geçişlerin ortak opak pikselleri
for f in files:
    al = np.asarray(Image.open(f).convert('RGBA'))[..., 3] > 0
    if not al.all(): common = al if common is None else (common & al)
if common is not None and common.mean() > 0.002:
    ys, xs = np.nonzero(common)
    print(f"> Bütün karakter geçişlerinde ortak {common.sum()} px, bbox ({xs.min()}, {ys.min()}, {xs.max()}, {ys.max()}): "
          "uygulamanın ayıramadığı bir nesne (ör. kupa). Kendin ayır: ortak alfa kesişimi = nesne maskesi; karakterlerden çıkar.\n")
else:
    common = None

seen, groups = {}, {}
for f in files:
    im = Image.open(f); rgba = im.convert('RGBA'); h = hashlib.md5(rgba.tobytes()).hexdigest()
    if h in seen:
        print(f"- kopya: `{f.name}` = `{seen[h]}` (atlandı)"); continue
    seen[h] = f.name
    a = np.asarray(rgba).astype(np.float32); alpha = a[..., 3] > 0
    has_alpha = not alpha.all()
    px = a[..., :3][alpha] if has_alpha else a[..., :3].reshape(-1, 3)
    px = px[~(px.min(1) > 245)]                                  # saf beyaz (NMS gökyüzü) dışı
    gray = len(px) == 0 or (np.abs(px[:, 0] - px[:, 1]).mean() < 2 and np.abs(px[:, 1] - px[:, 2]).mean() < 2)
    unit = (np.abs(np.linalg.norm(px / 127.5 - 1, axis=1) - 1) < 0.15).mean() if len(px) else 0
    dx = np.abs(np.diff(a[..., :3], axis=1)).sum(-1); m = alpha[:, 1:] & alpha[:, :-1]
    tex = (dx[m] > 6).mean() if m.any() else 0
    key = (Image.fromarray(((alpha & ~common) if common is not None else alpha).astype(np.uint8) * 255).getbbox()
           if has_alpha else 'arka-plan')
    near = round(float(a[..., 0][alpha].mean())) if (gray and has_alpha) else None
    groups.setdefault(key, []).append(dict(name=f.name, hint=name_hint(f.name), gray=gray, score=unit - tex, near=near))

# sınıflandır: önce dosya adı; yoksa gri = DMS; kalan iki renkli geçişten skoru yüksek (birim normal − doku) NMS
for key, items in groups.items():
    out = {}
    for it in items:
        if it['hint']: out[it['hint']] = (it['name'], it['near'])
    rest = [it for it in items if not it['hint']]
    for it in [it for it in rest if it['gray'] and 'dms' not in out]:
        out['dms'] = (it['name'], it['near']); rest.remove(it)
    rest.sort(key=lambda it: -it['score'])
    if len(rest) >= 2 and 'nms' not in out: out['nms'] = (rest.pop(0)['name'], None)
    elif len(rest) == 1 and 'nms' not in out and 'shadersiz' in out: out['nms'] = (rest.pop(0)['name'], None)
    if rest and 'shadersiz' not in out:
        it = rest.pop(0); out['nms' if it['score'] > 0.45 and 'nms' not in out else 'shadersiz'] = (it['name'], None)
    groups[key] = out

print("\n| Katman | Konum (bbox) | Shader'sız | DMS (yakınlık 0–255) | NMS |\n|---|---|---|---|---|")
order = sorted(groups, key=lambda k: (k != 'arka-plan', -(groups[k].get('dms', ('', 0))[1] or 0)))
for i, k in enumerate(order):
    g = groups[k]; name = 'Arka plan' if k == 'arka-plan' else f'K{i}'
    dms = g.get('dms', ('–', None)); dtxt = dms[0] + (f' ({dms[1]})' if dms[1] is not None else '')
    print(f"| {name} | {k if k != 'arka-plan' else 'tam kare'} | `{g.get('shadersiz', ('–',))[0]}` | `{dtxt}` | `{g.get('nms', ('–',))[0]}` |")
bg = groups.get('arka-plan', {})
if 'dms' in bg:
    d = np.asarray(Image.open(next(f for f in files if f.name == bg['dms'][0])).convert('L'))
    if d.max() < 5: print("\n> Arka plan DMS'i tamamen siyah (sadece gökyüzü): depth sis arka plana uygulanamaz.")
