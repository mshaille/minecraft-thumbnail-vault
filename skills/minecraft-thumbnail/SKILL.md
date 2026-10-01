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
| Photopea'da nasıl yapılır | `techniques/photopea-compatibility.md` |
| Hangi video, hangi dakika | `sources/*.md` |
| Ayar penceresinin görüntüsü (sadece yerelde) | `local/video-frames/` (varsa; Read ile görüntü olarak aç) |

## Komutlar
`/mcthumb:ref` → B · `/mcthumb:plan` → C · `/mcthumb:check` → C.3 (kaydetmeden kontrol) · `/mcthumb:learn` → D. Teknik soruları (A) komutsuz, doğrudan sorulur. Komut dosyaları: `commands/`.

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

### C) Yeni thumbnail planla
1. `references/lessons.md` notunu oku. Konuya/biyoma uyan 2–3 referansı etiketlerinden seç ve oku.
2. Alttan üste bir katman planı öner: render'lar → NMS gölge/ışık → depth sis → Camera Raw → Layer Style → elle gölge → renk → glow → asset'ler → highlight → (yazı) → export. Her satıra ilgili teknik notunun linkini ve referanslardan gelen hex renkleri ekle.
3. Kullanıcı taslağını gönderirse script'i onun üzerinde de çalıştır. Referansla yan yana analiz listesi tablosu ve 168x94 testi yap.
4. Bitmiş işi `type: referans`, `kaynak: kendi` ile referanslara ekle.

### D) Yeni tutorial videosu öğren
`AGENTS.md` → "Yeni tutorial videosu ekleme" bölümünü uygula. Videoyu kare kare izle, değerleri ayar pencerelerinden oku. Kaynak notunu aç, teknik notlarını güncelle, bu tablodaki ve `Home.md` içindeki yönlendirmeyi güncelle.
