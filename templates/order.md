---
type: siparis
client: ""
video: ""
deadline:
size: 1920x1080
style: ""
style_secondary: ""
skins: []
status: yeni
tags: [siparis]
---
# {{title}}

> Sipariş klasörü sadece yerelde durur (`orders/` gitignore'da). Müşteri adı yerine takma ad yeterli.

## Tarz
- **Ana tarz:** (S1–S11, bkz. [Tarz rehberi](../../styles/README.md))
- **Yan tarz (en fazla bir):**
- **Neden bu tarz:** (brief'teki kelimeler / referanstaki ipuçları)

## Render'lar
Render dosyalarını `renders/` altına koy (split işte `renders/left/`, `renders/right/`). Her karakter için shader'sız / DMS / NMS geçişlerini eşleştir: aynı karakterin geçişlerinde şeffaflık sınırları (bbox) birebir aynıdır. DMS gri değeri yakınlığı verir (beyaz = yakın).

| Karakter / katman | Shader'sız | DMS (yakınlık) | NMS | Konum |
|---|---|---|---|---|
| | | | | |

## İstenenler
- **Konu / video:**
- **Karakterler, skin'ler, pozlar:**
- **Sahne / biyom:**
- **Yazı (varsa):**
- **Renk / hava (mood):**
- **Mutlaka olsun:**
- **Olmasın:**

## Brief soruları (eksikse sor)
- Video başlığı (taslak da olur) ve videoda **gerçekten olan** 1–2 sahne. Thumbnail videoda olmayan bir şeyi göstermemeli.
- Kanal "çocuklar için yapılmış" mı? Küfür, korku ve kan hassasiyeti nedir? (Reklam uygunluğu ve A/B testi buna bağlı.)
- A/B testi yapılacak mı? Yapılacaksa birbirinden gerçekten farklı 3 konsept hazırlanır.
- Marka: renkler, fontlar, kanal logosu, skin dosyaları (.png), yüz fotoğrafları, kullanılan texture pack ve shader adı.
- Referanslar ve kaçınılacak tarzlar. Rakip kanal birebir kopyalanmaz.
- Teslim tarihi: yayından 24–48 saat önce olmalı (premiere ve planlı yayın saati de sorulur).
- Atıf gerektiren varlıklar (rig, texture pack, ücretsiz stok) için açıklamaya yazılacak metin.

## Teslim paketi
- [ ] 3840x2160 PNG (ana dosya)
- [ ] 2 MB altı JPG (mobilden yükleme için)
- [ ] Gerekirse 2160x3840 Shorts sürümü
- [ ] PSD (anlaşıldıysa; lisanslı font/stok katmanları rasterize, font dosyası değil adı + linki)
- [ ] Açıklamaya eklenecek atıf metni ve "NOT AN OFFICIAL MINECRAFT PRODUCT…" notu önerisi

## Referanslar
| Görsel | Bundan ne alınacak? | Analiz (palet, parlaklık, doygunluk) |
|---|---|---|
| | | |

## Referanstan uyarlanan ayarlar
Kurallar için bkz. [Referansa göre ayar uyarlama](../../techniques/adapt-to-reference.md).

| Adım | Videodaki değer | Tarz kartındaki değer | Bu iş için (referansa göre) | Neden |
|---|---|---|---|---|
| | | | | |

## Katman planı (alttan üste)
1. 

## Eksik bilgiler / sorular
- 

## Teslim kontrolü
- [ ] `/mcthumb:check` → boyut, oran, dosya, 120/168 px okunabilirlik
- [ ] [Dikkat edilecekler](../../guides/pitfalls.md): yanıltıcı değil, kan/küfür yok, Minecraft logosu/logo fontu yok, sağ alt köşe boş
- [ ] İstenenlerdeki her madde var
- [ ] Referansla yan yana karşılaştırıldı
