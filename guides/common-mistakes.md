---
type: rehber
title: Yaygın hatalar ve düzeltmeleri
sources: [pqtrick-fixing-thumbnails]
tags: [rehber, hatalar, kompozisyon]
status: stabil
---
# Yaygın hatalar ve düzeltmeleri

Profesyonel eleştiri/yeniden tasarım videolarından derlendi. Politika ve telif hataları için: [Dikkat edilecekler](pitfalls.md).

| # | Hata | Düzeltme | Tarz |
|---|---|---|---|
| 1 | **Sıkıcı konsept:** karakter elinde eşyayla öylece duruyor | Aksiyon anı seç: havada, partiküllerle, kritik bir hamlenin ortasında | hepsi |
| 2 | **Söylüyor ama göstermiyor:** başlık "sunucuyu mahvetti" diyor, görselde sadece yazı var | Kanıtı göster: dev krater, gökyüzüne uzanan sütun, elde TNT. Gösterince yazıya gerek kalmaz. | hepsi |
| 3 | **Başlık yazısı thumbnail'a kopyalanmış** | Yapma. İstisna seri/fragman adı; o zaman Minecraft tarzı 3D başlık ([Yazı](../techniques/text-typography.md)) | hepsi |
| 4 | **Yazım hatası** | Teslimden önce oku | hepsi |
| 5 | **Yazı rengi arka planla ilgisiz** | Tamamlayıcı renk: mavi gökyüzü/su → turuncu/altın | yazılı |
| 6 | **Kalabalık veya boş arka plan** | Tek sade yüzeyle yeniden çek (ör. sadece su + gökyüzü). Kareyi doldur, kenarlar boş kalmasın. | hepsi |
| 7 | **Konu arka plana karışıyor** | Karakterin arkasına yumuşak koyu gölge (Gaussian Blur 50 px) veya Distance 0 Drop Shadow ([Aksiyon efektleri](../techniques/action-effects.md)) | hepsi |
| 8 | **Kesimin etrafında arka plan pikselleri kalmış** | Yeni katman, yakındaki rengi damlalıkla al, kalıntıları boya | hepsi |
| 9 | **Karakteri kesmek zor** | Aynı kameradan iki ekran görüntüsü: oyunculu ve oyuncusuz. Temiz arka plan sayesinde arkada delik kalmaz. | hepsi |
| 10 | **Önemli öğe sağ alt köşede** (süre etiketinin altında) | Sağ alt ve alt kenarı boş bırak | hepsi |
| 11 | **Daha "heyecanlı" ama renk ve kontrastını kaybetmiş tasarım** | Parlaklık ve kontrast konsepten önemlidir; Pqtrick bir yeniden tasarımda orijinali daha iyi buldu (parlak mavi + kalın sarı/kırmızı yazı > koyu kırmızı + ince piksel font). | hepsi |
| 12 | **Tutarsız ışık:** highlight'lar farklı yönlerden geliyor | Tek ışık yönü seç; gölge, highlight ve rim aynı yöne uysun ([uyarlama](../techniques/adapt-to-reference.md)) | hepsi |
| 13 | **Karakter yazıyı kapatıyor**, hikâye öğeleri karışık sırada | Yazıyı karakterin önüne/üstüne değil yanına koy; hikâyeyi soldan sağa diz | yazılı |
| 14 | **Bulanık parlayan yazı**, gereksiz drop shadow, genel renk kayması | Yazı keskin kalsın; işe yaramayan efekti sil; renk dengesini kontrol et | hepsi |

Satır 12–14: zestu'nun "Judging YOUR Minecraft Thumbnails" (L07Khs5HeqI) videosunun transkriptinden (not henüz yazılmadı, [Yol haritası](../dev/roadmap.md)).

Kaynak: [Pqtrick — Fixing Your Minecraft Thumbnails](../sources/pqtrick-fixing-thumbnails.md)
