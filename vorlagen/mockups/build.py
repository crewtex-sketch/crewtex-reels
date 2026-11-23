import json, os
L = json.load(open('/home/claude/crewtex-reels/vorlagen/text-reel/logo/logo.json'))
paths = ''.join(f'<path d="{d}"/>' for d in L['letters'])
cx, cy, r = L['dot']

def logo(fill, dot, emb=False):
    f = 'filter="url(#stitch)"' if emb else 'filter="url(#ink)"'
    return f'''<svg viewBox="0 -8 1512 164" class="logo"><g {f}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{dot}"/><g fill="{fill}">{paths}</g></g></svg>'''

DEFS = '''<svg width="0" height="0" style="position:absolute"><defs>
<filter id="stitch" x="-5%" y="-20%" width="110%" height="140%">
 <feTurbulence type="fractalNoise" baseFrequency="0.9 0.06" numOctaves="2" seed="3" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .25 0" result="nm"/>
 <feComposite in="nm" in2="SourceGraphic" operator="in" result="tex"/>
 <feMorphology in="SourceAlpha" operator="dilate" radius="2" result="d"/>
 <feGaussianBlur in="d" stdDeviation="3" result="b"/>
 <feOffset in="b" dx="0" dy="4" result="o"/>
 <feFlood flood-color="#000" flood-opacity=".45"/><feComposite in2="o" operator="in" result="sh"/>
 <feSpecularLighting in="b" surfaceScale="3" specularConstant=".25" specularExponent="18" lighting-color="#fff" result="sp"><feDistantLight azimuth="235" elevation="55"/></feSpecularLighting>
 <feComposite in="sp" in2="SourceAlpha" operator="in" result="spc"/>
 <feMerge><feMergeNode in="sh"/><feMergeNode in="SourceGraphic"/><feMergeNode in="tex"/><feMergeNode in="spc"/></feMerge>
</filter>
<filter id="ink"><feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="1" seed="7" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .10 0" result="nm"/>
 <feComposite in="nm" in2="SourceGraphic" operator="in" result="t"/>
 <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="t"/></feMerge></filter>
<filter id="fabric"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="11" result="n"/>
 <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .10 0" result="nm"/>
 <feComposite in="nm" in2="SourceGraphic" operator="in" result="t"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="t"/></feMerge></filter>
<radialGradient id="light" cx="45%" cy="35%" r="75%"><stop offset="0" stop-color="#fff" stop-opacity=".16"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></radialGradient>
</defs></svg>'''

HOODIE = 'M330 210 Q360 150 420 130 Q470 175 540 178 Q610 175 660 130 Q720 150 750 210 L870 330 Q900 360 905 420 L935 860 Q938 900 900 905 L835 910 Q805 905 800 870 L770 520 L770 1060 Q770 1095 735 1100 L345 1100 Q310 1095 310 1060 L310 520 L280 870 Q275 905 245 910 L180 905 Q142 900 145 860 L175 420 Q180 360 210 330 Z'
HOOD = 'M420 130 Q400 40 540 30 Q680 40 660 130 Q610 190 540 192 Q470 190 420 130 Z'
TEE = 'M360 170 Q450 205 540 205 Q630 205 720 170 L900 260 Q925 272 918 300 L870 440 Q862 462 838 455 L770 432 L770 1060 Q770 1095 735 1100 L345 1100 Q310 1095 310 1060 L310 432 L242 455 Q218 462 210 440 L162 300 Q155 272 180 260 Z'
POLO = TEE

def garment(path, color, extra='', logo_svg='', lx=560, ly=420, lw=200, rib=True):
    return f'''<svg viewBox="0 0 1080 1180" class="g">
<g filter="url(#fabric)"><path d="{path}" fill="{color}"/></g>
<path d="{path}" fill="url(#light)"/>
{extra}
<foreignObject x="{lx}" y="{ly}" width="{lw}" height="{lw*0.12}">{logo_svg}</foreignObject>
</svg>'''

