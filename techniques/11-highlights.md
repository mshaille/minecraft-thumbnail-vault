---
type: teknik
order: 11
title: Highlight (kenar parlaması)
sources: [spare-clean-thumbnails, zestu-highlights]
tags: [teknik, highlight, brush, lasso]
status: stabil
---
# 11. Highlight (kenar parlaması)

İki videonun birleşimi. Ayrıntılı anlatım [zestu — Highlights](../sources/zestu-highlights.md) videosunda.

## Kurulum
- **B** (Brush) → **Hard Round**, Hardness %100, **beyaz**, Opacity/Flow %100.
- Boyut: **3–5 px**. 1080p'de 3–4 px, 4K'da 4–5 px (Spare 1080p'de 4 px kullanıyor).
- Oyuncunun üstüne yeni katman aç → **Ctrl+G** ile gruba al, grubun adını **"H"** koy. Farklı bölgeler (ör. saç) için ayrı katmanlar kullanabilirsin.

## Çizme
1. Kenarın başına tıkla, sonuna **Shift+tık** → düz çizgi. Köşeden köşeye ilerle.
2. **Kural:** fırça dairesi **karakterin İÇİNDE** kalmalı. Çizgi kenarın üstüne yarı yarıya taşmamalı, arka plana kaymamalı.
3. Sadece ışığın vurduğu / vuracağı kenarlara uygula (üst kenarlar, ışığa bakan sırtlar). Kenarı gölgeye girdiği yere kadar takip et.

## Uçları sivriltme (temiz bitirme)
- **Yöntem A (Spare):** Hardness 0 (yumuşak) silgiyle uçları söndür.
- **Yöntem B (zestu, daha temiz):** **Polygonal Lasso (L)** ile çizginin bitmesini istediğin yerden karşı tarafa çapraz, **ince uzun bir kama** seçimi yap. Sonra **Eraser** ile seçimin içini sil. Çizgi kalından inceye sivrilerek biter. Yakından arada tek tük piksel kalır ama uzaktan çok temiz görünür.
- Yolda kalan / fazla görünen highlight'ları (ör. saç çıkıntıları) aynı yöntemle kısalt.

## Karıştırma
- Highlight katmanını **Overlay** yap. Abartısız ve ince durur, iki kaynak da bunu öneriyor. Soft Light da denenebilir.

## Tarz farkı: yumuşak highlight (Swiffex, Unstable SMP / no-shader)
- Fırça **3 px, Hardness %0**, Normal, %100. Uçları yumuşak silgiyle söndür: Opacity **%11**, ~50 px (anlatıcı ~20 px ve %10 diyor).
- Spare/zestu yöntemi (Hard Round %100 + Overlay) ile çelişir; ikisi de geçerli, **tarza göre** seç: temiz render → sert + Overlay; parlak no-shader SMP → yumuşak + Normal.
- **Işık geçişi:** oyuncuya **clipping mask** olarak yeni katman, yumuşak beyaz fırça (%20, 100 px, hardness 0) ile güneş tarafındaki kenarları boya. Overlay yap, kopyala, kopyayı Normal yap ve opaklığı göz kararı ayarla.

Önceki: [Gökyüzü ve asset'ler](10-sky-and-assets.md) · Sonraki: [Export](12-export.md)
Kaynaklar: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (12:43–13:17) · [zestu — Highlights](../sources/zestu-highlights.md) (tamamı)
