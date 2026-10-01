---
type: kaynak
title: How to Make CLEAN Minecraft Renders With Blender
creator: ItsProger
url: https://www.youtube.com/watch?v=tvDzfBp6gjE
duration: "13:31"
watched: "tamamı (transkript + ayar kareleri)"
watched_on: 2026-10-01
tags: [kaynak, video, render, blender, mcprep, blockbench, clean-render]
---
# ItsProger — How to Make CLEAN Minecraft Renders With Blender

- Video: <https://www.youtube.com/watch?v=tvDzfBp6gjE> (9 Haziran 2025, ~560 B izlenme, seslendirme: qBedwars, İngilizce)
- Araçlar: **Blockbench** (oyuncu/zırh/mod modeli), **Blender + MCprep** eklentisi, isteğe bağlı **Mineways** (dünyayı OBJ olarak dışa aktarma), Poly Haven HDRI, Sketchfab.
- Yazar açıklamada Mineways indirmelerinde virüslü dosya bulunduğunu söyleyip uyarıyor. Mineways'i sadece resmî kaynaktan indir, ya da MCprep'in jmc2obj yolunu kullan.
- NPC Studio yolunun alternatifi. Karakter Blender'da pozlanıp **şeffaf arka planla** render edilir, arka plan ayrı alınır. Teknik notu: [01 Render hazırlığı](../techniques/01-render-prep.md)

