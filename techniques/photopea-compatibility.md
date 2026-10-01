---
type: teknik
title: Photopea uyumluluğu
sources: []
tags: [teknik, photopea]
status: stabil
checked_on: 2026-10-01
---
# Photopea uyumluluğu

Her adımın ücretsiz [Photopea](https://www.photopea.com)'daki karşılığı. 2026-10-01'de Photopea dokümanlarından kontrol edildi ve tarayıcıda boş bir belgede denendi. Türkçe arayüzde menü adları farklıdır, örneğin *Seç > Renk Aralığı*, *Dosya > Farklı Dışa Aktar*.

| Adım | Destek | Photopea'da | Eksik varsa çözüm |
|---|---|---|---|
| [Color Range](03-nms-shading.md) | ✅ | Select > Color Range. *Sampled Colors* seçeneği var, Fuzziness 0–200. | – |
| [Parlaklıktan seçim](04-depth-map-fog.md) | ✅ | Channels'ta RGB küçük resmine **Ctrl+tık**. | – |
| [Solid Color + maske + Ctrl+I](04-depth-map-fog.md) | ✅ | Layer > New Fill Layer > Solid Color. Maske küçük resmine tıkla, sonra Image > Adjustments > Invert (Ctrl+I). Sadece seçili alan ters çevrilir. | – |
| [Maskeye Curves](04-depth-map-fog.md) | ✅ | Maske seçiliyken Image > Adjustments > Curves (Ctrl+M). | – |
| [Camera Raw](05-camera-raw.md) | ⚠️ Kısmi | Filter > Camera Raw (Shift+Ctrl+A). Light, Color (Temp/Tint/Vibrance/Saturation), Effects (Texture/Clarity/Dehaze), Curves ve Noise Reduction var. **HSL Color Mixer ve Sharpening yok.** | HSL için Hue/Saturation ayar katmanı (Ctrl+U) ile renk bazında Aqua/Blue doygunluğunu artır, ya da Selective Color kullan. Keskinlik için Filter > Sharpen > Unsharp Mask'ı smart filter olarak ekle. |
| Smart Object / Smart Filter | ✅ | Layer > Smart Object > Convert to Smart Object. Filtreler sonradan düzenlenebilir. | Smart object üstüne boyama yapma, yeni katman aç. |
| [Layer Style](06-layer-style-ambient-light.md) | ✅ | Katmana çift tıkla. Gradient Overlay (açı, scale, align), Inner Glow (Softer/Edge, choke, size), Inner Shadow (choke, size, noise) ve Drop Shadow var. Stil kopyalama: sağ tık > Copy/Paste Layer Style. | – |
| [Polygonal Lasso](07-hand-shadows.md) | ✅ | L grubu. Enter veya çift tık seçimi kapatır, Delete son noktayı siler. | – |
| [Quick Selection](08-recolor.md) | ⚠️ Kısmi | W grubu. **"Sample All Layers" seçeneği yok.** | Select All → Edit > Copy Merged (Shift+Ctrl+C) → Paste. Birleşik katmanda seçimi yap, sonra o katmanı sil. Magic Wand'da Sample All Layers var. |
| [Blend mode'lar](09-glow.md) | ✅ | Overlay, Soft Light, Vivid Light, Linear Dodge (Add), Color Dodge, Screen. | – |
| [Highlight çizgisi](11-highlights.md) | ✅ | B, sonra tıkla + Shift+tık. Hard Round, 3–5 px. | – |
| [Export](12-export.md) | ⚠️ Kısmi | File > Export As → PNG/JPG/WebP. Genişlik/yükseklik ve kalite ayarı var. | **Resample yöntemi seçilemiyor.** Önce Image > Image Size (Alt+Ctrl+I) ile *Bicubic Sharper* kullanarak boyutlandır, sonra %100'de export et. |
| PSD açma | ✅ Büyük ölçüde | Smart object, layer style, fill ve adjustment katmanları açılır ve düzenlenebilir kalır. | Photoshop'taki Camera Raw HSL/Sharpening ayarları Photopea'da aynı görünmeyebilir (tahmin, denenmedi). Karşılaştırmak için Photoshop'tan düz bir PNG de sakla. |

## Otomasyon (ileride işe yarar)
- **File > Script:** Photoshop scripting API'sine benzeyen JavaScript (`app.activeDocument` ...).
- **Actions:** Window > Actions ile adım kaydedip oynatabilirsin, Photoshop **.ATN** dosyaları da içe aktarılır. File > Automate > Batch.
- **URL API / Live Messaging:** Photopea iframe içinde açılıp `postMessage` ile script ve dosya gönderilebilir, PNG geri alınabilir. Örnek kullanım: şablon PSD'yi yükle, görseli değiştir, PNG al. Ayrıntı için [Yol haritası](../dev/roadmap.md).

## Ek notlar (Swiffex ve Pqtrick videolarından)
- **Hazır şablon eski:** New Project → Social → "Youtube Thumbnail" **1280x720** veriyor. Boyutu elle 1920x1080 veya 3840x2160 yap.
- **Smart object'te silme:** seçimi silmeye çalışınca "Smart Object must be rasterized first" çıkar. OK dersen Camera Raw smart filtresi düzenlenemez olur. Ayak kırpma gibi işleri **layer mask** ile yap.
- **Export As > PNG** "Save for web" penceresini açar: genişlik/yükseklik, Quality, "don't use palettes", "attach metadata" ve canlı dosya boyutu önizlemesi var (1280x720, Quality %100 → 560 KB).
- **Maske:** Lasso ile seç, sonra Layers panelinin altındaki *Add Layer Mask* düğmesi.
- **Clipping mask** Photoshop'taki gibi çalışır.
- **Layer Style** pencereleri Photoshop'la aynı: Outer Glow (Softer/Range/Jitter), Drop Shadow ("Knock out drop shadow" dahil).
- **Camera Raw Exposure** ondalık kabul eder (0.6, 0.8).
- **Fırça sertliği** boyut açılır penceresinde; fırça çubuğunda "Smooth" ayarı var.

Kaynaklar:
- photopea.com/learn: [advanced-selecting](https://www.photopea.com/learn/advanced-selecting), [channels](https://www.photopea.com/learn/channels), [masks](https://www.photopea.com/learn/masks), [adjustments-filters](https://www.photopea.com/learn/adjustments-filters), [smart-objects](https://www.photopea.com/learn/smart-objects), [layer-styles](https://www.photopea.com/learn/layer-styles), [opening-saving](https://www.photopea.com/learn/opening-saving), [scripts](https://www.photopea.com/learn/scripts), [actions](https://www.photopea.com/learn/actions)
- API: [photopea.com/api](https://www.photopea.com/api/), [api/live](https://www.photopea.com/api/live)
- Camera Raw eksik paneller: [GitHub issue #7152](https://github.com/photopea/photopea/issues/7152)
