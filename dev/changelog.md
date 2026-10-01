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
