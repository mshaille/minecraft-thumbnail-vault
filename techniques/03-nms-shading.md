---
type: teknik
order: 3
title: NMS ile gölge ve ışık
sources: [spare-clean-thumbnails]
tags: [teknik, shading, color-range]
status: stabil
---
# 3. NMS ile gölge ve ışık

Fikir: NMS render'ında her yüz yönü farklı renktedir. Bir rengi seçmek, o yöne bakan **bütün yüzleri** seçmek demektir.

## Gölge
1. Arazi NMS katmanını seç → **Select > Color Range**.
2. *Select: Sampled Colors*. Damlalıkla gölgede kalması gereken yüz rengine tıkla (videoda **kırmızı** = blokların yan yüzleri).
3. **Fuzziness: 200** (en geniş alan) → OK.
4. NMS katmanını gizle. Arazinin hemen üstüne **yeni katman** aç.
5. Fırça: **Soft Round, ~508 px, Hardness %1, siyah**. Seçimin üstünü boya.
6. Katman **Opacity ≈ %18**.

## Işık
1. NMS katmanında tekrar Color Range. Bu sefer **yeşil** (üst yüzler) seçilir, Fuzziness 200.
2. NMS'i gizle ve yeni katman aç. **Beyaz**, çok büyük soft fırça (~2554 px) ile boya.
3. Blend mode **Overlay**, **Opacity ≈ %10**. Seçimi **Ctrl+D** ile kaldır.

Aynı işlemi oyuncuların NMS render'ıyla oyunculara da uygula.

> [!tip] Hangi rengin gölge olduğu ışık yönüne göre değişir. Önce sahnedeki ana ışığın nereden geldiğine karar ver.

Önceki: [Belge kurulumu](02-document-setup.md) · Sonraki: [Depth map sis](04-depth-map-fog.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (6:59–7:56)
