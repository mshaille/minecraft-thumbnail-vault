---
type: tarz
code: S2
title: "Sinematik / dramatik ışık ("Unstable SMP" epik stili)"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S2 — Sinematik / dramatik ışık ("Unstable SMP" epik stili)

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Film karesi gibi kurulan bir sahne: ölçek kontrastı, tek baskın ışık kaynağı, atmosfer. 2025–2026'nın en görünür SMP stili. İki ışık modu var:
- **S2a parlak epik** (Wemmbu, Spoke): mavi gökyüzü, devasa ordu ya da şato, doygun renkler.
- **S2b karanlık-moody** (Parrot): yeşil ya da teal sis, god-ray, karakter küçük ve arkadan görünüyor.

**Görsel özellikler (gözlem: Wemmbu, Parrot, Spoke)**
- *Kompozisyon:* küçük bir kahraman karşısında dev bir yapı ya da ordu. Karakter çoğu zaman kadrajın sol kenarında ve alttan kesik: ya omzunun üstünden (arkası dönük) ya da yakın ve kameraya dönük görünüyor. Yüzlerce NPC tekrar ediyor (NPC çoğaltma).
- *Palet:* S2a'da tamamlayıcı çiftler (mor/camgöbeği, altın/mor) ve yüksek doygunluk. S2b'de yeşil-siyah sis ve sıcak sarı ışık sütunu.
- *Işık:* sahnede tek bir güçlü kaynak var (ışık sütunu, portal, aurora, güneş). Volumetrik sis, karakterde rim light.
- *Kontur/glow:* sticker kontur yok. Silah ve büyüde glow var, ışık kaynağı Screen/Add ile parlatılmış.
- *Yazı:* **yok**. Bakılan 3 Unstable SMP thumbnail'inin hiçbirinde yazı yok (gözlem).
- *Arka plan:* uzak dağlar ya da yapılar haze ile soluyor. Gökyüzü değiştirilmiş (aurora, fırtına).
- Üst seviye tasarımcılar efektleri **elle boyamaya** geçiyor. Wemmbu'nun tasarımcısı loppezz/loppy, Ağustos 2025'te bir nükleer patlamayı hazır asset kullanmadan elle çizdiğini paylaştı.

**Örnek kanallar:** Wemmbu (thumbnail ve replay çekimleri: loppezz), ParrotX2, Spoke, FlameFrags. Lifesteal SMP kanalları da bu stile kayıyor.

**Tutorial'lar:** "How to Make Thumbnails Like Wemmbu" (Toofzy, 2026-03, 215 bin izlenme; Flashback modu + Photoshop/Photopea), Le_Beurre GFX ("dramatic lighting, cinematic poses" tarifi, 2026-05), EmixFG (2026-07), Swiffex (Unstable SMP, 2026-03), ToofzyTwo (2025-06).

