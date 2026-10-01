"""thumbkit — vault tekniklerinin kodla uygulanmış hali (Pillow + numpy).

Render'lardan (shader'sız / NMS / DMS geçişleri) taslak thumbnail üretmek için.
Her fonksiyon bir teknik notuna karşılık gelir; değerlerin anlamı o notlarda.

    import sys; sys.path.insert(0, 'tools'); from thumbkit import *
"""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

def load(p): return Image.open(p).convert('RGBA')
def A(im): return np.asarray(im).astype(np.float32) / 255
def I(a): return Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
def hexrgb(h): return np.array([int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]) / 255
def overlay(b, c): return np.where(b < 0.5, 2 * b * c, 1 - 2 * (1 - b) * (1 - c))
def white(size, alpha): return Image.merge('RGBA', [Image.new('L', size, 255)] * 3 + [alpha])

def nms_shade(base, nms, shadow=0.20, light=0.10, valid=None):
    """03 NMS gölgelendirme. Işık yukarıdan + bir yandan. Oyuncu dış katmanı ters normal
    taşıdığı için x bileşeninin mutlak değeri alınır. Döner: (görsel, ışık maskesi)."""
    b, n = A(base), A(nms)[..., :3] * 2 - 1
    d = 0.8 * n[..., 1] + 0.35 * n[..., 2] + 0.2 * np.abs(n[..., 0])
    sh, li = np.clip((0.05 - d) / 0.6, 0, 1), np.clip((d - 0.3) / 0.5, 0, 1)
    if valid is not None: sh, li = sh * valid, li * valid
    rgb = b[..., :3] * (1 - shadow * sh[..., None])
    b[..., :3] = rgb + (1 - rgb) * (light * li)[..., None]
    return I(b), li

def grade(im, sat=1.12, con=1.08, bri=1.0):
    """05 Camera Raw yaklaşığı: doygunluk + kontrast (+ parlaklık), alfa korunur."""
    a = im.getchannel('A'); rgb = im.convert('RGB')
    for f, k in ((ImageEnhance.Color, sat), (ImageEnhance.Contrast, con), (ImageEnhance.Brightness, bri)):
        rgb = f(rgb).enhance(k)
    out = rgb.convert('RGBA'); out.putalpha(a); return out

def remap(im, src_a, dst_a, src_b, dst_b):
    """Referansa renk eşleme: iki ölçülmüş renk çifti (ör. gökyüzü zemini, bulut) ile kanal başına doğrusal eşleme."""
    b = A(im); sa, da, sb, db = (np.array(c) / 255 for c in (src_a, dst_a, src_b, dst_b))
    den = sb - sa; k = np.where(np.abs(den) > 1e-3, (db - da) / np.where(np.abs(den) > 1e-3, den, 1), 1.0)
    b[..., :3] = da + (b[..., :3] - sa) * k
    return I(np.clip(b, 0, 1))

def depth_fog(bg, dms, color, curve=0.69, blur=4, geo_max=0.55, sky_max=0.30):
    """04 depth sis (+ uzak bulanıklık). dms: 0..1 dizi (1 yakın). curve=0.69 ≈ Curves 86→120."""
    fog = np.clip(1 - dms, 0, 1) ** curve
    b = A(bg); bl = A(bg.filter(ImageFilter.GaussianBlur(blur)))
    b = b * (1 - fog[..., None]) + bl * fog[..., None]
    fa = np.where(dms > 0.02, geo_max, sky_max) * fog
    b[..., :3] = b[..., :3] * (1 - fa[..., None]) + color * fa[..., None]
    return I(b)

