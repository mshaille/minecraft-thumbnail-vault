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
