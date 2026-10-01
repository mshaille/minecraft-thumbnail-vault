---
type: kaynak
title: How to Make CLEAN Minecraft Thumbnails (Free) — Render kısmı (0:00–6:27)
creator: Spare
url: https://www.youtube.com/watch?v=5XbxbzdN0x0
duration: "13:48"
watched: "0:00–6:27 (Minecraft / NPC Studio kısmı), kare kare"
watched_on: 2026-10-01
tags: [kaynak, video, render, npc-studio, clean-render]
---
# Spare — CLEAN Thumbnails: Render kısmı (0:00–6:27)

- Video: <https://www.youtube.com/watch?v=5XbxbzdN0x0>
- Photoshop kısmı (6:27 sonrası): [spare-clean-thumbnails.md](spare-clean-thumbnails.md)
- Modpack: <https://modrinth.com/modpack/thumbnailing> (Minecraft **1.21.11 / Fabric**, ana menüde "88 Mods")
- Sahne: karlı dağ, iki ana oyuncu (mor zırh + mace), yamaçta elmas zırhlı koşan kalabalık. Tamamı **shader'sız** (vanilla ışık) çekildi.
- Bütün içerik tek teknik notuna gider: [01 Render hazırlığı](../techniques/01-render-prep.md)

## Zaman damgası → konu
| Zaman | Konu | Not |
|---|---|---|
| [0:19](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=19s) | Gerekli modlar | NPC Studio + Iris. Paket ayrıca 3d-Skin-Layers, Bobby, Entity View Distance, Fadeless, Lithium, Mod Menu, Chat Heads, Simple Voice Chat vb. içeriyor |
| [0:37](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=37s) | Dünya oluşturma | Creative, Allow Commands ON, spawn kuralları OFF |
| [1:01](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=61s) | Yer bulma | Referans thumbnail'e benzeyen arazi, kar katmanlarıyla zemini düzeltme |
| [1:48](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=108s) | NPC Wand ve editör | Display / Pose / Presets / World / Camera sekmeleri |
| [2:28](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=148s) | Kalabalık için örnek NPC | Steve, Running, Frame 13.2, enchanted zırh ve kılıç |
| [3:35](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=215s) | Duplicate (kalabalık) | Square 20x20, offset, noise, Ground Snap, Variants |
| [4:43](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=283s) | World sekmesi | Light Rotation 184.7, Glint %120 + Freeze, bulut Freeze |
| [5:37](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=337s) | Kamera | Camera 1, Thirds kılavuzu, FOV |
| [5:54](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=354s) | Batch Screenshots | Kaynak × NPC grubu × shader matrisi |
| [6:02](https://www.youtube.com/watch?v=5XbxbzdN0x0&t=362s) | Shader paketleri | Iris > Download Shaders → DMS 1.5, NMS 1.6 |

## İzleme notları (ekranda okunan değerler)

### Dünya (0:37)
- Game Mode **Creative**, Difficulty Normal, Allow Commands **ON**.
- Game Rules > Spawning: Spawn mobs, Monsters, pillager patrols, phantoms, Wandering Traders, Wardens → hepsi **OFF**.
- World Updates: Advance time of day **OFF**, Update weather **OFF**. İsteğe bağlı, çünkü saat NPC Studio'dan da değişiyor.

### NPC editörü (1:48)
- Creative envanter > "NPC studio Mod" sekmesi > **NPC Wand** (`npcstudio:npc_wand`). Yere tıklayınca NPC oluşur ve editör açılır.
- **Display** sekmesi:
  - Model Settings: Model (Wide/Slim ikonları, Mobs, Custom), Skin > Choose (Official Slim / Official Wide klasörleri + kendi PNG'lerin), Cloak > Choose (pelerin galerisi), Nametag, Sneak, Living ✓, Shadow ✓, Animation (Idle, Running…) + Frame kaydırıcısı.
  - Inventory: 6 slot (kask, göğüs, pantolon, bot, ana el, yan el). Slot menüsünde **Enchanted** kutusu, Material, Template (trim), Clear.
  - Transform: Position XYZ, Rotation x/y/z, Look At / Head Look, Flip, Scale 1.00 + Unlock.
  - Modifiers: Opacity 1.0, Hit Overlay, Gravity, Visibility "Deactivate NPC".
- Kalabalık şablonu: Steve, Animation **Running**, Frame **13.2**. Önce netherite, sonra elmas zırh (ekran yazısı), hepsi Enchanted. Kılıç enchanted. Arka plan kalabalığında trim kullanılmadı.
- Ana iki oyuncu: kendi skin'leri + pelerin. Poz/mace tutuşu adım adım gösterilmedi.

### Duplicate / kalabalık (3:35)
- Mod: Line / **Square** / Circle. Count **20 x 20** (400 NPC).
- Dağdaki ayar: Offset dX **-1**, dY **0**, dZ **-1**. Noise X **0 – 0.5**, Y 0 – 0, Z 0 – 0. Düz zemindeki demoda offset 1.00 / 0.00 / 1.00.
- Diğer: **Ground Snap** (yamaçta aç), No Inside Blocks (bloğa gömülecek NPC'yi atlar), Clear Plants, Avoid `water,lava`, Only On `grass_block,sand`, Face: Pick Target.
- **Variants**: Character Variants ekranında her varyantın Name, Preset, **Weight** (örnekte %43.4), Tags, Equipment ON/OFF, Skin, Cloak (Cape On/Off), Nametag ayarı var. Ağırlığa göre karışık kalabalık doğar.
- Create: **NPCs** veya **BlockNPCs**. 400 canlı NPC'de "256 üstü performansı düşürür" uyarısı çıkıyor. Anlatıcıya göre BlockNPC daha az kasıyor.
- Sonuç: Batch ekranında "duplicated (311)" grubu, toplam 313 NPC (2 ana oyuncu dahil).

### World sekmesi (4:43). Son ekrandaki değerler
- General: Fire Spread kapalı, Keep Inventory açık, Tick Speed 3.0, Clear / Rain / Thunder düğmeleri.
- Lighting: NPC Bright ve World Bright kapalı. **Time Override** denendi (6000 → 11854.8 → 8225.8 → 2032.3 → 0), sonra kapatıldı. Kaydırıcı 5322.0'da kaldı. **Light Rotation açık, Rotation 184.7**. Gölge yönünü bu belirliyor.
- Glint: **Strength %120** (100–266 arası denendi), Reduce Item Glint kapalı, **Freeze Animation açık**, Frozen State %0.0. Enchant parıltısı her pass'te aynı kalsın diye donduruldu.
- Sun: Override denendi (Elevation 360, Intensity 1.2), sonra Elevation 0.0 / Rotation 0.0 / Scale 1.0 / Intensity 1.0'a döndürüldü. Anlatıcıya göre bu ayar daha çok shader kullanırken işe yarıyor.
- Moon: Override kapalı, Phase 0.0. Clouds: **Freeze açık**, Height 192, Seed 0. Dropped Entities: Disable Bobbing / Disable Rotation / No Pickup seçenekleri var.

### Kamera (5:37)
- Kamera aracı: Creative > NPC tools sekmesi ya da **H** tuşu (ekran yazısı).
- Serbest kamera tuşları: WASD/Space/RShift hareket, fare bakış, Z/X roll (Shift ince, C sıfırla), Scroll = FOV, Ctrl+Scroll = hız, =/- FOV, L kilitle, 1–9 kamera değiştir, Del sil, G kılavuz, H çık.
- İlk kadraj (HUD): XYZ 1066.7 / 176.6 / -319.8, Yaw 144.6, Pitch 59.0, **Roll 22.8**, FOV 43, Speed 0.1x. Camera sekmesinde Rotation 144.3 / 59.0 / 22.8, FOV 41, Guide **Thirds**, Opacity %35.
- Büyük batch öncesi ekranda kalan son değerler: Position 1065.79 / 173.80 / -321.26, Rotation 148.1 / 58.5 / **0.0**, **FOV 67**, Guide Thirds, Opacity %20. Yani eğik (dutch) açı denendi ama roll sıfırlandı.
- Camera sekmesi: Add Camera, "Camera 1 [L]" (kilitli), View (H) / Unlock / Delete, en altta Render > **Batch Screenshots**.

### Batch Screenshots (5:54)
- Mantık: **kaynak (kamera) × NPC grubu × shader** matrisi. Her kombinasyon ayrı PNG olur.
- Sources: Viewport ☐, **Camera 1 ✓**.
- Resolution: **Default** / Fabrishot. Özel çözünürlük için Fabrishot modu gerekiyor (ekranda "Fabrishot off", "Iris ON"). Default çıktının dosya adında `…x1080_cam1_bg` görünüyor (1920x1080).
- Shaders: **No shader ✓, DMS 1.5 ✓, NMS 1.6 ✓**. Her satırda ◇ ayar düğmesi var.
- NPCs: Select All / Clear, **"No NPCs — background only"** kartı (sadece arazi), her NPC için kart (isim + uzaklık). Bir gruba sağ tıklayıp o gruba özel shader seçilebiliyor.
- Alt satır: **WEM Cutout** (açılır menü, Off), **Delay (ms) 2000**, Output klasörü (`…\screenshots`), "N shots planned", Run Batch.
- Deneme: 1 grup × 3 shader = **3 shots**. Onay penceresi: Sources 1 camera, Groups 1, Resolution Default, Shaders 3, WEM Cutout Off → Confirm & Run. Sohbette "Batch complete: 3 captured, 0 skipped (0:10)".
- Asıl çekim: **313/313 seçili, 313 grup → 939 shots** (her NPC × 3 shader), "Warming renderer: Camera 1".
- Photoshop'a gelen dosyalar: `…_cam1_bg` (arka plan) ve `…spare-c8f6697c` (tek oyuncu). Oyuncu katmanının küçük resmi **şeffaf (dama)** görünüyor.

### Shader paketleri (6:02)
- Iris > Shader Packs ekranında **Download Shaders** düğmesi var (modpack'in özelliği). Liste: `DMS 1.5.zip`, `NMS 1.6.zip`.
- **DMS 1.5 ayarları:** Gradient Start (Chunks) **0**, **Max. Distance (Chunks) 96 → 8** (ipucu: rengin siyaha döndüğü mesafe), Falloff Curve varsayılan (ekranda ~0.0, imleç yüzünden tam okunmuyor), Invert **false**, Debug Lines **Off** → Apply. Max. Distance sahnenin derinliğine göre ayarlanır. Yakın = beyaz, uzak = siyah.
- Anlatıcı 6:10'da "no map shaders" diyor. Ekran yazısı bunu **"normal map shaders"** olarak düzeltiyor (NMS).
