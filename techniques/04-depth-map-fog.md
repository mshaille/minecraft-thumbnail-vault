---
type: teknik
order: 4
title: Depth map ile sis / atmosfer
sources: [spare-clean-thumbnails]
tags: [teknik, depth-map, sis, maske]
status: stabil
---
# 4. Depth map ile sis / atmosfer

1. DMS (depth map) render'ını sürükle ve tam hizala.
2. Layers panelinin altından **Create new fill/adjustment layer > Solid Color** → **#c7e8ff** (açık mavi; H205 S22 B100).
3. Depth map katmanı **her şeyin en üstünde** dursun.
4. **Channels** paneli → **RGB** küçük resmine **Ctrl+tık**. Depth map'in parlaklığı seçim olarak yüklenir.
5. Layers'a dön. Color Fill'in **beyaz maske kutusuna** tıkla → **Ctrl+I**. Maske seçili alanda ters çevrilir: yakın yerler şeffaf kalır, uzak yerler mavi sisle kaplanır.
6. Depth map katmanını gizle.
7. Color Fill katmanını **ana oyuncuların altına**, kalabalık/arazinin üstüne taşı. Sis ana karakterleri kapatmasın.
8. Şiddeti ayarla: maske seçiliyken **Image > Adjustments > Curves (Ctrl+M)** → nokta **Input 86 → Output 134**. Eğriyi yukarı çekmek sisi artırır.
9. Rengi değiştirmek için Color Fill küçük resmine çift tıkla. Sis rengi sahnenin gökyüzü rengine uysun.

## Kodla ve özel durumlar (ilk testten)
- `thumbkit.depth_fog(bg, dms, color, curve, blur)`: sis maskesi (1 − DMS)^curve. `curve` 0,59 ≈ videodaki Curves 86→134, 0,69 ≈ 86→120 (testte kullanılan, daha hafif). Uzak kısım ayrıca `blur` px bulanıklaşır (testte 4).
- Sis rengi referansın gökyüzü tonundan: testte **#C4DCFA**.
- **Sadece gökyüzü olan arka plan:** DMS tamamen siyahtır, sis uygulanamaz. Uzaktaki karakterleri `thumbkit.tint()` ile ortam rengine çek. Gökyüzünü referansa `thumbkit.remap()` ile eşle: iki ölçülmüş renk çifti, testte gökyüzü tabanı (168,204,252) → (112,174,254) ve bulut (222,234,252) → (175,208,253).
- Çöl gibi sıcak sahnede yakın araziye hafif sıcak denge: RGB × (1,065; 1,06; 0,93), DMS ile yakına doğru artar (Color Balance karşılığı).

Önceki: [NMS gölgelendirme](03-nms-shading.md) · Sonraki: [Camera Raw](05-camera-raw.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (8:07–9:10)
