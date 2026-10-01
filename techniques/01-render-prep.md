---
type: teknik
order: 1
title: Render hazırlığı (Minecraft tarafı)
sources: [spare-clean-thumbnails, spare-clean-thumbnails-render-part, itsproger-blender-clean-renders]
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
- Oyuncular NPC başına ayrı, **şeffaf arka planlı** PNG olarak çıkar (Batch Screenshots). Anlatıcı bir yerde "no map shader" diyor; ekrandaki altyazı bunu **normal map shaders** olarak düzeltiyor.

## Yol A — Oyun içinde (Spare: Thumbnailing modpack + NPC Studio)
Ayrıntılı değerler: [Spare — render kısmı](../sources/spare-clean-thumbnails-render-part.md). Özet:
- **Modlar:** [Thumbnailing modpack](https://modrinth.com/modpack/thumbnailing) (Minecraft 1.21.11, Fabric). Ana modlar NPC Studio ve Iris. DMS 1.5 ve NMS 1.6 shader'ları: Iris > Shader Packs > *Download Shaders*.
- **Dünya:** Creative, Allow Commands açık; 6 Spawning kuralı kapalı; gün ilerlemesi ve hava güncellemesi kapalı.
- **NPC'ler:** Creative sekmesi "NPC studio Mod" > NPC Wand. Display sekmesinde skin, pelerin, animasyon ve 6 envanter yuvası (büyü, materyal, trim).
- **Kalabalık (Duplicate):** Square, 20x20, offset dX −1 / dZ −1, Noise X 0–0.5, eğimde Ground Snap + No Inside Blocks, yüzdeyle ağırlıklı varyantlar. Hafif olsun diye BlockNPC seçilebilir; 256 canlı NPC'nin üstünde uyarı verir.
- **World sekmesi:** Light Rotation açık (gölge yönünü belirler, örnekte 184.7). Glint Strength %120 + Freeze Animation, bulutlar donuk (Height 192). **Donuk glint ve bulutlar, bütün geçişlerin birebir aynı olmasını sağlar; katmanlar üst üste oturur.**
- **Kamera:** H tuşu. Örnekte son değerler FOV 67, Roll 0; üçte bir kılavuzu %20 opaklıkta.
- **Export:** Camera > Render > **Batch Screenshots**. Kamera × NPC grubu × shader kombinasyonlarının her biri ayrı PNG: No shader, DMS 1.5, NMS 1.6. Arazi için "No NPCs — background only" kartı. Delay 2000 ms.
- **Çözünürlük:** "Default" oyun penceresi boyutunu kullanır (dosya adları `…x1080`). Özel çözünürlük için Fabrishot mod'u gerekir.
- **DMS 1.5 ayarı:** Max. Distance 8 chunk (görüntünün siyaha döndüğü mesafe), Gradient Start 0, Invert kapalı.

## Yol B — Blender (ItsProger)
Ayrıntılı değerler: [ItsProger — Blender ile temiz render](../sources/itsproger-blender-clean-renders.md). Özet:
- **Oyuncu:** Blockbench > New > Minecraft Skin (Wide/Slim) → glTF export (scale 16, Embed Textures, Export Groups as Armature). Zırh: Armor (Main/Leggings) modelleri, kemik klasörlerine sürükle.
- **Işık:** üstte çok parlak beyaz area light, arkada ten rengi rim light, sağ altta daha koyu bir ışık; HDRI ile ortam.
- **Render:** Cycles, Noise Threshold 0.01, Denoise açık, **Film > Transparent** açık. Arka plan ve karakterleri Outliner'daki kamera ikonuyla ayrı ayrı render et.
- **Arka plan:** Minecraft ekran görüntüsü veya Mineways/jmc2obj + MCprep.
- **Poz ipucu:** uzuvları yuvalarından hafifçe kaydırmak, fazladan eklem varmış hissi verir.

> [!warning] ItsProger'ın video açıklamasına göre bazı **Mineways** indirmelerinde virüslü dosya bulunmuş. Mineways'i sadece resmi kaynaktan indir ya da jmc2obj + MCprep yolunu kullan.

## Ek ipuçları (SMP/aksiyon videolarından)
- Eldeki eşya yerine **çubuk** tutturup eşyayı Photoshop'ta değiştir. Kafayı yönlendirmek için `npc edit look` kullan. FOV 30 ve alttan açı aksiyonu güçlendirir. NewNPCs mod'unda F7 katmanları ayrı verir (Schxnappi_).
- Replay Mod'da aynı çekimi karakterli ve karaktersiz alırsan temiz bir arka plan elde edersin (Nebular). → [Aksiyon efektleri](action-effects.md)

## Çekim ipuçları (Swiffex, Unstable SMP tarzı)
- FOV **30–45** (kendisi 30). Ekran görüntüsünden önce **F1** (arayüzü gizle). F2 yerine F7 öneriyor (ekrandaki not, açıklamıyor).
- Superflat dünya, yapılar ve mob doğması kapalı. Seltop'un NewNPC mod'u (yalnızca 1.20.1). Arka plan için `/locate biome desert`.
- Aynı kameradan oyunculu ve oyuncusuz iki görüntü al: kesim temiz olur ([Yaygın hatalar](../guides/common-mistakes.md) #9).

Kaynaklar: [Spare — Clean Thumbnails](../sources/spare-clean-thumbnails.md) (6:10–6:48) · [Spare — render kısmı](../sources/spare-clean-thumbnails-render-part.md) (0:00–6:27) · [ItsProger — Blender](../sources/itsproger-blender-clean-renders.md)

Tarza göre render farkları için: [Tarz rehberi](../styles/README.md)