def hoodie(color, lc, dot):
    extra = f'''<path d="{HOOD}" fill="{color}" filter="url(#fabric)"/><path d="{HOOD}" fill="url(#light)"/>
<path d="M455 140 Q540 200 625 140" stroke="#000" stroke-opacity=".35" stroke-width="10" fill="none"/>
<path d="M505 175 L495 330" stroke="#e8e2d6" stroke-width="7" stroke-linecap="round"/><path d="M575 175 L585 330" stroke="#e8e2d6" stroke-width="7" stroke-linecap="round"/>
<path d="M380 760 L700 760 L730 940 L350 940 Z" fill="#000" fill-opacity=".14"/>
<path d="M310 1040 L770 1040" stroke="#000" stroke-opacity=".25" stroke-width="5"/>
<path d="M800 840 L935 830 M145 830 L280 840" stroke="#000" stroke-opacity=".25" stroke-width="5"/>'''
    return garment(HOODIE, color, extra, logo(lc, dot, True), lx=575, ly=400, lw=210)

def tee(color, lc, dot, chest=False):
    extra = '''<path d="M445 200 Q540 250 635 200" stroke="#000" stroke-opacity=".18" stroke-width="12" fill="none"/>
<path d="M242 455 L210 440 M838 455 L870 440" stroke="#000" stroke-opacity=".2" stroke-width="4"/>'''
    if chest:
        return garment(TEE, color, extra, logo(lc, dot), lx=575, ly=360, lw=190)
    return garment(TEE, color, extra, logo(lc, dot), lx=365, ly=420, lw=350)

def polo(color, lc, dot):
    extra = f'''<path d="M450 178 L540 300 L630 178 L600 165 L540 250 L480 165 Z" fill="{color}" stroke="#000" stroke-opacity=".3" stroke-width="5"/>
<path d="M540 300 L540 420" stroke="#000" stroke-opacity=".3" stroke-width="5"/>
<circle cx="540" cy="335" r="7" fill="#fff" fill-opacity=".8"/><circle cx="540" cy="385" r="7" fill="#fff" fill-opacity=".8"/>'''
    return garment(POLO, color, extra, logo(lc, dot, True), lx=585, ly=390, lw=180)

ACC = '#FF5A1F'
cards = [
    ('hoodie-schwarz', 'Hoodie, Logo gestickt', 'Brust links, ca. 9 cm breit', hoodie('#1c1b1a', '#f3efe6', ACC), '#d9d3c7'),
    ('tshirt-weiss', 'T-Shirt, Logo gedruckt', 'Brust gross, ca. 25 cm breit', tee('#f4f2ee', '#121110', ACC), '#2a2724'),
    ('polo-navy', 'Polo, Logo gestickt', 'Brust links, ca. 8 cm breit', polo('#1f2a44', '#f3efe6', ACC), '#e6e0d4'),
    ('hoodie-orange', 'Hoodie, Logo gestickt', 'Brust links, ca. 9 cm breit', hoodie('#e2531c', '#121110', '#121110'), '#f1ede4'),
]

CSS = '''@font-face{font-family:Archivo;src:local("Archivo")}
*{margin:0;box-sizing:border-box}body{width:1080px;height:1350px;font-family:Inter,Archivo,"DejaVu Sans",sans-serif;overflow:hidden}
.wrap{position:relative;width:1080px;height:1350px;display:flex;flex-direction:column;align-items:center}
.g{width:1000px;margin-top:20px}.logo{width:100%;height:100%;display:block;overflow:visible}
.cap{position:absolute;left:70px;right:70px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end}
.cap h1{font-size:46px;font-weight:900;letter-spacing:-.02em}.cap p{font-size:28px;opacity:.7;margin-top:8px}
.tag{position:absolute;top:44px;left:50px;font-size:22px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:10px 18px;border-radius:999px;border:3px solid currentColor;opacity:.75}
.brand{font-size:26px;font-weight:900;letter-spacing:.08em}'''

os.makedirs('/home/claude/mockups/out', exist_ok=True)
for name, t1, t2, svg, bg in cards:
    dark = bg in ('#2a2724',)
    fg = '#f3efe6' if dark else '#121110'
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{DEFS}
<div class="wrap" style="background:{bg};color:{fg}"><div class="tag">Visualisierung</div>{svg}
<div class="cap"><div><h1>{t1}</h1><p>{t2}</p></div><div class="brand">crewtex.ch</div></div></div></body></html>'''
    open(f'/home/claude/mockups/{name}.html', 'w').write(html)
print('ok')
