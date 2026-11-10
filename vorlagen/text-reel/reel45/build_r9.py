exec(open(__file__.replace('build_r9.py', 'common.py')).read())
# REEL 9: Warum tragen im Spital nicht alle die gleiche Farbe?
def fig(col, logo=False, w=200):
    lg = '<circle cx="232" cy="300" r="20" fill="#FF5A1F"/>' if logo else ''
    return f'''<svg viewBox="0 0 380 640" width="{w}" height="{w*640/380:.0f}">
 <path d="M70 640 v-260 q0 -110 120 -120 q120 10 120 120 v260z" fill="{col}"/>
 <path d="M70 380 q-30 60 -20 200 h45 v-200z" fill="{col}" opacity=".85"/><path d="M310 380 q30 60 20 200 h-45 v-200z" fill="{col}" opacity=".85"/>
 {lg}<rect x="168" y="215" width="44" height="50" fill="#E9B98F"/><circle cx="190" cy="165" r="70" fill="#F2C9A0"/>
 <path d="M122 150 q10 -80 68 -84 q58 4 68 84 q-20 -40 -68 -40 q-48 0 -68 40z" fill="#4A3B2E"/></svg>'''
cols = ['#5B8DB8', '#E2B93B', '#6BA77F', '#C76B9A']
row0 = ''.join(f'<div class="fg" style="left:{60+i*245}px;top:1020px" data-in="{0.15+i*0.12:.2f}" data-a="rise" data-dur=".35">{fig(c,False,230)}</div>' for i, c in enumerate(cols))
row1 = ''.join(f'<div class="fg" id="h{i}" style="left:{60+i*245}px;top:860px" data-in="{3.1+i*0.08:.2f}" data-a="pop" data-dur=".3">{fig(c,False,230)}</div>' for i, c in enumerate(cols))
crowd = []
import random; random.seed(4)
pos = [(40,980),(250,940),(470,990),(690,950),(880,1000),(140,1180),(360,1150),(580,1190),(800,1160),(30,1380),(250,1350),(470,1390),(690,1350),(900,1380)]
team = {2, 7, 11}
for i, (x, y) in enumerate(pos):
    t = i in team
    crowd.append(f'<div class="fg{" tm" if t else ""}" style="left:{x}px;top:{y}px;z-index:{y}" data-in="{8.7+i*0.04:.2f}" data-a="up" data-dur=".25">{fig("#FF5A1F" if t else "#4E4943", t, 170)}</div>')
