import json, re, qrcode

# Voiceover-Segmente mit gemessener Länge (Sekunden)
import subprocess
TEXTS = [
    "Moderne Soldaten haben angefangen, QR-Codes auf ihre Panzer zu kleben. Und zwar wirklich in jede Ecke.",
    "Der Grund? Feindliche Drohnen haben ihre Panzer immer öfter erwischt.",
    "Aber jetzt, wenn die Drohne den Panzer scannt, scannt sie den QR-Code. Und der führt direkt zu Crewtex.",
    "Crewtex. Teamkleidung mit eurem Logo, für Vereine und Firmen in der ganzen Schweiz. Hoodies, T-Shirts, Polos, Jacken, Caps, Traineranzüge, Taschen und vieles mehr. Bestickt oder bedruckt. Grössen sammeln per Link, statt WhatsApp-Chaos. Jedes Teil einzeln verpackt, mit Name und Grösse. Lust auf ein unverbindliches Angebot? Dann schreib jetzt TEAM in die Kommentare.",
]
def dur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).decode())
SEGMENTS = [(TEXTS[i], dur(f"/home/claude/reel/audio/vo{i+1}.mp3")) for i in range(4)]
TAIL = 0.7


def chunks_for(text):
    words = text.split()
    out, cur = [], []
    for w in words:
        cur.append(w)
        joined = " ".join(cur)
        if re.search(r"[.,:!?]$", w) or len(joined) >= 15 or len(cur) >= 3 or w == "TEAM" or (len(cur) == 1 and cur[0] in ("schreib",)):
            out.append(joined)
            cur = []
    if cur:
        out.append(" ".join(cur))
    return out


def weight(c):
    w = len(c) + 2
    if c.endswith((".", ":", "!", "?")):
        w += 7
    elif c.endswith(","):
        w += 3
    return w


subs, seg_starts, sentences = [], [], []
t = 0.0
for i, (text, dur) in enumerate(SEGMENTS):
    seg_starts.append(round(t, 3))
    cs = chunks_for(text)
    ws = [weight(c) for c in cs]
    usable = dur * 0.96
    lead = 0.08
    tt = t + lead
    for c, w in zip(cs, ws):
        d = usable * w / sum(ws)
        subs.append({"t0": round(tt, 3), "t1": round(tt + d, 3), "text": c.rstrip(".,:?"), "seg": i})
        if i == 3 and (not sentences or subs[-2]["text"] if len(subs) > 1 else True):
            pass
        tt += d
    t += dur

TOTAL = round(t + TAIL, 3)

# Satz-Starts im Pitch (Segment 4) für die Karten
s4 = [s for s in subs if s["seg"] == 3]
starts = [s4[0]["t0"]]
prev_end_punct = False
raw4 = chunks_for(SEGMENTS[3][0])
for k, c in enumerate(raw4[:-1]):
    if c.endswith((".", ":", "?")):
        starts.append(s4[k + 1]["t0"])

# QR-Code für crewtex.ch (echt scanbar)
qr = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
qr.add_data("https://crewtex.ch")
qr.make(fit=True)
m = qr.get_matrix()
n = len(m)
path = "".join(f"M{x} {y}h1v1h-1z" for y, row in enumerate(m) for x, v in enumerate(row) if v)

data = {
    "total": TOTAL,
    "segStarts": seg_starts,
    "subs": subs,
    "cardStarts": starts,
    "qrN": n,
    "teamTime": next(x["t0"] for x in subs if "TEAM" in x["text"]),
    "qrPath": path,
}
json.dump(data, open("/home/claude/reel/timeline.json", "w"), ensure_ascii=False, indent=1)
print("total", TOTAL, "segStarts", seg_starts)
print("cardStarts", starts, len(starts))
for s in subs:
    print(s)
