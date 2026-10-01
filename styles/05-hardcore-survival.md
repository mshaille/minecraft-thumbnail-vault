---
type: tarz
code: S5
title: "Hardcore / survival ("100 days")"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S5 — Hardcore / survival ("100 days")

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Başarı ya da tehlikeyle kanıtlanan bir hayatta kalma hikâyesi. Varyantlar:
- **S5a Üs vitrini:** Kadrajın tamamı tek bir üs ya da yapı (yüksek açıdan ya da 45°). Sol üstte "MINECRAFT HARDCORE" logosu ve altında beyaz "100 DAYS" yazısı (Fru, disruptive builds) (gözlem).
- **S5b Yaratık/kahraman:** Merkezde boss ya da dönüşüm, üstünde logo.
- **S5c Day1/Day100 split:** S4 ile birleşir.
- **S5d "Tek kalp" tehlikesi:** kırık hardcore kalbi, totem, lav.

**Görsel özellikler**
- *Palet:* 1of10'a göre turuncu, kırmızı ve sarı (korku, gurur, gerilim). Gözlemde sıcak fener ışığı karşısında soğuk kar ya da gece görülüyor.
- *Işık:* lavdan ya da gün batımından gelen rim light (1of10). Üs vitrininde içeriden sıcak ışık sızıyor.
- *Kompozisyon:* 1of10'a göre oyuncu merkezde ve kamera dramatik açıyla eğik. Üs vitrininde geniş açı ve simetri.
- *Karakter:* S5a'da yok ya da çok küçük, S5b'de büyük.
- *Yazı:* "100 DAYS" ya da "ONE HEART" gibi 1–3 kelime, beyaz ve siyah konturlu. Logo sol üstte.

**Örnek kanallar:** Luke TheNotable (formatın fikir sahibi; kaynak: Metricate'in 2021 videosu), Forge Labs, Fru, disruptive builds, WelcominTV, Cryptozoology, Metricate, Blooh, bentheboss.

**Mevcut teknikler: nasıl değişir**
| Teknik | S5'te ayar |
|---|---|
| [01 Render](../techniques/01-render-prep.md) | Üs için shader'lı render (Complementary gibi). Metricate, Complementary Shaders + Replay Mod kullanıyor. Post-prodüksiyon için BDS + DMS. |
| [03 NMS](../techniques/03-nms-shading.md) | Yapıda çok etkili: çatı yüzleri ışıkta, duvarlar gölgede. Siyah %18–25. |
| [04 Sis](../techniques/04-depth-map-fog.md) | Hafif, Curves 86→**110–125**. Rengi biyomun gökyüzü (kar için açık mavi, Nether için turuncu). |
| [05 Camera Raw](../techniques/05-camera-raw.md) | Sıcak üs için Temp +5…+15, HSL Orange/Yellow S +20…+40. Kar için Aqua/Blue S +20. Saturation +20…+30. |
| [06 Layer Style](../techniques/06-layer-style-ambient-light.md) | Karakter varsa sıcak ışık rengiyle. |
| [09 Glow](../techniques/09-glow.md) | Fener, lav, portal ve pencere ışıkları. Linear Dodge. |
| [10 Gökyüzü/asset](../techniques/10-sky-and-assets.md) | Kar partikülü, yağmur. Gün batımı gökyüzü. |
| [11 Highlight](../techniques/11-highlights.md) | Çatı kenarları ve karakter, Overlay. |

**Gereken yeni teknikler:** N10 logo ve hardcore kalpleri, N4 yazı, N9 partikül (kar, kıvılcım), N5 vinyet (hafif, −15…−25). Split varyantında N6.

**Brief soruları**
- Kaç gün ya da hangi seri bölümü?
- En güçlü "kanıt" görseli ne (üs, yenilen boss, nadir eşya, dönüşüm)?
- Biyom ve mevsim ne? Gece mi gündüz mü?
- Vurgu tehlike mi olacak (kırmızı) yoksa başarı mı (altın)?
- Logo ve "100 DAYS" yazısı nerede dursun? Kanalın sabit bir yerleşimi var mı?

**Referansta tanıma ipuçları:** "MINECRAFT HARDCORE" logosu (kırmızı HARDCORE ve kalp) · "100 DAYS", "1000 DAYS" yazısı · kadrajda üs vitrini · soğuk ortamda sıcak pencere ışıkları · hardcore kalp ikonları.