crowd = ''.join(crowd)
css = '''
.fg{position:absolute}
.fg svg{display:block}
.bub{position:absolute;left:120px;right:120px;top:600px;background:#fff;color:var(--ink);border-radius:40px;padding:34px 40px;font-size:54px;font-weight:900;text-align:center;box-shadow:0 20px 50px rgba(0,0,0,.18)}
.bub::after{content:"";position:absolute;left:50%;bottom:-30px;margin-left:-30px;border:30px solid transparent;border-top-color:#fff;border-bottom:0}
.sec{position:absolute;left:90px;right:90px;top:1520px;text-align:center;font-size:96px;font-weight:900;letter-spacing:-.04em}
.sec span{color:var(--acc)}
.tm{filter:drop-shadow(0 0 30px rgba(255,90,31,.8))}
.steps{position:absolute;left:90px;right:90px;top:640px;display:grid;gap:40px}
.steps div{display:flex;gap:30px;align-items:center;font-size:62px;font-weight:900;letter-spacing:-.02em}
.steps .n{width:110px;height:110px;border-radius:50%;background:var(--acc);color:var(--ink);display:grid;place-items:center;font-size:54px;flex:none}
.price{position:absolute;left:90px;right:90px;top:1380px;font-size:44px;font-weight:800;line-height:1.3}
.price b{color:var(--acc)}
.cbox{display:flex;align-items:center;gap:22px;margin:0 auto;width:820px;background:#26231F;border-radius:999px;padding:22px 26px 22px 40px;font-size:50px;font-weight:800;color:var(--paper);text-align:left}
.cbox i{width:70px;height:70px;border-radius:50%;background:var(--acc);flex:none}
.cbox .ph{opacity:.45}
.caret{display:inline-block;width:5px;height:54px;background:var(--acc);vertical-align:middle;margin-left:4px}
'''
body = f'''
<section class="scene ink" data-s="0" data-e="3.0"><div class="cam" data-zoom="0,3.0">
 <div class="title" style="top:220px;font-size:100px;line-height:.98">{words("Warum tragen im Spital nicht alle die *gleiche Farbe?",0.05,.11)}</div>
 {row0}
</div><div class="grain"></div></section>

<section class="scene paper" data-s="3.0" data-e="8.6"><div class="cam" data-zoom="3.0,8.6">
 <div class="title" style="top:200px;font-size:88px">{words("Weil man in Sekunden sehen muss, *wer wer ist.",3.05,.1)}</div>
 <div class="bub" id="bub" data-in="4.6" data-a="pop" data-dur=".3">Wen kann ich fragen?</div>
 {row1}
 <div class="sec" data-in="6.6" data-a="stamp" data-dur=".3">1 Blick. <span>Klar.</span></div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="8.6" data-e="13.0"><div class="cam" data-zoom="8.6,13.0">
 <div class="title" style="top:200px;font-size:92px">{words("Am Vereinsfest oder auf der Baustelle: *gleiches Prinzip.",8.65,.1)}</div>
 {crowd}
 <div class="sec" style="top:1700px;font-size:72px" data-in="11.2" data-a="up" data-dur=".3">Euer Team: <span>sofort erkennbar.</span></div>
</div><div class="grain"></div></section>

<section class="scene paper" data-s="13.0" data-e="17.4"><div class="cam" data-zoom="13.0,17.4">
 <div class="tag" data-in="13.0" data-a="pop" data-dur=".3">So einfach</div>
 <div class="title">{words("Euer Team mit *Logo:",13.1,.14)}</div>
 <div class="steps">
  <div data-in="13.7" data-a="left" data-dur=".3"><span class="n">1</span>Logo schicken</div>
  <div data-in="14.4" data-a="left" data-dur=".3"><span class="n">2</span>Grössen per Link</div>
  <div data-in="15.1" data-a="left" data-dur=".3"><span class="n">3</span>Einzeln verpackt mit Name</div>
 </div>
 <div class="price" data-in="15.9" data-a="up" data-dur=".3">Zum Beispiel: T-Shirt mit Druck <b>ab ca. CHF 23</b>, Hoodie mit Stick <b>ab ca. CHF 38</b></div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="17.4" data-e="99"><div class="cam" data-zoom="17.4,22.5">
 {endlogo(17.45)}
 <div style="position:absolute;left:0;right:0;top:820px;text-align:center">
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Teamkleidung, die man *erkennt.",18.1,.12)}</div>
  <div style="margin-top:80px" data-in="19.3" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.5" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.9" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.3" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''
js = '''
window.HOOK=function(t){
 for(let i=0;i<4;i++){const h=document.getElementById('h'+i);if(t>5.4){const on=(i===Math.floor((t-5.4)/0.35)%4);h.style.transform=`translateY(${on?-30:0}px) scale(${on?1.06:1})`;h.style.opacity=t>6.6?(i===0?1:.35):1;}}
 document.querySelectorAll('.tm').forEach(el=>{if(t>10.4){const f=cl((t-10.4)/.4);el.style.transform=`translateY(${-40*E(f)}px) scale(${1+.12*E(f)})`;}});
 const c=Math.floor(cl((t-19.7)/.8)*4);const ct=document.getElementById('ctext');
 if(c>0){ct.textContent='TEAM'.slice(0,c);ct.className='';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [3.0, 8.6, 13.0, 17.4], 'reel45/r9/reel.html')
print('ok')
