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

> [!warning] **Kullanıcı bunu fazla buldu.** Referansa eşlenmiş şiddette "inanılmaz fazla parlıyor, ben çok hafif istedim" dedi. Kullanıcı "biraz parlasın" diyorsa **hafif başla**: çekirdek ×(1,10; 1,0; 1,0), hale şiddetleri 0,12 / 0,30 / 0,10 (referansın ~%20'si). Sonuç: trim L 90, zırh L 65; hale 2 px'te %7. Gerekirse adım adım artır.
4. **Ortam:** trim rengi ortamın rengine yakınsa (Nether'de kırmızı trim) ortamın doygunluğunu yarıya indir. Referansta ortam doygunluğu 0,15–0,26, karakterler ve trim'ler doygundu; ortam doygun kalınca kırmızı trim kayboluyor.
5. **Ölç:** `python3 tools/glow_profile.py <görsel> --color g|r|b --region x0,y0,x1,y1` referansta ve taslakta aynı bölgede.

## Altın / metal nesne (kupa, ölçülmüş: Kupa siparişi 2026-10-04)
Render'da (no-shader) metal nesnenin bütün yüzleri neredeyse aynı parlaklıkta gelir (kupada L 0,63–0,67), metal gibi durmaz.
1. **Yüz yönüne göre gölge** (NMS): üst (yeşil) ×1,25, ön (kırmızı) ×0,82, yan (mavi) ×0,55, diğer ×0,45.
2. **Gradient Map** (altın rampası, L → renk): 0 (30,16,2) · 0,3 (110,62,8) · 0,55 (200,135,20) · 0,75 (245,190,50) · 0,92 (255,228,120) · 1,0 (255,245,200). Kod: `thumbkit.gradient_map`.
3. **Parlak detay:** üst yüz kenarlarında ince ışık (σ 1 px, %45), nesne boyunca çapraz parlak şerit (%22, Screen), 3–4 dört kollu yıldız parıltısı (`thumbkit.sparkles`, r ~42 px @1280).
4. **Hale yalnız parlak yüzlerden** (L > 0,6): bloom σ 3/14/45, şiddet 0,3/0,45/0,45. Bütün nesneden hale verilince silüet kayboldu.
5. Nesne sahnenin ışık kaynağıysa: huzme (`god_rays`, Screen ×0,75), karakterlerde ona bakan kenarlarda altın kenar ışığı, odada ışık düşüşü (nesne 1,0 → uzak köşe 0,5).

Photoshop karşılığı (metal): Gradient Map katmanı (Clipping Mask) + Curves ile yüz kontrastı + yumuşak beyaz fırçayla Overlay parlak şerit + yıldız fırçası.

Photoshop karşılığı: trim'leri Color Range ile seç → yeni katmana kopyala → Hue/Saturation ile parlat (Lightness +, Saturation +) → kopyayı Gaussian Blur ~5 px (1280'de) + Linear Dodge/Screen, bir kopya daha ~15 px blur ve düşük opaklıkla.

Önceki: [Renk değiştirme](08-recolor.md) · Sonraki: [Gökyüzü ve asset'ler](10-sky-and-assets.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (12:05–12:17)
