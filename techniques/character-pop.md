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

## Notlar
- Size 0 olan beyaz Inner Shadow sert bir kenar ışığı verir. Açısını sahnedeki ışık yönüne çevir ([uyarlama](adapt-to-reference.md)).
- Karakterin yüzüne ifade eklerken yüzü göz hizasından ağıza kadar oturt. Kafayla birlikte eğ, esnetme. 2D ve 3D öğelerin stili tutarlı olsun (Bakshh GFX tavsiyesi).
- Videolarda karakter etrafında kalın beyaz kontur kullanan güncel bir örnek bulunamadı. Referansta kontur varsa: Layer Style > **Stroke** 4–10 px, beyaz, Outside.

## Preset C — Pqtrick (sadece hale)
- Drop Shadow: Multiply, siyah, %50, Angle 45, **Distance 0**, Spread 0, **Size 200 px**. Glow yerine hale; vanilla/temiz görünüm için yeter.

Kaynaklar: [Nebular](../sources/nebular-sb737-action-thumbnail.md) · [Schxnappi_](../sources/schxnappi-layer-styles-text.md)