**Mevcut teknikler: nasıl değişir**
| Teknik | S2'de ayar |
|---|---|
| [01 Render](../techniques/01-render-prep.md) | Kamera için Flashback ya da Replay Mod. Uzak arazi için Voxy ya da Bobby. Kalabalık NPC Studio'nun Duplicate özelliğiyle çoğaltılır. |
| [03 NMS](../techniques/03-nms-shading.md) | Gölge siyah katmanı %18 yerine **%25–40**. Işık katmanı beyaz yerine **ışık kaynağının rengi** (sıcak #ffd9a0 ya da aurora yeşili), Overlay %15–25. |
| [04 Sis](../techniques/04-depth-map-fog.md) | S2a: açık haze, Curves 86→**150–170** (ölçek hissi). S2b: Solid Color **koyu teal/yeşil (#2e4038–#3d5a4c)**, Curves 86→140–160, üstüne ışık sütunu (N7). |
| [05 Camera Raw](../techniques/05-camera-raw.md) | Contrast +20…+35 · Clarity +15…+25 · Dehaze S2a'da +5…+15, S2b'de −5…−15 · HSL artışı sahnenin 2 baskın tonuna · Color grading (N15). |
| [06 Layer Style](../techniques/06-layer-style-ambient-light.md) | Inner Glow rengi sahnenin **anahtar ışığının rengi**, Size 60–120 px. S2b'de Inner Shadow koyu (Multiply %30–50). |
| [07 Elle gölge](../techniques/07-hand-shadows.md) | Opacity %62 yerine **%70–85**. |
| [09 Glow](../techniques/09-glow.md) | Silah, büyü ve ışık kaynağı. Linear Dodge, iki katman (çekirdek küçük, hale büyük). |
| [10 Gökyüzü/asset](../techniques/10-sky-and-assets.md) | Aurora, fırtına, ışık sütunu. Lens flare Screen. |
| [11 Highlight](../techniques/11-highlights.md) | Overlay yerine **Normal %100**, 4–6 px, ışık kaynağı tarafında sıcak renkte. |

**Gereken yeni teknikler:** N7 god rays, N12 elle boyanmış FX, N3 ön plan lens blur (isteğe bağlı), N5 vinyet (S2b'de −25…−45), N9 partikül, N15 renk grading.

**Brief soruları**
- Hikâyenin anı ne (savaş öncesi, kaçış, keşif)?
- Parlak epik mi olsun, karanlık moody mi?
- Ölçek nasıl gösterilecek: ordu mu, şato mu, dev yaratık mı?
- Karakter kameraya mı baksın, arkası mı dönük olsun?
- Yazısız thumbnail kabul mü?
- Kanalın sabit bir renk çifti var mı?

**Referansta tanıma ipuçları:** tekrar eden yüzlerce figür ya da dev bir yapı · karakter kadraj kenarında ve kesik · sahnede tek, çok parlak bir ışık kaynağı ve onu çevreleyen sis · yazı yok · S2b'de köşeler koyu · gerçekçi gökyüzü efektleri (aurora, god-ray).

## Doğrulanmış değerler (Trim klanı, S2b, 2026-10-03)
Referans: solda yakın plan karakter (kesik), sağda 5 kişilik zırhlı klan + 2 ghast, karanlık mağara, sağ üstte limon parlama. Bu iş Nether'de yapıldı; değerler 1280 px'e göre.
| Öğe | Ölçülen (ref) | Uygulanan |
|---|---|---|
| Genel | parlaklık %25, doygunluk %63 | %24 / %54 |
| Ortam | doygunluk 0,15–0,26, uzak L 35, üst L 46 | doygunluk ×0,5, koyu sıcak pus (curve 0,8, en fazla %45) |
| Sol yakın duvar | L 26 → kenara 30 px kala 45 → kenarda 72, ışık kaynağının renginde | ×0,27 + lav renginde kenar ışığı |
| Sol karakter | sol V 0,45, sağ V 0,59, sağ kenarda ~40 px içe doğru artan kenar ışığı; kontur yok | ışık × yüzey rengi, kenar ışığı yüzey rengiyle çarpılır |
| Işıyan trim | hale 1/2/4/6/8 px: %62/44/26/17/10 | `thumbkit.bloom` varsayılanı ([09 Glow](../techniques/09-glow.md)) |
| Ghast | yüz L 177, kontur yok | ×0,70 |
| Işık kaynağı | sağ üst köşe L 78, ~50 px geniş hale | lav ×1,9 + bloom σ 3/22/70 |

**Sinematik geçiş (kullanıcı: "ortam çok düz, normal resimden ayıran bir şey yok").** Referans ölçülerine eşlenmiş ilk taslak düz bulundu. Eklenenler (değerler 1280 px'e göre, `thumbkit`):
| Katman | Değer |
|---|---|
| N3 alan derinliği | odak klan (DMS 0,94), uzak 0,45'te σ 3,5 px; 5 px'te Nether dokusu kayboldu. Klandan yakın kökler σ 3,5 px bulanık katman olarak üstte. Ghast'lar σ 0,6 px. |
| Lav kenar ışığı | klan ve ghast'larda lava bakan kenarlar (ışık sağ üstten), ~3 px şerit, yüzey × (1 + lav rengi × 1,4) |
| N7 huzme | lav + parlak sağ arka plan, zoom 0,9, Screen × lav rengi × 1,2; karakterlerden önce |
| N9 partikül | 150 kızıl/turuncu spor (0,8–2,2 px, %35'i lava yakın) + 9 bokeh (9–18 px, %10–22, blur 3) |
| N15 grading | gölge ×(0,88; 1,0; 1,14), ışık ×(1,07; 1,0; 0,88) |
| N5 vinyet | %38, yakın plan kahraman muaf |
