---
type: index
title: Referans kütüphanesi
tags: [referans, index]
---
# Referans kütüphanesi

Beğenilen thumbnail'ler, ayar ekran görüntüleri ve kendi işlerin burada durur. Her görselin **bir notu** vardır. Claude yeni bir thumbnail'e yardım ederken önce [Öğrenilenler](lessons.md) notunu, sonra konuya uyan referansları okur.

## Klasör düzeni
```
references/
  README.md            ← bu sayfa (nasıl eklenir + analiz listesi)
  lessons.md      ← referanslardan çıkan ortak dersler (skill'in hafızası)
  ref-YYYY-MM-DD-short-name.md   ← her görsel için bir not
  images/
    ref-YYYY-MM-DD-short-name.png
    previews/          ← script'in ürettiği küçük boyut önizlemeleri
```

## Referans ekleme (elle)
1. Görseli `references/images/` içine `ref-YYYY-MM-DD-short-name.png` adıyla koy. Türkçe karakter ve boşluk kullanma.
2. Vault kökünde şu komutu çalıştır:
   ```bash
   python3 tools/analyze_reference.py references/images/ref-....png -o references/images/previews
   ```
3. [Referans şablonu](../templates/reference.md) ile yeni not aç (Obsidian: *Templates: Insert template*). Script çıktısını "Teknik analiz" bölümüne yapıştır.
4. Aşağıdaki listeyi doldur, gözlenen teknikleri [teknik notlarına](../Home.md) linkle.

## Referans ekleme (Claude ile)
Görseli sohbete at veya yolunu ver ve "bunu referans olarak ekle" de. Claude sırayla şunları yapar:
- dosyayı adlandırıp `images/` klasörüne koyar,
- script'i çalıştırır,
- orijinal görsele, 168x94 önizlemeye ve gri önizlemeye bakar,
- notu şablondan oluşturup analiz listesini doldurur,
- teknikleri ilgili notlara linkler ve [Öğrenilenler](lessons.md) notunu günceller.

Mevcut notlarda olmayan bir teknik görürse kendiliğinden not açmaz, önce sana önerir.

## Analiz listesi (18 madde)
| # | Madde | Neye bakılır |
|---|---|---|
| 1 | Odak noktası | Göz 1 saniyede nereye gidiyor? Tek bir baskın öğe olmalı. |
| 2 | Yerleşim | Konu üçte bir çizgilerinde mi, ortada mı? Yazı için boş alan nerede? |
| 3 | Karakter boyutu | Karakter kadrajın yüksekliğinin yaklaşık %30–50'sini kaplamalı. |
| 4 | Poz ve bakış | Poz dinamik mi, ifade okunuyor mu, bakış ana nesneye mi gidiyor? |
| 5 | Kalabalık | En fazla 3 ana öğe olmalı (karakter, nesne, kısa yazı). |
| 6 | Derinlik | Ön plan, konu ve arka plan ayrı mı? Sis, blur veya soluk arka plan var mı? → [Depth map sis](../techniques/04-depth-map-fog.md) |
| 7 | Ayrışma | **Karakterlerin etrafında ne var?** Yakından bak: ince beyaz kontur mu, dış glow mu, koyu hale mi, rim light mı? Arka plandaki nesnelerde (kaktüs gibi) de var mı? |
| 8 | Işık yönü | Tek ana ışık var mı, arka plandaki kaynakla uyuyor mu, sıcak/soğuk ayrımı var mı? |
| 9 | Kenar parlaması | Işığa bakan kenarlarda highlight veya rim light var mı? → [Highlight](../techniques/11-highlights.md) |
| 10 | Gölge ve vinyet | Temas veya drop shadow var mı, kenarlarda kararma var mı? → [Elle gölge](../techniques/07-hand-shadows.md) |
| 11 | Palet | 2–3 ana renk olmalı, ideali tamamlayıcı bir çift (mavi/turuncu, mor/sarı, kırmızı/camgöbeği). Biyom rengi anlam taşır (Nether kırmızı/turuncu, End mor). |
| 12 | Doygunluk ve kontrast | Konu arka plandan daha doygun mu? Gri önizlemede hâlâ ayrışıyor mu? |
| 13 | Yazı | 0–4 kelime, kalın ve konturlu, genelde üst üçte birde, başlığı tekrar etmemeli. |
| 14 | Küçük boyut | 168x94 önizlemede hâlâ anlaşılıyor mu (göz kısma testi)? |
| 15 | Güvenli alan | Sağ alt köşede (video süresi rozeti) önemli bir şey olmamalı. |
| 16 | Katman sırası | Kim kimin önünde? UI kutusu ya da yazı bir karakterin **arkasında** mı (ör. ayak kutunun üstünden geçiyor)? |
| 17 | UI öğeleri | Kutu, etiket ve ikonlar düz mü, **3D levha** mı (kalınlık, perspektif, eğim, dış kontur)? |
| 18 | Hareket efektleri | Hız çizgileri nasıl: uzun ve düz değil; ince, iki ucu sivri, yarı saydam, karakterlerin arkasında mı? |

Liste şu kaynaklardan derlendi:
- thumbnailcreator.com — thumbnail composition guide
- 1of10.com — Minecraft thumbnail rehberi
- 1of10.com — YouTube thumbnail design rehberi

Bu kaynakların linkleri [Export](../techniques/12-export.md) notunda.

## Referanslar
_Henüz referans yok. İlk referansı eklediğinde buraya link ver._
