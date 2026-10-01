---
type: tarz
code: S7
title: "Korku / creepypasta / korku modu"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S7 — Korku / creepypasta / korku modu

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** İma edilen bir tehdit, karanlık ve tekinsizlik. 2026'da horror modları çok izleniyor: Forge Labs'in videosu 1 ayda 7 milyon, ThatMob'unki 4 ayda 2,2 milyon (YouTube arama, 2026-10-01). Varyantlar:
- **S7a Karanlık render "afiş":** Siyah-kırmızı palet. Merkezde yaratık, etrafında kıvılcım ve kül partikülleri, yoğun vinyet. Altta kalın beyaz sans-serif başlık ve HARDCORE logosu (Forge Labs) (gözlem).
- **S7b Oyun içi POV lo-fi:** Birinci şahıs, hotbar görünür. Minecraft fontunda bir altyazı ("…blocks away from you") ve yakın planda gerçekçi, ürkütücü bir yüz (Vivilly). Ya da gece bir pencerede gerçekçi insan yüzlü bir ay (ThatMob) (gözlem).
- **S7c "Sıradan dünyada bir şey ters":** Parlak bir vanilla sahne ama içinde tuhaf bir öğe (dev bir çukur). Karakterler arkadan ona bakıyor ve yazı yok (ChiefXD) (gözlem). Gizem duygusu korkudan ağır basıyor.

**Görsel özellikler**
- *Palet:* S7a/S7b'de koyu ve doygunluğu düşük, tek bir vurgu var (kırmızı ya da göz parıltısı). Bir arama sonucu, korkuya yakın içerikte bulanık yeşil ve meşe kahvesi tonlarını, mor ve slime yeşili vurgularla öneriyor (düşük güvenilirlik).
- *Işık:* tek bir kaynak (ay, ekran, meşale). Geri kalan her şey karanlık.
- *Karakter:* yaratık ya da yüz büyük. Oyuncu küçük, arkadan görünüyor ya da POV'da hiç görünmüyor.
- *Kontur/glow:* kontur yok. Gözler parlıyor.
- *Yazı:* kalın beyaz başlık (S7a) ya da Minecraft fontunda diegetic altyazı (S7b). S7c'de yazı yok.
- *Tekinsizlik:* gerçekçi bir insan yüzü blok dünyayla çatışıyor.

**Örnek kanallar:** Forge Labs (horror videoları), Vivilly, ThatMob, ChiefXD, Calvin (CxIvxn), Nightes, Smellzzy, Vanilte, JSadiee.

**Tutorial'lar:** zestu's studio, "How To Make SCARY Minecraft Thumbnails" (2024-11): korkutucu fontlar, ürkütücü ışık, karanlık paletler, yoğun yüz ifadeleri. Aynı kanalın ChiefXD tarzı iki tutorial'ı var (2025-09 ve 2026-03). Seltop, "The Best effect for Horror Thumbnails" (2025-03): **BDS + DMS + NMS** shader'ları. Yani vault'taki NMS/DMS akışı korku stilinde de doğrudan kullanılabiliyor.

**Mevcut teknikler: nasıl değişir**
| Teknik | S7'de ayar |
|---|---|
| [01 Render](../techniques/01-render-prep.md) | BDS (gölge/AO), DMS, NMS (Seltop). Gece sahnesi, tek bir ışık kaynağı. |
| [03 NMS](../techniques/03-nms-shading.md) | Siyah katman **%40–60**. Işık sadece tek kaynağın yönünden. Işık rengi soğuk mavi ya da kırmızı, Overlay %10–20. |
| [04 Sis](../techniques/04-depth-map-fog.md) | **"Karanlık sis":** Solid Color açık mavi yerine **#05070c–#141a22** (ya da kırmızı tema için #1a0505). Aynı depth maskesi, uzak yerler karanlığa gömülür. Curves 86→140–170. |
| [05 Camera Raw](../techniques/05-camera-raw.md) | Exposure −0.3…−0.8 · Blacks **+62 yerine 0…+20** · Saturation −15…−35 (kırmızı hariç; HSL Red S +20…+40) · Temp soğuk (−10…−20) · Vignette −40…−70 · Grain 10–25. |
| [06 Layer Style](../techniques/06-layer-style-ambient-light.md) | Açık mavi Inner Glow **kullanılmaz**. Inner Shadow siyah, Multiply %40–60, Size 60–100 px. İsteğe bağlı kırmızı rim. |
| [07 Elle gölge](../techniques/07-hand-shadows.md) | %80–90. |
| [08 Renk değiştirme](../techniques/08-recolor.md) | Eşyaları desatüre et, kanı ya da vurguyu kırmızıya çek. |
| [09 Glow](../techniques/09-glow.md) | Göz glow'u (beyaz ya da kırmızı), Linear Dodge, küçük ve keskin. |
| [10 Gökyüzü/asset](../techniques/10-sky-and-assets.md) | Ay, kara bulut, sis PNG'si, kül. |
| [11 Highlight](../techniques/11-highlights.md) | Neredeyse yok. Sadece ışık kaynağına bakan bir iki kenar, soğuk renkte. |

**Gereken yeni teknikler:** N5 vinyet (ağır), N4 yazı (kalın başlık ya da Minecraft fontunda altyazı), N10 oyun içi UI (hotbar, chat, altyazı), N9 kül ve kıvılcım, N15 grading, N16 tekinsiz kompozit.

**Brief soruları**
- Hangi mod ya da varlık? Görünsün mü, sadece ima mı edilsin?
- Afiş mi (render ve başlık) yoksa oyun içi POV ekran görüntüsü mü?
- Kan ve şiddet sınırı ne (kitlenin yaşı)?
- Altyazı ya da başlık metni ne olacak?
- Sahne gece mi, iç mekân mı, liminal (dreamcore) mi?

**Referansta tanıma ipuçları:** ortalama parlaklık çok düşük · tek bir kırmızı vurgu · gerçekçi, insan dokulu bir yüz · hotbar ya da altyazı · ağır vinyet · Minecraft fontunda yazılmış rahatsız edici bir cümle.
