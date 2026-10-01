---
type: teknik
order: 12
title: Export ve YouTube limitleri
sources: [spare-clean-thumbnails]
tags: [teknik, export]
status: stabil
---
# 12. Export ve YouTube limitleri

## Videodaki ayarlar (Photoshop)
- **File > Export > Export As** (Alt+Shift+Ctrl+W)
- Format **PNG** (en yüksek kalite), Transparency ✓, **1920x1080**, Scale %100
- Resample: **Bicubic Sharper** veya **Bicubic Automatic**. Videoda dosya boyutu limiti yüzünden *Bicubic Automatic* tercih ediliyor.
- Metadata: None · Convert to sRGB ✓ · Embed Color Profile ✓
- Videodaki çıktı ~2.2 MB.

## Güncel YouTube thumbnail limitleri (2026-10-01'de kontrol edildi)
| | Değer |
|---|---|
| Önerilen çözünürlük | **3840x2160**, 16:9. 1920x1080 de sorun değil. |
| En küçük genişlik | 640 px |
| En büyük dosya | **50 MB** (masaüstünden yükleme). Mobilden hâlâ **2 MB**. |
| Format | JPG veya PNG |

- Limit 2 MB'tan 50 MB'a, önerilen boyut da 1280x720'den 4K'ya çıktı. Değişiklik Ekim 2025'te duyuruldu, 2026 başında herkese açıldı. 1280x720 / 2 MB yazan rehberler eskidi.
- Masaüstünden yükle. Mobilden yükleyeceksen 2 MB altına inmek için JPG (kalite ~90) export et.
- **Shorts:** 2160x3840 (9:16). Özel Shorts thumbnail'ı Temmuz 2026'dan beri YPP üyelerine açılıyor, A/B testi yok. Dikey videolarda Ana Sayfa'da otomatik **4:5** kırpma gösterilir; önemli öğeleri ortada tut.
- **Teslim paketi:** 3840x2160 PNG + 2 MB altı JPG (+ gerekirse Shorts sürümü). Ayrıntı: [Dikkat edilecekler](../guides/pitfalls.md).
- **Kontrol:** 120 px ve 168 px genişlikte okunuyor mu, sağ alt köşe (süre etiketi) ve alt kenar (ilerleme çubuğu) boş mu.

Kaynaklar:
- <https://support.google.com/youtube/answer/72431>
- <https://9to5google.com/2025/10/30/youtube-video-thumbnail-file-size-limits/>
- <https://www.androidheadlines.com/2026/03/youtube-thumbnail-size-limit-50mb-tv-upgrade.html>

Referans analiz listesinin kaynakları:
- <https://www.thumbnailcreator.com/blog/thumbnail-composition-guide>
- <https://1of10.com/blog/minecraft-thumbnail-maker-how-to-create-viral-minecraft-thumbnails-with-ai/>
- <https://1of10.com/blog/youtube-thumbnail-design/>

> [!tip] Export'tan önce `tools/analyze_reference.py` ile kendi çıktını kontrol et: oran, boyut ve 168x94 okunabilirlik testi → [Referanslar](../references/README.md)

Önceki: [Highlight](11-highlights.md)
Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (13:17–13:38)
