---
type: kaynak
title: How to make the BEST Minecraft Thumbnails (Bedwars, SMP, Horror, ...) | Tutorial
creator: Schxnappi_
url: https://www.youtube.com/watch?v=zGVLm-9RM6I
duration: "9:06"
watched: "tamamı (transkript), 2:20–4:56 kare kare, 5:00–8:30 örnekleme"
watched_on: 2026-10-01
tags: [kaynak, video, smp, yuksek-enerji, layer-style, metin, stroke]
---
# Schxnappi_ — How to make the BEST Minecraft Thumbnails (Bedwars, SMP, Horror, ...)

- Video: <https://www.youtube.com/watch?v=zGVLm-9RM6I> (yayın 05.02.2025)
- Beş stil var: temel, Bedwars ASMR, SMP, texture pack, korku. En ayrıntılı kısım temel thumbnail: karakter Layer Style'ı ve **kalın siyah konturlu 3D başlık yazısı**. Ayarlar ekranda görünüyor, anlatıcı da "kopyalayabilirsiniz" diyor.
- Program: Photoshop (Photopea da anılıyor). Render: Fabric 1.20.1 + Seltop's NewNPCs mod + Iris + Proger shader.
- Bu videoda video kareleri yakınlaştırılıp uzaklaştırılıyor. Bazı sayılar kare kenarında kesik, onlar aşağıda belirtildi.

