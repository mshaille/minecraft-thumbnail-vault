---
type: index
title: Tarz rehberi
tags: [tarz, index]
status: taslak
checked_on: 2026-10-01
---
# Tarz rehberi

Her Minecraft thumbnail'i aynı tarzda değil. Vault'un ana iş akışı (`techniques/01–12`) **S1 Temiz render** tarzının tarifi. Sipariş gelince önce **tarz seçilir**, sonra o tarzın kartına göre teknikler açılır, kapatılır veya ayarları değiştirilir; en son referansa göre ince ayar yapılır ([uyarlama](../techniques/adapt-to-reference.md)).

Web araştırması ve 28 güncel thumbnail incelemesiyle derlendi (2026-10-01). "(gözlem)" etiketi bir thumbnail'e bakılarak çıkarılan bilgiyi gösterir. Kartlardaki değerler taslak; videolardan doğrulananlar teknik notlarında.

## Tarzlar
| Kod | Kart |
|---|---|
| **S1** | [Temiz / yumuşak render ("clean render")](01-clean-render.md) |
| **S2** | [Sinematik / dramatik ışık ("Unstable SMP" epik stili)](02-cinematic.md) |
| **S3** | [SMP / drama: büyük karakter ve yüz ifadesi](03-smp-drama.md) |
| **S4** | [Challenge / ilerleme split ("Day 1 vs Day 100", "X vs Y")](04-split-progression.md) |
| **S5** | [Hardcore / survival ("100 days")](05-hardcore-survival.md) |
| **S6** | [Speedrun / manhunt / PvP](06-speedrun-manhunt-pvp.md) |
| **S7** | [Korku / creepypasta / korku modu](07-horror.md) |
| **S8** | [Build / showcase / timelapse](08-build-showcase.md) |
| **S9** | [Çizim / illüstre 2D (ve hibritleri)](09-drawn-2d.md) |
| **S10** | [Meme / bilinçli low-effort](10-meme-lofi.md) |
| **S11** | [Shorts (dikey 9:16)](11-shorts.md) |

## 0. Nasıl kullanılır, nasıl hazırlandı

**Plugin akışı**
1. Brief ve referansla **ana stili** seç. Gerekirse en fazla **bir yan stil** ekle (§1).
2. Stil kartındaki "mevcut teknikler" tablosuna göre vault adımlarını aç, kapat ya da ayarlarını değiştir (§2). Toplu bakış için §2.12'deki matrise bak.
3. Vault'ta olmayan teknikleri §3 kataloğundan ekle (N1–N20).
4. Stilin 2025–2026'da yükselişte mi, eskimiş mi olduğunu §4'te kontrol et. Müşteriye bunu söyle.

**Yöntem**
- Web araştırması: tasarımcı portfolyoları, 1of10 makaleleri, YouTube tutorial açıklamaları, YouTube Yardım/Blog, şablon siteleri ve Wikipedia.
- 2026-10-01 tarihli YouTube arama sonuçlarından seçilen **28 thumbnail'e görsel olarak bakıldı** (i.ytimg.com `hqdefault`, 480x360). Liste §6'da. Bu bakışlardan çıkan bilgiler metinde **(gözlem)** etiketiyle geçiyor.
- Tutorial videolarının sadece başlık, açıklama ve bölüm listesi okundu. Transkript alınamadı, videolar izlenmedi.

**Sınırlar (dürüst not)**
- **reddit.com araç tarafından engellendi.** r/NewTubers ve r/Minecraft başlıkları açılamadı ve alıntılanamadı.
- X (Twitter) gönderileri sadece arama özetinden görüldü.
- AI-thumbnail şirketlerinin blogları (thumby, bananathumbnail, thumbs.ai, launchlens, tubetuner) **düşük güvenilirlikte**. Verdikleri yüzdeler doğrulanmadı ve burada "iddia" olarak geçiyor.
- §3'teki yeni tekniklerin ayar aralıkları **başlangıç değeri**. Bir tutorial'dan ölçülmediler. Vault'a eklenirlerse `status: taslak` olmalılar.
- Tüm px değerleri **1920x1080** içindir. 3840x2160'ta ×2 al.

