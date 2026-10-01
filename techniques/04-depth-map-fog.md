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

Önceki: [NMS gölgelendirme](03-nms-shading.md) · Sonraki: [Camera Raw](05-camera-raw.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (8:07–9:10)
