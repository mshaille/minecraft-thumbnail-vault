# AGENTS.md — bu vault'ta çalışan yapay zekâ oturumları için

## Bu nedir?
Minecraft YouTube thumbnail'lerini Photoshop/Photopea ile yapma bilgisi. Kullanıcı tutorial videolarını izletir, Claude kare kare izleyip **kesin değerleriyle** not alır. Aynı klasör üç şeydir:
1. **Obsidian vault**: giriş notu [Home.md](Home.md).
2. **Claude Code plugin** `mcthumb` (skill: `skills/minecraft-thumbnail/SKILL.md`). Yerel kurulumda `~/.claude/skills/mcthumb` bu klasöre symlink olur (README).
3. **GitHub reposu**: herkese açık. Push öncesi aşağıdaki "Yapma" listesine bak.

Notlar Türkçe yazılır. Yanıtlar kullanıcının dilinde verilir.

## Klasörler
| Klasör | İçerik |
|---|---|
| `techniques/` | 1 not = 1 teknik/adım, kesin ayarlarla. `order` alanı süreç sırasıdır. |
| `styles/` | Tarz rehberi (`README.md`: karar rehberi, matris, trendler) + her tarz için bir kart (S1–S11). Sipariş önce tarz seçer. |
| `guides/` | Konu dışı ama kritik rehberler: `pitfalls.md` (politika, telif, sipariş), `common-mistakes.md`. |
| `sources/` | 1 not = 1 tutorial video: zaman damgası → teknik notu tablosu. |
| `references/` | Referans görsel notları, `images/`, `lessons.md`, `gallery.base`. |
| `templates/` | Obsidian şablonları: `teknik.md`, `video-source.md`, `referans.md`. |
| `tools/` | `analyze_reference.py` (Pillow): boyut, oran, palet, parlaklık/doygunluk, 120/168 px önizleme. `mc_effect_box.py`: oyunun kendi font/kutu/ikon dosyalarıyla efekt kutusu PNG'si (Mojang dosyaları repoya konmaz). |
| `dev/` | Yol haritası, değişiklik günlüğü. |
| `skills/minecraft-thumbnail/` | Skill giriş noktası (SKILL.md). |
| `.claude-plugin/` | Plugin ve marketplace manifestleri. |
| `commands/` | Plugin slash komutları: `/mcthumb:order`, `/mcthumb:ref`, `/mcthumb:check`, `/mcthumb:learn`. |
| `assets/` | Logo ve banner (SVG kaynak + PNG). Özgün tasarım: normal-map renkli voxel küp + highlight çizgisi. |
| `orders/` | **Sadece yerel** (gitignore). Müşteri siparişleri: `orders/YYYY-MM-DD-kisa-ad/brief.md` + `refs/`. `/mcthumb:order` oluşturur. |
| `local/` | **Sadece yerel** (gitignore). Videolardan alınmış ayar ekranı kareleri. Değer doğrulamak için Read ile bakılabilir. |

## Kurallar
- **Dosya adları:** ASCII kebab-case, Türkçe karakter ve boşluk yok (ı→i, ş→s, ğ→g, ç→c, ö→o, ü→u). Türkçe başlık H1'e ve `title` alanına yazılır.
- **Linkler:** gövdede standart göreli markdown linki kullanılır (`[x](../techniques/x.md)`), çünkü GitHub wikilink göstermez. Wikilink sadece frontmatter'da, tırnak içinde (`gorsel: "[[ref-....png]]"`).
- **Frontmatter:** her notta `type` olur (teknik | kaynak | referans | index | ozet | gelistirme). Etiketler küçük harf ve ASCII.
- **Değerler kesin olmalı:** menü yolu + değer + birim (ör. "Fuzziness 200", "Opacity %18"). Videoda değer değiştiyse ekranda kalan son değer yazılır ve bu belirtilir.
- **Kaynaklar çelişirse** ikisini de kaynak adıyla yaz, sessizce üzerine yazma. Çelişki çoğu zaman **tarz farkıdır**: değeri ilgili tarz kartına ve teknik notunun "Tarz farkı" bölümüne yaz. Kullanıcı denemediği yeni içeriğe `status: taslak` ver.
- **Telif:** video transkriptini veya uzun alıntıları kopyalama, kendi cümlelerinle özetle. Video karelerini sadece `local/` klasörüne koy, asla commit'leme.

## Yeni tutorial videosu ekleme
1. Videoyu izle. Transkripti al, sonra ilgili kısmı kare kare incele. Ayar pencerelerini kırpıp büyüterek sayıları oku.
2. `templates/video-source.md` şablonundan `sources/<kanal>-<konu>.md` notunu oluştur. Zaman damgalarını teknik notlarına linkle.
3. Her teknik için mevcut `techniques/` notunu güncelle veya `templates/technique.md` şablonuyla yeni not aç. Gerekirse `order` sırasını koru.
4. `Home.md` tablosunu, `skills/minecraft-thumbnail/SKILL.md` içindeki yönlendirme tablosunu ve `dev/changelog.md` notunu güncelle.
5. Önemli ayar karelerini istersen `local/video-frames/` klasörüne koy.

## Yeni referans görsel ekleme
`references/README.md` içindeki adımları izle: dosyayı adlandır, `tools/analyze_reference.py` çalıştır, görsele ve önizlemelere bak, şablondan not aç, 15 maddelik listeyi doldur, teknikleri linkle, `lessons.md` notunu güncelle.
Görseller en fazla ~1280x720 ve ~500 KB (JPG/WebP) olsun. Başkasının thumbnail'ini herkese açık repoya koymadan önce kullanıcıya sor. Gerekirse `local/` altında tut.

## Yapma
- `.obsidian/` içinde sadece `app.json`, `core-plugins.json`, `templates.json` repoya girer. Community plugin ekleme.
- PSD/PSB commit'leme.
- `local/` ve `orders/` klasörlerini commit'leme. Müşteri verisini (sipariş, skin, referans) public repoya koyma.

## Kontrol
- `claude plugin validate .` → manifest + skill doğrulaması
- Kırık link kontrolü: tüm `](...md)` linklerinin hedefi var mı (README'deki komut)
