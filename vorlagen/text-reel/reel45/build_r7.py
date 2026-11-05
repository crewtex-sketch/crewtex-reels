exec(open(__file__.replace('build_r7.py', 'common.py')).read())
# REEL 7: Wem öffnest du die Tür? (Firmen)

def worker(kind):
    if kind == 'a':
        shirt, sleeve, extra = '#7D7A74', '#5E8FB8', '<path d="M150 330 l40 70 l-30 10z" fill="#3a3a3a" opacity=".35"/><circle cx="235" cy="420" r="16" fill="#3a3a3a" opacity=".3"/>'
        cap = '<path d="M120 120 q70 -70 140 0 v12 h-140z" fill="#C8432B"/><rect x="230" y="122" width="70" height="14" rx="7" fill="#C8432B"/>'
        logo = ''
    else:
        shirt, sleeve, extra = '#121110', '#121110', ''
        cap = '<path d="M120 120 q70 -70 140 0 v12 h-140z" fill="#121110"/><rect x="230" y="122" width="70" height="14" rx="7" fill="#121110"/><circle cx="190" cy="98" r="10" fill="#FF5A1F"/>'
        logo = '<rect x="208" y="285" width="78" height="40" rx="8" fill="#FF5A1F"/><text x="247" y="313" font-size="22" font-weight="900" text-anchor="middle" fill="#121110" font-family="Inter">LOGO</text>'
    return f'''<svg viewBox="0 0 380 640" width="380" height="640">
 <path d="M70 640 v-260 q0 -110 120 -120 q120 10 120 120 v260z" fill="{shirt}"/>
 <path d="M70 380 q-30 60 -20 200 h45 v-200z" fill="{sleeve}"/><path d="M310 380 q30 60 20 200 h-45 v-200z" fill="{sleeve}"/>
 {extra}{logo}
 <rect x="168" y="215" width="44" height="50" fill="#E9B98F"/>
 <circle cx="190" cy="165" r="70" fill="#F2C9A0"/>
 {cap}
</svg>'''

css = '''
.wk{position:absolute;width:420px;height:760px;border-radius:44px;background:#E6DFD2;overflow:hidden;display:flex;align-items:flex-end;justify-content:center}
.wk svg{display:block}
.wk .lb{position:absolute;left:28px;top:24px;width:90px;height:90px;border-radius:50%;background:var(--ink);color:var(--paper);display:grid;place-items:center;font-size:52px;font-weight:900}
.ink .wk{background:#4A453F}
.door{position:absolute;left:70px;right:70px;top:300px;height:900px;border:18px solid #8A6A4A;border-bottom:none;border-radius:20px 20px 0 0}
.poll{position:absolute;left:90px;right:90px;top:1340px;display:grid;grid-template-columns:1fr 1fr;gap:30px}
.poll div{height:150px;border-radius:40px;border:6px solid var(--ink);display:grid;place-items:center;font-size:64px;font-weight:900;background:#fff}
.poll div.on{background:var(--acc);border-color:var(--acc)}
.q{position:absolute;left:90px;right:90px;top:1540px;font-size:84px;font-weight:900;letter-spacing:-.03em;text-align:center}
.q span{color:var(--acc)}
.rowck{display:flex;gap:30px;align-items:center;font-size:60px;font-weight:900;letter-spacing:-.02em;margin-bottom:46px}
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
A, B = worker('a'), worker('b')
body = f'''
<section class="scene ink" data-s="0" data-e="3.0"><div class="cam" data-zoom="0,3.0">
 <div class="title" style="top:200px;font-size:108px;line-height:.96">{words("2 Handwerker klingeln. Wem *öffnest du?",0.05,.12)}</div>
 <div class="wk" style="left:80px;top:900px" data-in="0.1" data-a="left" data-dur=".35"><div class="lb">A</div>{A}</div>
 <div class="wk" style="left:580px;top:900px" data-in="0.25" data-a="right" data-dur=".35"><div class="lb">B</div>{B}</div>
</div><div class="grain"></div></section>

<section class="scene paper" data-s="3.0" data-e="8.6"><div class="cam" data-zoom="3.0,8.6">
 <div class="door" data-in="3.0" data-a="up" data-dur=".3"></div>
 <div class="wk" id="wa" style="left:100px;top:400px" data-in="3.1" data-a="pop" data-dur=".3"><div class="lb">A</div>{A}</div>
 <div class="wk" id="wb" style="left:560px;top:400px" data-in="3.25" data-a="pop" data-dur=".3"><div class="lb">B</div>{B}</div>
 <div class="poll" data-in="3.6" data-a="up" data-dur=".3"><div id="pa">A</div><div id="pb">B</div></div>
 <div class="tap" id="tap"></div>
 <div class="q" data-in="6.4" data-a="pop" data-dur=".3">Ehrlich? <span>B.</span></div>
</div><div class="grain"></div></section>

<section class="scene org" data-s="8.6" data-e="13.0"><div class="cam" data-zoom="8.6,13.0">
 <div class="title" style="top:260px;font-size:100px;line-height:.98">{words("Der erste Eindruck hängt am *Shirt.",8.65,.13)}</div>
 <div style="position:absolute;left:90px;right:60px;top:700px">
  <div class="rowck" data-in="9.6" data-a="left" data-dur=".3"><div class="ck"></div>Wirkt sofort professionell</div>
  <div class="rowck" data-in="10.3" data-a="left" data-dur=".3"><div class="ck"></div>Schafft Vertrauen an der Tür</div>
  <div class="rowck" data-in="11.0" data-a="left" data-dur=".3"><div class="ck"></div>Werbung auf jeder Baustelle</div>
 </div>
</div><div class="grain"></div></section>

<section class="scene paper" data-s="13.0" data-e="17.4"><div class="cam" data-zoom="13.0,17.4">
 <div class="tag" data-in="13.0" data-a="pop" data-dur=".3">So einfach</div>
 <div class="title">{words("Euer Team in *Firmenkleidung:",13.1,.14)}</div>
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
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Arbeitskleidung mit eurem *Firmenlogo.",18.1,.12)}</div>
  <div style="margin-top:80px" data-in="19.3" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.5" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.9" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.3" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''
js = '''
window.HOOK=function(t){
 const tap=document.getElementById('tap');const a=5.4,q=cl((t-a)/.4);
 tap.style.left='740px';tap.style.top='1390px';tap.style.opacity=(t>a&&t<a+.4)?(1-q):0;tap.style.transform=`scale(${0.6+q*0.8})`;
 document.getElementById('pb').classList.toggle('on',t>5.5);
 if(t>5.6){const f=cl((t-5.6)/.4);const wa=document.getElementById('wa');wa.style.opacity=1-0.6*f;wa.style.filter=`grayscale(${f})`;
   document.getElementById('wb').style.transform=`scale(${1+0.04*E(f)})`;}
 const c=Math.floor(cl((t-19.7)/.8)*4);const ct=document.getElementById('ctext');
 if(c>0){ct.textContent='TEAM'.slice(0,c);ct.className='';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [3.0, 8.6, 13.0, 17.4], 'reel45/r7/reel.html')
print('ok')