## 1. Hızlı karar rehberi

### 1a. Brief'teki kelimeler → stil

| Brief'te geçen | Ana stil | Sık yan stil |
|---|---|---|
| "clean", "temiz", "aesthetic", "soft", "pastel", Spare/mangofx tarzı | **S1 Temiz render** | S2 |
| "cinematic", "epic", "movie", "film afişi", Unstable SMP, Wemmbu, Parrot, Spoke, ordu, şato, savaş | **S2 Sinematik** | S3 |
| "SMP", "Lifesteal", "betrayal/ihanet", "drama", "kalp çaldı", "X beni öldürdü", tepki yüzü, facecam | **S3 SMP/drama** | S2, S10 |
| "Day 1 vs Day 100", "Noob vs Pro", "Lv1/Lv100", "X vs Y", "before/after", "evolve", "upgrade" | **S4 Split/ilerleme** | S5 |
| "100 days", "1000 days", "hardcore", "survived", "one heart" | **S5 Hardcore** | S4, S8 |
| "manhunt", "speedrunner vs hunters", "speedrun", "world record", "PvP", "bedwars", "clutch" | **S6 Speedrun/manhunt/PvP** | S10 (rekor) |
| "horror", "scary", "creepypasta", "dreamcore", "liminal", "stalker", mod adı (Otherworld, Dreamshift...) | **S7 Korku** | S5 (hardcore horror) |
| "build", "timelapse", "base tour", "showcase", "megabuild", "X saat/blok" | **S8 Build** | S5 |
| "animation", "çizim", "drawn", "cartoon", "anime", Life Series movie, roleplay, çocuk kitlesi | **S9 Çizim/2D** | S4 |
| "meme", "funny", "cursed", "episode 12", seri bölümü, "low effort olsun" | **S10 Meme/lo-fi** | S6 |
| "short", "Shorts", "TikTok", "Reels", "dikey" | **S11 Shorts** (format, üstüne bir stil daha seçilir) | – |

### 1b. Referans görselden stil (Claude'un sırayla kontrol edeceği karar ağacı)
Önce `tools/analyze_reference.py` ile ortalama parlaklık, doygunluk ve palet alınır, sonra görsele bakılır. **İlk tutan dal kazanır.**

1. **Oran 9:16 mı?** Evet → **S11**. Sonra içerik için 2. maddeden devam et.
2. **Çizgi (line art) var mı, karakterlerin anatomisi bloklu değil mi, gölgeler cel tipinde mi?** Evet → **S9a**. Render ama yüz anime gözleriyle boyanmışsa → **S9b**.
3. **Görünür bir bölme (dikey, çapraz ya da panel) ve tekrar eden bir etiket kalıbı var mı** ("DAY 1 / DAY 100", "Lv1 / Lv100")? Ya da önce→sonra gösteren kavisli bir ok? Evet → **S4**.
4. **Ham oyun içi ekran görüntüsü mü?** (HUD/hotbar görünüyor, shader yok, işlenmemiş ışık)
   - Karanlık, ürkütücü yüz ya da Minecraft fontunda altyazı varsa → **S7b**.
   - Büyük piksel fontta "WORLD RECORD" ya da süre varsa → **S6b**.
   - Meme çerçevesi, el çizimi ok, "EPISODE nn" varsa → **S10**.
   - Sahte chat satırıyla hikâye anlatılıyorsa → **S3b**.
5. **Ortalama parlaklık çok düşük mü** (koyu alan > %50), tek bir kırmızı ya da teal vurgu ve yaratık var mı? → **S7a**.
6. **"MINECRAFT HARDCORE" logosu ya da "100 DAYS" yazısı var mı?** → **S5**. Kadrajın çoğu bir üsse aitse **S5a + S8**.
7. **Merkezde tek kahraman, çevresinde aynı zırhlı bir kalabalık radyal ya da V şeklinde dizilmiş mi?** → **S6a**.
8. **Kadrajın %70'inden fazlası tek bir yapı mı, karakter yok ya da çok küçük mü?** → **S8**.
9. **Tek karakter kadraj yüksekliğinin %60'ından fazlasını kaplıyor, arka plan koyu, sade ya da kalp desenli mi?** Ya da gerçek bir insan yüzü kesilmiş mi? → **S3**.
10. **Devasa tekrar eden kalabalık ya da yapı, sahnede tek güçlü ışık kaynağı (ışın, portal, güneş), sis var ve yazı yok mu?** → **S2**.
11. **Açık ve pastel mi, sis yumuşak mı, highlight ince mi, beyaz kontur yok mu?** → **S1**.

