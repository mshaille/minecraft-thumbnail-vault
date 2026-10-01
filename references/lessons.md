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
  - Sağ panelde **odak çizgileri**: kadraj kenarından yakın karakterin kafasına doğru sivrilen ince beyaz üçgenler, karakterlerin arkasında. Ayırıcının yanında beyaz parlama. Sol arka plan hafif bulanık ve sisli.
  - Efekt kutusu oyundakinden dar (~96 oyun pikseli, yazıya göre) ve büyük ölçekli (6,0 px/oyun pikseli @1280).

## Testten dersler
- Kural: **ÜŞENGEÇLİK YOK.** İlk kenar denemesi tek bir beyaz çizgiydi. Ölçünce kenarın 3 katman olduğu çıktı (dış koyu bant, mavimsi beyaz kontur, içte ışık/gölge şeridi). Ayrıca karakterler fazla soluktu, gökyüzü referanstan çok açıktı, kutu küçüktü ve karakterler yanlış yerdeydi. Hepsi **ölçülerek** düzeltildi: `remap` ile renk eşleme, `place_fit` ile referans konumu, `outline` ile kenar.
- Plan çıkarıp bırakmak yetmez. Render varsa taslağı `tools/thumbkit.py` ile üret ve referansla `tools/compare.py` ile ölçerek kontrol et.
- Efektin **yönü** de ölçülür: hız çizgileri ilk taslakta sol alttan dışa yayıldı, referansta odağa doğru sivriliyordu. Kullanıcı ilk bakışta fark etti.
- UI boyutu oyun pikseli ölçeğinden ölçülür (harf yüksekliği 7 oyun pikseli). Gözle "aynı genişlikte" yapılan kutu, referanstan %25 küçük ölçekli çıktı.
- Referans gelmeden tasarıma başlama; render'ları sadece katalogla ([Sipariş akışı](../guides/order-workflow.md)).
- Analizde ilk bakışta kaçanlar: karakterlerin etrafı (kontur), katman sırası, UI'nin düz mü 3D mi olduğu, hız çizgilerinin stili.

## Videolardan gelen varsayılanlar (referans eklenene kadar)
- Palet: açık mavi ortam (#c7e8ff civarı) + mor vurgu → [Spare](../sources/spare-clean-thumbnails.md)
- Karakteri ortam rengiyle "boyamak": Gradient Overlay + Inner Glow + Inner Shadow, hepsi Overlay → [Ortam ışığı](../techniques/06-layer-style-ambient-light.md)
- İnce, karakterin içinde kalan ve uçları sivrilen highlight'lar, katman Overlay → [Highlight](../techniques/11-highlights.md)
