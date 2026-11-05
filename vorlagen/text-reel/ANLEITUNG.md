# Text-Reel ohne Stimme (Vorlage 5.11.2026)

Für Wochen ohne vidIQ-Credits (Sprecherstimme kostet Credits). 20 bis 23 s, 1080x1920, 30 fps.
Aufbau, der Kunden bringen soll: Hook mit klarer Zielgruppe (POV / Rätsel) in Sekunde 0 mit Bewegung ->
Problem zeigen -> Lösung Crewtex (Grössen per Link, einzeln verpackt mit Name, Logo bestickt/bedruckt) ->
Preisbeispiel nur "Hoodie mit Stick ab ca. CHF 38" / "T-Shirt mit Druck ab ca. CHF 23" ->
Endszene: Logo, Kommentarfeld tippt "TEAM", "Schreib TEAM in die Kommentare", Pill crewtex.ch.

Beispiele: reel45/build_r6.py (Vereine, WhatsApp-Chaos) und reel45/build_r7.py (Firmen, "Wem öffnest du die Tür?").
Jedes neue Reel: eigenes Konzept, eigene Szenen; nur das Gerüst (common.py: words, endlogo, page, Animationen) wiederverwenden.

Ablauf (WORK = dieser Ordner, Pfade relativ dazu):
1. cp reel45/build_r6.py reel45/build_rX.py, Szenen neu schreiben, page(..., 'reel45/rX/reel.html')
2. python3 reel45/build_rX.py
3. Testbilder: node reel45/rec45.js $PWD/reel45/rX 22.5 1,5,10,15,21  -> test_*.png ansehen (nichts abgeschnitten/überlappend)
4. Alle Frames: node reel45/rec45.js $PWD/reel45/rX 22.5
5. Musik: in music_rx.py einen Block für 'rX' anlegen (ROOTS/RIFF/CUTS/END + FX), dann
   python3 reel45/music_rx.py rX 22.5 130 reel45/rX/music.wav
6. ffmpeg -y -framerate 30 -i reel45/rX/f_%04d.png -i reel45/rX/music.wav -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -af loudnorm=I=-14:TP=-1.5:LRA=11 reel.mp4

Regeln: keine Emojis, echte Umlaute, ss statt ß, keine erfundenen Kunden oder Statistiken, Buchrain und Jungwacht nie erwähnen.
