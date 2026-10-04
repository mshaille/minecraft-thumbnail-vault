#!/usr/bin/env python3
"""UserPromptSubmit hook: mesaj thumbnail işiyle ilgiliyse kuralı ve kullanıcı tercihlerini bağlama ekler.
Kullanıcı kuralı her mesajda tekrar yazmak zorunda kalmasın diye. İlgisiz mesajlarda hiçbir şey yazmaz."""
import json, re, sys

WORDS = r'thumbnail|kapak|render|kupa|trim|skin|zırh|zirh|referans|sipariş|siparis|mcthumb|ghast|npc|parla|bulanık|bulanik|photopea|photoshop'
try:
    prompt = json.load(sys.stdin).get('prompt', '')
except Exception:
    sys.exit(0)
if not re.search(WORDS, prompt.lower()):
    sys.exit(0)
print("""[mcthumb] KURAL: ÜŞENGEÇLİK YOK — mükemmellik aranır (minecraft-thumbnail skill'ini kullan, AGENTS.md'deki 6 madde geçerli):
ölç (≥5x, piksel profili), efektin bütün katmanlarını yap, plan değil gerçek taslak üret, yan yana doğrula, ilişkileri koru, kalan her farkı yaz.
Kullanıcı tercihleri (guides/order-workflow.md): referans varsa gelmeden tasarlama, yoksa planı sen kur; render'lar masaüstündeki klasörde
(4K orijinaller Modrinth profilinin screenshots klasöründe); yakın karakterler aydınlık; parlamalar hafif (trim ~referansın %20'si);
arka plan bulanıklığı hafif (σ ~1,5 px @1280); ortam düz kalmasın (alan derinliği, ışık kaynağı, partikül, grading, vinyet);
oyun yazısı resmi çeviri + oyun fontu; kullanıcıyla Türkçe konuş; repoya müşteri verisi/isim koyma; commit'te Claude co-author yok.""")
