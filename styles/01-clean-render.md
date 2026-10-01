---
type: tarz
code: S1
title: "Temiz / yumuşak render ("clean render")"
tags: [tarz]
status: taslak
checked_on: 2026-10-01
---
# S1 — Temiz / yumuşak render ("clean render")

> Bu kart [tarz rehberinin](README.md) parçası. **N1–N20** kodları: [tarz teknikleri kataloğu](../techniques/style-catalog.md) (taslak değerler). § numaraları rehberdeki bölümler.

**Tanım:** Vanilla ya da BDS render üstüne NMS/DMS ile yapılan post-prodüksiyon. Görüntü açık ve pastel, derinlik yumuşak bir sisle veriliyor. Karakter, ortam ışığıyla sahneye "oturtuluyor". Vault'un şu anki iş akışı tam olarak bu.

**Görsel özellikler**
- *Kompozisyon:* 1–3 ana karakter ön planda, üçte bir çizgilerinde. Arkada sisle solan bir kalabalık ya da arazi var.
- *Palet:* açık mavi ortam (#c7e8ff civarı) ve tek bir doygun vurgu (mor ya da turuncu). Spare'in tutorial thumbnail'i mavi/mor (gözlem).
- *Işık:* yumuşak ve yönlü, düşük kontrastlı. Siyah neredeyse hiç yok.
- *Karakter:* kadraj yüksekliğinin %40–70'i. Poz dinamik (silah kaldırmış, koşuyor).
- *Kontur/glow:* beyaz sticker kontur yok. 3–5 px'lik ince rim highlight var. Silahta küçük bir glow olabilir.
- *Yazı:* genelde yok, olursa 1–3 kelime.
- *Arka plan:* depth-fog ile soluk. Blur yok ya da çok az.

**Örnek kanallar/tasarımcılar:** Spare (vault kaynağı), mangofx (Thumbnailing modpack'in yazarı), gfxrhino, ItsProger, Seltop (NPC Studio). Spoke'un parlak thumbnail'leri S1 ile S2 arasında duruyor.

**Mevcut teknikler**
| Teknik | Kullanım |
|---|---|
| [01 Render](../techniques/01-render-prep.md) – [12 Export](../techniques/12-export.md) | Hepsi, vault'taki varsayılan değerlerle. |

**Gereken yeni teknikler:** az. İsteğe bağlı olarak N4 (yazı), N3 (hafif blur), N5 (vinyet, −10…−20).

**Brief soruları**
- Pastel ve yumuşak mı olsun, yoksa yüksek kontrastlı mı (S2'ye kayar)?
- Sahnenin ortam rengi ne olsun (gökyüzü, biyom)?
- Tek bir vurgu rengi var mı (kanal rengi, eşya)?
- Yazı olacak mı?
- Kaç karakter olacak ve kalabalık gerekiyor mu?

**Referansta tanıma ipuçları:** açık ortalama parlaklık · arka plan sisle soluyor, uzak bloklar ortam rengine karışıyor · blok yüzleri NMS ile ayrışmış (üst yüzler aydınlık, yan yüzler hafif koyu) · kenarlarda 3–5 px'lik ince beyaz çizgiler var · beyaz kontur ve vinyet yok · kontrast düşük.
