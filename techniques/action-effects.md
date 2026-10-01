---
type: teknik
title: Aksiyon efektleri (blur, hız çizgileri, gölge, parıltı)
sources: [nebular-sb737-action-thumbnail, schxnappi-layer-styles-text]
tags: [teknik, efekt, yuksek-enerji]
styles: [smp-action]
status: stabil
---
# Aksiyon efektleri

| Efekt | Nasıl | Ayar |
|---|---|---|
| **Arka plan blur** | Arka plan katmanına Filter > Blur > Gaussian Blur | Radius **4.0 px** (Nebular) |
| **Temiz arka plan** | Replay Mod'da aynı çekimi karakterli ve karaktersiz al (B tuşu) | FOV 30–50 (örnekte 34) |
| **Zemin gölgesi** | Zemin ile karakterler arasına siyah elips. Zıplayan karakterde uzat ve yumuşat. | – |
| **Hız çizgileri** | Anime "zoom lines" asset'i, rasterize et. Ortayı yumuşak silgiyle sil. | Eraser Hardness 0, ~618 px |
| **Büyü parıltısı** | Sadece zırhın kopyası olan katmana Layer Style > **Satin** | Linear Dodge (Add), magenta ~#c923f1, %57, −136°, Distance 49 px, Size 98 px, Contour Linear, Invert ✓; sonra katman opaklığını düşür |
| **Tek rengi ayırma** | Selective Color (Absolute) | Blues: Cyan −45, Magenta −14, Yellow −38, Black −50 |
| **Işık noktaları** | Beyaz yumuşak fırça noktaları | Blend Overlay |
| **3D arayüz (GUI)** | Texture pack arayüzünü Nearest Neighbor ile yapıştır, Ctrl+T ile perspektif ver. Tekrarlayan kopyalar için Ctrl+T ile bir adım kaydır, sonra Ctrl+Shift+Alt+T'yi tekrarla. | – |

## Sıra önemli
Zırh kopyasında önce Vibrance/Saturation/Exposure (ör. Vibrance 0, Saturation +30, Exposure +0.40), **sonra** Satin ve Selective Color uygula. Sıra tersine olunca Nebular işi baştan yapmak zorunda kaldı. Karakterin kendisinde: Vibrance +38, Saturation +50.

> [!note] Photopea'da Satin, Selective Color ve Path Blur desteği [Photopea notunda](photopea-compatibility.md) henüz doğrulanmadı.

## Ayrıştırma ve vurgu (Pqtrick)
| Efekt | Nasıl | Ayar |
|---|---|---|
| **Ayrıştırma gölgesi** | Elliptical Marquee → Paint Bucket siyah → Gaussian Blur | Blur **50 px**; katman arka planın üstünde, karakter ve başlığın altında |
| **Eşya glow'u** (ör. TNT) | Layer Style > Outer Glow | Screen, %100, kırmızı, Softer, Size **200 px**, Range **%50** |

Kaynaklar: [Nebular](../sources/nebular-sb737-action-thumbnail.md) · [Schxnappi_](../sources/schxnappi-layer-styles-text.md)