def ambient(im, color, glow=0.35, size=10, grad=0.19):
    """06 Layer Style: Inner Glow (ortam rengi, Overlay) + Gradient Overlay (Overlay)."""
    b = A(im); a = b[..., 3]
    er = A(im.getchannel('A').filter(ImageFilter.MinFilter(2 * size + 1)))
    band = A(I(a - er).filter(ImageFilter.GaussianBlur(size * 0.8)))
    rgb = b[..., :3]
    rgb = rgb * (1 - glow * band[..., None]) + overlay(rgb, color) * (glow * band[..., None])
    ys = np.linspace(0, 1, im.height)[:, None, None]
    g = color * (1 - ys) + np.array([0.45, 0.47, 0.52]) * ys
    b[..., :3] = rgb * (1 - grad) + overlay(rgb, g) * grad
    return I(b)

def tint(im, color, k):
    """Uzak karakteri ortam rengine çek (sis yerine)."""
    b = A(im); b[..., :3] = b[..., :3] * (1 - k) + color * k; return I(b)

def rim(im, li, width=3, strength=0.85):
    """11 Highlight: karakterin İÇİNDE, ışığa bakan kenarlarda ince beyaz çizgi."""
    b = A(im)
    er = A(im.getchannel('A').filter(ImageFilter.MinFilter(2 * width + 1)))
    edge = np.clip(b[..., 3] - er, 0, 1) * np.clip(li * 1.5, 0, 1)
    b[..., :3] = b[..., :3] + (1 - b[..., :3]) * (strength * edge)[..., None]
    return I(b)

def stroke(im, px, alpha=1.0):
    """Beyaz 'sticker' kontur (Layer Style > Stroke, Outside)."""
    a = im.getchannel('A').filter(ImageFilter.MaxFilter(2 * px + 1)).filter(ImageFilter.GaussianBlur(0.7))
    s = white(im.size, a.point(lambda v: int(v * alpha))); s.alpha_composite(im); return s

def edge_sides(alpha, light=(-0.6, -0.8), sigma=2.0):
    """Kenarın baktığı yöne göre (ekran uzayı) ışık/gölge tarafı. light: ışığın geldiği yön (x sağ+, y aşağı+).
    NMS'e bağlı değil; oyuncu dış katmanındaki ters normaller kenarı bozmaz."""
    a = A(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(sigma)))
    gy, gx = np.gradient(a); n = np.hypot(gx, gy) + 1e-6
    dot = (-gx / n) * light[0] + (-gy / n) * light[1]          # dışa bakan normal · ışık
    return np.clip(dot, 0, 1), np.clip(-dot, 0, 1)

def outline(im, stroke_px=3, stroke_rgb=(245, 251, 255), tint=0.0, outer_px=2, outer_alpha=0.10,
            outer_rgb=(25, 35, 70), inner_px=3, inner_light=0.80, inner_dark=0.18, light=(-0.6, -0.8)):
    """Referanstan ölçülen kenar işlemi (3 katman, dıştan içe):
    1) konturun DIŞINDA ince koyu bant (açık gökyüzünde konturu tanımlar),
    2) mavimsi beyaz kontur (tint>0: nesnenin kenar rengine doğru karıştır),
    3) kenarın İÇİNDE: ışık tarafında sıcak beyaz şerit, gölge tarafında koyulaşma."""
    b = A(im); a = b[..., 3]
    er = A(im.getchannel('A').filter(ImageFilter.MinFilter(2 * inner_px + 1)))
    band = A(I(np.clip(a - er, 0, 1)).filter(ImageFilter.GaussianBlur(0.8))) * a
    lit, shade = edge_sides(a, light)
    lit, shade = A(I(lit).filter(ImageFilter.GaussianBlur(1.5))), A(I(shade).filter(ImageFilter.GaussianBlur(1.5)))
    rgb = b[..., :3] * (1 - inner_dark * (band * shade)[..., None])
    warm = np.array([1.0, 0.95, 0.90])
    rgb = rgb + (warm - rgb) * (inner_light * band * lit)[..., None]
    b[..., :3] = np.clip(rgb, 0, 1); body = I(b)
    sc = np.array(stroke_rgb) / 255
    if tint:                                                       # kenar rengini konturun içine taşı
        edge_col = (b[..., :3] * band[..., None]).sum((0, 1)) / max(band.sum(), 1)
        sc = sc * (1 - tint) + edge_col * tint
    sa = im.getchannel('A').filter(ImageFilter.MaxFilter(2 * stroke_px + 1)).filter(ImageFilter.GaussianBlur(0.6))
    out = Image.new('RGBA', im.size)
    if outer_alpha:
        oa = im.getchannel('A').filter(ImageFilter.MaxFilter(2 * (stroke_px + outer_px) + 1)).filter(ImageFilter.GaussianBlur(1.0))
        o = Image.new('RGBA', im.size, tuple(outer_rgb) + (0,)); o.putalpha(oa.point(lambda v: int(v * outer_alpha))); out.alpha_composite(o)
    s = Image.new('RGBA', im.size, tuple(int(v * 255) for v in sc) + (0,)); s.putalpha(sa); out.alpha_composite(s)
    out.alpha_composite(body); return out