> [!tip] Metrik sezgileri (kaba, doğrulanmadı): S7a/S7b ortalama parlaklık < %25 · S1 parlaklık %55–75 ve orta doygunluk · S4/S9c doygunluk çok yüksek · S2 karanlık modda koyu ama tek bir çok parlak bölge (yüksek dinamik aralık). Her referanstan sonra eşikleri `references/lessons.md` notuna yaz.

### 1c. Stiller birleşir (sık görülen kombinasyonlar)
- **S5 + S8:** hardcore üs vitrini. Logo, "100 DAYS" yazısı ve büyük üs görüntüsü (Fru, disruptive builds) (gözlem).
- **S5 + S7:** hardcore korku. Karanlık yaratık, kalın başlık ve HARDCORE logosu (Forge Labs) (gözlem).
- **S4 + S9c:** çocuk kitlesine yönelik ilerleme. 3D cartoon karakterler ve 3 panel (Maizen) (gözlem).
- **S2 + S3:** Unstable/Lifesteal. Sinematik sahne ve öne çıkan karakter (Spoke, Reddoons) (gözlem).
- **S11 + herhangi biri:** Shorts bir format. Stil ayrıca seçilir.

## 2. Matris
`V` = varsayılan değerler · `D` = değiştir (karttaki ayar) · `–` = kullanma · `O` = isteğe bağlı

| Teknik | S1 | S2 | S3 | S4 | S5 | S6a | S6b | S7 | S8 | S9a | S9b | S10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 Render | V | D | V | V | D | V | – | D | D | O | V | – |
| 02 Belge | V | V | V | V | V | V | V | V | V | V | V | V |
| 03 NMS | V | D | D | D | V | D | – | D | D | – | V | – |
| 04 Sis | V | D | – | – | D | O | – | D | D | – | O | – |
| 05 Camera Raw | V | D | D | D | D | D | D | D | D | O | V | D |
| 06 Layer Style | V | D | D | O | V | D | – | D | – | – | V | – |
| 07 Elle gölge | V | D | V | O | V | V | – | D | – | – | V | – |
| 08 Renk | O | O | O | D | O | O | – | D | O | – | O | – |
| 09 Glow | V | D | D | O | D | O | – | D | D | – | O | – |
| 10 Gökyüzü/asset | O | D | O | O | D | O | – | D | D | – | O | – |
| 11 Highlight | V | D | D | V | V | V | – | D | V | – | V | – |
| 12 Export | V | V | V | V | V | V | V | V | V | V | V | V |

## 4. 2025–2026 trend durumu

