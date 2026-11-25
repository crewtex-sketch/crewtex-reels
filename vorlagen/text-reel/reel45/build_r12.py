exec(open(__file__.replace('build_r12.py', 'common.py')).read())
# REEL 12: Wovor hat ein Wirt *wirklich Angst?
STROKE = 'stroke="#121110" stroke-width="14" stroke-linecap="round" stroke-linejoin="round" fill="none"'

def prez(w=420, extra=''):
    # Strichmännchen mit Trompete
    return f'''<svg viewBox="-60 0 520 560" width="{w*1.3:.0f}" height="{w*560/400:.0f}" style="overflow:visible">
 <g {STROKE}>
  <circle cx="200" cy="110" r="62" fill="#fff"/>
  <path d="M200 172 v190"/>
  <path d="M200 362 l-70 150"/><path d="M200 362 l70 150"/>
  <path d="M200 230 l-80 60 l40 40"/>
  <path d="M200 230 l70 20 l40 10"/>
 </g>
 <g id="eyes"><circle cx="178" cy="102" r="8" fill="#121110"/><circle cx="222" cy="102" r="8" fill="#121110"/></g>
 <path id="mouth" d="M175 140 q25 -14 50 0" {STROKE} stroke-width="10"/>
 <g transform="translate(250,250)">
  <ellipse cx="70" cy="10" rx="85" ry="16" fill="#FF5A1F" stroke="#121110" stroke-width="8"/>
  <rect x="30" y="-48" width="24" height="52" rx="6" fill="#fff" stroke="#121110" stroke-width="7"/>
  <rect x="80" y="-62" width="26" height="66" rx="6" fill="#fff" stroke="#121110" stroke-width="7"/>
 </g>
 {extra}
</svg>'''

drops = ''.join(f'<path class="drop" d="M{x} {y} q-12 22 0 30 q12 -8 0 -30z" fill="#5B8DB8" style="opacity:0"/>' for x, y in [(120, 70), (285, 60), (300, 120)])

bubbles = [('l', 'Entschuldigung, arbeiten Sie hier?', 9.2), ('r', 'Nein, ich bin auch Gast', 9.7), ('l', 'Und Sie?', 10.2), ('r', 'Ich warte seit 20 Minuten', 10.7), ('l', 'Wer bringt hier die Rechnung?', 11.2)]
chat = ''.join(f'<div class="bb {s}" data-in="{t}" data-a="pop" data-dur=".25">{txt}</div>' for s, txt, t in bubbles)

css = '''
.serif{font-family:Caladea,"DejaVu Serif",serif}
.st{position:absolute;left:80px;right:80px;top:170px;font-weight:700;font-size:96px;line-height:1.0;letter-spacing:-.02em;text-align:center;color:var(--ink)}
.st .kw.hl{color:var(--acc)}
.fig{position:absolute;left:50%;top:640px;transform:translateX(-50%)}
.fig svg{display:block}
.meter{position:absolute;left:110px;right:110px;top:1500px}
.meter .lab{display:flex;justify-content:space-between;font-family:Inter,sans-serif;font-weight:900;font-size:50px;color:var(--ink);margin-bottom:22px}
.meter .lab b{color:var(--acc);font-size:64px}
.track{position:relative;height:90px;border:10px solid var(--ink);border-radius:999px;background:#fff}
.fill{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:999px;background:var(--acc)}
.over{position:absolute;right:-40px;top:-200px;font-family:Inter,sans-serif;font-weight:900;font-size:150px;color:var(--acc);transform:rotate(-10deg);letter-spacing:-.04em}
.sit{position:absolute;left:90px;right:90px;top:170px;text-align:center;font-weight:700;font-size:92px;line-height:1.02;color:var(--ink)}
.chatwrap{position:absolute;left:70px;right:70px;top:560px;display:flex;flex-direction:column;gap:30px}
.bb{max-width:760px;padding:28px 38px;border-radius:40px;font-size:48px;font-weight:700;line-height:1.2}
.bb.l{align-self:flex-start;background:#2B2825;color:var(--paper);border-bottom-left-radius:10px}
.bb.r{align-self:flex-end;background:#DCF8C6;color:var(--ink);border-bottom-right-radius:10px}
.unread{position:absolute;right:90px;top:420px;background:var(--acc);color:var(--ink);font-weight:900;font-size:52px;padding:12px 30px;border-radius:999px}
.steps{position:absolute;left:90px;right:90px;top:560px;display:grid;gap:40px}
.steps div{display:flex;gap:30px;align-items:center;font-size:62px;font-weight:900;letter-spacing:-.02em}
.steps .n{width:110px;height:110px;border-radius:50%;background:var(--acc);color:var(--ink);display:grid;place-items:center;font-size:54px;flex:none}
.price{position:absolute;left:90px;right:90px;top:1130px;font-size:44px;font-weight:800;line-height:1.3}
.price b{color:var(--acc)}
.m2{top:1460px}
.cbox{display:flex;align-items:center;gap:22px;margin:0 auto;width:820px;background:#26231F;border-radius:999px;padding:22px 26px 22px 40px;font-size:50px;font-weight:800;color:var(--paper);text-align:left}
.cbox i{width:70px;height:70px;border-radius:50%;background:var(--acc);flex:none}
.cbox .ph{opacity:.45}
.caret{display:inline-block;width:5px;height:54px;background:var(--acc);vertical-align:middle;margin-left:4px}
'''

