---
type: kaynak
title: "Fixing Your Minecraft Thumbnails!"
creator: Pqtrick
url: https://www.youtube.com/watch?v=8W67cb0JJBM
duration: "7:07"
published: 2025-08-02
watched: "tamamı: transkript + kare kare (3 yeniden tasarım, önce/sonra)"
watched_on: 2026-10-01
tags: [kaynak, video, elestiri, yeniden-tasarim, kompozisyon, photopea, vanilla, temiz]
---
# Pqtrick — Fixing Your Minecraft Thumbnails!

- Video: <https://www.youtube.com/watch?v=8W67cb0JJBM>
- Biçim: Discord'dan gelen 3 thumbnail önce eleştiriliyor, sonra sıfırdan yeniden çekilip düzenleniyor, en sonda önce/sonra gösteriliyor.
- Editör: **Photopea** (koyu tema, ücretsiz sürüm). Kamera için **Flashback** modu, 3. örnekte **NPC modu** kullanılıyor (Flashback kaydında custom NPC görünmüyor). Başlık yazısı **Blockbench**'te 3D yapılıyor.
- Stil: shader'sız, temiz "vanilla Minecraft" görünümü. Az efekt, güçlü konsept.

## Zaman damgası → teknik notu
| Zaman | Konu | Not |
|---|---|---|
| [0:16](https://www.youtube.com/watch?v=8W67cb0JJBM&t=16s) | 1. örnek: "Assassination Series" eleştirisi | Konsept sıkıcı: sadece trident tutan karakter. → [Analiz listesi](../references/README.md) madde 1, 4 |
| [0:47](https://www.youtube.com/watch?v=8W67cb0JJBM&t=47s) | Yeni konsept: havada, trident + parçacıklar | Aksiyon anı. → [01 Render hazırlığı](../techniques/01-render-prep.md) |
| [1:23](https://www.youtube.com/watch?v=8W67cb0JJBM&t=83s) | Karakteri kesip gökyüzünden ayırma | Karakter ve gökyüzü ayrı katman. |
| [1:41](https://www.youtube.com/watch?v=8W67cb0JJBM&t=101s) | Kesim artıklarını temizleme | Yeni katman → damlalıkla yakındaki rengi al → artığın üstünü boya. |
| [2:04](https://www.youtube.com/watch?v=8W67cb0JJBM&t=124s) | Gökkuşağı parçacık denemesi | Başka bir thumbnail'den ilham. Denendi, **vazgeçildi**. |
| [2:25](https://www.youtube.com/watch?v=8W67cb0JJBM&t=145s) | Yazı kararı | Normalde başlığı thumbnail'e yazma. Seri/trailer adında istisna. Fontu değiştir. |
| [2:41](https://www.youtube.com/watch?v=8W67cb0JJBM&t=161s) | Yazım hatası + renk | Orijinalde kelime yanlış yazılmış. Mavi arka plana **tamamlayıcı turuncu** daha iyi. |
| [3:06](https://www.youtube.com/watch?v=8W67cb0JJBM&t=186s) | Blockbench'te 3D başlık | Altın renkli, Minecraft logosu tarzı 3D yazı, PNG olarak içeri. |
| [3:23](https://www.youtube.com/watch?v=8W67cb0JJBM&t=203s) | Arka plan sadeleştirme | Önce kara + su vardı, boş/karışık durdu. Sadece su + gökyüzü olan yeni çekim alındı. → [10 Gökyüzü](../techniques/10-sky-and-assets.md) |
| [3:44](https://www.youtube.com/watch?v=8W67cb0JJBM&t=224s) | Camera Raw (bg ve title) | Değerler aşağıda. → [05 Camera Raw](../techniques/05-camera-raw.md) |
| [3:45](https://www.youtube.com/watch?v=8W67cb0JJBM&t=225s) | Ayırıcı gölge | Ellipse + boya + Gaussian Blur 50 px. → [07 Elle gölge](../techniques/07-hand-shadows.md) |
| [4:02](https://www.youtube.com/watch?v=8W67cb0JJBM&t=242s) | 2. örnek: su kovası clutch | Daha "heyecanlı" olsun diye Nether'de tekne clutch'a çevrildi. |
| [4:53](https://www.youtube.com/watch?v=8W67cb0JJBM&t=293s) | 2. örnek önce/sonra | Düzenleme kaydı kaybolmuş. Yaratıcı **orijinali daha çok beğendiğini** söylüyor. |
| [5:06](https://www.youtube.com/watch?v=8W67cb0JJBM&t=306s) | 3. örnek: "sunucuyu mahvetti" eleştirisi | Ana hata: başlık söylüyor, görsel göstermiyor. |
| [5:49](https://www.youtube.com/watch?v=8W67cb0JJBM&t=349s) | Krater haritası + gökyüzü sınırına kule | Yüksek açıdan, kraterin ölçeği görünüyor. |
| [6:16](https://www.youtube.com/watch?v=8W67cb0JJBM&t=376s) | Oyunculu ve oyuncusuz iki çekim | Aynı kamera. Oyuncu kesilince arkada boşluk kalmıyor. |
| [6:38](https://www.youtube.com/watch?v=8W67cb0JJBM&t=398s) | Outer Glow mı, gölge mi? | Oyuncuda glow denendi, kapatıldı, Drop Shadow kaldı. TNT'ye kırmızı Outer Glow. → [06 Layer Style](../techniques/06-layer-style-ambient-light.md), [09 Glow](../techniques/09-glow.md) |
| [6:46](https://www.youtube.com/watch?v=8W67cb0JJBM&t=406s) | 3. örnek önce/sonra | Yazı yok, hikâyeyi sahne anlatıyor. |

## Ekranda okunan ayarlar (Photopea)
**Camera Raw** (Filter > Camera Raw, smart object üstünde smart filter). `bg` ve `title` katmanında aynı değerler. `skin` (karakter) katmanında filtre yok.
| Exposure | Contrast | Highlights / Shadows / Whites / Blacks | Temp / Tint | **Vibrance** | Saturation | Texture | Clarity | Dehaze |
|---|---|---|---|---|---|---|---|---|
| 0 | +10 | 0 | 0 | **+100** | 0 | +10 | +10 | 0 |

**Ayırıcı gölge** (1. örnek, 3:45): `shadow` katmanı karakter ve başlığın altında, `bg`'nin üstünde. History sırası: Ellipse Select → Paint Bucket → Move → Layer Opacity Change → Deselect → **Gaussian Blur, Radius 50 px**. Opacity değeri ekranda okunmadı.
- Son katman sırası (yukarıdan aşağı): `skin` → `title` (+Camera Raw) → `shadow` → `bg` (+Camera Raw).

**Layer Style** (3. örnek, 6:38–6:46, 49x hızlı):
- Oyuncuda önce **Outer Glow** denendi: Screen, Opacity %50, beyaz, Softer, Spread 0, Size 50→100 px, Range %100. Sonra kapatıldı.
- Oyuncuda kalan **Drop Shadow**: Multiply, siyah, Opacity %50, Angle 45° (Use Global Light ✓), **Distance 0**, Spread 0, **Size 200 px**, Noise 0, Knock Out ✓. Uzaklık 0 olduğu için kenar boyunca koyu, yumuşak bir hale oluşur.
- TNT (ayrı katman) **Outer Glow**: Screen, Opacity %100, **kırmızı**, Softer, Spread 0, Size 50/100/200 px arasında değişti (ekranda son görülen **200 px**), **Range %50**, Jitter 0.

## Eleştiriden çıkan dersler
- **Önce konsept.** Bir eşyayı tutup duran karakter sıkıcıdır. Bir eylem anı seç: havada, parçacıklı, düşerken, patlamadan önce.
- **Anlatma, göster.** Başlık "sunucuyu mahvetti" diyorsa sahne bunu kanıtlamalı: dev krater, gökyüzüne kadar kule, elde TNT. Başlığı tekrar eden yazı bir şey katmaz. 3. örnekte yazıya hiç gerek kalmadı.
- **Başlığı yazıya dökme.** İstisna: seri ya da trailer adı gibi başka söylenecek bir şey yoksa. O zaman bile font Minecraft tarzında olsun (ör. Blockbench 3D başlık).
- **Yazım hatasını kontrol et.**
- **Yazı rengi arka planın tamamlayıcısı olsun:** mavi gökyüzü/su → turuncu/altın.
- **Arka planı sadeleştir.** Boş ya da karışık arazi yerine tek bir sade yüzey (su + gökyüzü) karakteri öne çıkarır.
- **Ayrışma için az efekt yeter.** Karakterin arkasına yumuşak koyu gölge koymak, Minecraft görünümünü bozmadan ayrıştırır. "Fancy" efekte gerek yok.
- **Kesim kenarlarını temizle.** Arka plandan kalan pikselleri yakındaki renkle boya.
- **Daha heyecanlı konsept her zaman daha iyi thumbnail değildir.** 2. örnekte yaratıcı kendi sonucunu beğenmedi. Kare gözlemi: orijinalde parlak mavi + sarı/kırmızı kalın yazı var, yeniden tasarımda koyu Nether kırmızısı ve ince piksel font. Renk ve kontrast kaybı, konseptin kazancını götürmüş olabilir.

## Kare gözlemleri (videoda söylenmiyor)
- 1. örneğin orijinali: karakter neredeyse siyah gece arka planında kayboluyor. "OFFICIAL TRAILER" yazısı **sağ alt köşede**, süre rozetinin altında kalıyor → [Analiz listesi](../references/README.md) madde 15.
- 3. örnekte kompozisyon: oyuncu solda, krater sağda büyük koyu bir kütle. Kuş bakışı açı ölçeği gösteriyor.

## İzleme notları
- Video hızlandırılmış (29x–100x). Değerler bazı karelerde değişiyor, ekranda kalan son değerler yazıldı.
- 2. örneğin düzenleme kaydı kaybolmuş, sadece önce/sonra var.
