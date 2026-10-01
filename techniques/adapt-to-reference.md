---
type: teknik
title: Referansa göre ayar uyarlama
sources: [spare-clean-thumbnails, zestu-highlights]
tags: [teknik, referans, uyarlama]
status: taslak
---
# Referansa göre ayar uyarlama

**Sıra:** önce [tarz](../styles/README.md) seçilir; tarz kartı hangi adımın açık, kapalı veya değişik olacağını söyler. Bu tablo ondan sonra gelir ve değerleri **referansa göre** ince ayarlar.

Videolardaki değerler tek bir sahne için (karlı dağ, açık mavi + mor). Sipariş farklı bir sahne ya da referans resim içeriyorsa, aşağıdaki tablo hangi referans özelliğinin **hangi adımı ve ayarı** değiştirdiğini gösterir.

> [!warning] Bu tablo bir **uyarlama rehberi**. Videolardan gelen değerler başlangıç noktası; aralıklar öneri. Bir değer bir işte denenip işe yaradıysa notu `status: stabil` yap ve örneği ekle.

## Önce referanstan ölç
1. `python3 tools/analyze_reference.py <referans> -o <klasör>` → palet, ortalama parlaklık ve doygunluk.
2. Görsele bakıp şunları not et:
   - **ortam/gökyüzü rengi:** arka planın en açık, az doygun tonu,
   - **ana ışığın yönü ve rengi:** sıcak mı soğuk mu,
   - **vurgu rengi:** küçük ama en doygun alan (glow, eşya),
   - **sisin/derinliğin miktarı,**
   - **karakterin boyutu ve yerleşimi,**
   - **kontur/rim light olup olmadığı.**

## Referans → ayar tablosu
| Referansta gözlenen | Değişen adım | Nasıl uyarlanır | Videodaki değer |
|---|---|---|---|
| Ortam / gökyüzü rengi | [04 Sis](04-depth-map-fog.md), Solid Color | Referansın en açık arka plan tonunun **rengini (H)** al. Doygunluğu %15–30, parlaklığı %90–100 aralığına çek. | #c7e8ff (H205 S22 B100) |
| Ortam rengi | [06 Layer Style](06-layer-style-ambient-light.md) | Gradient Overlay'in açık ucu, Inner Glow ve Inner Shadow renkleri **sis rengiyle aynı tonda** olsun. Karakter ancak böyle ortama oturur. | açık mavi |
| Ana ışığın yönü | [03 NMS](03-nms-shading.md), [07 Elle gölge](07-hand-shadows.md), [11 Highlight](11-highlights.md) | Işığa bakmayan yüzün NMS rengini gölge, ışığa bakanı ışık olarak seç. Elle gölgeyi ışığın ters tarafına, highlight'ı ışığa bakan kenarlara koy. | gölge: kırmızı yüzler, ışık: yeşil (üst) yüzler |
| Işığın rengi (sıcak/soğuk) | [03 NMS](03-nms-shading.md), ışık katmanı | Soğuk ışıkta beyaz Overlay. Sıcak ışıkta (lav, gün batımı) açık turuncu/sarı Overlay (ör. #ffd9a0). Opacity %10–20. | beyaz, Overlay %10 |
| Baskın 2–3 renk | [05 Camera Raw](05-camera-raw.md), HSL | Videoda Aqua/Blue doygunluğu artırılıyor (+86 / +100). Bu artışı **referansın baskın tonlarına** taşı (ör. Nether için Red/Orange S +40…+80), diğerlerini 0'a yakın bırak. | Aqua S+86 L+49, Blue S+100 L+52 |
| Ortalama parlaklık | [05 Camera Raw](05-camera-raw.md), Light | Kendi işin referanstan karanlıksa Exposure'ı +0.1…+0.3 aralığında artır. Karanlık bir atmosfer isteniyorsa Blacks'i +62'den aşağı çek. | Exposure +0.10, Blacks +62 |
| Ortalama doygunluk | [05 Camera Raw](05-camera-raw.md), Saturation | Script'in verdiği doygunluk referansınkine yaklaşana kadar ayarla. | +18 |
| Vurgu rengi | [08 Renk değiştirme](08-recolor.md), [09 Glow](09-glow.md) | Eşyanın yeni rengi ve glow rengi bu renk olsun. | mor, Soft Light %36 + Linear Dodge |
| Sis / derinlik miktarı | [04 Sis](04-depth-map-fog.md), Curves | Referansın arka planı çok solgunsa eğriyi daha yukarı çek (ör. 86→160). Arka plan netse az çek (ör. 86→110). | 86→134 |
| Karakter boyutu ve yerleşimi | Kompozisyon ([checklist](../references/README.md)) | Referanstaki oranı (kadraj yüksekliğinin %30–50'si) ve üçte bir yerleşimini taklit et. Render'ı alırken kamerayı buna göre kur. | – |
| Beyaz kontur / dış glow | [06 Layer Style](06-layer-style-ambient-light.md) | Referansta varsa **Stroke** ekle (4–10 px beyaz, Outside) veya Outer Glow. Videolarda yok, referanstan gelir. | – |
| Highlight yoğunluğu | [11 Highlight](11-highlights.md) | Belirgin rim light varsa highlight katmanını Normal %100 bırak. İnce bir his isteniyorsa Overlay kullan. | Overlay |

## Sonra karşılaştır
`/mcthumb:check <çıktı> <sipariş klasörü>` → paleti, parlaklığı ve 168x94 önizlemeyi referansla yan yana koyar.