body = f'''
<section class="scene" style="background:#fff" data-s="0" data-e="3.0"><div class="cam" data-zoom="0,3.0">
 <div class="st serif">{words("Wovor hat ein Wirt *wirklich Angst?", 0.0, .06)}</div>
 <div class="fig" id="fig0">{prez(430)}</div>
 <div class="meter"><div class="lab"><span>Angst-Skala</span><b id="num0">0/10</b></div><div class="track"><div class="fill" id="fill0"></div></div></div>
</div><div class="grain"></div></section>

<section class="scene" style="background:#fff" data-s="3.0" data-e="8.6"><div class="cam" data-zoom="3.0,8.6">
 <div class="sit serif">{words("Freitagabend, volles Haus, und *niemand erkennt, wer bedient.", 3.05, .08)}</div>
 <div class="fig" id="fig1" style="top:700px">{prez(400, drops)}</div>
 <div class="meter"><div class="lab"><span>Angst-Skala</span><b id="num1">5/10</b></div><div class="track"><div class="fill" id="fill1"></div></div>
  <div class="over" id="over" style="opacity:0">11/10</div></div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="8.6" data-e="13.0"><div class="cam" data-zoom="8.6,13.0">
 <div class="title" style="top:200px;font-size:88px">{words("Am *Tisch 7:", 8.65, .12)}</div>
 
 <div class="chatwrap">{chat}</div>
</div><div class="grain"></div></section>

<section class="scene paper" data-s="13.0" data-e="17.4"><div class="cam" data-zoom="13.0,17.4">
 <div class="tag" data-in="13.0" data-a="pop" data-dur=".3">Mit Crewtex</div>
 <div class="title">{words("Euer Team, *sofort erkennbar:", 13.1, .14)}</div>
 <div class="steps">
  <div data-in="13.7" data-a="left" data-dur=".3"><span class="n">1</span>Logo schicken</div>
  <div data-in="14.3" data-a="left" data-dur=".3"><span class="n">2</span>Grössen per Link</div>
  <div data-in="14.9" data-a="left" data-dur=".3"><span class="n">3</span>Einzeln verpackt mit Name</div>
 </div>
 <div class="price" data-in="15.5" data-a="up" data-dur=".3">Zum Beispiel: Hoodie mit Stick <b>ab ca. CHF 38</b>, T-Shirt mit Druck <b>ab ca. CHF 23</b></div>
 <div class="meter m2" data-in="15.9" data-a="up" data-dur=".3"><div class="lab"><span>Angst-Skala</span><b id="num2">11/10</b></div><div class="track"><div class="fill" id="fill2"></div></div></div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="17.4" data-e="99"><div class="cam" data-zoom="17.4,22.5">
 {endlogo(17.45)}
 <div style="position:absolute;left:0;right:0;top:820px;text-align:center">
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Shirts, Schürzen, Polos *mit eurem Logo.", 18.1, .12)}</div>
  <div style="margin-top:80px" data-in="19.3" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.5" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.9" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.3" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''

js = '''
window.HOOK=function(t){
 // Szene 0: Balken läuft sofort los bis 5/10
 const v0=5*E(cl(t/2.6));
 document.getElementById('fill0').style.width=(v0*10)+'%';
 document.getElementById('num0').textContent=Math.round(v0)+'/10';
 // Szene 1: von 5 auf 10, dann Überlauf 11/10
 const p1=cl((t-5.2)/1.6),v1=5+5*E(p1);
 const f1=document.getElementById('fill1');f1.style.width=(v1*10)+'%';
 const n1=document.getElementById('num1');n1.textContent=Math.round(v1)+'/10';n1.style.opacity=t>6.9?0:1;
 const ov=document.getElementById('over');
 if(t>6.9){const q=cl((t-6.9)/.3);ov.style.opacity=1;ov.style.transform=`rotate(-10deg) scale(${1+(1-Bk(q))*1.5})`;
  f1.style.width=(108+5*Math.sin(t*40))+'%';}else ov.style.opacity=0;
 const fig=document.getElementById('fig1');const sh=t>5.2?Math.sin(t*55)*(t>6.9?16:7):0;
 fig.style.transform=`translateX(calc(-50% + ${sh}px))`;
 document.querySelectorAll('.drop').forEach((d,i)=>{const a=5.6+i*.3;if(t>a){const q=((t-a)%1.0);d.style.opacity=1-q;d.setAttribute('transform',`translate(0,${q*120})`);}else d.style.opacity=0;});
 const f0=document.getElementById('fig0');f0.style.transform=`translateX(-50%) translateY(${Math.sin(t*6)*6}px)`;
 // Szene 2: Zähler steigt
 
 // Szene 3: Angst fällt auf 0/10
 const p2=cl((t-16.3)/.9),v2=11-11*E(p2);
 document.getElementById('fill2').style.width=Math.min(100,v2*10)+'%';
 document.getElementById('num2').textContent=Math.round(v2)+'/10';
 // Endszene Kommentar
 const k=Math.floor(cl((t-19.7)/.8)*4);const ct=document.getElementById('ctext');
 if(k>0){ct.textContent='TEAM'.slice(0,k);ct.className='';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [3.0, 8.6, 13.0, 17.4], 'reel45/r12/reel.html')
print('ok')
