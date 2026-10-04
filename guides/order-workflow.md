---
type: rehber
title: Sipariş akışı (uçtan uca, kodla taslak)
tags: [rehber, siparis, akis]
status: stabil
updated: 2026-10-01
---
# Sipariş akışı (uçtan uca)

İlk gerçek testte (split "Yükselme X", 2026-10-01) kullanıcının söyledikleri ve iş yapılırken öğrenilenlerle yazıldı. `/mcthumb:order` bu sırayı izler. Kural her adımda geçerli: **ÜŞENGEÇLİK YOK** ([AGENTS.md](../AGENTS.md)).

## Kullanıcının çalışma tercihleri
| Tercih | Ne yapılır |
|---|---|
| **Referans gelmeden tasarıma başlama** | Render'lar gelince sadece katalogla (hangi dosya hangi geçiş, kim nerede, kim yakın). Kompozisyon, renk ve efekt kararları referans gelince verilir. Kullanıcıya "neye başladın?" dedirtme. |
| Yükleme sırası: **sağ panel → sol panel → referans** | Kullanıcı mesajda "sağ panel" / "sol panel" yazar. Split işte her mesaj bir panelin render'larıdır, referans en son gelir. Dosyalar numaralı ve adsız gelebilir. **Aynı dosya iki kez gelebilir**; kopyalar atılır. |
| Render'lar masaüstündeki bir klasörde | Çok dosya olunca kullanıcı render'ları masaüstüne bir klasöre koyar (ör. `MMM`; adlar `<tarih>_<geçiş>_3840x2160_cam1_npc-<ad>-<hash>.png`, geçiş = `no-shader`, `DMS_1.6` ya da `NMS_1.7`). Dosyaları `orders/<is>/renders/` içine `<ad>-<hash4>-<geçiş>.png` adıyla kopyala, sonra katalogla. |
| Tek karakter için yeni render (skin değişikliği) | Sohbete yüklenen görseller küçülmüş gelir (ör. 2000 px webp). Aynı NPC'nin 4K orijinali Modrinth App'te profilin `screenshots` klasöründedir (`..._npc-<yeni-ad>-<aynı hash>.png`). Hash aynıysa poz aynıdır: bbox ve alfayı karşılaştır, sonra `CLAN` listesinde adı değiştir. Kullanıcının "sol/sağ" demesine değil, bbox eşleşmesine bak. |
| Referans yok | Tarzı brief'ten ve sahneden seç (Kupa işi: tek ışık kaynağı olan nesne → S2), varsayılanlarla başla: karakterler aydınlık, parlamalar hafif, arka plan bulanıklığı hafif, ortam düz değil. Referans ölçümü yerine 168x94 okunurluk ve bölge parlaklıklarıyla kontrol et. |
| Uygulamanın ayıramadığı nesne | "Uygulama kesememiş" denirse: nesne her karakter render'ına aynen kopyalanmıştır. `catalog_renders.py` uyarır; maske = bütün karakter geçişlerinde ortak opak pikseller. Karakterlerden çıkar, ayrı katman yap (NMS/DMS herhangi bir karakter geçişinden). |
| Kural her mesajda yazılmaz | Plugin hook'u (`hooks/rule.py`) kuralı ve bu tercihleri otomatik ekler. Kullanıcı yazmasa da geçerli. |
| "Planı sana bırakıyorum" | Tarzı, renk kararlarını ve yerleşimi sen seç; değişen her kararı (ör. palet referanstan farklı kaldıysa) teslimde seçenek olarak yaz. |
| Kullanıcının çıkardığı öğe konmaz | Örnek: "oku şimdilik ekleme" → ok yok. Sonra istenirse eklenir. Referanstaki her şeyi körü körüne kopyalama; brief'teki "Olmasın" listesi önce gelir. |
| **Oyun yazısı uydurulmaz** | UI metni oyunun resmi çevirisiyle (dil dosyası) ve oyunun kendi fontuyla yazılır: [`tools/mc_effect_box.py`](../techniques/text-typography.md). Benzer bir piksel font kullanılmaz. |
| **Plan yetmez** | Render varsa gerçek taslak üretilir ve gösterilir. Sadece katman planı vermek, kullanıcının gözünde "hiçbir şey yapmamak" demektir. |
| **Efektin bütün katmanları** | Karakter kenarı = dış koyu bant + kontur + içte ışık/gölge şeridi ([ölçülmüş profil](../techniques/character-pop.md)). Tek beyaz çizgi koyup geçmek kabul edilmez. |
| **İlişkiler korunur** | Referansta UI kutusu karakterin ayağının arkasındaysa taslakta da öyle. UI kutusu düz değil, 3D levha olabilir ([slab_3d](../techniques/text-typography.md)). |
| Efektler referanstaki gibi | Hız çizgilerinin **yönü, odağı**, sayısı ve kalınlığı ölçülür. Levitation referansında çizgiler kadraj kenarından başlayıp yakın karakterin kafasına doğru sivriliyordu (anime "focus lines"). İlk denemede sol alttan dışa yayılıyorlardı; kullanıcı hemen fark etti ("çizgiler ortaya doğru, sen arkaya eklemişsin"). Kalın beyaz çubuklar da "saçma" görünür. |
| UI boyutu referanstan | Kutunun boyutu gözle değil **oyun pikseli ölçeğiyle** ölçülür (harf yüksekliği 7 oyun pikseli). Kullanıcı "kutuyu azcık büyüt" dediğinde ölçüm referansın 6,0 px/oyun pikseli (1280'de) kullandığını, taslağın küçük kaldığını gösterdi. |
| Toplanan bilgi kullanılır | Videolardan ve araştırmadan gelen değerler gerçekten uygulanır. Kullanıcı "okadar datayı boşuna mı topladık?" dememeli. |
| Dil | Kullanıcıyla Türkçe konuşulur. Komut, dosya ve klasör adları İngilizce/ASCII. |
| Gizlilik | Sipariş dosyaları (render, skin, referans) sadece `orders/` altında, yerelde durur. Repoya kişisel bilgi, müşteri verisi, Mojang dosyası, video karesi girmez. Commit'lerde Claude co-author satırı olmaz. |

## Adımlar
1. **Klasör:** `orders/YYYY-MM-DD-kisa-ad/` → `brief.md` ([şablon](../templates/order.md)), `renders/` (split işte `renders/left/` ve `renders/right/`), `refs/`.
2. **Render'ları katalogla.** Referans beklenirken yapılacak tek iş budur.
   ```bash
   python3 tools/catalog_renders.py orders/<is>/renders/right
   ```
   Çıktı bir Markdown tablosu: her karakter için shader'sız / DMS / NMS eşleşmesi, bbox, DMS yakınlığı (beyaz = yakın) ve atlanan kopyalar. Tabloyu `brief.md` → "Render'lar" bölümüne koy. Dosyaları anlamlı adlarla yeniden adlandır (`p1-white-purple-nms.webp` gibi). Arka plan DMS'i tamamen siyahsa (sadece gökyüzü) script uyarır: o arka plana sis uygulanamaz.
3. **Referans gelince:** `tools/analyze_reference.py` çalıştır, görsele ve önizlemelere bak. Tarzı seç ([Tarz rehberi](../styles/README.md)).
4. **Referansı ölç** ([18 maddelik liste](../references/README.md)), en az 5x büyüterek:
   - **Konum/boyut:** her karakterin bbox merkezi ve yüksekliği. Referans boyutunda ölç, çalışma boyutuna çevir (ör. ×2000/1280).
   - **Renkler:** gökyüzü tabanı, bulut, zemin, karakter (5x5 ortalama).
   - **Kenar profili:** kenara dik bir piksel satırı (dış bant, kontur, iç şerit; ışık ve gölge tarafı ayrı).
   - **Katman sırası:** kim kimin önünde, UI neyin arkasında, ayak neyin üstüne geliyor.
   - **Efekt stili:** hız çizgilerinin odağı ve yönü (her çizgi: açı, sivri ucun odağa uzaklığı, genişlik, opaklık), parlama, ayırıcı kalınlığı ve açısı.
   - **UI ölçeği:** oyun yazısının harf yüksekliğinden px/oyun pikseli; kutunun genişliği (oyun pikseli cinsinden), eğimi ve 3D kalınlığı.
5. **Taslak üret:** `orders/<is>/compose.py`, `tools/thumbkit.py` ile (aşağıdaki "compose iskeleti").
6. **Yan yana karşılaştır, tekrar ölç:**
   ```bash
   python3 tools/compare.py refs/ref.webp thumbnail-2000x1125.png -o /tmp/kars \
       --crop 1100,200,1180,300=1110,250,1190,350 \
       --profile 255,1160,1178=300,1150,1168 \
       --color 1180,255=1175,300
   ```
   Çıktılar: `tam.png` (üstte referans, altta taslak), `kesitler.png` (büyütülmüş çiftler), piksel profilleri, renk farkları ve ortalama parlaklık. Koordinatlar varsayılan olarak referans boyutundadır. Fark varsa `compose.py` değerini düzelt, tekrar üret, tekrar ölç. Kesit almadan önce kenarın yerini satır farkı taramasıyla bul; tahminle alınan kesitte karakter çıkmayabilir.
7. **Export:** `export()` → tam boyut PNG, 1920x1080 PNG ve JPG (q92, 2 MB altı). Teslimde 3840x2160 isteniyorsa render'ları o boyutta al; küçük render'ı büyütmek bulanıklaştırır.
8. **`brief.md` güncelle:** son uygulanan değerleri (plan değerleri değil) "Referanstan uyarlanan ayarlar" tablosuna yaz, `status: taslak`.
9. **Teslim mesajı:** taslağı referansla yan yana göster. Kalan her farkı nedeniyle yaz (ör. "pembe karakterin göğsündeki çapraz gölge NMS'ten çıkmıyor, elle gölge gerekir"). Sonra sadece işi durduran soruları sor.

## compose iskeleti
Testte kullanılan değerlerle (split işte iki panel ayrı kurulur ve `split()` ile birleşir; bkz. [S4](../styles/04-split-progression.md)):
```python
import sys; sys.path.insert(0, '../../tools')
from thumbkit import *
W, H = 2000, 1125; SKY = hexrgb('#C4DCFA')            # ortam/sis rengi = referans gökyüzü tonu

# arka plan: NMS gölge → renk → depth sis (gökyüzüne gölge verme: valid = DMS > 0)
bg, nms = load('renders/bg-noshader.webp'), load('renders/bg-nms.webp')
dms = A(load('renders/bg-dms.webp'))[..., 0]
bg, _ = nms_shade(bg, nms, shadow=0.22, light=0.12, valid=(dms > 0.02).astype(np.float32))
bg = depth_fog(grade(bg, sat=1.28, con=1.06), dms, SKY)
# sadece gökyüzü (DMS siyah): sis yok, ölçülen iki renk çiftiyle referansa eşle
# bg = remap(load('renders/bg-sky-noshader.webp'), (168,204,252), (112,174,254), (222,234,252), (175,208,253))

def char(name):                                         # NMS → ambient → renk → 3 katmanlı kenar
    c, _ = nms_shade(load(f'renders/{name}-noshader.webp'), load(f'renders/{name}-nms.webp'), shadow=0.30, light=0.14)
    c = grade(ambient(c, SKY, glow=0.15, size=10, grad=0.06), sat=1.30, con=1.15)
    return outline(c, stroke_px=3, outer_alpha=0.10)

canvas = bg.copy()
place_fit(canvas, char('p3'), (1422, 218), 141)        # uzaklar önce; hedef = referanstan ölçülen merkez + yükseklik
FOCUS = [(64.2, 386), (80.2, 483), (127.2, 702)]       # odak çizgileri: (açı°, sivri ucun odağa uzaklığı), referanstan ölçülür
canvas.alpha_composite(speed_lines(canvas.size, (1625, 166), FOCUS))   # odak = yakın karakterin kafası; karakterlerin ARKASINA
flat = Image.open('assets-made/effect.png').convert('RGBA')      # mc_effect_box.py --scale 10 --width 95
flat = flat.resize((round(flat.width * 0.9375), round(flat.height * 0.9375)), Image.NEAREST)  # ref: 9,4 px / oyun pikseli
slab = slab_3d(flat, depth=10, tilt=1.3, persp=(4, 14, 10))
bx, by, bx1, by1 = slab.getchannel('A').getbbox()     # kutuyu referanstaki kutunun merkezine oturt
pos = (round(1486 - (bx + bx1) / 2), round(919 - (by + by1) / 2))
canvas.alpha_composite(drop_shadow(slab), (pos[0] + 10, pos[1] + 12)); canvas.alpha_composite(slab, pos)
place_fit(canvas, char('p1'), (1672, 363), 539)        # yakınlar UI'nin önünde (ayak kutunun üstüne biner)
export(canvas, 'thumbnail')
```

## Tuzaklar (yaparken öğrenilenler)
| Tuzak | Belirti | Çözüm |
|---|---|---|
| Tek eşikle NMS tanımak | Balkabağı skini NMS sanılır, gerçek NMS kaçırılır | Aynı gruptaki geçişleri karşılaştır: "birim normal oranı − doku" skoru en yüksek olan NMS. `catalog_renders.py` bunu yapar. |
| Oyuncu dış katmanının normali ters | Ceket/şapka katmanı ters ışık alır | `nms_shade` x bileşeninin mutlak değerini kullanır. Kenarın ışık/gölge tarafı NMS'ten değil, alfa kenarının yönünden hesaplanır (`edge_sides`). |
| Sadece gökyüzü olan arka plan | DMS tamamen siyah | Sis yok. Uzak karakteri `tint()` ile ortam rengine çek, gökyüzünü `remap` ile referans rengine eşle. |
| RGBA'yı şeffaf siyahla bulanıklaştırmak | Beyaz çizgilerin etrafında gri hale | Sadece alfa maskesini (L) bulanıklaştır, beyazla birleştir: `white(size, alpha)`. |
| Ambient fazla | Karakterler soluk, yıkanmış | glow 0.15, grad 0.06; ardından sat 1.30, con 1.15. |
| Gözle tahmin | Gökyüzü çok açık, kutu küçük, karakterler yanlış yerde | `compare.py --color` ve bbox ölçümü, `remap`, `place_fit`. |
| Hız çizgileri ters yönde | Çizgiler bir köşeden dışa yayılıyor; referansta ise odağa doğru sivriliyor | Odağı ölç: çizgileri kenardan içe doğru izle, en küçük kareler kesişimini bul (Levitation: 1280'de (1040,106), P1'in kafası). `speed_lines(size, focus, [(açı, r0), ...])`. |
| UI kutusunun genişliği oyundaki gibi değil | Oyunda kutu 120 oyun pikseli, referansta ~96 (yazıya göre) | `mc_effect_box.py --width 95` (0 = yazıya göre). Ölçeği harf yüksekliğinden al. |
| Ayak yazının üstüne biner | "Yü" harfleri kapanır | Kutunun ölçeğini ve genişliğini referanstan ölçünce yazı referanstaki yerine gelir ve karakter referans konumunda kalabilir. Ayak **ikonun** üstüne ve yazının hemen soluna gelsin. Sapma olursa teslimde yaz. |
| Font dosyasını `unzip -j` ile çıkarmak | `default.json`, `include/default.json` ile ezilir | Klasör yapısını koru. `mc_effect_box.py` jar'dan doğrudan okur. |
| Font sağlayıcısı `reference` | `default.json` içinde bitmap yok, araç hata verir | `reference` sağlayıcılarını özyinelemeli çöz (`include/space`, `include/default`, `include/unifont`). |
| Birden çok NPC render'ı üst üste | NPC'ler birbirini doğru kesmiyor | NPC'ler tek tek render edilir, birbirini kesmez. Piksel başına en yakın DMS'i seçen z-buffer ile birleştir (Trim klanı `compose.py`). |
| NPC'yi tek başına taşımak | Önündeki kök/ot bloklarının deliği yerinde kalmaz | NPC render'ları dünya bloklarıyla kesik gelir. Ya hiç taşıma ya da sahnenin tamamını (arka plan + bütün NPC'ler) birlikte ölçekle. |
| Kenar ışığını beyaz eklemek | Siyah şapka ve gözlükte beyaz hale | Işık yüzey rengiyle **çarpılır**: rgb = yüzey × (anahtar ışık + kenar ışığı). Siyah yüzey ışık almaz. |
| Işıyan öğe ortamla aynı renkte | Kırmızı trim kırmızı Nether'de kaybolur | Ortamın doygunluğunu düşür (referansta ortam 0,15–0,26, karakterler doygun). Işıyan pikselleri desatürasyondan önce ayır. |
| Mutlak eşikle hale ölçmek | Taslaktaki parlak hale "çekirdek" sayılır, oranlar tutmaz | `tools/glow_profile.py` göreli eşik kullanır: iki görselde aynı tanım. |
| Render'da sönük ışık kaynağı | Lav (128,48,0) gibi sönük, maske yakalamaz | Rengini tanımla (turuncu: R > 1,8 G, G > 0,2 R, B ≈ 0), ×1,9 parlat, geniş bloom ver. |
| İkili alfa (yumuşatma yok) | 4K'da tırtıklı kenar | Görünürlük maskesini ~1 px bulanıklaştır. |
| Render'da metal yüzler düz | Altın kupa tek renk sarı leke gibi, hale silüeti yutar | Yüzleri NMS yönüne göre elle gölgele (üst ×1,25, ön ×0,82, yan ×0,55), `gradient_map` ile altın rampası; haleyi yalnız parlak yüzlerden çıkar ([09 Glow](../techniques/09-glow.md)). |
| Kenar ışığı skin'in iç boşluklarına uygulanır | Dış katman ile kol arasında ince parlak çizgiler | Kenar ışığını boşlukları kapatılmış silüete uygula (`blur(alfa) > 0,35`). Çizgi kalırsa **önce ham render'a bak**: skin'in kendi detayı olabilir (Kupa işinde bileklik). |

İlgili: [Referansa göre uyarlama](../techniques/adapt-to-reference.md) · [Dikkat edilecekler](pitfalls.md) · [Yaygın hatalar](common-mistakes.md) · [Referanslardan öğrenilenler](../references/lessons.md)
