---
type: tarz
code: S3
title: "SMP / drama: büyük karakter ve yüz ifadesi"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S3 — SMP / drama: büyük karakter ve yüz ifadesi

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Tek bir karakterin duygusu ve kime karşı olduğu anlatılır. Varyantlar:
- **S3a Lifesteal portre:** Karakter ortada, belden yukarısı ve kameraya dönük. Arka plan karartılmış ve üstünde Minecraft kalp ikonları var (dizi ya da desen halinde). Ayakların altında kırmızı bir aura (SB737, Reddoons) (gözlem).
- **S3b Oyun içi chat ile drama:** Sahte bir chat satırı (`<Oyuncu> ...`), yüze boyanmış bir ifade, ön planda birinci şahıs kılıç (Spongs) (gözlem).
- **S3c Sticker:** Skin yüzü ya da karakter beyaz konturla kesilmiş, yanında kırmızı ok ya da daire. 2019–2021 SMP dönemi. Bugün daha çok çocuk ve reaction kanallarında görülüyor.
- **S3d Gerçek yüz + Minecraft:** Sol tarafta büyük bir şaşkın gerçek yüz (eller yanakta), sağda Minecraft sahnesi ve kalp barları. Kesim temiz, belirgin beyaz kontur yok (PrestonPlayz) (gözlem).

**Görsel özellikler**
- *Kompozisyon:* karakter kadraj yüksekliğinin %60–90'ı, ortada ya da sol üçte birde, kameraya bakıyor. 1of10'a göre SMP'de iki oyuncu karşı karşıya, ikincil karakterler bulanık, kompozisyon üçte bir kuralına göre.
- *Palet:* karakter sıcak, ortam soğuk (1of10). Lifesteal'de siyah ve kırmızı.
- *Işık:* karakter arka plandan çok daha parlak. Arkadan kırmızı ya da mavi aura.
- *Kontur/glow:* S3c'de 6–14 px beyaz stroke. S3a'da kontur yok, onun yerine outer glow ya da aura.
- *Yazı:* 0–3 kelime ya da **oyun içi UI** (chat, kalp barı).
- *Arka plan:* koyu ya da düz, bulanık ya da ikon desenli.

**Örnek kanallar:** SB737, Reddoons, Spongs, Rumyy (Lifesteal SMP) · PrestonPlayz (gerçek yüz) · TommyInnit/Dream SMP dönemi (2020). O dönemde ham ekran görüntüsü kullanılıyordu, bugün sadece tarihsel referans (gözlem).

**Mevcut teknikler: nasıl değişir**
| Teknik | S3'te ayar |
|---|---|
| [03 NMS](../techniques/03-nms-shading.md) | Karakterde tam uygulanır. Arka plan ayrı bir siyah katmanla **%40–60 karartılır**. |
| [04 Sis](../techniques/04-depth-map-fog.md) | Çoğunlukla **kapalı**. S3a'da sis yerine koyu düz fon ya da ikon deseni. |
| [05 Camera Raw](../techniques/05-camera-raw.md) | Saturation +25…+35 · Clarity +15…+20. Arka planda Saturation −20. |
| [06 Layer Style](../techniques/06-layer-style-ambient-light.md) | Inner Glow rengi **aura rengi** (Lifesteal'de kırmızı #ff2a2a), Size 40–80 px. S3c'de bunun yerine N1 stroke. |
| [08 Renk değiştirme](../techniques/08-recolor.md) | Zırh ya da silahı kanal rengine çekmek için. |
| [09 Glow](../techniques/09-glow.md) | Ayak altında aura (N2) ve silah glow'u. |
| [11 Highlight](../techniques/11-highlights.md) | Normal %100, 4–5 px. |

**Gereken yeni teknikler:** N8 yüz düzenleme (en kritik olanı), N1 stroke (S3c), N2 outer glow/aura, N10 oyun içi UI (kalp, chat), N5 vinyet (−25…−45), N3 arka plan blur, N13 gerçek yüz kesimi (S3d).

**Brief soruları**
- Thumbnail'de hangi duygu olacak (öfke, şok, kibir, korku)?
- Kim kime karşı, rakip görünecek mi?
- Kalp ya da Lifesteal mekaniği görselde yer alacak mı?
- Gerçek yüz fotoğrafı kullanılacak mı? Kullanılacaksa fotoğrafın ışığı nereden geliyor?
- Hikâye bir chat satırıyla anlatılsın mı? Metni ne olacak?
- Hangi skin(ler) kullanılacak? Yüze ifade boyamak serbest mi?

**Referansta tanıma ipuçları:** tek karakter kadrajın yarısından fazlası · arka plan koyu, düz ya da desenli · skin yüzünde 2D boyanmış ifade (kaş, gözyaşı, öfke işareti, büyük göz bebekleri) · kalp ikonları · Minecraft chat kutusu (yarı saydam siyah şerit, piksel font) · gerçek insan yüzü · S3c'de karakterin çevresinde düzgün kalınlıkta beyaz bir hat.
