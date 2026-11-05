import sys
exec(open(__file__.replace('music_pop.py', 'music_base.py')).read())
# Pop-Track (C-Dur, I-V-vi-IV), Four-on-the-floor, Klingel E-C als Intro, Drops bei 3.0 und 5.45
S16 = B / 4; BAR = 4 * B
D1, D2, END = 3.0, 5.45, 17.4
CHORDS = [[60, 64, 67], [59, 62, 67], [57, 60, 64], [57, 60, 65]]   # C, G/B, Am, F
BASS = [36, 35, 33, 29]
HOOK = [76, 0, 79, 0, 76, 74, 72, 0, 74, 0, 76, 0, 72, 0, 0, 0,
        76, 0, 79, 0, 81, 79, 76, 0, 74, 0, 72, 74, 76, 0, 0, 0]

def supersaw(n, d):
    f = mid(n); s = sum(saw(f, d, 12, dt) for dt in (-.008, -.003, .003, .008)) / 4
    return lp(s, 3200)

def chord_stab(ch, d):
    t = T(d); s = sum(supersaw(n + 12, d) for n in ch) / len(ch)
    return s * np.exp(-t * 3.5) * np.minimum(1, t / .005) * .5

def pluck(n, d=.3):
    f = mid(n); t = T(d); s = saw(f, d, 14, .002) + saw(f, d, 14, -.002)
    return lp(s, 5000) * np.exp(-t * 11) * .3

def popbass(n, d):
    f = mid(n); t = T(d); s = np.sin(2 * np.pi * f * t) + .35 * lp(saw(f, d, 6), 700)
    return s * adsr(len(t), .003, .12, .6, .02) * .8

kicks = []

def pop_section(t0, t1, level, bar0=0):
    t = t0; i = bar0
    while t < t1 - .01:
        blen = min(BAR, t1 - t); ci = i % 4
        # Akkorde: Offbeat-Stabs (Pop-House)
        for k in (2, 6, 10, 14) if level >= 1 else (0,):
            if k * S16 < blen: add('pad', chord_stab(CHORDS[ci], .32), t + k * S16, .9)
        if level >= 2: add('pad', pad([n + 12 for n in CHORDS[ci]], blen), t, 1.4)
        # Drums
        for b in range(4):
            if b * B < blen:
                add('drums', kick(), t + b * B, 1.0); kicks.append(t + b * B)
                add('drums', hat(True), t + b * B + B / 2, .45, .2)
        for b in (1, 3):
            if b * B < blen: add('drums', clap(), t + b * B, .9)
        if level >= 2:
            for k in range(16):
                if k * S16 < blen and k % 2: add('drums', hat(), t + k * S16, .25, -.25)
        # Bass: Oktav-Bounce
        for k in range(8):
            if k * B / 2 < blen:
                add('bass', popbass(BASS[ci] + (12 if k % 2 else 0), B / 2 * .9), t + k * B / 2, .9)
        # Hook
        if level >= 1:
            h = HOOK[(i % 2) * 16:(i % 2) * 16 + 16]
            for k, n in enumerate(h):
                if n and k * S16 < blen:
                    add('lead', pluck(n, .35), t + k * S16, .8, -.15 if k % 2 else .15)
                    add('lead', bell(n + 12, .4), t + k * S16, .25)
        t += BAR; i += 1
    return i

# Intro: Ding-Dong (E-C), dann Pop-Build
for a in (0.05, 0.9):
    add('lead', bell(76, 1.2), a, 1.3); add('lead', bell(72, 1.4), a + .3, 1.3)
add('pad', pad([60, 64, 67], 1.2), 0, 1.2); add('pad', pad([59, 62, 67], 1.2), 1.2, 1.2)
for k in range(8):   # gefilterte Akkorde, werden heller
    tt = 1.2 + k * B / 2
    if tt < D1 - .15: add('pad', lp(chord_stab(CHORDS[k // 4 % 4], .25), 600 + 400 * k), tt, .6 + .05 * k)
t = 1.5
while t < D1 - .15:  # Clap-Build
    x = (t - 1.5) / (D1 - 1.65); add('drums', clap(), t, .2 + .5 * x); t += B / (2 if x < .5 else 4 if x < .8 else 8)
add('fx', noise_rise(1.5), 1.4, 1.0)

add('fx', impact(), D1, .8)
bi = pop_section(D1, D2 - .25, 1)
add('fx', noise_rise(.8), D2 - 1.0, .8)
add('fx', impact(), D2, .9); add('lead', bell(84, 1.0), D2, .7)
bi = pop_section(D2, END - .2, 2, bi)
add('fx', rev_cym(.6), 8.0, .7); add('fx', rev_cym(.6), 12.4, .7)
add('fx', impact(), END, .8)
# Outro: Akkorde ausklingen + Klingel
add('pad', pad([60, 64, 67, 72], DUR - END), END, 1.4)
add('bass', popbass(36, 2.0), END, .9)
for k, a in enumerate([END + .3, END + .9, END + 2.4, END + 3.0]):
    add('lead', bell(76 if k % 2 == 0 else 72, 1.6), a, 1.0)

for k in range(10): add('fx', tick(), 9.3 + k * .11, .25)
for tt in (11.0, 11.45, 11.9): add('fx', tick(), tt, .6)
for k in range(4): add('fx', tick(), 19.7 + k * .2, .6)

for a, b in ((2.87, 3.0), (5.2, 5.45)):
    i, j = int(a * SR), int(b * SR)
    for k in ('drums', 'bass', 'lead', 'pad'): bus[k][:, i:j] = 0
sc = np.ones(N)
for k in kicks:
    a = int(k * SR); n = int(.2 * SR); j = min(N, a + n); xx = np.arange(j - a) / SR
    sc[a:j] = np.minimum(sc[a:j], 1 - .55 * np.exp(-xx * 12))
mix = bus['drums'] * .85 + bus['bass'] * sc * .9 + bus['lead'] * .9 + bus['pad'] * sc * .9 + bus['fx'] * .6
fade = np.ones(N); fs = int((DUR - 1.0) * SR); fade[fs:] = np.linspace(1, 0, N - fs)
mix *= fade
out = np.tanh(mix / np.abs(mix).max() * 1.5) * .92
stt = np.empty(N * 2); stt[0::2] = out[0]; stt[1::2] = out[1]
w = wave.open(sys.argv[4], 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((stt * 32767).astype(np.int16).tobytes()); w.close(); print('ok')
