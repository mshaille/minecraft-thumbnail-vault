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

## Minecraft isim etiketi (Nebular)
- Yarı saydam siyah dikdörtgen. Kesin opaklık ekranda okunamadı; ~%25–40 ile başla.
- Font: Minecraft tarzı bir piksel font (videoda Minecraftia), faux bold, tracking 60, dikey %110 / yatay %103.
- Drop Shadow: Normal, siyah, %69, 135°, Distance 13 px, Size 0. Bu, oyundaki sert yazı gölgesini taklit eder.
- Etiketi karakterin kafa eğimine göre döndür.

Kaynaklar: [Schxnappi_](../sources/schxnappi-layer-styles-text.md) · [Nebular](../sources/nebular-sb737-action-thumbnail.md)
