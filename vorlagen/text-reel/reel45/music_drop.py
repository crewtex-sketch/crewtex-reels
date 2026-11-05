import sys
exec(open(__file__.replace('music_drop.py', 'music_base.py')).read())
# Eigener Track für Reel 7b: Türklingel-Motiv wird zum Beat, echte Drops bei 3.0 (Tür -> Szene) und 5.45 (B gewählt)
S16 = B / 4
D1, D2, END = 3.0, 5.45, 17.4
CUTS = [8.6, 13.0]

def b808(n, d, glide=0.0):
    t = T(d); f = mid(n) * (1 + .7 * np.exp(-t * 38)) * (2 ** (glide * np.minimum(1, t / .12) / 12))
    s = np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * 4) * .75
    e = np.exp(-t * .8); rl = min(len(t) - 1, int(.02 * SR)); e[-rl:] *= np.linspace(1, 0, rl)
    return s * e

def pluck(n, d=.35):
    f = mid(n); t = T(d)
    s = saw(f, d, 12, .003) + saw(f, d, 12, -.003)
    return lp(s, 3800) * np.exp(-t * 9) * .32

def snare_roll(a, b, start_rate=8, end_rate=32):
    t = a
    while t < b:
        x = (t - a) / (b - a); rate = start_rate + (end_rate - start_rate) * x ** 2
        add('drums', clap(), t, .18 + .5 * x); t += 1 / rate

def silence_gap(a, b):
    i, j = int(a * SR), int(b * SR)
    for k in bus: bus[k][:, i:j] *= np.linspace(1, 0, j - i) if False else 0

# --- Intro: Ding-Dong + Spannung
for a in (0.05, 0.9):
    add('lead', bell(76, 1.2), a, 1.2); add('lead', bell(72, 1.4), a + .3, 1.2)
add('pad', pad([52, 59, 64], 3.0), 0, 1.0)
for k in range(4): add('drums', lp(kick(), 300), k * B * 1.0, .5)
snare_roll(1.35, 2.85)
add('fx', noise_rise(1.6), 1.25, 1.0)
add('fx', rev_cym(1.0), 1.85, .9)

# --- Hauptteil
motif = [76, 0, 72, 0, 76, 0, 79, 72, 0, 0, 76, 0, 74, 0, 72, 0]
motif2 = [76, 0, 72, 0, 76, 0, 79, 81, 0, 79, 76, 0, 74, 72, 0, 0]
roots = [40, 40, 36, 38]   # E E C D
kicks = []

def section(t0, t1, level):
    t = t0; i = 0
    while t < t1 - .01:
        blen = min(4 * B, t1 - t)
        m = motif if i % 2 == 0 else motif2
        for k, n in enumerate(m):
            tt = t + k * S16
            if k * S16 >= blen: break
            if n:
                add('lead', bell(n + 12, .5), tt, .55)
                if level >= 2: add('lead', pluck(n, .3), tt, .5, -.2 if k % 2 else .2)
        for p in (0, 3, 10) if level >= 1 else (0,):
            if p * S16 < blen: add('drums', kick(), t + p * S16, 1.0); kicks.append(t + p * S16)
        for p in (4, 12):
            if p * S16 < blen: add('drums', clap(), t + p * S16, .8)
        for k in range(16):
            if k * S16 >= blen: break
            g = .55 if k % 2 == 0 else .3
            add('drums', hat(), t + k * S16, g, .3 if k % 4 == 1 else -.15)
            if level >= 2 and i % 2 == 1 and k >= 12:
                add('drums', hat(), t + k * S16 + S16 / 2, .25)
        add('bass', b808(roots[i % 4] - 12, blen * .95, glide=(-2 if i % 2 else 0)), t, .9)
        t += 4 * B; i += 1

# Drop 1 bei 3.0
add('fx', impact(), D1, 1.0); add('bass', b808(28, 1.2), D1, 1.0)
section(D1, D2 - .3, 1)
# Mini-Pause vor dem Klick auf B, dann Drop 2
add('fx', noise_rise(.7), D2 - 1.0, .8)
add('fx', impact(), D2, 1.0); add('bass', b808(28, 1.4, glide=-5), D2, 1.0)
add('lead', bell(88, 1.0), D2, .7); add('lead', bell(84, 1.0), D2 + .12, .6)
section(D2, CUTS[0] - .05, 2)
# Szene 3 und 4: volle Energie, kurze Breaks bei Schnitten
for c in CUTS:
    add('fx', rev_cym(.6), c - .6, .8); add('fx', impact(), c, .6)
section(CUTS[0], CUTS[1], 2)
section(CUTS[1], END - .3, 2)
snare_roll(END - 1.1, END - .1, 10, 28)
# Ende: Hit, dann Klingel-Motiv solo über Sub
add('fx', impact(), END, 1.0); add('bass', b808(28, DUR - END - .2), END, .8)
for k, a in enumerate([END + .4, END + 1.1, END + 2.6, END + 3.3]):
    add('lead', bell(76 if k % 2 == 0 else 72, 1.6), a, .9)
add('pad', pad([52, 59, 64, 67], DUR - END), END, .9)

# Effekte passend zum Bild
for k in range(10): add('fx', tick(), 9.3 + k * .11, .3, .3 * (1 if k % 2 else -1))
for t in (11.0, 11.45, 11.9): add('fx', tick(), t, .7)
for t in (13.7, 14.3, 14.9): add('fx', thud(), t + .2, .5)
for k in range(4): add('fx', tick(), 19.7 + k * .2, .7)

# Mix: Lücken vor den Drops (Stille = Spannung)
for a, b in ((2.88, 3.0), (5.2, 5.45)):
    i, j = int(a * SR), int(b * SR)
    for k in ('drums', 'bass', 'lead', 'pad'): bus[k][:, i:j] = 0
sc = np.ones(N)
for k in kicks:
    a = int(k * SR); n = int(.16 * SR); j = min(N, a + n); xx = np.arange(j - a) / SR
    sc[a:j] = np.minimum(sc[a:j], 1 - .4 * np.exp(-xx * 14))
mix = bus['drums'] * .9 + bus['bass'] * 1.0 + bus['lead'] * sc * .9 + bus['pad'] * sc + bus['fx'] * .75
fade = np.ones(N); fs = int((DUR - 1.0) * SR); fade[fs:] = np.linspace(1, 0, N - fs)
mix *= fade
out = np.tanh(mix / np.abs(mix).max() * 1.6) * .92
stt = np.empty(N * 2); stt[0::2] = out[0]; stt[1::2] = out[1]
w = wave.open(sys.argv[4], 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((stt * 32767).astype(np.int16).tobytes()); w.close(); print('ok')
