---
type: index
title: Minecraft Thumbnail Vault
tags: [index]
---
# Minecraft Thumbnail Vault

![logo](assets/logo.png)

Minecraft YouTube kapak fotoğraflarını (thumbnail) **Photoshop / Photopea** ile yapmak için öğrenilen her şey. Tutorial videolar kare kare izlenip değerleriyle birlikte not alındı. Aynı klasör hem bir Claude Code skill'i hem de GitHub reposu.

## Adım adım süreç
| # | Teknik | Kısaca |
|---|---|---|
| 1 | [Render hazırlığı](techniques/01-render-prep.md) | Aynı kameradan shader'sız, NMS ve DMS render'ları |
| 2 | [Belge kurulumu](techniques/02-document-setup.md) | 1920x1080, render'ları katman olarak al |
| 3 | [NMS gölgelendirme](techniques/03-nms-shading.md) | Color Range, Fuzziness 200, siyah %18, beyaz Overlay %10 |
| 4 | [Depth map sis](techniques/04-depth-map-fog.md) | Solid Color #c7e8ff + depth maske + Curves |
| 5 | [Camera Raw](techniques/05-camera-raw.md) | Preset değerleri |
| 6 | [Ortam ışığı (Layer Style)](techniques/06-layer-style-ambient-light.md) | Gradient Overlay + Inner Glow + Inner Shadow |
| 7 | [Elle gölge](techniques/07-hand-shadows.md) | Polygonal Lasso, %62 |
| 8 | [Renk değiştirme](techniques/08-recolor.md) | Quick Selection, Soft Light %36 |
| 9 | [Glow](techniques/09-glow.md) | Soft fırça, Linear Dodge |
| 10 | [Gökyüzü ve asset'ler](techniques/10-sky-and-assets.md) | Sky, kar, lens flare (Screen) |
| 11 | [Highlight](techniques/11-highlights.md) | 3–5 px, karakterin içinde, uçları sivrilt, Overlay |
| 12 | [Export](techniques/12-export.md) | PNG, güncel YouTube limitleri |
| – | [Referansa göre uyarlama](techniques/adapt-to-reference.md) | Sipariş/referansa göre hangi ayar nasıl değişir |
| – | [Photopea uyumluluğu](techniques/photopea-compatibility.md) | Her adımın Photopea karşılığı |

## Kaynaklar
- [Spare — How to Make CLEAN Minecraft Thumbnails](sources/spare-clean-thumbnails.md)
- [zestu's studio — How to do Highlights](sources/zestu-highlights.md)

## Referanslar
- [Referans kütüphanesi ve analiz listesi](references/README.md)
- [Referanslardan öğrenilenler](references/lessons.md)
- Obsidian'da görsel galeri: `references/gallery.base`

## Siparişler
- `/mcthumb:order` ile açılır, `orders/` klasöründe sadece yerelde durur. Şablon: [templates/order.md](templates/order.md)

## Geliştirme
- [Yol haritası](dev/roadmap.md) · [Değişiklik günlüğü](dev/changelog.md)
- Yeni oturumlar için kurallar: [AGENTS.md](AGENTS.md)