## Zaman damgası → teknik notu
| Zaman | Konu | Not |
|---|---|---|
| [0:50](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=50s) | Dünya ayarı | Creative, Peaceful, Superflat, yapı yok. Gamerule'da spawning ve world updates kapalı |
| [1:50](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=110s) | Kamera | **FOV 30**, alçak açı ("sinematik"). NPC modunda F2 yerine **F7**: arka plan ve karakter ayrı, en yüksek çözünürlük → [01 Render](../techniques/01-render-prep.md) |
| [2:15](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=135s) | Gökyüzü değiştirme | **Select > Sky** → Delete, yeni gökyüzü. Gökyüzüne Brightness/Contrast (parlaklık +, kontrast −) → [10 Gökyüzü](../techniques/10-sky-and-assets.md) |
| [2:40](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=160s) | Arka plan rengi | Brightness/Contrast + Hue/Saturation: "daha parlak, daha doygun". Karaktere de kırpılmış (clipped) Hue/Sat, Vibrance ve Brightness katmanları |
| [2:55](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=175s) | **Karakter Layer Style** | Aşağıdaki tablo (5 efekt) → [06 Ortam ışığı](../techniques/06-layer-style-ambient-light.md) ile karşılaştır |
| [3:45](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=225s) | **Başlık yazısı** | Burbank Big Condensed + 3D gri gölge + gradient + grup Stroke, aşağıda |
| [4:28](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=268s) | Alt başlık | Montserrat (anlatıcı söylüyor). Turuncu→pembe dolgu GFX paketindeki hazır stilden geliyor. Grupta aynı siyah Stroke + renkli Outer Glow |
| [4:40](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=280s) | Işık noktaları | Yeni katmanda beyaz soft fırçayla birkaç nokta → **Overlay**. Karaktere de elle ışık boyandı → [09 Glow](../techniques/09-glow.md) |
| [5:00](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=300s) | Bedwars ASMR | Pen tool ile arka planı katmanlara ayır, aralarına mavi soft fırça ışığı. Karakter kopyasına **Path Blur** (hareket izi). Klavye/mouse PNG'leri, "ASMR" yazısı, vuruş partikülleri. Sonra **Ctrl+Alt+Shift+E** ile birleşik kopya → Camera Raw (canlılık) → doku |
| [6:00](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=360s) | SMP | Konsept: "okulun SMP'sinden banlandım". Karakter duvarın tepesinde, iki arkadaş ona nişan alıyor. SMP kapakları shader'sız ve sade: gökyüzü, katman ayırma, basit Layer Style, renk, büyük kırmızı "Banned." yazısı |
| [6:30](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=390s) | Texture pack | widgets/icons PNG'sinden hotbar, kalp, yemek, XP barını kes. Resample **Nearest Neighbor** ile yapıştır. Ctrl+T + Ctrl ile perspektif. 3D kalınlık için: grupla, Ctrl+T, **↑ ve ←** bir kez, Enter, sonra **Ctrl+Shift+Alt+T** birkaç kez, birleştir |
| [7:50](https://www.youtube.com/watch?v=zGVLm-9RM6I&t=470s) | Korku | Ekran görüntüsü gündüz alınır, gece gökyüzü Photoshop'ta eklenir. Kızıl meşale ışıkları, karakterlerde Inner Shadow, Herobrine'a ışık efekti. "Karanlık ama okunur" kuralı |

## Kesin ayarlar

**Karakter Layer Style** (ekranda kalan son değerler)

| Efekt | Ayarlar |
|---|---|
| Gradient Overlay | Blend **Overlay**, Opacity **%52**, gradient **siyah→beyaz**, Linear, Align with Layer ✓, Angle **90°**, Scale **%150**, Method Perceptual |
| Inner Glow | Blend **Overlay**, Opacity **%76**, Noise 0, **beyaz**, Technique Softer, Source **Edge**, Choke 0, Size **32 px**, Range %50, Jitter 0 |
| Drop Shadow | Blend Multiply, **siyah**, Opacity **%100**, Angle 44° (Global Light kapalı), **Distance 0**, Spread 0, Size **24 px** (önce 147 denendi). Distance 0 olduğu için karakterin çevresinde koyu bir hale yapar |
| Inner Shadow | Blend **Normal**, **beyaz**, Opacity **%100**, Angle **12°** (önce 50°), Global Light kapalı, Distance **6 px** (önce 15), Choke 0, **Size 0**. Bir yandan sert beyaz kenar ışığı (rim light) verir |
| Outer Glow | Blend **Overlay** (önce Screen %26 denendi), Opacity **%100**, Noise 0, **beyaz**, Softer, Spread 0, Size **250 px** |

**Başlık yazısı ("Thumbnail")**
1. **T** ile yaz. Font **Burbank Big Condensed** (kalın, dar), beyaz.
2. Yazı katmanına Layer Style:
   - **Drop Shadow**: Normal, **açık gri** (ekrandan ~**#9c9c9c**), Opacity %100, Angle **90°**, Global Light kapalı, Distance **~19 px** (sürüklerken okunan değer), Spread 0, **Size 0**. Sonuç: harflerin altında sert gri bir "kalınlık", 3D blok yazı görünümü.
   - **Gradient Overlay**: açık gri → beyaz (harfin üstü beyaz, altı griye döner).
   - **Inner Glow**: karakterdeki ayarların aynısı.
3. Yazıyı **Ctrl+G** ile gruba al. **Gruba** Layer Style ver:
   - **Stroke**: Size **13 px**, Position **Outside**, Blend Normal, Opacity %100, Fill Type Color, **siyah**. Ana başlıkta sayı kare kenarında kesik ("13…"). Alt başlık grubunda **13 px** net okunuyor.
   - **Drop Shadow**: Multiply, siyah, Angle 44°.
   - Neden grup? Stroke, gri 3D gölgenin de çevresini sarar. Böylece kontur harf + kalınlık bütününün dışında tek parça olur.
4. Alt başlık grubunda **Outer Glow**: Overlay, Opacity **%35**, Softer, Spread 0, Size **92 px**. Renk beyazdan kırmızıya doğru deneniyor.

## İzleme notları
- Karakterin efekt sırası (Layers panelinde): Inner Shadow, Inner Glow, Gradient Overlay, Outer Glow, Drop Shadow.
- Path Blur, texture pack ve korku bölümleri hızlı özet. Ayar pencereleri gösterilmedi.
