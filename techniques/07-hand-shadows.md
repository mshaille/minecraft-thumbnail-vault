---
type: teknik
order: 7
title: Elle gölge
sources: [spare-clean-thumbnails]
tags: [teknik, shading, lasso]
status: stabil
---
# 7. Elle gölge

1. Oyuncu katmanının üstüne yeni katman aç.
2. **Polygonal Lasso Tool (L)** ile sahnede gölgede kalması gereken yan yüzlerin kenarlarını çiz. Hangi yüzün gölgede kalacağı ışık yönüne göre değişir.
3. Seçimi koyu/siyah ile boya → **Opacity ~%62**.
4. Her oyuncu için ayrı katman kullan (videoda 2. oyuncu ayrı katmanda brush ile yapılıyor).

## Tarz farkı: Swiffex (Photopea, no-shader)
- Yüzleri Lasso ile seç. Güneşe bakan yüzler: beyaz, **Overlay**. Güneşe bakmayan yüzler: siyah, **Normal ~%65**.
- **Temas gölgesi:** oyuncunun altındaki katmanda Elliptical Marquee, siyahla doldur, Normal **%49**, blur yok. Her oyuncu için kopyala.
- **Ayak kırpma:** ayakların altından ince bir şerit kes ki oyuncular kuma/zemine otursun. Fazla kesme; Photopea'da layer mask ile yap.

Önceki: [Ortam ışığı (Layer Style)](06-layer-style-ambient-light.md) · Sonraki: [Renk değiştirme](08-recolor.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (10:57–11:32)
