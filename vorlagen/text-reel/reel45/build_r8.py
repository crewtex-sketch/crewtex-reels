exec(open(__file__.replace('build_r8.py', 'common.py')).read())
import math
# REEL 8: Warum kostet ein gesticktes Logo beim ersten Mal extra? (Stickdatei)
R = 250; pts = []; y = -R + 6; k = 0
while y < R - 6:
    x = math.sqrt(max(0, R*R - y*y)) - 4
    a, b = (-x, x) if k % 2 == 0 else (x, -x)
    pts.append(f'{a:.1f},{y:.1f}'); pts.append(f'{b:.1f},{y+5:.1f}'); y += 10; k += 1
satin = ' '.join(pts)
ring = []
for i in range(0, 361, 3):
    a = math.radians(i); r1 = R + 18 + (6 if (i//3) % 2 else -6)
    ring.append(f'{r1*math.cos(a):.1f},{r1*math.sin(a):.1f}')
ring = ' '.join(ring)
code = ['STICH 0001   X 112   Y 040', 'STICH 0002   X 118   Y 044', 'STICH 0003   X 109   Y 049',
        'FARBE 2      ORANGE', 'STICH 0004   X 121   Y 053', 'STICH 0005   X 107   Y 058', 'SPRUNG       X 240   Y 061', '...']
codeh = ''.join(f'<div class="cl" data-in="{5.5+i*0.32:.2f}" data-a="left" data-dur=".18">{c}</div>' for i, c in enumerate(code))
css = '''
.mach{position:absolute;left:140px;right:140px;top:980px;height:640px;border-radius:50px;background:#26231F}
.mach .arm{position:absolute;left:60px;right:60px;top:-120px;height:170px;border-radius:40px;background:#3A3631}
.mach .ndl{position:absolute;left:50%;top:40px;width:10px;height:150px;margin-left:-5px;background:#cfc8bb;border-radius:4px}
.mach .hoop{position:absolute;left:50%;top:260px;width:420px;height:260px;margin-left:-210px;border-radius:50%;border:16px solid #8A6A4A;background:#F3EFE6}
.q{position:absolute;left:50%;top:330px;margin-left:-60px;width:120px;height:120px;border-radius:50%;background:var(--acc);color:var(--ink);display:grid;place-items:center;font-size:90px;font-weight:900}
.pic{position:absolute;left:90px;top:640px;width:330px;height:330px;border-radius:40px;background:#fff;display:grid;place-items:center;box-shadow:0 20px 40px rgba(0,0,0,.15)}
.pic i{width:200px;height:200px;border-radius:50%;background:var(--acc)}
.pic b{position:absolute;bottom:-70px;left:0;right:0;text-align:center;font-size:40px;font-weight:900}
.arr{position:absolute;left:450px;top:770px;font-size:90px;font-weight:900;color:var(--acc)}
.code{position:absolute;left:560px;right:60px;top:630px;height:420px;border-radius:30px;background:var(--ink);color:#9BE38A;padding:30px 28px;font-family:monospace;font-size:27px;line-height:1.5;overflow:hidden;white-space:pre}
.code .cl{white-space:pre}
.lbl{position:absolute;left:560px;right:60px;top:1080px;text-align:center;font-size:40px;font-weight:900}
.big{position:absolute;left:90px;right:90px;top:1300px;font-size:64px;font-weight:900;letter-spacing:-.03em;line-height:1.05}
.big span{color:var(--acc)}
.stage{position:absolute;left:50%;top:1020px;width:700px;height:700px;margin:-350px 0 0 -350px}
.stage svg{overflow:visible}
.cnt{position:absolute;left:90px;right:90px;top:1460px;text-align:center;font-size:52px;font-weight:900}
.rowck{display:flex;gap:30px;align-items:center;font-size:56px;font-weight:900;letter-spacing:-.02em;margin-bottom:46px;line-height:1.05}
.cbox{display:flex;align-items:center;gap:22px;margin:0 auto;width:820px;background:#26231F;border-radius:999px;padding:22px 26px 22px 40px;font-size:50px;font-weight:800;color:var(--paper);text-align:left}
.cbox i{width:70px;height:70px;border-radius:50%;background:var(--acc);flex:none}
.cbox .ph{opacity:.45}
.caret{display:inline-block;width:5px;height:54px;background:var(--acc);vertical-align:middle;margin-left:4px}
'''
body = f'''
<section class="scene ink" data-s="0" data-e="3.0"><div class="cam" data-zoom="0,3.0">
 <div class="title" style="top:220px;font-size:100px;line-height:.98">{words("Warum kostet ein gesticktes Logo beim ersten Mal *extra?",0.05,.11)}</div>
 <div class="mach" data-in="0.15" data-a="rise" data-dur=".4"><div class="arm"><div class="ndl" id="ndl0"></div></div><div class="hoop"></div><div class="q" id="q0">?</div></div>
</div><div class="grain"></div></section>

<section class="scene paper" data-s="3.0" data-e="8.6"><div class="cam" data-zoom="3.0,8.6">
 <div class="title" style="top:220px;font-size:86px">{words("Die Stickmaschine sieht *kein Bild.",3.05,.12)}</div>
 <div class="pic" data-in="3.6" data-a="pop" data-dur=".3"><i></i><b>Dein Logo</b></div>
 <div class="arr" data-in="4.6" data-a="left" data-dur=".25">&rarr;</div>
 <div class="code" data-in="4.9" data-a="pop" data-dur=".3">{codeh}</div>
 <div class="lbl" data-in="5.0" data-a="up" data-dur=".3">Stickdatei</div>
 <div class="big" data-in="7.2" data-a="up" data-dur=".3">Jeder Stich muss <span>programmiert</span> werden.</div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="8.6" data-e="13.0"><div class="cam" data-zoom="8.6,13.0">
 <div class="title" style="top:200px;font-size:88px">{words("Tausende Stiche, Reihe für *Reihe.",8.65,.12)}</div>
 <div class="stage"><svg viewBox="-350 -350 700 700" width="700" height="700">
  <circle r="{R+40}" fill="#26231F"/>
  <polyline id="sat" points="{satin}" fill="none" stroke="#FF5A1F" stroke-width="7" stroke-linejoin="round"/>
  <polyline id="rng" points="{ring}" fill="none" stroke="#F3EFE6" stroke-width="6" stroke-linejoin="round"/>
  <circle id="nd" r="12" fill="#fff"/>
 </svg></div>
 <div class="cnt" data-in="9.0" data-a="up" data-dur=".3">Länge, Richtung, Dichte: <span style="color:var(--acc)">alles festgelegt</span></div>
</div><div class="grain"></div></section>

<section class="scene org" data-s="13.0" data-e="17.4"><div class="cam" data-zoom="13.0,17.4">
 <div class="tag" data-in="13.0" data-a="pop" data-dur=".3">Gute Nachricht</div>
 <div class="title">{words("Das passiert nur *einmal.",13.1,.14)}</div>
 <div style="position:absolute;left:90px;right:60px;top:680px">
  <div class="rowck" data-in="13.9" data-a="left" data-dur=".3"><div class="ck"></div>Nachbestellung: Datei ist schon da</div>
  <div class="rowck" data-in="14.6" data-a="left" data-dur=".3"><div class="ck"></div>Neue Leute im Team: gleiches Logo</div>
  <div class="rowck" data-in="15.3" data-a="left" data-dur=".3"><div class="ck"></div>Bei uns transparent in der Offerte</div>
 </div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="17.4" data-e="99"><div class="cam" data-zoom="17.4,22.5">
 {endlogo(17.45)}
 <div style="position:absolute;left:0;right:0;top:820px;text-align:center">
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Euer Logo, sauber *gestickt.",18.1,.12)}</div>
  <div style="margin-top:80px" data-in="19.3" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.5" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.9" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.3" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''
js = '''
const S=document.getElementById('sat'),RG=document.getElementById('rng'),ND=document.getElementById('nd');
const LS=S.getTotalLength(),LR=RG.getTotalLength();S.style.strokeDasharray=LS;RG.style.strokeDasharray=LR;
window.HOOK=function(t){
 document.getElementById('ndl0').style.transform=`translateY(${Math.abs(Math.sin(t*14))*60}px)`;
 const q=document.getElementById('q0');q.style.transform=`rotate(${Math.sin(t*5)*10}deg) scale(${1+0.06*Math.sin(t*9)})`;
 const p=E(cl((t-9.0)/2.6)),r=cl((t-11.6)/1.2);
 S.style.strokeDashoffset=LS*(1-p);RG.style.strokeDashoffset=LR*(1-r);
 const pt=r>0?RG.getPointAtLength(LR*r):S.getPointAtLength(LS*p);ND.setAttribute('cx',pt.x);ND.setAttribute('cy',pt.y);
 ND.style.opacity=(t>9&&t<12.8)?1:0;
 const c=Math.floor(cl((t-19.7)/.8)*4);const ct=document.getElementById('ctext');
 if(c>0){ct.textContent='TEAM'.slice(0,c);ct.className='';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [3.0, 8.6, 13.0, 17.4], 'reel45/r8/reel.html')
print('ok')
