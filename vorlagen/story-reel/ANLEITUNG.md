# Story-Reel (Vorlage "Panzer mit QR-Codes", 30.10.2026)

Format, das Mael gut findet und ab jetzt immer so will:

1. **Story-Hook (ca. 15-19 s):** überraschende, wahre oder plausible Geschichte als flache 2D-Animation
   (Panzer + QR-Codes + Drohnen). Erste Sekunde: sofort Bewegung und grosser Untertitel.
2. **Twist (ca. 4-5 s):** die Story führt direkt zu Crewtex (z. B. Drohnen-HUD öffnet crewtex.ch).
3. **Pitch (ca. 25 s, dunkelblau #0a1020, Orange #FF6B1A, Grid-Hintergrund):**
   Crewtex - Teamkleidung mit eurem Logo für Vereine und Firmen in der ganzen Schweiz -
   Sortiment mit Aufzählung UND IMMER "und vieles mehr" (+ Laufband weiterer Artikel) -
   bestickt oder bedruckt - Grössen per Link statt WhatsApp-Chaos - einzeln verpackt mit Name und Grösse -
   "Lust auf ein unverbindliches Angebot? Dann schreib jetzt TEAM in die Kommentare." (Kommentarfeld-Animation).
4. Gesamtlänge ca. 45 s, 1080x1920, 30 fps.

## Technik
- Stimme: vidiq_voiceover_generate, voiceId TX3LPaxmHKxFdv7VOQHJ (Liam, locker). Ein Clip pro Abschnitt (4 Clips).
  Download der MP3 von ai-voiceovers.s3.us-east-1.amazonaws.com ist freigegeben -> audio/vo1..vo4.mp3.
- Dateien nach /home/claude/reel kopieren (Pfade sind dort fest), dann:
  `python3 timeline.py && python3 render.py full && python3 audio.py && bash mix.sh`
  danach Lautheit: `ffmpeg -i crewtex_reel.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k out.mp4`
- Vorschau: `python3 render.py preview 2 8 14 ...` -> prev/*.png ansehen.
- timeline.py: TEXTS anpassen. scene.html: Szenen 1-3 (Welt/HUD) pro Story neu bauen, Pitch-Karten c0-c7 wiederverwenden.
- Pakete: pip install qrcode --break-system-packages.

## Regeln
Keine Emojis, echte Umlaute, keine erfundenen Kunden. Freewording, locker, für Social Media.
