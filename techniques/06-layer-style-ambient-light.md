---
type: teknik
order: 6
title: Layer Style ile karakteri ortama oturtma
sources: [spare-clean-thumbnails]
tags: [teknik, layer-style, rim-light]
status: stabil
---
# 6. Layer Style ile karakteri ortama oturtma

Amaç: gökyüzü/ortam renginin karakterin kenarlarına "sızması". Böylece karakter sahneye sonradan yapıştırılmış gibi değil, sahnenin içindeymiş gibi durur. Ayarlar kişisel tercih, sahneye göre oynanır.

Oyuncu katmanına çift tıkla → **Layer Style**:

| Efekt | Ayarlar |
|---|---|
| **Gradient Overlay** | Blend **Overlay**, Opacity **~%19**, gradient **griden açık maviye** (Gradient Editor'da orta nokta ~%29), Style **Linear**, Align with Layer ✓, Angle **−120°**, Scale **%31**, Method Perceptual |
| **Inner Glow** | Blend **Overlay**, Opacity %100, Noise 0, renk **açık mavi**, Technique **Softer**, Source **Edge**, Choke 0, Size **~90 px**, Range %50, Jitter 0 |
| **Inner Shadow** | Blend **Overlay**, renk **açık mavi**, Opacity %100, Angle 90° (Use Global Light ✓), Distance 0, Choke **~%9**, Size **~57 px**, Noise %2 |

- Aynı stil 2. oyuncuya kopyalanıyor (sağ tık > Copy/Paste Layer Style). Kalabalık katmanına 2 adet Inner Shadow ekleniyor.
- Sonradan oyuncu 1'in efekt listesinde Drop Shadow da görünüyor ama ayarı videoda gösterilmedi.
- Değerler videoda birkaç kez değişti. Tabloda ekranda kalan son değerler var.

> [!tip] Bu preset karakteri sahneye **oturtur** (yumuşak, temiz render tarzı). Yüksek enerjili SMP/aksiyon tarzında karakteri sahneden **koparan** preset'ler için: [Karakteri öne çıkarma](character-pop.md).

Önceki: [Camera Raw](05-camera-raw.md) · Sonraki: [Elle gölge](07-hand-shadows.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (9:42–10:57)