def ring(mask, px=4):
    """Bir maskenin (ör. kaktüs) dış çevresi — arka plandaki nesneye kontur için."""
    m = np.asarray(mask.filter(ImageFilter.MaxFilter(2 * px + 1))).astype(int) - np.asarray(mask)
    return Image.fromarray(np.clip(m, 0, 255).astype(np.uint8))

def place(canvas, im, s, dx, dy, cx=None, cy=None):
    """Katmanı (cx,cy) etrafında s ölçekle, (dx,dy) kaydırıp tuvale bindir."""
    cx = canvas.width / 2 if cx is None else cx; cy = canvas.height / 2 if cy is None else cy
    im2 = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    tmp = Image.new('RGBA', canvas.size); tmp.paste(im2, (round(cx - cx * s + dx), round(cy - cy * s + dy)))
    canvas.alpha_composite(tmp)

def place_fit(canvas, im, center, height):
    """Katmanı, referanstan ölçülen hedef merkeze ve yüksekliğe oturt (karakter bazlı yerleşim)."""
    bb = im.getchannel('A').getbbox(); c = im.crop(bb); s = height / c.height
    c = c.resize((max(1, round(c.width * s)), max(1, round(c.height * s))), Image.LANCZOS)
    tmp = Image.new('RGBA', canvas.size); tmp.paste(c, (round(center[0] - c.width / 2), round(center[1] - c.height / 2)))
    canvas.alpha_composite(tmp); return (round(center[0] - c.width / 2), round(center[1] - c.height / 2), round(center[0] + c.width / 2), round(center[1] + c.height / 2))

def contact_shadow(size, box, opacity=0.5, blur=14):
    """07 Temas gölgesi: ayakların altına yumuşak siyah elips. box=(x0,y0,x1,y1)."""
    m = Image.new('L', size, 0); ImageDraw.Draw(m).ellipse(box, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opacity))
    return Image.merge('RGBA', [Image.new('L', size, 0)] * 3 + [m])

def speed_lines(size, focus, lines, k=0.038, alpha=0.78, fade=250):
    """Odak çizgileri (anime 'focus lines'): kadraj kenarından başlayıp ODAĞA doğru sivrilen ince beyaz üçgenler.
    Odağın çevresi boş kalır; katman karakterlerin ve UI'nin ARKASINA konur (çizgi karakterin kenarından çıkar).
    lines: [(açı°, r0), ...]  açı: odaktan dışa (0 = sağ, 90 = aşağı), r0: sivri ucun odağa uzaklığı (px).
    k: genişlik artışı (px/px, ölçülen 0.035–0.045). alpha: dış uçta beyaz opaklık (ölçülen 0.6–0.8),
    sivri uca doğru `fade` px boyunca azalır. Rastgele: [(rnd.uniform(0, 360), rnd.uniform(300, 600)) for _ in range(16)]."""
    W, H = size; fx, fy = focus; R = math.hypot(W, H) * 1.2
    yy, xx = np.mgrid[0:H, 0:W]; rad = np.hypot(xx - fx, yy - fy); out = np.zeros((H, W), np.float32)
    for ang, r0 in lines:
        ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang)); hw = k * (R - r0) / 2
        m = Image.new('L', size, 0)
        ImageDraw.Draw(m).polygon([(fx + ux * r0, fy + uy * r0), (fx + ux * R - uy * hw, fy + uy * R + ux * hw),
                                   (fx + ux * R + uy * hw, fy + uy * R - ux * hw)], fill=255)
        ramp = np.clip((rad - r0) / fade, 0, 1) ** 0.5
        out = np.maximum(out, A(m) * ramp)
    return white(size, I(out * alpha).filter(ImageFilter.GaussianBlur(1.0)))

