---
type: kaynak
title: "How To Make Unstable SMP Thumbnails For Free"
creator: Swiffex
url: https://www.youtube.com/watch?v=IXVwYGiyrVY
duration: "13:03"
published: 2026-03-24
watched: "tamamı: transkript + kare kare (8:40–12:45 arası anlatımsız, sadece kare)"
watched_on: 2026-10-01
tags: [kaynak, video, tam-surec, photopea, unstable-smp, wemmbu, vanilla, shading, highlight]
---
# Swiffex — How To Make Unstable SMP Thumbnails For Free

- Video: <https://www.youtube.com/watch?v=IXVwYGiyrVY>
- Bütün düzenleme **Photopea**'da (açık tema, ücretsiz sürüm). Shader yok, NMS/DMS yok. Işık ve gölge tamamen elle.
- Hedef stil: Unstable SMP (Wemmbu, Parrot, Spoke, FlameFrags). Referans olarak Wemmbu'nun bir thumbnail'i seçiliyor: önde büyük karakter, arkada zırhlı bir grup.
- Sonuç: solda kerpiç (mud brick) duvar önünde kadraja bakan Steve, sağda çölde yürüyen 3 zırhlı oyuncu (elmas, netherite/mor, elmas), parlak gökyüzü, yazı yok.
- Mod: **Seltop's NewNPC** (sadece **1.20.1**). Linki video açıklamasında.

