---
type: ozet
title: Referanslardan öğrenilenler
tags: [referans, ozet]
updated: 2026-10-01
---
# Referanslardan öğrenilenler

Skill'in "hafızası" bu not. Her referans eklendiğinde tekrar eden kalıplar buraya yazılır. Örnek: "7 favorinin 5'inde turuncu/camgöbeği palet + beyaz kontur + üstte yazı". Yeni thumbnail planlanırken Claude ilk bu notu okur.

## Tekrar eden kalıplar
- **Split "önce→sonra" (Levitation testi, 2026-10-01):**
  - Karakterlerin hepsinde ince beyaz kontur (~5 px @2000), kalın sticker değil.
  - UI kutusu yakın karakterin bacağının **arkasında**. Kutu 3D levha gibi: sol-alta kalınlık, beyaz dış kontur, hafif eğim.
  - Sağ panelde ince ve sivri hız çizgileri, ayırıcının yanında beyaz parlama. Sol arka plan hafif bulanık ve sisli.

## Testten dersler
- Plan çıkarıp bırakmak yetmez. Render varsa taslağı `tools/thumbkit.py` ile üret ve referansla yan yana kontrol et.
- Analizde ilk bakışta kaçanlar: karakterlerin etrafı (kontur), katman sırası, UI'nin düz mü 3D mi olduğu, hız çizgilerinin stili.

## Videolardan gelen varsayılanlar (referans eklenene kadar)
- Palet: açık mavi ortam (#c7e8ff civarı) + mor vurgu → [Spare](../sources/spare-clean-thumbnails.md)
- Karakteri ortam rengiyle "boyamak": Gradient Overlay + Inner Glow + Inner Shadow, hepsi Overlay → [Ortam ışığı](../techniques/06-layer-style-ambient-light.md)
- İnce, karakterin içinde kalan ve uçları sivrilen highlight'lar, katman Overlay → [Highlight](../techniques/11-highlights.md)