## Zaman damgası → konu
| Zaman | Konu | Not |
|---|---|---|
| [0:14](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=14s) | Blockbench'te oyuncu modeli | Pose kapalı, Layer Texture açık, glTF export |
| [0:45](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=45s) | Blender arayüzü | Varsayılan küp ve ışığı sil. Sadece Layout + Shading sekmeleri |
| [1:56](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=116s) | Kamera | View Lock > Camera to View |
| [2:10](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=130s) | MCprep | Item/Mob/Block spawner, Swap Texture Pack |
| [3:16](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=196s) | Poz | 6 kemik + 5 "hayali kemik" fikri |
| [4:47](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=287s) | Zırh | Armor (Main) / Armor (Leggings) model tipleri |
| [6:15](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=375s) | Arka plan | Minecraft ekran görüntüsü ya da Mineways + Prep Materials |
| [7:38](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=458s) | Işıklar | 3 area light düzeni, HDRI |
| [8:49](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=529s) | Şeffaf arka plan | Film > Transparent |
| [9:00](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=540s) | Mod/özel modeller | Mod jar içinden model + doku → Blockbench, Sketchfab |
| [11:27](https://www.youtube.com/watch?v=tvDzfBp6gjE&t=687s) | Render ayarları | Cycles, Denoise, samples, ayrı pass'ler |

## İzleme notları (ekranda okunan değerler)

### Blockbench oyuncu modeli (0:14)
- File > New > **Minecraft Skin**: Model **Player - Wide** (Steve) ya da **Player - Slim** (Alex), Resolution Default, Texture = skin PNG.
- **Pose ☐ (kapat)**, **Layer Texture ☑ (aç)**. İkinci katmanın görünürlüğünü de aç.
- File > Export > glTF. Export Options: Encoding **ASCII (glTF)**, Model Export Scale **16**, Embed Textures ✓, **Export Groups as Armature (Experimental) ✓**, Export Animations ☐.

### Blender temel (0:45 – 2:10)
- Esc ile açılış ekranını kapat, küp ve ışığı sil. Gezinme: orta tuş sürükle = döndür, Shift + orta tuş = kaydır, tekerlek = yakınlaştır. Seçili nesnede G = fareyle taşı. Object properties > Scale XYZ.
- Kamera: kamera ikonuyla kameradan bak, N paneli > View > View Lock > Lock **Camera to View ✓**. Artık gezinme kamerayı oynatır. Ekranda Focal Length 50 mm, Clip Start 0.01 m, End 1000 m (varsayılanlar).

### MCprep (2:10)
- N panelinde MCprep sekmesi. Spawner: Mob / Block (model) / **Item spawner** → Reload assets → öğe seç (ör. diamond pickaxe) → Place. Sonra döndür/taşı ile pozla.
- Doku paketi değiştirme: modeli seç, World Imports > World exporter **jmc2obj** seçili olsun → MCprep tools > **Swap Texture Pack** → paketin zip'ini önce aç, klasördeki bir resme çift tıkla.
- Diğer düğmeler: Prep Materials, Mesh Swap, Create MC Sky, Prep World, Skin Swapper.

### Poz (3:16)
- glTF'yi içe aktar (File > Import > glTF). Minecraft oyuncusunda 6 kemik var.
- Daha gerçekçi poz için 5 "hayali kemik" varmış gibi davran: parçaları normal eklem yerinden hafifçe ayırıp kaydır. Böylece dirsek, diz, bel kırılmış gibi görünür. Ekranda önce/sonra karşılaştırması var.
- Poz için gerçek insan fotoğraflarını referans al. Ne kadar hareket olacağı thumbnail tarzına ve müşteriye göre değişir.

### Zırh (4:47)
- Blockbench > Minecraft Skin, model tipi **Armor (Main)** (kask + göğüslük) ve ayrıca **Armor (Leggings)**. Doku olarak resource pack'teki zırh katman PNG'si seçilir. Pose ☐, Layer Texture ✓.
- File > **Convert Project** → Generic Model, **Create Copy kapalı** → Confirm.
- Normal skin modelini de generic yapıp zırhı içine aktar. Her zırh klasörünü skin'in ilgili kemik klasörüne sürükle (head → head, pantolon ve botlar → legs). Sonra aynı glTF ayarlarıyla export et.

### Arka plan (6:15)
- Kolay yol: Minecraft'ta ekran görüntüsü al, Blender'da Add > Image > **Background** ile arkaya koy (render süresi kısalır).
- Mineways yolu: File > Open World > dünya klasöründeki `level.dat` → sağ tıkla sürükleyerek alan seç → File > **Export for Rendering** → Blender'da OBJ içe aktar (ya da sürükle-bırak) → MCprep > **Prep Materials** (bulanık dokuları düzeltir).

### Işık (7:38)
- Add > Light > **Area** (bazen Spot). Sabit değer verilmiyor, deneyerek bulunuyor.
- Önerilen düzen: karakterin **üstünde** beyaz, çok güçlü area. **Arkasında** skin rengiyle area (rim). **Altında ve biraz sağında** daha karanlık area.
- HDRI: World properties > Color > **Environment Texture** > Open. Döndürmek için Shading sekmesi > Object yerine World > texture node'u seç > **Ctrl+T** (Node Wrangler, Mapping ekler) > Rendered görünümde Mapping **Rotation Z** kaydır.

### Mod ve özel modeller (9:00)
- Mod jar'ını arşiv programıyla aç, dosyaları klasöre çıkar, mob/öğe adını ara. Model dosyası (`.geo` uzantılı) Blockbench'e, aynı adın `.png` dokusu "import texture" ile eklenir. Blockbench'te pozla.
- glTF export: pozlanacak mob için Export Groups as Armature açık, silah gibi pozlanmayan modelde kapalı. Export Animations kapalı.
- Pelerin: Minecraft Skin modelinde cape seçeneği + cape dokusu. Sketchfab'den GLB/glTF indirilebilir (bazıları ücretli).
- Çok parçalı modeli seçip Join yap ya da bir Collection'a koy. Collection ikonuna çift tıklayınca hepsi seçilir.

### Render (11:27)
- Render Engine **Cycles** (ekranda Device CPU).
- Viewport: Noise Threshold 0.1000, Max Samples 1024, Denoise ✓.
- Render: Noise Threshold **0.0100**, Max Samples ekranda **900**, Time Limit 0 s, **Denoise ✓**. Anlatım: zayıf PC'de 40–200, kendisi 2000–3000 kullanıyor. Sample arttıkça kalite ve süre artar.
- Film: Exposure 1.00, **Transparent ✓** (arka plan render edilmez).
- **Ayrı pass:** Outliner'da render'da olmasını istemediğin nesnelerin kamera ikonunu kapat → **F12** (Render > Render Image) → Image > Save As. Sonra tersini yap: karakterleri kapat, arka planı aç, tekrar render al. İstersen hepsini birlikte alıp karakteri elle kesebilirsin.
- Çözünürlük ayarı videoda gösterilmiyor.
