---
type: tarz
code: S4
title: "Challenge / ilerleme split ("Day 1 vs Day 100", "X vs Y")"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S4 — Challenge / ilerleme split ("Day 1 vs Day 100", "X vs Y")

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Değişim ya da karşılaştırma panellerle anlatılır. Varyantlar:
- **Day 1 vs Day 100:** Görüntü dikey ya da hafif çapraz bölünmüş. Sol taraf yağmurlu, karanlık ve küçük (ağlayan yüz). Sağ taraf güneşli, doygun ve devasa. Üst ortada Minecraft logosu ve sarı bir kelime, alt köşelerde "DAY 1" ve "DAY 100" (Ryguyrocky) (gözlem).
- **Lv1 / Lv100 / Lv9999:** 3 eşit panel, beyaz ayırıcı çizgi. Her panelin üstünde kırmızı bir başlık bandı ve beyaz yazı var. Köşelerde küçük 3D cartoon karakterler (Maizen) (gözlem).
- **Önce → sonra oku:** Sol tarafta küçük ya da başlangıç hali, sağda sonuç. Arada kalın kırmızı kavisli bir ok. Sol üstte HARDCORE logosu (CASTER) (gözlem).
- **Noob vs Pro vs Hacker**, **X vs Y** (1of10 "Versus" tipi).

**Görsel özellikler**
- *Kompozisyon:* 2–3 panel. Kontrast kuralı: "Day 1 zayıf/boş, Day 100 epik/dolu" (launchlens şablon notu).
- *Palet:* çok doygun ve parlak. Paneller arasında ruh hali zıt (soğuk ve gri karşısında sıcak ve renkli).
- *Işık:* düz ve parlak, dramatik gölge az.
- *Karakter:* panel başına bir öğe. Yaratık ya da yüz 2D ifadeyle abartılmış.
- *Kontur:* küçük karakterlerde bazen beyaz stroke. Yazılarda kalın siyah kontur.
- *Yazı:* etiketler ("DAY 1", "Lv100") ve 1 başlık kelimesi. Yırtık kâğıt ya da şimşek şeklinde ayırıcı bu türün klasiği (launchlens).

**Örnek kanallar:** Ryguyrocky, Bronzo, Fozo (100 days as X) · Maizen, Milo and Chip (Noob vs Pro, Lv) · CASTER, Firelight (brainrot challenge).

**Mevcut teknikler: nasıl değişir**
| Teknik | S4'te ayar |
|---|---|
| [03 NMS](../techniques/03-nms-shading.md) | Hafif: siyah %10–15. Ya da kapalı (düz cartoon görünüm). |
| [04 Sis](../techniques/04-depth-map-fog.md) | Genelde kapalı. Panel içi derinlik gerekirse Curves 86→100–115. |
| [05 Camera Raw](../techniques/05-camera-raw.md) | Saturation **+30…+50**, Vibrance +15…+25, Clarity +10. "Kötü" panelde Saturation −20…−40 ve Temp −10. |
| [06 Layer Style](../techniques/06-layer-style-ambient-light.md) | Kapalı ya da çok hafif. Her paneldeki karakter **kendi panelinin** ortam rengini almalı. |
| [08 Renk değiştirme](../techniques/08-recolor.md) | Seviye renkleri (yeşil → pembe → kırmızı gibi). |
| [11 Highlight](../techniques/11-highlights.md) | İnce, Overlay. |

**Gereken yeni teknikler:** N6 split düzeni (en kritik olanı), N4 yazı ve etiketler, N8 yüz düzenleme, N11 ok ve doodle, N10 Minecraft/HARDCORE logosu, N1 stroke (küçük karakterler için).

**Brief soruları**
- Kaç aşama olacak (2 mi 3 mü)? Her aşamada tam olarak ne görünecek?
- Etiket metinleri ne (DAY 1/DAY 100, Lv1/Lv100/Lv9999, NOOB/PRO)?
- Bölme düz mü, çapraz mı, yırtık kâğıt mı, şimşek mi?
- Aşamalar arasındaki ruh hali farkı ne olsun (yağmur/güneş, küçük/dev)?
- Hedef yaş grubu ne? Çocuk kitlesiyse daha doygun ve daha cartoon olur.

**Referansta tanıma ipuçları:** görünür bir bölme çizgisi ya da panel çerçevesi · tekrar eden sayısal etiketler · sol ve sağ arasında renk ve ruh hali zıtlığı · kavisli büyük ok · üst ortada Minecraft logosu.

## Doğrulanmış değerler (Levitation testi, 2026-10-01)
"Önce → sonra" split, 2000x1125 tuval, referans 1280x720'den ölçüldü. Kod: `orders/` altındaki `compose.py` (yerel), iskelet [Sipariş akışı](../guides/order-workflow.md).
| Öğe | Değer |
|---|---|
| Ayırıcı | Beyaz **10 px**, üst x = 1188, alt x = 828 (≈18° sola yatık, üstte %59, altta %41). Arkasında beyaz parlama: 46 px çizgi, blur ≈20, %55 (`split()`). |
| Sol panel | Arka plan + karakter birlikte ×1,12, −500/−60 px. NMS gölge %22 / ışık %12, sat 1,28, kontrast 1,06, depth sis #C4DCFA (curve 0,69, uzak blur 4 px), yakın kuma sıcak denge. Kaktüse ince açık yeşil kontur (2 px, %95). |
| Sol karakter | Kadraj yüksekliğinin ~%67'si. NMS %30/%12, ambient zayıf (0,25), kontur 2 px ve hafif renkli, dış koyu bant yok. Ayak altında temas gölgesi. |
| Sağ panel gökyüzü | Render gökyüzü blur 2,5 → `remap` ile referans renklerine; ayırıcının sağında beyaz radyal parlama (%31, blur 170). |
| Sağ karakterler | Her biri referanstaki merkez ve yüksekliğe `place_fit` ile: büyükler ~%45–48, uzak küçükler ~%13–17 yükseklik. NMS %30/%14, ambient 0,15, sat 1,30, kontrast 1,15, 3 katmanlı kenar (3 px mavimsi beyaz + dışta 2 px %10 koyu bant + içte ışık/gölge şeridi). |
| Odak çizgileri | Odak yakın karakterin kafası; 15 ince beyaz üçgen kenardan içe sivrilir; karakterlerin ve kutunun arkasında ([Aksiyon efektleri](../techniques/action-effects.md)). |
| Efekt kutusu | Oyunun fontu ve kutusuyla, genişlik 95 oyun pikseli, 9,4 px/oyun pikseli (≈ tuval genişliğinin %45'i), 3D levha, yakın karakterin ayağının **arkasında**; ayak ikonun üstüne biner ([Yazı](../techniques/text-typography.md)). |
| Katman sırası | gökyüzü → parlama → odak çizgileri → uzak karakterler → kutu (gölgesiyle) → yakın karakterler; sol panel çapraz maskeyle en üstte, ayırıcı en üstte. |
