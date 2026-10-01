---
name: minecraft-thumbnail
user-invocable: false
description: Minecraft YouTube thumbnail design in Photoshop/Photopea — exact-settings workflow learned frame by frame from tutorials (NMS/normal-map shading with Color Range, depth-map fog, Camera Raw, layer styles, hand shadows, recolor, glow, highlights, export), a reference image library with palette/checklist analysis, planning new thumbnails and checking finished ones. Use for Minecraft thumbnails, Photoshop/Photopea editing steps, adding or analyzing reference images. Türkçe: Minecraft thumbnail, kapak fotoğrafı, Photoshop, Photopea, referans görsel.
---

# Minecraft Thumbnail

Bu skill bir Obsidian vault'unun içinde durur. **Vault kökü = bu dosyanın iki üst klasörü (`../../`).** Aşağıdaki bütün yollar vault köküne göredir. Notlar Türkçe; kullanıcı hangi dilde yazıyorsa o dilde yanıt ver.

Vault'a yazmadan önce `AGENTS.md` dosyasını oku. Dosya adı, link ve telif kuralları orada.

## Nereye bakmalı
| İstek | Oku |
|---|---|
| Genel bakış, tüm adımlar | `Home.md` |
| Render / NMS / DMS alma | `techniques/01-render-prep.md` |
| Belge açma, katman düzeni | `techniques/02-document-setup.md` |
| Gölge/ışık (Color Range) | `techniques/03-nms-shading.md` |
| Sis, atmosfer, depth map | `techniques/04-depth-map-fog.md` |
| Renk düzeni, Camera Raw | `techniques/05-camera-raw.md` |
| Karakteri ortama oturtma, rim light | `techniques/06-layer-style-ambient-light.md` |
| Elle gölge | `techniques/07-hand-shadows.md` |
| Zırh/eşya rengini değiştirme | `techniques/08-recolor.md` |
| Glow | `techniques/09-glow.md` |
| Gökyüzü, kar, lens flare, overlay | `techniques/10-sky-and-assets.md` |
| Highlight (kenar parlaması) | `techniques/11-highlights.md` |
| Export, YouTube boyut/limit | `techniques/12-export.md` |
| **Tarz seçimi** (clean render, sinematik, SMP/drama, split, hardcore, manhunt, korku, build, 2D, meme, Shorts) | `styles/README.md` → `styles/NN-*.md` |
| Referansa / siparişe göre ayarları değiştirme | `techniques/adapt-to-reference.md` |
| Karakteri sahneden koparma (hale + beyaz kenar) | `techniques/character-pop.md` |
| Yazı, 3D başlık, isim etiketi | `techniques/text-typography.md` |
| Blur, hız çizgileri, zemin/ayrıştırma gölgesi, parıltı, eşya glow | `techniques/action-effects.md` |
| Kontur, aura, vinyet, split, god rays, partikül, UI, 2D... (taslak) | `techniques/style-catalog.md` |
| Politika, Mojang kuralları, lisans, sipariş/teslim, en sık 10 hata | `guides/pitfalls.md` |
| Yaygın tasarım hataları → düzeltme | `guides/common-mistakes.md` |
| Photopea'da nasıl yapılır | `techniques/photopea-compatibility.md` |
| Hangi video, hangi dakika | `sources/*.md` |
| Ayar penceresinin görüntüsü (sadece yerelde) | `local/video-frames/` (varsa; Read ile görüntü olarak aç) |

## Komutlar
`/mcthumb:order` → C (sipariş) · `/mcthumb:ref` → B · `/mcthumb:check` → teslim kontrolü · `/mcthumb:learn` → D. Teknik soruları (A) komutsuz sorulur. Komut dosyaları: `commands/`.

## İş akışları

### A) Bir tekniği anlat / uygula
İlgili teknik notunu oku. Adımları kesin değerleriyle ver. Kullanıcının sahnesi farklıysa (renk teması, ışık yönü) değerlerin neye göre değişeceğini söyle. Photopea kullanıyorsa `techniques/photopea-compatibility.md` notuna bak.

### B) Referans görsel ekle ("bunu referans olarak ekle")
1. Görseli `references/images/ref-YYYY-MM-DD-short-name.<png|jpg>` olarak kaydet (ASCII, boşluksuz).
2. Vault kökünden şu komutu çalıştır:
   ```bash
   python3 tools/analyze_reference.py references/images/<dosya> -o references/images/previews
   ```
3. Orijinal görsele, `_168x94` ve `_320x180_gri` önizlemelerine **Read ile bak**.
4. `templates/reference.md` şablonundan `references/ref-...md` notunu oluştur. Frontmatter'ı doldur (palet hex'leri, parlaklık, doygunluk script çıktısından gelir). 15 maddelik analiz listesini **somut gözlemlerle** doldur. Script çıktısını "Teknik analiz" bölümüne yapıştır.
5. Gözlenen teknikleri `techniques/` notlarına linkle. Not yoksa yeni not açmadan önce kullanıcıya öner.
6. `references/lessons.md` notunu güncelle (tekrar eden kalıplar). `references/README.md` içindeki listeye link ekle.
7. Görsel başkasına aitse ve repo herkese açıksa, commit'lemeden önce kullanıcıya sor. Gerekirse `local/` altında tut.

### C) Sipariş / yeni thumbnail (`/mcthumb:order`)
Normal akış: iş gelir → istenenler söylenir → istenirse referans resim verilir.
1. `orders/YYYY-MM-DD-kisa-ad/` klasörünü aç: `brief.md` (`templates/order.md` şablonundan) + `refs/`. **`orders/` gitignore'da**; müşteri verisi asla public repoya girmez, `references/` kütüphanesine de kullanıcı istemeden kopyalanmaz.
2. İstenenleri `brief.md` → "İstenenler" bölümüne yaz.
2b. **Tarzı seç:** `styles/README.md` §1 (brief kelimeleri → tarz, referans karar ağacı). Bir ana tarz + en fazla bir yan tarz; emin değilsen sor. Tarz kartı hangi adımların açılıp kapanacağını ve hangi ek tekniklerin gerektiğini söyler.
3. Referans resimleri `refs/` içine koy. Her biri için script'i çalıştır (vault kökünden):
   `python3 tools/analyze_reference.py orders/<is>/refs/<img> -o orders/<is>/refs/previews --rel orders/<is>`
   Sonra görsellere ve önizlemelere Read ile bak.
4. Tarz kartından başla, sonra `techniques/adapt-to-reference.md` tablosuyla "Referanstan uyarlanan ayarlar" bölümünü doldur: değişen her adım için videodaki değer → bu işteki değer → neden. Referans yoksa `references/lessons.md` + video değerleriyle başla.
5. Alttan üste katman planını kesin ayarlar ve teknik notu linkleriyle yaz.
5b. Planı `guides/pitfalls.md` ve `guides/common-mistakes.md` ile kontrol et.
6. Sadece işi durduran eksikleri kısa sorular olarak sor (skin, sahne, yazı, boyut).
7. Teslimden önce `/mcthumb:check <çıktı> orders/<is>` → brief maddeleri + referansla yan yana karşılaştırma. İş bitince `status: teslim`.

### D) Yeni tutorial videosu öğren
`AGENTS.md` → "Yeni tutorial videosu ekleme" bölümünü uygula. Videoyu kare kare izle, değerleri ayar pencerelerinden oku. Kaynak notunu aç, teknik notlarını güncelle, bu tablodaki ve `Home.md` içindeki yönlendirmeyi güncelle.