def radial_glow(size, ellipse, strength=105, blur=180):
    """Gökyüzünde beyaz radyal parlama (Screen benzeri)."""
    m = Image.new('L', size, 0); ImageDraw.Draw(m).ellipse(ellipse, fill=strength)
    return white(size, m.filter(ImageFilter.GaussianBlur(blur)))

def slab_3d(flat, depth=16, outline=4, tilt=2.5, persp=(14, 8, 6)):
    """Düz UI kutusunu 3D levhaya çevir: sol-alta kalınlık, beyaz dış kontur, hafif perspektif + eğim."""
    pad = 40; s = Image.new('RGBA', (flat.width + 2 * pad, flat.height + 2 * pad))
    dark = Image.new('RGBA', flat.size, (14, 14, 14, 255)); dark.putalpha(flat.getchannel('A'))
    for k in range(1, depth + 1):
        s.alpha_composite(dark, (pad - k // 2, pad + k))
    s.alpha_composite(flat, (pad, pad)); s = stroke(s, outline)
    w, h = s.size; tl, br, bl = persp
    src = [(0, 0), (w, 0), (w, h), (0, h)]; dst = [(0, tl), (w, 0), (w, h - br), (0, h + bl)]
    M = []
    for (x, y), (u, v) in zip(dst, src):
        M += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
    c = np.linalg.solve(np.array(M, float), np.array([q for p in src for q in p], float))
    return s.transform((w, h + bl + 4), Image.PERSPECTIVE, tuple(c), Image.BICUBIC).rotate(tilt, expand=True, resample=Image.BICUBIC)

def drop_shadow(im, opacity=0.35, blur=10):
    s = Image.new('RGBA', im.size); s.putalpha(im.getchannel('A').filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opacity)))
    return s

def split(left, right, top_x, bottom_x, line=10, glow=46, glow_alpha=0.55):
    """Çapraz split: sol paneli maskeyle sağın üstüne koy, beyaz ayırıcı + yumuşak parlama."""
    W, H = right.size
    mask = Image.new('L', (W, H), 0); ImageDraw.Draw(mask).polygon([(0, 0), (top_x, 0), (bottom_x, H), (0, H)], fill=255)
    out = right.copy(); out.paste(left, (0, 0), mask)
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).line((top_x, 0, bottom_x, H), fill=255, width=glow)
    out.alpha_composite(white((W, H), g.filter(ImageFilter.GaussianBlur(glow * 0.43)).point(lambda v: int(v * glow_alpha))))
    ImageDraw.Draw(out).line((top_x, 0, bottom_x, H), fill=(255, 255, 255, 255), width=line)
    return out

def export(img, stem):
    """12 Export: tam boyut PNG + 1920x1080 PNG + JPG (mobil yükleme için 2 MB altı)."""
    rgb = img.convert('RGB'); rgb.save(f'{stem}-{img.width}x{img.height}.png')
    small = rgb.resize((1920, 1080), Image.LANCZOS); small.save(f'{stem}-1920x1080.png'); small.save(f'{stem}-1920x1080.jpg', quality=92)
