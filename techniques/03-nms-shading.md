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

## NMS renklerini okuma (ilk testten)
Renk = dünya normali: R = x, G = y, B = z, her kanal −1…+1 → 0…255.
| NMS rengi | Yüz yönü | Tipik kullanım |
|---|---|---|
| (128, 255, 128) yeşil | yukarı (+Y) | ışık (üst yüzler, zemin) |
| (255, 128, 128) kırmızı | +X (bu çekimde kameraya bakan yan yüz) | gölge ya da ışık, ışık yönüne göre |
| (128, 128, 0) zeytin | −Z | çöl testinde tepelerin yan yüzleri → gölge |
| koyu mor | aşağı (−Y) | karakterlerin alt yüzleri → gölge |
| saf beyaz | normal yok (gökyüzü) | maskeden çıkar |

- **Oyuncu dış katmanının (ceket, şapka) normali ters gelir.** Kodda x bileşeninin mutlak değeri alınır. Karakter kenarındaki ışık/gölge tarafı NMS'ten değil, kenarın ekrandaki yönünden hesaplanır (`thumbkit.edge_sides`).
- Kod karşılığı: `thumbkit.nms_shade(base, nms, shadow, light, valid)`. Işık skoru d = 0,8·y + 0,35·z + 0,2·|x|. Testte arka plan için shadow 0,22 / light 0,12 (gökyüzü `valid = DMS > 0` ile dışarıda), karakterler için 0,30 / 0,12–0,14 kullanıldı.
- NMS düz arka plandan (ör. kaktüs) maske de verir: NMS x > 0,9 ve DMS > 0,93 → yakın kaktüs yüzü. Bu maskenin çevresine ince kontur `thumbkit.ring()` ile çekildi.

Önceki: [Belge kurulumu](02-document-setup.md) · Sonraki: [Depth map sis](04-depth-map-fog.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (6:59–7:56)
