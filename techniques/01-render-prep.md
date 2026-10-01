---
type: teknik
order: 1
title: Render hazırlığı (Minecraft tarafı)
sources: [spare-clean-thumbnails]
tags: [teknik, render, nms, dms]
status: stabil
---
# 1. Render hazırlığı (Minecraft tarafı)

Photoshop'a geçmeden önce Minecraft'tan **aynı kamera açısıyla**, **1920x1080** boyutunda ayrı ayrı render alınır. Her render ayrı bir katman olur.

| Render | Ne işe yarar | Sonraki adım |
|---|---|---|
| Arazi, shader'sız, NPC'ler gizli ("background only") | Ana arka plan | [Belge kurulumu](02-document-setup.md) |
| Arazi, **NMS** (normal map shader). Yüzler yöne göre kırmızı/yeşil/mavi görünür | Hangi yüzün gölgede, hangisinin ışıkta kalacağını seçmek | [NMS gölgelendirme](03-nms-shading.md) |
| Oyuncular ayrı, şeffaf arka planlı | Ana karakterler | [Ortam ışığı (Layer Style)](06-layer-style-ambient-light.md) |
| Oyuncuların NMS render'ı | Oyunculara da aynı gölgelendirme | [NMS gölgelendirme](03-nms-shading.md) |
| Kalabalık (çoğaltılmış NPC'ler) ayrı katman | Arka plandaki kalabalık | [Camera Raw](05-camera-raw.md) |
| **DMS** (depth map shader). Gri tonlu derinlik: yakın = beyaz, uzak = siyah | Sis/atmosfer maskesi | [Depth map sis](04-depth-map-fog.md) |

- NMS = normal map shaders, DMS = depth map shaders.
- Oyuncuları ayırmak için videoda "no map" shader ile oyuncuların etrafında beyaz maske alınıyor.
- Render için kullanılan modpack: <https://modrinth.com/modpack/thumbnailing> (NPC Studio ile karakter/kalabalık dizme). Ayrıntılar videonun 0:00–6:27 kısmında. O kısım henüz not alınmadı, bkz. [Yol haritası](../dev/roadmap.md).

Kaynak: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (6:10–6:48)
