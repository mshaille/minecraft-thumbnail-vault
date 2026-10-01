---
type: tarz
code: S8
title: "Build / showcase / timelapse"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S8 — Build / showcase / timelapse

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Yapının kendisi kahraman. Ölçek, sayı ve ışıkla etkiler.

**Görsel özellikler**
- *Kompozisyon:* yapı kadrajın %70'inden fazlası. 3/4 (45°) açı ya da kuş bakışı. 1of10'a göre 45° açılı çekim, geniş derinlik, simetri ve akışı gösteren oklar.
- *Palet:* 1of10'a göre beyaz, açık mavi ve yeşil, temiz arka plan. Gece ya da uzay temasında koyu fon ve sıcak/neon ışıklar (Timtenth) (gözlem).
- *Işık:* shader'lı (altın saat, gece pencere ışıkları).
- *Karakter:* yok ya da köşede küçük bir ölçek göstergesi (Timtenth'te astronot) (gözlem). Hermitcraft'ta yapının yanında büyük, düz ışıklı bir skin yüzü (GoodTimesWithScar) (gözlem).
- *Yazı:* sayı odaklı ("36 MILLION BLOCKS", "500 HOURS"), çoğu zaman piksel fontta, ya da hiç yazı yok.

**Örnek kanallar:** Timtenth_Buildings, haraxx, captain0106, CookieCrumb (timelapse) · GoodTimesWithScar, Grian, Mumbo Jumbo (Hermitcraft) · Fru, disruptive builds (S5 ile).

**Mevcut teknikler: nasıl değişir**
| Teknik | S8'de ayar |
|---|---|
| [01 Render](../techniques/01-render-prep.md) | Shader'lı render, uzak arazi için Distant Horizons ya da Voxy. DMS mutlaka alınsın. |
| [03 NMS](../techniques/03-nms-shading.md) | Yapıda en verimli adım. Siyah %18–30. |
| [04 Sis](../techniques/04-depth-map-fog.md) | Ölçek için hafif haze, Curves 86→**110–130**. |
| [05 Camera Raw](../techniques/05-camera-raw.md) | HSL artışı yapının malzeme renklerine (ör. turuncu terracotta, mavi cam). Texture +15…+30 (blok dokusu). |
| [06](../techniques/06-layer-style-ambient-light.md) / [07](../techniques/07-hand-shadows.md) | Karakter yoksa atlanır. |
| [09 Glow](../techniques/09-glow.md) | Pencere, fener ve motor ışıkları. |
| [10 Gökyüzü/asset](../techniques/10-sky-and-assets.md) | Gökyüzü değişimi (gece, galaksi, gün batımı). |
| [11 Highlight](../techniques/11-highlights.md) | Çatı kenarları ve silüet. |

**Gereken yeni teknikler:** N4 sayı yazısı (piksel font), N3 tilt-shift (isteğe bağlı, minyatür etkisi), N6 önce/sonra, N10 blueprint overlay (isteğe bağlı), N5 hafif vinyet.

**Brief soruları**
- Yapı hangi açıdan en iyi görünüyor?
- Gündüz mü gece mi? Hangi shader?
- Ölçek nasıl gösterilecek: karakter mi, sayı mı?
- Önce/sonra gösterilecek mi?
- Yazı olarak hangi sayı ya da süre kullanılacak?

**Referansta tanıma ipuçları:** kadrajın çoğu tek yapı · karakter yok ya da çok küçük · shader ışığı · sayı içeren yazı · yüksek açı.
