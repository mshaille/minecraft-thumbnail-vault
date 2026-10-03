---
type: teknik
order: 9
title: Glow (parlama)
sources: [spare-clean-thumbnails]
tags: [teknik, glow, blend-mode]
status: stabil
---
# 9. Glow (parlama)

- Yeni katman aç. **Hardness 0** soft fırça, temanın rengi (videoda **mor**). Parlayacak noktaya (mace'in küre ucu) tek dokunuş yap.
- Blend mode **Linear Dodge (Add)**. Color Dodge da denendi ama Linear Dodge seçildi.

- Alternatif (Nebular): beyaz yumuşak fırça noktaları, Blend **Overlay** → küçük ışık parlamaları.

## Işıyan zırh trim'i (ölçülmüş, Trim klanı siparişi 2026-10-03)
Referansta yeşil trim'ler zırhtan daha parlak ve çevrelerine yumuşak bir hale taşıyor. Kullanıcının isteği: "trim'ler normal zırha göre biraz daha parlayacak".
1. **Maske:** trim renginin pikselleri (kırmızı trim: R > 0,43, G ve B < 0,31, R > 2,2 × max(G,B)). Skin'deki aynı renkli yerleri (ör. kırmızı gözler) çıkar; yüz komşuluğuna bakan kural sınırda kaldı, ölçülmüş kutular kesin çalıştı.
2. **Çekirdek:** trim'i NMS gölgesinden **sonra**, gölgesiz rengiyle geri yaz (ışıyan yüzey gölgede kalmaz). Rengi kendi tonunda parlat: ×(1,30; 1,05; 1,0) + 0,06 R. Turuncuya kaydırma (G'yi artırma) lav çatlağı gibi görünür; referanstaki yeşil de yeşil kaldı.
3. **Hale:** Screen (Linear Dodge'a yakın) ile üç bulanık kopya, σ 1,5 / 5,5 / 14 px (1280'de; 4K'da ×3), şiddet 0,55 / 1,5 / 0,55. Ölçülen hale: trimden 1/2/4/6/8 px uzakta çekirdek farkının %62/44/26/17/10'u. Kod: `thumbkit.bloom(rgb, emit, k)`.
4. **Ortam:** trim rengi ortamın rengine yakınsa (Nether'de kırmızı trim) ortamın doygunluğunu yarıya indir. Referansta ortam doygunluğu 0,15–0,26, karakterler ve trim'ler doygundu; ortam doygun kalınca kırmızı trim kayboluyor.
5. **Ölç:** `python3 tools/glow_profile.py <görsel> --color g|r|b --region x0,y0,x1,y1` referansta ve taslakta aynı bölgede.

Photoshop karşılığı: trim'leri Color Range ile seç → yeni katmana kopyala → Hue/Saturation ile parlat (Lightness +, Saturation +) → kopyayı Gaussian Blur ~5 px (1280'de) + Linear Dodge/Screen, bir kopya daha ~15 px blur ve düşük opaklıkla.

Önceki: [Renk değiştirme](08-recolor.md) · Sonraki: [Gökyüzü ve asset'ler](10-sky-and-assets.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (12:05–12:17)
