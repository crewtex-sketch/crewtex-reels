#!/bin/bash
# Mischt Video + Musik + SFX (+ Voiceover, falls audio/vo1-4.mp3 vorhanden)
cd /home/claude/reel
read S2 S3 S4 < <(python3 -c "import json;s=json.load(open('timeline.json'))['segStarts'];print(s[1],s[2],s[3])")
if [ -f audio/vo1.mp3 ] && [ -f audio/vo4.mp3 ]; then
  ffmpeg -y -loglevel error -i video_silent.mp4 -i audio/music.wav -i audio/sfx.wav \
    -i audio/vo1.mp3 -i audio/vo2.mp3 -i audio/vo3.mp3 -i audio/vo4.mp3 -filter_complex "
    [3:a]adelay=0|0[v1];[4:a]adelay=$(echo "$S2*1000/1"|bc)|$(echo "$S2*1000/1"|bc)[v2];
    [5:a]adelay=$(echo "$S3*1000/1"|bc)|$(echo "$S3*1000/1"|bc)[v3];[6:a]adelay=$(echo "$S4*1000/1"|bc)|$(echo "$S4*1000/1"|bc)[v4];
    [v1][v2][v3][v4]amix=inputs=4:normalize=0,volume=1.6[vo];
    [1:a]volume=0.22[m];[2:a]volume=0.6[s];
    [vo][m][s]amix=inputs=3:normalize=0,alimiter=limit=0.95[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest crewtex_reel.mp4
else
  ffmpeg -y -loglevel error -i video_silent.mp4 -i audio/music.wav -i audio/sfx.wav -filter_complex "
    [1:a]volume=0.5[m];[2:a]volume=0.75[s];[m][s]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest crewtex_reel_ohne_stimme.mp4
fi
ls -la *.mp4
