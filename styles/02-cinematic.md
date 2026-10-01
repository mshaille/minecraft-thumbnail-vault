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
