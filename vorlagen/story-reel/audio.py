import json, numpy as np, wave

SR = 44100
tl = json.load(open("/home/claude/reel/timeline.json"))
lands = json.load(open("/home/claude/reel/lands.json"))
TOTAL = tl["total"]
S = tl["segStarts"]; T1, T2, T3 = S[1], S[2], S[3]
HUD0 = T2 + 3.55
CS = tl["cardStarts"]
N = int(TOTAL * SR) + SR
rng = np.random.default_rng(3)

def env(n, a=0.002, r=0.1):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
    return e

def add(buf, sig, at, gain=1.0):
    i = int(at * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain

def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.zeros_like(x); s = 0.0
    for k in range(len(x)):
        s = (1 - a) * x[k] + a * s; y[k] = s
    return y

def osc_saw(f, n):
    t = np.arange(n) / SR
    return 2 * ((t * f) % 1) - 1

# ---------------- Musik ----------------
music = np.zeros(N)
bpm = 124; beat = 60 / bpm
kick_n = int(0.35 * SR); tk = np.arange(kick_n) / SR
kick = np.sin(2 * np.pi * (45 + 110 * np.exp(-tk * 28)) * tk) * np.exp(-tk * 9)
hat = rng.standard_normal(int(0.05 * SR)); hat = np.diff(hat, prepend=0) * env(len(hat), 0.001, 0.012)
clap = rng.standard_normal(int(0.2 * SR)) * env(int(0.2 * SR), 0.001, 0.05)
clap = lowpass(clap, 3500) - lowpass(clap, 900)
roots = [55.0, 43.65, 65.41, 49.0]  # A1 F1 C2 G1
chords = [[220, 261.63, 329.63], [174.61, 220, 261.63], [261.63, 329.63, 392.0], [196.0, 246.94, 293.66]]
nbeats = int(TOTAL / beat) + 2
for b in range(nbeats):
    t0 = b * beat
    bar = (b // 4) % 4
    add(music, kick, t0, 0.9)
    add(music, hat, t0 + beat / 2, 0.25)
    if b % 4 in (1, 3): add(music, clap, t0, 0.35)
    # Bass auf Achteln
    for h in range(2):
        n = int(beat / 2 * SR)
        s = osc_saw(roots[bar], n) * env(n, 0.003, 0.12)
        add(music, lowpass(s, 500), t0 + h * beat / 2, 0.45)
    # Pluck-Arpeggio auf Sechzehnteln
    for q in range(4):
        f = chords[bar][(b * 4 + q) % 3] * (2 if q % 2 else 1)
        n = int(0.18 * SR)
        s = (osc_saw(f, n) + osc_saw(f * 1.005, n)) * 0.5 * env(n, 0.002, 0.06)
        add(music, lowpass(s, 2600), t0 + q * beat / 4, 0.12)
music = music / (np.abs(music).max() + 1e-9)
# Musik-Dynamik: kurz weg beim Knall, sanftes Ende
g = np.ones(N); tt = np.arange(N) / SR
g *= np.where((tt > T1 + 2.6) & (tt < T1 + 3.6), 0.35, 1)
g *= np.clip((TOTAL - tt) / 1.2, 0, 1)
g *= np.clip(tt / 0.3, 0, 1)
music *= g

# ---------------- SFX ----------------
sfx = np.zeros(N)
def noise(n): return rng.standard_normal(n)

def slap():
    n = int(0.09 * SR)
    s = lowpass(noise(n), 2500) * env(n, 0.0005, 0.018)
    tk = np.arange(n) / SR
    s += np.sin(2 * np.pi * 180 * tk) * np.exp(-tk * 60) * 0.6
    return s

def whoosh(d=0.45, up=True):
    n = int(d * SR); x = noise(n); t = np.arange(n) / SR
    shape = np.sin(np.pi * t / d) ** 2
    lo = lowpass(x, 1800 if up else 900)
    return (lo - lowpass(lo, 300)) * shape

def tone(f, d, a=0.003, r=0.08, wave="sine"):
    n = int(d * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) if wave == "sine" else np.sign(np.sin(2 * np.pi * f * t))
    return s * env(n, a, r)

def drone_hum(d):
    n = int(d * SR); t = np.arange(n) / SR
    s = osc_saw(190, n) * 0.5 + osc_saw(197, n) * 0.5 + osc_saw(380, n) * 0.25
    s = lowpass(s, 1400) * (0.8 + 0.2 * np.sin(2 * np.pi * 23 * t))
    fade = np.minimum(1, np.minimum(t / 0.4, (d - t) / 0.4))
    return s * fade

def explosion():
    n = int(2.2 * SR); t = np.arange(n) / SR
    x = noise(n)
    body = lowpass(x, 400) * np.exp(-t * 2.2) * 3
    crack = lowpass(x, 4000) * np.exp(-t * 14)
    sub = np.sin(2 * np.pi * (30 + 50 * np.exp(-t * 6)) * t) * np.exp(-t * 2.5)
    return body + crack * 0.8 + sub * 1.2

def whistle(d):
    n = int(d * SR); t = np.arange(n) / SR
    f = 1800 - 1200 * (t / d)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * 0.4 * np.minimum(1, t / 0.1)

for L in lands:
    if L < T1: add(sfx, slap(), L, 0.55)
add(sfx, whoosh(0.5), max(0, lands[0] - 0.35), 0.15)
add(sfx, whoosh(0.7, False), T1, 0.5)
add(sfx, drone_hum(3.4), T1 + 0.2, 0.18)
add(sfx, whistle(0.65), T1 + 1.95, 0.25)
add(sfx, explosion(), T1 + 2.6, 0.9)
add(sfx, drone_hum(HUD0 - T2), T2, 0.16)
# Scanner-Piepser
t = T2 + 1.2
while t < HUD0 - 0.4:
    add(sfx, tone(1650, 0.08, r=0.03), t, 0.12); t += 0.32
add(sfx, whoosh(0.4), HUD0 - 0.4, 0.5)
add(sfx, tone(880, 0.12, r=0.05, wave="sq"), HUD0 + 0.9, 0.08)
add(sfx, tone(1320, 0.18, r=0.08, wave="sq"), HUD0 + 1.0, 0.08)
add(sfx, tone(1046.5, 0.5, r=0.2), HUD0 + 1.75, 0.25)
add(sfx, tone(1568, 0.6, r=0.25), HUD0 + 1.85, 0.2)
add(sfx, whoosh(0.5), T3 - 0.15, 0.45)
for c in CS[1:8]:
    add(sfx, whoosh(0.35), c - 0.12, 0.22)
    add(sfx, tone(2400, 0.04, r=0.01), c + 0.05, 0.08)
TT = tl["teamTime"]
for k in range(4):
    add(sfx, tone(3000, 0.03, r=0.008), TT - 0.15 + k * 0.11, 0.12)
add(sfx, tone(784, 0.4, r=0.18), TT + 0.75, 0.22)
add(sfx, tone(1175, 0.6, r=0.3), TT + 0.83, 0.22)
add(sfx, tone(1568, 0.3, r=0.12), TT + 1.45, 0.15)

def write(path, x):
    x = np.clip(x, -1, 1)
    st = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())

sfx = sfx / (np.abs(sfx).max() + 1e-9) * 0.9
write("/home/claude/reel/audio/music.wav", music[: int(TOTAL * SR)] * 0.9)
write("/home/claude/reel/audio/sfx.wav", sfx[: int(TOTAL * SR)])
print("ok")
