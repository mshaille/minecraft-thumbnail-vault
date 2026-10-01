---
type: teknik
title: Karakteri öne çıkarma (koyu hale + beyaz kenar)
sources: [nebular-sb737-action-thumbnail, schxnappi-layer-styles-text]
tags: [teknik, layer-style, yuksek-enerji, smp]
styles: [smp-action]
status: stabil
---
# Karakteri öne çıkarma (koyu hale + beyaz kenar)

[06 Ortam ışığı](06-layer-style-ambient-light.md) notundaki yumuşak Overlay preset'i karakteri sahneye **oturtur**. Bu preset'ler ise karakteri sahneden **koparır**. Yüksek enerjili SMP/aksiyon tarzında kullanılır. İnce bir kontur yok; karakteri ayıran şey koyu bir hale ile sert beyaz bir iç kenar.

## Preset A — Nebular (daha sade)
| Efekt | Ayar |
|---|---|
| Outer Glow | Normal, **siyah**, %50, Softer, Spread %13, Size **106 px** |
| Inner Shadow | Normal, **beyaz**, %7–20, 90° (Global Light ✓), Distance **9–12 px**, Choke 0, Size **0** |

## Preset B — Schxnappi (daha güçlü)
| Efekt | Ayar |
|---|---|
| Drop Shadow | Multiply, siyah, %100, **Distance 0**, Spread 0, Size **24 px**. Distance 0 olduğu için gölge değil, hale gibi çalışır. |
| Inner Shadow | Normal, **beyaz**, %100, Angle 12°, Distance **6 px**, Size **0** (sert beyaz kenar) |
| Outer Glow | Overlay, beyaz, %100, Softer, Size **250 px** |
| Gradient Overlay | Overlay %52, siyahtan beyaza, Linear, 90°, Scale %150 |
| Inner Glow | Overlay %76, beyaz, Softer, Edge, Size **32 px** |

## Ölçülmüş kenar profili (Levitation split referansı, 2026-10-01)
Referansta karakter kenarı 3 katman. Değerler 1280'lik referanstan ölçüldü, 2000 px'e çevrildi:
| Katman | Sağ panel (açık gökyüzü önünde) | Sol panel (bulanık arka plan önünde) |
|---|---|---|
| Konturun **dışı** | 1–2 px koyu bant, ~%8–10 (konturu açık gökyüzünden ayırır) | belirgin değil |
| **Kontur** | ~3,5–4 px, mavimsi beyaz (~#F5FBFF) | ~2 px, nesnenin rengine çalan açık renk |
| Kenarın **içi** | ışık tarafında (sol-üst) ~3 px sıcak beyaz şerit, gölge tarafında (sağ-alt) ~3 px %10–20 koyulaşma | hafif |
- Kod: `tools/thumbkit.py` → `outline()` (varsayılanlar bu ölçümler). Işık/gölge tarafı kenarın baktığı yönden hesaplanır, NMS'ten değil.
- Ölçüm yöntemi: kenara dik bir piksel satırı boyunca RGB değerlerini oku; uzaktaki arka plan rengiyle karşılaştır. Araç: `tools/compare.py --profile y,x0,x1=y,x0,x1` referans ve taslağın aynı satırını yan yana basar.
- Kontur öncesi karakter ayarı (testte): `nms_shade` 0,30/0,14 → `ambient(glow=0.15, size=10, grad=0.06)` → `grade(sat=1.30, con=1.15)`. Ambient daha güçlü olunca (0,35) karakterler soluk ve yıkanmış göründü.

## Notlar
- Size 0 olan beyaz Inner Shadow sert bir kenar ışığı verir. Açısını sahnedeki ışık yönüne çevir ([uyarlama](adapt-to-reference.md)).
- Karakterin yüzüne ifade eklerken yüzü göz hizasından ağıza kadar oturt. Kafayla birlikte eğ, esnetme. 2D ve 3D öğelerin stili tutarlı olsun (Bakshh GFX tavsiyesi).
- Videolarda karakter etrafında kalın beyaz kontur kullanan güncel bir örnek bulunamadı. Referansta kontur varsa: Layer Style > **Stroke** 4–10 px, beyaz, Outside.

## Preset C — Pqtrick (sadece hale)
- Drop Shadow: Multiply, siyah, %50, Angle 45, **Distance 0**, Spread 0, **Size 200 px**. Glow yerine hale; vanilla/temiz görünüm için yeter.

Kaynaklar: [Nebular](../sources/nebular-sb737-action-thumbnail.md) · [Schxnappi_](../sources/schxnappi-layer-styles-text.md)
