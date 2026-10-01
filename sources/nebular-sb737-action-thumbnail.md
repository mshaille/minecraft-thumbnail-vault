---
type: kaynak
title: How To Make THE BEST Minecraft Thumbnails [2026]
creator: Nebular
url: https://www.youtube.com/watch?v=uVg0hR0uUS4
duration: "21:02"
watched: "tamamı (transkript), 6:37–19:00 Photoshop kısmı kare kare"
watched_on: 2026-10-01
tags: [kaynak, video, smp, yuksek-enerji, aksiyon, layer-style]
---
# Nebular — How To Make THE BEST Minecraft Thumbnails [2026]

- Video: <https://www.youtube.com/watch?v=uVg0hR0uUS4> (yayın 31.10.2024)
- Anlatıcı SB737, SolidarityGaming gibi kanallara thumbnail yapıyor. Stil: **SB737 / Lifesteal SMP aksiyon kapağı**. Örnekte SB737 mace ile zıplayıp ClownPierce'a vuruyor. Parlak gökyüzü, doygun zırh renkleri, Minecraft isim etiketi, hız çizgileri var.
- Program: Photoshop. Açıklamada Photopea alternatif olarak geçiyor, PSD linki açıklamada.
- Render: Taterzens NPC modu + Replay Mod (shader yok). Item'lar için Mine-imator veya Sketchfab modeli.