## Zaman damgası → teknik notu
| Zaman | Konu | Not |
|---|---|---|
| [0:30](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=30s) | Referans seç | Bir SMP kanalından tek thumbnail seç ve onu yeniden yapmaya çalış. → [Referansa göre uyarlama](../techniques/adapt-to-reference.md) |
| [1:00](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=60s) | Dünya kurulumu | Superflat, Generate Structures kapalı, spawning ayarları kapalı. → [01 Render hazırlığı](../techniques/01-render-prep.md) |
| [1:30](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=90s) | Pozlar | Referanstaki pozları NPC'lerle kopyala. Ön plandaki karakterin arkasına mud brick duvar ör. |
| [1:58](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=118s) | Ekran görüntüsü | Ekran yazısı: **FOV 30–45** (kendisi 30), çekmeden önce **F1** (HUD gizle), F2 yerine **F7**. F7'nin ne olduğu söylenmiyor, muhtemelen bir mod tuşu. Dosyalar `%appdata%/.minecraft/screenshots`. |
| [2:06](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=126s) | Photopea belge | New Project → **Social** → **Youtube Thumbnail** = **1280x720**, 72 DPI, beyaz, sRGB 8 bit. → [02 Belge kurulumu](../techniques/02-document-setup.md) |
| [2:40](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=160s) | Gökyüzünü atma | Lasso ile duvar + oyuncu bölgesini seç → Layers panelinin altındaki **Add Layer Mask** düğmesi. |
| [2:50](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=170s) | Smart Object | Katmana sağ tık → Convert to Smart Object. |
| [3:00](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=180s) | Arka plan çekimi | Yeni normal dünya, `/locate biome` → desert, tp, ekran görüntüsü. → [10 Gökyüzü ve asset'ler](../techniques/10-sky-and-assets.md) |
| [3:10](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=190s) | Diğer 3 oyuncu | Aynı işlem, hepsi Photopea'ya. |
| [3:30](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=210s) | Ayak altını kesme | Kumun içinde dursunlar diye ayak tabanından ince bir şerit sil. Çok kesme, garip durur. Photopea burada smart object'i rasterize etmeyi soruyor (3:48). |
| [4:00](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=240s) | Temas gölgesi | Değerler aşağıda. → [07 Elle gölge](../techniques/07-hand-shadows.md) |
| [5:00](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=300s) | Camera Raw (Steve) | Abartma uyarısı. Değerler aşağıda. → [05 Camera Raw](../techniques/05-camera-raw.md) |
| [5:20](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=320s) | Elle shading (lasso) | Güneşe bakan yüz beyaz + Overlay, bakmayan yüz siyah. → [07 Elle gölge](../techniques/07-hand-shadows.md), [03 NMS](../techniques/03-nms-shading.md) |
| [7:00](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=420s) | Highlight | 3 px, Hardness 0. → [11 Highlight](../techniques/11-highlights.md) |
| [7:40](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=460s) | Highlight söndürme | Yumuşak silgi, düşük opacity. → [11 Highlight](../techniques/11-highlights.md) |
| [8:20](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=500s) | Işık (clipping mask) | Değerler aşağıda. → [06 Ortam ışığı](../techniques/06-layer-style-ambient-light.md) |
| [9:02](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=542s) | Tek parça gölgelemek | Ekran yazısı: sadece kafa vb. için önce lasso ile seç, sonra boya. |
| [9:42](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=582s) | Camera Raw (duvar) | Değerler aşağıda. |
| [10:56](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=656s) | Diğer oyuncular | Aynı adımları tekrar et (anlatımsız). |
| [12:48](https://www.youtube.com/watch?v=IXVwYGiyrVY&t=768s) | Export | File > Export as > PNG. → [12 Export](../techniques/12-export.md) |

## Ekranda okunan ayarlar
**Temas gölgesi (4:00–4:40)**
1. Yeni katmanı gölge verilecek oyuncunun **altına** koy (ekran yazısı).
2. Elliptical Marquee ile ayakların altına yassı bir elips çiz, siyahla doldur.
3. Katman **Normal, Opacity %49**. Blur yok, kenar sert.
4. Diğer oyuncular için yeni çizme: katmanı **kopyala** (Layer 1 copy, copy 2), taşı, ölçekle.

**Camera Raw** (Filter > Camera Raw, smart filter). Sıfır olmayanlar:
| Katman | Exposure | Contrast | Temperature | Vibrance | Texture |
|---|---|---|---|---|---|
| Steve (5:22) | **0.8** | 11 | 4 | 20 | 11 |
| Mud brick duvar (9:47) | **0.6** | 25 | 5 | 24 | 18 |
Highlights, Shadows, Whites, Blacks, Tint, Saturation, Clarity, Dehaze: hepsi 0.

**Elle shading (5:20–7:05)**
- `Layer 2`: güneşe bakan yüzler (kafa üstü vb.) lasso ile seçilip **beyaz** boyandı → **Overlay**.
- Güçlendirme: `Layer 2` kopyalandı, kopya Overlay **%35** yapıldı, **Merge Down** ile birleştirildi, birleşen katman tekrar Overlay %100 yapıldı (7:01). Etkisi denenmedi. Kopya tamamen aynı beyaz alanı kapladığı için fark sadece yarı saydam kenarlarda olabilir.
- `Layer 3`: güneşe bakmayan yüzler **siyah**, **Normal**, opacity sürüklenerek ayarlandı (%59–61, ekranda son değer **%65**).
- Katmanlar clipping mask değil. Boyama lasso seçimi içinde yapıldığı için taşma yok.

**Highlight (7:00–8:00)**
- Brush **3 px** (2 px de olur), **Hardness %0**, Blend Normal, Opacity %100, Flow %100, Smooth %0, beyaz. Sadece güneşin vurduğu kenarlar (ekran yazısı).
- Söndürme: Eraser, Mode Brush, **Opacity %11**, Flow %100, Hardness 0, boyut ekranda **51 px**. Anlatımda "boyut ~20, opacity 10" deniyor, ekranda kalan değerler yazıldı. Highlight'ın üstünden geçirip uçlarını söndür.

**Işık (8:20–9:10)**
1. Yeni katman → oyuncu katmanına **Clipping Mask** (History: *Enable Clipping Mask*).
2. Soft brush: **Opacity %20, Size 100, Hardness 0**, beyaz. Güneş tarafındaki üst/sağ kenarları boya.
3. Ekran yazısı: katmanı **Overlay** yap, kopyala, kopyayı **Normal** yap, opacity'yi göze göre ayarla.
4. Videoda iki clip katman var (`Layer 5`, `Layer 6`).

**Son katman sırası** (yukarıdan aşağı, yaklaşık): highlight (`Layer 4`) → siyah shading (`Layer 3`, Normal %65) → beyaz shading (`Layer 2`, Overlay) → ışık clip'leri (`Layer 6`, `Layer 5`) → Steve (+Camera Raw) → diğer oyuncular → duvar (+Camera Raw) → temas gölgeleri (`Layer 1` + kopyalar, %49) → çöl arka planı → Background.

**Export (12:48–12:55):** File > **Export as > PNG** → "Save for web" penceresi: Width **1280**, Height **720** px, **Quality %100**, "don't use palettes" ✗, "attach metadata" ✓ → Save. Önizlemedeki dosya boyutu **560.3 KB**.

## Photopea'ya özgü noktalar
- **New Project** penceresinde hazır şablonlar var. *Social > Youtube Thumbnail* **1280x720** veriyor, bu eski ölçü. Width/Height'ı elle 1920x1080 ya da 3840x2160 yap → [12 Export](../techniques/12-export.md).
- Smart object üstünde seçimi silmeye çalışınca "Smart Object must be rasterized first. Rasterize?" onayı çıkıyor. OK dersen katman düz piksele döner ve smart filter düzenlenemez. Ayak kesmek için silmek yerine **layer mask** kullan.
- **Export as > PNG**, Photoshop'taki Export As yerine "Save for web" penceresini açıyor. Boyut, kalite ve dosya boyutu önizlemesi var, resample seçimi yok.
- Clipping mask, Overlay/Normal, Camera Raw smart filter, Elliptical Marquee ve layer mask Photoshop'takiyle aynı yerde.

## İzleme notları
- Transkript otomatik altyazıdan alındı. 8:40–12:45 arası anlatım yok, kare kare izlendi.
- Videoda opacity'ler birkaç kez değişiyor. Ekranda kalan son değerler yazıldı.
- Bu notun highlight ayarları vault'taki [11 Highlight](../techniques/11-highlights.md) ile çelişiyor: Spare/zestu **Hard Round %100 + Overlay** kullanıyor, Swiffex **Hardness %0 + Normal %100** ve yumuşak silgiyle söndürme. İki yöntem de kaynak adıyla tutulmalı.
