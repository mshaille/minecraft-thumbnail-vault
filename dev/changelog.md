---
type: gelistirme
title: Değişiklik günlüğü
tags: [gelistirme]
---
# Değişiklik günlüğü

## 2026-10-01
- Vault oluşturuldu. İki video kare kare izlenip notlara döküldü: [Spare](../sources/spare-clean-thumbnails.md) (6:27 sonrası), [zestu](../sources/zestu-highlights.md) (tamamı).
- 12 teknik notu, referans kütüphanesi, şablonlar ve `tools/analyze_reference.py` eklendi.
- Skill (`skills/minecraft-thumbnail/SKILL.md`) ve Claude Code plugin paketlemesi eklendi.
- Slash komutları (`commands/`), özgün logo ve banner (`assets/`), İngilizce README ve MIT lisansı eklendi.
- Klasör ve dosya adları İngilizce yapıldı (içerik Türkçe). Plugin adı `mcthumb`, komutlar: `/mcthumb:ref`, `:plan`, `:check`, `:learn`.
- Sipariş akışı: `/mcthumb:order` (istekler + referans resimler → uyarlanmış ayarlar ve katman planı), `templates/order.md`, `techniques/adapt-to-reference.md`. `orders/` sadece yerel. `/mcthumb:plan` yerine `/mcthumb:order` geldi.
- 5 ajanla araştırma: 7 yeni video kaynağı (render: Spare 0:00–6:27 + Blender; SMP/aksiyon; eleştiri; Photopea), `styles/` (11 tarz kartı + karar rehberi + matris + trendler), `guides/` (dikkat edilecekler, yaygın hatalar), yeni teknik notları (character-pop, text-typography, action-effects, style-catalog). Sipariş akışı artık önce tarz seçiyor. `01-render-prep` notundaki "no map" ifadesi düzeltildi.
- İlk gerçek test (split sipariş): `tools/mc_effect_box.py` eklendi (oyunun kendi fontu/kutusu/ikonuyla efekt kutusu; resmi Türkçe ad dil dosyasından). Sipariş şablonuna render listesi bölümü eklendi.
- Testten sonra: `tools/thumbkit.py` (teknikler kod olarak) eklendi; `/mcthumb:order` artık plan + gerçek taslak üretiyor ve referansla yan yana kontrol ediyor. Analiz listesi 18 maddeye çıktı (karakter etrafı, katman sırası, 3D UI, hız çizgisi stili).
- KURAL eklendi: ÜŞENGEÇLİK YOK — mükemmellik aranır (AGENTS, SKILL, tüm komutlar). thumbkit: `outline()` (ölçülmüş 3 katmanlı kenar), `remap()` (ölçülen renklerle eşleme), `place_fit()` (referans konum/boyutuna yerleşim).
- Öğrenilenler işlendi: [Sipariş akışı](../guides/order-workflow.md) rehberi (kullanıcının çalışma tercihleri, uçtan uca adımlar, `compose.py` iskeleti, kodla üretim tuzakları). AGENTS ve SKILL'e "Kullanıcının çalışma tercihleri" bölümü.
- Yeni araçlar: `tools/catalog_renders.py` (render geçişlerini tanır/eşleştirir, kopyaları atar, siyah DMS uyarısı) ve `tools/compare.py` (taslağı referansla ölçer: yan yana, kesit, piksel profili, renk farkı).
- thumbkit: `speed_lines` artık ölçülmüş **odak çizgileri** (kenardan odağa sivrilen üçgenler; ilk sürüm ters yönde dışa yayılıyordu). `mc_effect_box.py --width` (kutu yazıya göre daraltılabilir).
- Teknik notlarına testte ölçülen değerler: NMS renk tablosu ve ters normal, siyah DMS ve `remap`, efekt kutusu ölçeği ve 3D levha, odak çizgileri, S4 doğrulanmış değerler.

## 2026-10-03
- İkinci gerçek sipariş: "Trim klanı" (S2b sinematik-karanlık + S1). Render'lar masaüstündeki bir klasörden, adlı dosyalar (3840x2160, no-shader/DMS 1.6/NMS 1.7, 10 NPC + arka plan). Teslim 4K.
- [09 Glow](../techniques/09-glow.md): ölçülmüş **ışıyan trim** tekniği (maske, gölgesiz çekirdek, üç katmanlı hale, ortam desatürasyonu). thumbkit: `bloom()`, `screen()`; `export()` artık tam boy JPG'yi 2 MB altına sığdırıyor.
- Yeni araçlar: `tools/zoom.py` (ızgaralı büyütülmüş kesit), `tools/glow_profile.py` (hale ölçümü, göreli çekirdek eşiği).
- Sipariş akışı: render'ların masaüstü klasöründen gelmesi, "planı sana bırakıyorum", çoklu NPC z-buffer birleştirme, NPC'lerin dünya bloklarıyla kesik gelmesi, ışığın yüzey rengiyle çarpılması, sönük ışık kaynağı tuzakları. S2 kartına doğrulanmış değerler, uyarlama tablosuna üç satır.
- Trim klanı revizyonları: sol karakter aydınlatıldı, trim parlaması "çok hafif"e indirildi (referansın ~%20'si), ortam "düz" bulununca sinematik geçiş eklendi. thumbkit: `gblur`, `dof`, `god_rays`, `particles`, `vignette`, `split_tone`; kataloğun N3/N5/N7/N9/N15 satırlarına kod karşılıkları.