## Zaman damgası → teknik notu
| Zaman | Konu | Not |
|---|---|---|
| [0:09](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=9s) | Önce stil seç | Kategoriyi ara, hangi kanala/stile göre yapacağına karar ver |
| [1:20](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=80s) | NPC kurulumu | `npc create`, `npc edit pose crouching`, `npc edit look` (NPC hep kameraya baksın). Elde olmayan item yerine **çubuk** tut, Photoshop'ta değiştir |
| [3:00](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=180s) | Replay Mod kamera | Aksiyon için **FOV 30–50** (örnekte **34**), hız **2.3**. Karakterli kareyi al, sonra **B** ile karakterleri gizleyip **aynı yerden boş sahne** al → [01 Render](../techniques/01-render-prep.md) |
| [4:33](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=273s) | Item modeli | Mine-imator veya Sketchfab'dan mace modeli, açısını ayarlayıp ekran görüntüsü al |
| [6:37](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=397s) | Belge | 1920x1080, 72 ppi. Tüm ekran görüntülerini katman yap. İsim etiketi için karakterin üstünde boşluk bırak → [02 Belge](../techniques/02-document-setup.md) |
| [7:40](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=460s) | Karakteri kesme | **Polygonal Lasso** + Layer Mask. Magic Wand yerine bunu öneriyor, çünkü Minecraft kenarları düz |
| [9:15](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=555s) | Çubuk → mace | Çubuğu maskeyle sil, referans için kopya katmanda tut. Mace'i aynı açıyla döndürüp yerleştir |
| [10:50](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=650s) | Eli item'a oturtma | Yeni katman, renkleri damlalıkla al, **Hardness 0** yumuşak fırça, çalışırken katman Opacity **%50** |
| [12:00](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=720s) | Zırhı ayırıp parlatma | Katmanı çoğalt, sadece zırh kalsın diye maskele. **Vibrance 0 / Saturation +30**, **Exposure +0.40** (Offset 0, Gamma 1.00) → [08 Renk](../techniques/08-recolor.md) |
| [12:40](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=760s) | Büyü parıltısı (Satin) | Aşağıdaki tablo. Sonra opaklığı düşürdü (son değer gösterilmedi) |
| [13:20](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=800s) | Kılıcı Selective Color ile patlatma | Image > Adjustments > Selective Color, **Blues**: Cyan **−45**, Magenta **−14**, Yellow **−38**, Black **−50**, **Absolute**. Sahnedeki tek mavi kılıç olduğu için sadece o etkilenir |
| [13:45](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=825s) | Karakter rengi | Vibrance **+38**, Saturation **+50** (kırmızılar), sonra Exposure artı. **Sıra önemli:** önce Vibrance/Exposure, sonra Satin/Selective Color. Ters yapınca bozuldu, geri aldı |
| [14:40](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=880s) | Arka planı yeniden kurma | Sadece ön zemini tut (lasso), Vibrance + Exposure. Arkaya hazır ön plan asset'i, özel gökyüzü (Exposure artı) ve eğik güneş asset'i → [10 Gökyüzü](../techniques/10-sky-and-assets.md) |
| [16:25](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=985s) | Minecraft isim etiketi | Aşağıdaki tablo |
| [17:15](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=1035s) | Zemin gölgesi | Zemin katmanının üstüne, karakterlerin altına **Ellipse** (siyah). Zıplayan karakterde gölge uzatıldı. Yumuşatma değeri gösterilmedi (x12 hızlı) |
| [17:40](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=1060s) | Arka plan bulanıklığı | Filter > Blur > **Gaussian Blur, Radius 4.0 px** (arka ağaç/ön plan asset'ine) |
| [18:00](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=1080s) | Karakteri ayırma (pop) | **Siyah Outer Glow + beyaz Inner Shadow**, aşağıdaki tablo |
| [18:35](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=1115s) | Hız çizgileri | Anime "zoom lines" asset'i. Rasterize et, ortasını **Hardness 0, ~618 px** yumuşak silgiyle temizle, karakterler açıkta kalsın |
| [19:00](https://www.youtube.com/watch?v=uVg0hR0uUS4&t=1140s) | Test | Önizleme aracında diğer thumbnail'lerin yanında gör, arkadaş/kreatörden geri bildirim al. Bir video için 2–3 versiyon yap |

## Kesin ayarlar

**Satin (büyülü zırh parıltısı)**, sadece zırh katmanına:

| Ayar | Değer |
|---|---|
| Blend Mode | **Linear Dodge (Add)** |
| Renk | mor/magenta, ekrandan ölçülen yaklaşık **#c923f1** |
| Opacity | **%57** (sonra düşürüldü) |
| Angle | **−136°** |
| Distance | **49 px** |
| Size | **98 px** |
| Contour | Linear, Anti-aliased ✓, **Invert ✓** |

**İsim etiketi (ClownPierce yazısı)**
- Arkada Rectangle şekli: siyah, yarı saydam (opaklık değeri ekranda okunmadı), kafanın eğimine göre hafif döndürülmüş.
- Metin: **Minecraftia Regular**, Faux Bold açık, beyaz, tracking **60**, dikey ölçek **%110**, yatay ölçek **%103**. Punto dönüşümle değişiyor (208 → 79 pt).
- Metne **Drop Shadow**: Normal, siyah, Opacity **%69**, Angle **135°**, Use Global Light kapalı, Distance **13 px**, Spread 0, Size **0**. Bu, oyundaki sert yazı gölgesini taklit ediyor.

**Karakter Layer Style (ayırma)**

| Efekt | Ayarlar |
|---|---|
| Outer Glow | Normal, **siyah**, Opacity **%50**, Noise 0, Technique Softer, Spread **%13**, Size **106 px** |
| Inner Shadow | Normal, **beyaz**, Opacity **%7** (ClownPierce) / **%20** (SB737), Angle **90°** (Global Light ✓), Distance **9 px** / **12 px**, Choke 0, Size **0** |

Siyah dış parlama karakteri arka plandan koparıyor. Sert beyaz iç gölge de üst kenara ince bir ışık çizgisi koyuyor. Anlatıcı bunu "siyahla beyaz kontrast yapınca kenar patlıyor" diye açıklıyor.

## İzleme notları
- Açıklamada başlık [2026] ama video 2024 sonu. Teknikler güncel SMP kapaklarıyla uyumlu.
- Hız çizgisi asset'i, gökyüzü, güneş ve ön plan anlatıcının kendi asset paketinden. Linki videoda yok.
- 16:30–16:50 ve 17:20–17:45 hızlandırılmış. İsim etiketi kutusunun opaklığı ve elips gölgenin yumuşatma değeri okunamadı.