### Yükselen ya da şu an baskın
| Ne | Kanıt | Kaynak |
|---|---|---|
| **S2 Unstable SMP sinematik stili** (Wemmbu, Parrot, Spoke) | YouTube araması (2026-10-01): Wemmbu 11 günde 20,3 milyon, Parrot 9 günde 6,4 milyon, Spoke 10 günde 4,6 milyon izlenme. 2026'da bu stil üzerine bir tutorial dalgası var: Toofzy 215 bin, Le_Beurre GFX 104 bin, EmixFG 65 bin, Swiffex 59 bin. | YouTube arama ve video sayfaları (§7) |
| **S1 Temiz render + NPC Studio / Thumbnailing modpack akışı** | Spare'in "CLEAN" tutorial'ı 2 ayda 194 bin. Seltop'un NPC Studio videosu (2026-05) 197 bin. Thumbnailing modpack'i yaklaşık 39 bin indirme. WEM shader yaklaşık 51 bin indirme. | YouTube, Modrinth |
| **Hazır asset yerine elle boyanmış FX** | loppy (Wemmbu'nun tasarımcısı), 2025-08 tarihli X gönderisi | X (arama özeti) |
| **S7 Korku modları** (dreamcore, liminal, stalker) | Forge Labs 1 ayda 7 milyon. ThatMob 4 ayda 2,2 milyon. Vivilly 3 ayda 734 bin. ChiefXD'nin "Dreamshift" videosu (2026-08) 202 bin. | YouTube arama |
| **"Proof of human" / otantik görünüm:** oyun içi UI, chat ve Minecraft fontlu altyazı, ham ekran görüntüsü | Gözlem: Vivilly, ThatMob, Spongs, skycrab1. Bloglara göre cilalı AI görünümü cezalandırılıyor ve otantik görseller öne çıkıyor. | bananathumbnail (2026-03), thumby (2026-05/07). **Düşük güvenilirlik.** |
| **Az yazı ya da hiç yazı yok** | Gözlem: SMP ve manhunt örneklerinden 7'si yazısız (Wemmbu, Parrot, Spoke, Dream, Baablu, Reddoons, SB737). Blog iddiası: 5 kelimelik thumbnail dönemi 2024 civarında bitti, en fazla 3 kelime. | thumby, Paddy Galloway (Creator Science podcast) |
| **"Sticker-effect" ışığı** (sıcak key light, soğuk fon, rim light) | Blog iddiası: 2026'nın baskın stili. S2 ve S3a ile örtüşüyor. | thumby (düşük güvenilirlik) |
| **S11 Shorts özel thumbnail'leri** | Özellik 2026-07-24'te YPP'ye açıldı. Dikey kapak tasarımı yeni bir iş kalemi. | YouTube Blog, YouTube Help |
| **Brainrot crossover** (çocuk kitlesi, S4 tarzında) | CASTER 7 ayda 2,5 milyon. Firelight 9 ayda 2 milyon. Kaspersky: 2025'te çocukların en çok aradığı oyun Minecraft, brainrot aramaları da üst sıralarda. | YouTube arama, Kaspersky 2025 |

### Kalıcı (evergreen, düşüşte değil)
- **S5 100 days hardcore:** son 2 haftada 300–600 bin izlenen çok sayıda yükleme var (WelcominTV, disruptive builds, Fru, Cryptozoology). Thumbnail'ler split'ten çok **üs vitrini + logo** yönünde (gözlem: 3 örneğin 2'si).
- **S4 Split/ilerleme:** Maizen'in Lv1/Lv100/Lv9999 videosu 5 günde 1,25 milyon. Ryguyrocky'nin Day 1/Day 100 thumbnail'leri hâlâ milyonlarca izleniyor.
- **S6a Manhunt:** Dream'in videosu 6 ayda 15,9 milyon. Baablu 4 ayda 1,9 milyon.
- **S9 İllüstre:** Life Series ve Aphmau kitlesi sabit. Aphmau 2026 itibarıyla 25 milyondan fazla aboneye sahip (Wikipedia).
- **S8 Build timelapse:** Timtenth'in videoları 4–9 ayda 160–490 bin.

### Eskiyen (ya da dikkatli kullanılmalı)
| Ne | Neden | Kaynak |
|---|---|---|
| **Kırmızı daire ve parlak 3D kırmızı ok** | Aşırı kullanılınca "pop" etkisi kayboluyor. 2025–26'da daha temiz thumbnail'lere geçiş var. *Not:* Grian'ın elle çizilmiş ok ve doodle'ları otantik görüntünün parçası olarak hâlâ çalışıyor (gözlem). | tjr.org.tr makalesi; allfreemockups (düşük güvenilirlik) |
| **Her şeye kalın beyaz sticker kontur + gerçek yüz** | Template siteleri bunu "reaction" şablonu olarak tanımlıyor. Bakılan 2026 SMP thumbnail'lerinde kalın beyaz kontur yok (gözlem). Yazıda kontur ise hâlâ en güvenilir teknik (1of10). | thumbs.ai, 1of10 |
| **Ağzı açık, gözleri fal taşı gibi şok yüzü** | Blog iddiası: kapalı ağızlı, kararlı ifade %15–20 önde. Çocuk ve reaction kanallarında (Preston) hâlâ kullanılıyor. | thumby (düşük güvenilirlik); 1of10 gaming: "gaming hâlâ fayda görüyor" |
| **5 kelimeden uzun yazı ve sağ alt köşede yazı** | Süre rozetiyle çakışıyor. Mobilde okunmuyor. | 1of10 (2026-05), thumby |
| **Tamamen AI ile üretilmiş thumbnail** | ViewStats'in AI thumbnail aracı Haziran 2025'te tepki üzerine geri çekildi. Blog iddiası: yaratıcıların %47'si AI thumbnail kullanmayı bıraktı (Social Blade anketi; doğrulanmadı). | Newsweek ve Fast Company başlıkları (arama özeti), uppbeat, bananathumbnail |
| **2016–2020 tarzı düz Mine-imator render + lens flare + ham ekran görüntüsü** (Dream SMP dönemi) | Bugünün SMP standardı NPC Studio + NMS/DMS post-prodüksiyonu ya da S2 sinematik sahne. Ham ekran görüntüsü artık sadece **bilinçli** lo-fi tercih olarak (S6b, S7b, S10) işe yarıyor. | Gözlem (TommyInnit 2020 ve 2026 örnekleri karşılaştırıldı), tutorial tarihleri |

## 5. Her siparişte sorulacak genel brief soruları (stil tespiti için)
1. Video türü ne (SMP, hardcore, challenge, korku, build, speedrun, meme, short)? Başlık ne?
2. Kanalın son 3–5 thumbnail'i neye benziyor (tutarlılık)? Beğendiğin 1–3 referans hangileri?
3. Karakter kaç tane? Skin dosyaları var mı? Gerçek yüz fotoğrafı kullanılacak mı?
4. Duygu ya da anlatılacak an ne (tek cümle)?
5. Yazı olacak mı? Olacaksa en fazla 3 kelime, ne yazacak?
6. Parlak mı karanlık mı olsun, palet tercihi var mı (kanal rengi)?
7. Render mı, çizim mi, ham ekran görüntüsü mü?
8. Format 16:9 mu, 9:16 mı, ikisi birden mi?
9. Hedef kitle yaşı (çocuk, genç, yetişkin)? Kan ve şiddet sınırı?
10. Teslim süresi ne? S9 çizim ve S2 elle FX daha uzun sürer.

## 6. Görsel olarak incelenen örnekler (kanıt tablosu)
2026-10-01 tarihli YouTube arama sonuçlarından. `https://i.ytimg.com/vi/<id>/hqdefault.jpg` adreslerine bakıldı. Görseller kaydedilmedi ve vault'a konmadı.

| Video ID | Kanal | Stil | Kısa gözlem |
|---|---|---|---|
| 5hG_nAYEC2g | Wemmbu | S2a | Karakter omzunun üstünden ve kesik, elmas zırhlı yüzlerce NPC, aurora ve şato, mor/camgöbeği, yazı yok |
| BWmWZTDxFrk | Parrot | S2b | Yeşil sis, sıcak ışık sütunu, karakter arkadan ve küçük, yazı yok |
| IOS7FKtiyxE | Spoke | S2a/S1 | Karakter yakın planda solda, mor ordu, altın saray, mavi gökyüzü, yazı yok |
| OF4Sw5RMppY | Forge Labs | S7a+S5 | Kırmızı-siyah yaratık, kıvılcımlar, beyaz kalın başlık ve HARDCORE logosu |
| 3OOWMv_qJNQ | Vivilly | S7b | POV, hotbar, Minecraft fontunda altyazı, gerçekçi ürkütücü yüz |
| O-JmwIA10c8 | ThatMob | S7b | Gece, pencerede gerçekçi yüzlü ay, Minecraft fontunda altyazı |
| 7bamisfVKuY | ChiefXD | S7c | Parlak vanilla, dev çukur, 3 karakter arkadan bakıyor, yazı yok |
| XdwhKeUyiko | Ryguyrocky | S4 | Day 1 yağmurlu ve ağlayan solucan / Day 100 dev solucan, logo ve "WORM" |
| qqOu2XoK7PI | Fru | S5a+S8 | Üs iç mekânı, HARDCORE logosu ve "100 DAYS" |
| JeFiVma1HmI | disruptive builds | S5a+S8 | Karlı üs, sıcak pencereler, logo ve "100 DAYS" |
| 8Ir5YsJib_U | Maizen | S4+S9c | 3 panel Lv1/Lv100/Lv9999, kırmızı başlık bantları |
| dD7UX02eIiA | CASTER | S4 | Brainrot karakteri, kırmızı kavisli ok, petek şeklinde yapı, HARDCORE logosu |
| E_RXOSNzztg | Grian | S10b | Ham ekran görüntüsü, sarı el çizimi ok ve "!!", "EPISODE 28" |
| 10OJhIc_-vw | Dream | S6a | Koşucu ortada, avcılar V düzeninde, yazı yok |
| 073Dnsn3sI0 | Baablu | S6a | Kuş bakışı, radyal sütunlar, merkeze doğru hız çizgileri |
| NemhyWVAY68 | skycrab1 | S6b | Stronghold ekran görüntüsü, piksel fontta "WORLD RECORD 6:39" |
| pgNABQnWqQ4 | SB737 | S3a | Karakter belden yukarı ve ortada, karanlık fon, kalp sırası, kıvılcımlar |
| 28XHJlkaGqk | Reddoons | S3a+S2 | Karakter ortada, kırmızı klonlar, kalp deseni, kırmızı aura |
| y96G4GS0XMU | Spongs | S3b | Sahte chat satırı, boyanmış gülümseme, birinci şahıs kılıç |
| BMhvBRAOCzc | PrestonPlayz | S3d | Gerçek şaşkın yüz solda, mob'lar ve kalp barları |
| SLshNWUwQdg | Timtenth_Buildings | S8 | Uzay gemisi, küçük astronot, piksel fontta "36 MILLION BLOCKS" |
| eTugHI2Sfp4 | GoodTimesWithScar | S8+S3 | Galaksi build'i ve büyük, düz ışıklı skin yüzü |
| 4Op5N92yl24 | Not Safe | S10a | Demotivational çerçeve ve "HOW" |
| cITT748zAgs | Two Much Grian | S9a | Tam 2D illüstrasyon, radyal fon, Wild Life logosu |
| Qlk8frPSoiQ | Aphmau | S9b | Render ve boyanmış öfkeli anime gözler, mezar taşları |
| b7nTzE51Ybw | TommyInnit (2020) | Tarihsel | Ham vanilla ekran görüntüsü, yazı ve kontur yok |
| 5XbxbzdN0x0 | Spare | S1 | Mavi/mor temiz render, karakterde mavi glow |
| vNusKe4cAOo (Short) | – | S11 | Video karesi ve üstte siyah bantta TikTok tarzı başlık |

## 7. Kaynaklar

**Stil, nişe göre palet ve tipografi**
- 1of10, Minecraft Thumbnail Maker (2026-01-23): niş bazında renkler ve ipuçları: <https://1of10.com/blog/minecraft-thumbnail-maker-how-to-create-viral-minecraft-thumbnails-with-ai/>
- 1of10, YouTube Thumbnail Design (2026-05-01): yazı konturu 4–8 px, güvenli alanlar, 4.5:1 kontrast: <https://1of10.com/blog/youtube-thumbnail-design/>
- 1of10, 7 types of thumbnails (2025-05-27): before/after ve versus tipleri: <https://1of10.com/blog/types-of-thumbnails-for-youtube/>
- 1of10, Gaming thumbnail (rim light, gaming'de şok yüzü): <https://1of10.com/blog/gaming-thumbnail-maker/>
- Paddy Galloway, Creator Science podcast (1–3 odak, 2–4 kelime): <https://podcast.creatorscience.com/paddy-galloway/>
- launchlens, 100 Days şablonu (Day 1/Day 100 split kuralı, yırtık kâğıt veya şimşek ayırıcı): <https://launchlens.tech/templates/minecraft-100-days-hardcore>
- thumbs.ai, Minecraft şablon tipleri (reaction: kalın beyaz kontur + kırmızı daire): <https://www.thumbs.ai/minecraft-thumbnail> *(düşük güvenilirlik)*
- vuki, Minecraft thumbnail designer portfolyosu (sinematik ve enerjik ayrımı): <https://vukidesign.netlify.app/>
- CherriFire portfolyosu (Grian ve InTheLittleWood thumbnail'leri, "full renders" illüstrasyon): <https://cherriportfolio.carrd.co/>
- Life Series Thumbnail Artists listesi (fandom, arama özetinden): <https://the-life-series.fandom.com/wiki/Thumbnail_Artists>
- loppezz (Wemmbu'nun thumbnail'leri): <https://lifesteal.fandom.com/wiki/Loppezz> (arama özeti) · X gönderisi: <https://x.com/loppezzpuff/status/1959995206117609605>

**Tutorial videoları (başlık, kanal, tarih)**
- Spare, "How to Make CLEAN Minecraft Thumbnails (Free)", 2026-08: <https://www.youtube.com/watch?v=5XbxbzdN0x0>
- Toofzy, "How to Make Thumbnails Like Wemmbu", 2026-03: <https://www.youtube.com/watch?v=Dewf7Y9WbH4>
- Le_Beurre GFX, "How To Make The BEST Minecraft Thumbnails (FREE)!", 2026-05: <https://www.youtube.com/watch?v=XuMTUEVv8CY>
- EmixFG, "How To Make Wemmbu Style Thumbnails", 2026-07: <https://www.youtube.com/watch?v=RusmdblgEt4>
- Ryuvair, "How to Make Thumbnails Like Wemmbu (Full Tutorial)", 2026-03: <https://www.youtube.com/watch?v=qaoHgt876Ng>
- Swiffex, "How To Make Unstable SMP Thumbnails For Free", 2026-03: <https://www.youtube.com/watch?v=IXVwYGiyrVY> · "How To Make Minecraft SMP Thumbnails For Free", 2025-12: <https://www.youtube.com/watch?v=m1FHOH81qno>
- ToofzyTwo, "How To Make Thumbnails Like Parrot and Wemmbu", 2025-06: <https://www.youtube.com/watch?v=M9NqK1E2S_U>
- Seltop, "This Mod Is Changing Minecraft Thumbnails Forever" (NPC Studio), 2026-05: <https://www.youtube.com/watch?v=j3lGA7y5b9o> · "The Best effect for Horror Thumbnails!", 2025-03: <https://www.youtube.com/watch?v=rNTXbrJgLaE>
- zestu's studio, "How To Make SCARY Minecraft Thumbnails", 2024-11: <https://www.youtube.com/watch?v=_kApHc_tb50> · "How To Make Minecraft Thumbnails Like Chiefxd", 2025-09: <https://www.youtube.com/watch?v=Wa3cxVf5wns> · "How to make thumbnails like ChiefXD", 2026-03: <https://www.youtube.com/watch?v=SB92YKsB7lw>
- gfxrhino, "How To Make Minecraft Thumbnails (From Start To Finish)", 2026-07: <https://www.youtube.com/watch?v=WhPVxNHOjA8>
- Nebular, "How To Make THE BEST Minecraft Thumbnails [2026]" (SB737 ve Seapeekay için çalışmış): <https://www.youtube.com/watch?v=uVg0hR0uUS4>
- ItsProger, "How to make THE BEST Minecraft Thumbnails", 2024-11: <https://www.youtube.com/watch?v=id4J7qYKlD4>
- Schxnappi_, "How to make the BEST Minecraft Thumbnails (Bedwars, SMP, Horror, ...)", 2025-02: <https://www.youtube.com/watch?v=zGVLm-9RM6I>
- korbann, "The EASIEST Way To Make Minecraft Thumbnails" (Procreate, Nomad Sculpt, Blockbench), 2026-08: <https://www.youtube.com/watch?v=5DNIb5YdfSA>
- th3pooka, "How to make a Minecraft thumbnail in Blender - Beginner", 2025-07: <https://www.youtube.com/watch?v=Sw4k1I5Eh5o>
- lowresbonus, "How to Make Minecraft Thumbnails", 2024-07: <https://www.youtube.com/watch?v=OAASCid1SyE>
- Skullk, "How to draw Minecraft Characters!" (cartoon, 2016): <https://www.youtube.com/watch?v=D0lldbsYzpQ>
- SammyGreen, "how i make my thumbnails" (PvP/Bedwars, 2020): <https://www.youtube.com/watch?v=Ozgwn4agXxo>
- Metricate, "How I Make My 100 Days in HARDCORE Minecraft Videos" (2021; LTN formatın fikir sahibi): <https://www.youtube.com/watch?v=o2tlvH4B3Ts>
- Kingy AI, "How To Create White Outline On Images" (Stroke Outside ~30 px, genel thumbnail): <https://www.youtube.com/watch?v=BHxVoAAqjy4>

**Araçlar ve modlar**
- Thumbnailing modpack (mangofx; NPC Studio, Voxy, DMS, NMS, WEM, BDS): <https://modrinth.com/modpack/thumbnailing>
- WEM, White Entities Mask: <https://modrinth.com/shader/wem-white-entities-mask>
- Flashback (Wemmbu tarzında kullanılıyor): <https://modrinth.com/mod/flashback>
- Just Expressions resource pack: <https://modrinth.com/resourcepack/just-expressions>
- Photopea learn (layer styles: stroke, outer glow, drop shadow, bevel): <https://www.photopea.com/learn/layer-styles> · <https://www.photopea.com/learn/adjustments-filters> · arka plan blur'u: <https://www.photopea.com/tuts/blur-the-image-background-online/>

**Platform kuralları ve Shorts**
- YouTube Help, özel thumbnail (Shorts 9:16, 2160x3840, 50 MB, doğrulanmış hesap, masaüstü): <https://support.google.com/youtube/answer/72431>
- YouTube Blog, Shorts için özel thumbnail (2026-07-24, YPP): <https://blog.youtube/news-and-events/youtube-studio-custom-thumbnail-updates/>
- creatortoolly, Shorts thumbnail 2026: <https://creatortoolly.com/youtube-shorts-custom-thumbnails/>

**Trend, otantiklik ve AI**
- thumby, YouTube Thumbnail Trends 2026 (2026-05, güncelleme 2026-07): <https://thumby.app/en/blog/youtube-thumbnail-trends-2026> *(düşük güvenilirlik)*
- bananathumbnail, 2026 Thumbnail Trends (2026-03): <https://blog.bananathumbnail.com/2026-thumbnail-trends/> *(düşük güvenilirlik)*
- uppbeat, "Are AI thumbnails putting viewers off": <https://uppbeat.io/blog/creator-questions/are-ai-thumbnails-putting-viewers-off-your-videos>
- Newsweek, MrBeast'in ViewStats AI aracını geri çekmesi: <https://www.newsweek.com/mrbeast-youtube-video-ai-thumbnail-tool-viewstats-2091432> (arama özeti)
- Kırmızı daire ve ok üzerine: <https://tjr.org.tr/the-red-circle-with-arrow-why-your-brain-cant-stop-clicking-on-clickbait-thumbnails-6lj>
- Kaspersky, çocuk raporu 2025 (Minecraft ve brainrot aramaları): <https://www.kaspersky.com/blog/kids-report-2025/>
- Wikipedia: Minecraft Manhunt (Dream'in thumbnail ve SEO stratejisi): <https://en.wikipedia.org/wiki/Minecraft_Manhunt> · Aphmau: <https://en.wikipedia.org/wiki/Aphmau>
- McServ, Lifesteal SMP rehberi 2026: <https://mcserv.org/blog/what-is-lifesteal-smp-minecraft-complete-guide-2026>
- PlanetMinecraft, promo art render stili (bloom, motion blur): <https://www.planetminecraft.com/blog/minecraft-render-promo-art-style/> (arama özeti)

**Erişilemeyenler:** reddit.com (r/NewTubers, r/Minecraft) araç tarafından engellendi. vidIQ blog ve şablon sayfaları ile Fast Company 403 hatası verdi. Fandom sayfaları 402 hatası verdi, sadece arama özetinden kullanıldı.
