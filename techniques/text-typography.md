---
type: teknik
title: Yazı (3D başlık ve isim etiketi)
sources: [schxnappi-layer-styles-text, nebular-sb737-action-thumbnail]
tags: [teknik, yazi, stroke, layer-style]
styles: [smp-action, challenge]
status: stabil
---
# Yazı (3D başlık ve isim etiketi)

Yazı kullanılacaksa kısa olmalı: 0–4 kelime, başlığı tekrar etmemeli, sağ alt köşeye konmamalı ([Dikkat edilecekler](../guides/pitfalls.md)).

## Kalın 3D başlık (Schxnappi_)
1. Font: kalın, sıkışık (condensed) bir yazı tipi, beyaz. Videoda **Burbank Big Condensed** kullanılıyor. Bu ticari bir fonttur; lisans al ya da ticari kullanıma izin veren bir benzerini seç. **Minecraft logo fontunu kullanma.**
2. Yazı katmanına:
   - Drop Shadow: Normal, açık gri (~#9c9c9c), %100, 90°, Distance ~19 px, Size 0. Bu, aşağı doğru gri bir "kalınlık" verir.
   - Gradient Overlay: açık griden beyaza.
   - Inner Glow.
3. Yazıyı **Ctrl+G** ile gruba al. Gruba **Stroke 13 px, Outside, Normal, %100, siyah** ve Multiply bir Drop Shadow ekle. Grup üzerindeki kontur, harflerle gri kalınlığı tek parça gibi sarar.
4. Alt yazı: aynı grup konturu ve Outer Glow Overlay %35, Size 92 px.

## Oyun içi efekt kutusu (ör. "Yükselme X / 00:21")
Envanterdeki iksir/efekt kutusunu **oyunun kendi dosyalarıyla** üretir: piksel font (Türkçe harfler dahil), kutu ve efekt ikonu kurulu oyunun client `.jar` dosyasından okunur, repoda Mojang dosyası tutulmaz.
```bash
python3 tools/mc_effect_box.py --jar <client.jar> --name "Yükselme X" --time 00:21 --icon levitation --scale 8 -o kutu.png
```
- Efektin **resmi adını uydurma**: oyunun dil dosyasından al. Örnek: `tr_tr.json` → `effect.minecraft.levitation` = "Yükselme", `enchantment.level.10` = "X". Dil dosyası asset index'inde `minecraft/lang/tr_tr.json`.
- Taban boyut oyunda 120x32. Thumbnail'larda kutu çoğu zaman **yazıya göre** daraltılmış: Levitation referansında ~96 oyun pikseli. `--width 95` (0 = yazıya göre). `--scale` ile tam sayı katına büyüt (Nearest Neighbor).
- **Ölçeği referanstan ölç:** oyun yazısının harf yüksekliği 7 oyun pikselidir. Levitation referansında "L" 42 px (1280'de) → 6,0 px/oyun pikseli → 2000 px'lik tuvalde 9,4 px. İlk taslak 7,5 px ile küçük kaldı, kullanıcı "azcık büyüt" dedi.
- **3D levha** (`thumbkit.slab_3d`): referansta üst kenar −1,55°, alt kenar −2,7° (sol taraf yakın, daha yüksek). Karşılığı `slab_3d(flat, depth=10, tilt=1.3, persp=(4, 14, 10))`, beyaz dış kontur 4 px, hafif gölge (siyah %35, blur 10, +10/+12 px).
- **Yerleşim:** yakın karakterin ayağı kutunun üst kenarına, ikonun üstüne ve yazının hemen soluna biner (kutu ayağın **arkasında**). Kutuyu referanstaki kutunun merkezine oturt. Referanstaki gibi sağ alta yakın durursa süre etiketiyle çakışma riskini teslimde yaz.
- İkon adları: `textures/mob_effect/<ad>.png` (levitation, speed, strength, regeneration…).
- Font notu: yeni sürümlerde `font/default.json` sadece `reference` sağlayıcıları içerir (`include/space`, `include/default`, `include/unifont`); bitmap'ler (`ascii.png`, `accented.png`) bunların içindedir. Araç bunları özyinelemeli çözer. Harf ilerlemesi = en sağdaki dolu sütun + 1, boşluk 4, yazı gölgesi renk/4 ve +1,+1. Süre satırı y=16, renk 0x7F7F7F.
- Dil dosyası yeri: `.minecraft/assets/indexes/<sürüm>.json` içinde `minecraft/lang/tr_tr.json` → hash → `assets/objects/<ilk 2 karakter>/<hash>`.

## Minecraft isim etiketi (Nebular)
- Yarı saydam siyah dikdörtgen. Kesin opaklık ekranda okunamadı; ~%25–40 ile başla.
- Font: Minecraft tarzı bir piksel font (videoda Minecraftia), faux bold, tracking 60, dikey %110 / yatay %103.
- Drop Shadow: Normal, siyah, %69, 135°, Distance 13 px, Size 0. Bu, oyundaki sert yazı gölgesini taklit eder.
- Etiketi karakterin kafa eğimine göre döndür.

Kaynaklar: [Schxnappi_](../sources/schxnappi-layer-styles-text.md) · [Nebular](../sources/nebular-sb737-action-thumbnail.md)
