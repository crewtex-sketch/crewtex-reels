exec(open(__file__.replace('build_r7b.py', 'common.py')).read())
# REEL 7b: Wem öffnest du die Tür? (Firmen) - hochwertigere Animation

def worker(kind, uid):
    if kind == 'a':
        top1, top2, pants, cap, accent = '#8C8983', '#6E6B66', '#4F6E91', '#C8432B', '#C8432B'
        torso = f'''<path d="M108 300 q82 -40 164 0 l26 210 h-216z" fill="url(#t{uid})"/>
 <path d="M160 268 q30 40 60 0 l6 34 q-36 26 -72 0z" fill="#5E5B56"/>
 <path d="M140 330 q-10 70 10 140" stroke="#5E5B56" stroke-width="6" fill="none"/>
 <ellipse cx="236" cy="420" rx="20" ry="14" fill="#4a4741" opacity=".55"/>
 <path d="M150 380 l34 52 l-26 6z" fill="#4a4741" opacity=".45"/>
 <rect x="168" y="470" width="50" height="40" rx="8" fill="#5E5B56" opacity=".7"/>'''
        sleeveL = '#7A9CC0'; sleeveR = '#8C8983'
        capsvg = f'<path d="M126 132 q64 -78 128 0 v10 h-128z" fill="{cap}"/><rect x="226" y="134" width="74" height="15" rx="7" fill="{cap}" transform="rotate(14 226 134)"/>'
        hair = '<path d="M128 150 q-6 40 10 60 l6 -50z" fill="#6B4A2E"/>'
        belt = ''
        boots = '#6B5A48'
    else:
        top1, top2, pants, accent = '#1E1C1A', '#0E0D0C', '#24221F', '#FF5A1F'
        torso = f'''<path d="M108 300 q82 -40 164 0 l26 210 h-216z" fill="url(#t{uid})"/>
 <path d="M160 268 l30 46 l30 -46 l10 10 l-40 56 l-40 -56z" fill="#2E2B28"/>
 <line x1="190" y1="314" x2="190" y2="380" stroke="#2E2B28" stroke-width="5"/>
 <circle cx="190" cy="336" r="5" fill="#3A3733"/><circle cx="190" cy="360" r="5" fill="#3A3733"/>
 <g transform="translate(212 334)"><rect width="66" height="40" rx="9" fill="#FF5A1F"/><circle cx="16" cy="20" r="8" fill="#121110"/><rect x="29" y="14" width="28" height="5" rx="2.5" fill="#121110"/><rect x="29" y="23" width="20" height="5" rx="2.5" fill="#121110"/></g>
 <rect x="104" y="488" width="174" height="10" fill="#FF5A1F"/>'''
        sleeveL = sleeveR = '#1A1816'
        capsvg = '<path d="M126 132 q64 -78 128 0 v10 h-128z" fill="#121110"/><rect x="226" y="134" width="74" height="15" rx="7" fill="#121110" transform="rotate(14 226 134)"/><circle cx="178" cy="100" r="11" fill="#FF5A1F"/>'
        hair = ''
        belt = '<rect x="96" y="508" width="190" height="22" rx="4" fill="#3A2E24"/><rect x="226" y="512" width="44" height="64" rx="6" fill="#4A3C2E"/><rect x="236" y="500" width="8" height="40" rx="3" fill="#9A9A9A"/>'
        boots = '#121110'
    return f'''<svg viewBox="0 0 380 760" width="380" height="760" style="overflow:visible">
 <defs><linearGradient id="t{uid}" x1="0" x2="1"><stop offset="0" stop-color="{top1}"/><stop offset="1" stop-color="{top2}"/></linearGradient>
 <radialGradient id="f{uid}" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#F7D3AE"/><stop offset="1" stop-color="#DDA77C"/></radialGradient></defs>
 <ellipse cx="190" cy="742" rx="150" ry="18" fill="#000" opacity=".25"/>
 <path d="M112 500 h80 l-8 230 h-62z" fill="{pants}"/><path d="M188 500 h80 l-10 230 h-62z" fill="{pants}" opacity=".92"/>
 <path d="M118 718 h70 q6 22 -4 26 h-74 q-4 -20 8 -26z" fill="{boots}"/><path d="M196 718 h70 q12 6 8 26 h-74 q-10 -4 -4 -26z" fill="{boots}"/>
 <path d="M108 305 q-46 30 -50 190 l40 6 q4 -110 30 -150z" fill="{sleeveL}"/>
 <path d="M272 305 q46 30 50 190 l-40 6 q-4 -110 -30 -150z" fill="{sleeveR}"/>
 <circle cx="78" cy="508" r="22" fill="url(#f{uid})"/><circle cx="302" cy="508" r="22" fill="url(#f{uid})"/>
 {torso}{belt}
 <rect x="170" y="226" width="40" height="52" rx="10" fill="#D79F74"/>
 <ellipse cx="190" cy="178" rx="64" ry="72" fill="url(#f{uid})"/>
 {hair}
 <circle cx="168" cy="182" r="6" fill="#2A211B"/><circle cx="212" cy="182" r="6" fill="#2A211B"/>
 <path d="M172 214 q18 {12 if kind=='b' else 4} 36 0" stroke="#8A4A34" stroke-width="5" fill="none" stroke-linecap="round"/>
 {capsvg}
</svg>'''

css = '''
.scene{will-change:transform}
.bg-hall{position:absolute;inset:0;background:radial-gradient(120% 70% at 50% 35%,#2B2723 0%,#121110 70%)}
.persp{position:absolute;left:0;right:0;top:720px;height:1200px;perspective:1800px}
.frame{position:absolute;left:170px;top:0;width:740px;height:1180px;border-radius:26px 26px 0 0;background:linear-gradient(180deg,#FFE2C9,#FF9A63 60%,#F3EFE6);overflow:hidden;box-shadow:inset 0 0 0 22px #3A2E24}
.frame .wk2{position:absolute;bottom:0}
.doorp{position:absolute;left:170px;top:0;width:740px;height:1180px;transform-origin:0 50%;border-radius:20px 20px 0 0;background:linear-gradient(90deg,#5A4330,#6E5239 50%,#5A4330);box-shadow:inset 0 0 0 22px #3A2E24;backface-visibility:hidden}
.doorp i{position:absolute;left:90px;right:90px;height:300px;border:10px solid rgba(0,0,0,.18);border-radius:14px}
.doorp b{position:absolute;right:70px;top:560px;width:40px;height:110px;border-radius:20px;background:#C9A26B}
.doorp em{position:absolute;left:50%;top:230px;width:46px;height:46px;margin-left:-23px;border-radius:50%;background:#1A1512;box-shadow:0 0 0 8px #C9A26B}
.ring{position:absolute;left:925px;top:1240px;width:60px;height:60px;border-radius:50%;border:6px solid var(--acc);opacity:0}
.bell{position:absolute;left:930px;top:1245px;width:50px;height:50px;border-radius:50%;background:var(--acc);box-shadow:0 0 30px rgba(255,90,31,.8)}
.ht{position:absolute;z-index:5;left:80px;right:60px;top:150px;font-weight:900;letter-spacing:-.04em;line-height:.95;color:var(--paper)}
.ht .l1{font-size:72px;opacity:.7}
.ht .l2{font-size:104px;margin-top:10px;white-space:nowrap}
.ht .l2 span{color:var(--acc)}
.mask{display:block;overflow:hidden;padding-bottom:10px}
.mask > span{display:inline-block}
.stage{position:absolute;inset:0;background:linear-gradient(180deg,#F6F1E8 0%,#EAE2D3 62%,#D9CDB8 62.2%,#CDBFA6 100%)}
.spot{position:absolute;left:520px;top:300px;width:620px;height:1100px;background:radial-gradient(closest-side,rgba(255,90,31,.42),rgba(255,90,31,0));opacity:0}
.wk{position:absolute;width:380px;height:760px}
.chipl{position:absolute;width:96px;height:96px;border-radius:50%;background:var(--ink);color:var(--paper);display:grid;place-items:center;font-size:54px;font-weight:900;box-shadow:0 10px 24px rgba(0,0,0,.25)}
.vote{position:absolute;left:90px;right:90px;top:1430px;height:150px;border-radius:75px;background:#fff;box-shadow:0 20px 50px rgba(18,17,16,.18);overflow:hidden}
.vote .fill{position:absolute;left:0;top:0;bottom:0;width:0;background:var(--acc)}
.vote .lab{position:absolute;inset:0;display:flex;justify-content:space-between;align-items:center;padding:0 60px;font-size:56px;font-weight:900}
.q2{position:absolute;left:90px;right:90px;top:140px;font-size:92px;font-weight:900;letter-spacing:-.04em;line-height:.98;color:var(--ink)}
.q2 u{text-decoration:none;position:relative;color:var(--acc)}
.q2 u::after{content:"";position:absolute;left:0;right:0;bottom:-6px;height:14px;background:var(--acc);transform-origin:0 50%;transform:scaleX(var(--ul,0));opacity:.35}
.tap2{position:absolute;width:110px;height:110px;border-radius:50%;border:9px solid var(--ink);opacity:0;z-index:20}
.macro{position:absolute;left:90px;right:90px;top:560px;height:700px;border-radius:50px;background:radial-gradient(120% 90% at 30% 20%,#2C2926,#121110);overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.45)}
.macro .weave{position:absolute;inset:-50%;background-image:repeating-linear-gradient(45deg,rgba(255,255,255,.035) 0 3px,transparent 3px 9px),repeating-linear-gradient(-45deg,rgba(255,255,255,.03) 0 3px,transparent 3px 9px)}
.macro svg{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)}
.sweep{position:absolute;top:-20%;bottom:-20%;width:180px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);transform:skewX(-18deg)}
.org3 {background:var(--acc)}
.t3{position:absolute;left:90px;right:90px;top:170px;font-size:92px;font-weight:900;letter-spacing:-.04em;line-height:.98;color:var(--ink)}
.t3 span{color:var(--paper)}
.ckrow{position:absolute;left:90px;right:90px;top:1330px;display:grid;gap:22px}
.ckrow div{display:flex;gap:26px;align-items:center;font-size:52px;font-weight:900;color:var(--ink)}
.ckrow .ck{width:80px;height:80px}
.ckrow .ck::after{left:27px;top:14px;width:18px;height:36px;border-right-width:10px;border-bottom-width:10px}
.cards{position:absolute;left:90px;right:90px;top:560px;perspective:1600px;display:grid;gap:34px}
.card3{height:300px;border-radius:44px;background:#fff;display:flex;align-items:center;gap:40px;padding:0 50px;box-shadow:0 26px 60px rgba(18,17,16,.16);transform-origin:50% 0}
.card3 .ic{width:170px;height:170px;border-radius:40px;background:var(--ink);flex:none;display:grid;place-items:center}
.card3 h6{font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:#8A847B;margin-bottom:10px}
.card3 p{font-size:62px;font-weight:900;letter-spacing:-.03em;line-height:1}
.pricebar{position:absolute;left:90px;right:90px;top:1620px;display:flex;gap:20px}
.pricebar div{flex:1;background:var(--ink);color:var(--paper);border-radius:34px;padding:26px 30px;font-size:34px;font-weight:800;line-height:1.2}
.pricebar b{display:block;color:var(--acc);font-size:58px;font-weight:900;letter-spacing:-.03em}
.cbox{display:flex;align-items:center;gap:22px;margin:0 auto;width:820px;background:#26231F;border-radius:999px;padding:22px 26px 22px 40px;font-size:50px;font-weight:800;color:var(--paper);text-align:left}
.cbox i{width:70px;height:70px;border-radius:50%;background:var(--acc);flex:none}
.cbox .ph{opacity:.45}
.caret{display:inline-block;width:5px;height:54px;background:var(--acc);vertical-align:middle;margin-left:4px}
.glow{position:absolute;left:50%;top:640px;width:900px;height:900px;margin-left:-450px;background:radial-gradient(closest-side,rgba(255,90,31,.35),transparent);opacity:0}
.heart{position:absolute;font-size:0;width:40px;height:40px;background:var(--acc);border-radius:50%;opacity:0}
'''

A1, B1 = worker('a', 'a1'), worker('b', 'b1')
A2, B2 = worker('a', 'a2'), worker('b', 'b2')

icon_up = '<svg viewBox="0 0 100 100" width="100" height="100"><path d="M50 18 v52 M28 40 l22 -22 l22 22" stroke="#FF5A1F" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M20 78 h60" stroke="#F3EFE6" stroke-width="10" stroke-linecap="round"/></svg>'
icon_link = '<svg viewBox="0 0 100 100" width="100" height="100"><rect x="12" y="38" width="44" height="24" rx="12" stroke="#F3EFE6" stroke-width="9" fill="none"/><rect x="44" y="38" width="44" height="24" rx="12" stroke="#FF5A1F" stroke-width="9" fill="none"/></svg>'
icon_bag = '<svg viewBox="0 0 100 100" width="100" height="100"><rect x="18" y="32" width="64" height="54" rx="10" fill="#F3EFE6"/><path d="M36 32 v-8 a14 14 0 0 1 28 0 v8" stroke="#FF5A1F" stroke-width="8" fill="none"/><rect x="30" y="52" width="40" height="8" rx="4" fill="#FF5A1F"/><rect x="30" y="66" width="26" height="8" rx="4" fill="#121110"/></svg>'

body = f'''
<section class="scene ink" id="s1" data-s="0" data-e="3.35"><div class="cam" id="cam1">
 <div class="bg-hall"></div>
 <div class="ht"><span class="mask"><span class="l1" data-in="0.0" data-a="up" data-dur=".3">Ding Dong.</span></span>
  <span class="mask"><span class="l2" data-in="0.25" data-a="up" data-dur=".35">2 Handwerker.</span></span>
  <span class="mask"><span class="l2" data-in="0.6" data-a="up" data-dur=".35">Wem <span>öffnest</span> du?</span></span></div>
 <div class="persp"><div class="frame">
   <div class="wk2" id="h1a" style="left:-10px">{A1}</div><div class="wk2" id="h1b" style="left:370px">{B1}</div>
  </div><div class="doorp" id="door"><i style="top:90px"></i><i style="top:690px"></i><em></em><b></b></div></div>
 <div class="ring" id="r1"></div><div class="ring" id="r2"></div><div class="bell"></div>
</div><div class="grain"></div></section>

<section class="scene paper" id="s2" data-s="3.0" data-e="8.95"><div class="cam" id="cam2">
 <div class="stage"></div><div class="spot" id="spot"></div>
 <div class="q2">Wem öffnest du <u id="ul">die Tür?</u></div>
 <div class="wk" id="wa" style="left:60px;top:560px">{A2}</div>
 <div class="wk" id="wb" style="left:620px;top:560px">{B2}</div>
 <div class="chipl" style="left:80px;top:520px" data-in="3.4" data-a="pop" data-dur=".3">A</div>
 <div class="chipl" style="left:900px;top:520px" data-in="3.5" data-a="pop" data-dur=".3">B</div>
 <div class="vote" data-in="3.7" data-a="up" data-dur=".35"><div class="fill" id="vfill"></div><div class="lab"><span>A</span><span id="vb">B</span></div></div>
 <div class="tap2" id="tap"></div>
 <div class="q2" style="top:1620px;font-size:84px;text-align:center" data-in="6.6" data-a="pop" data-dur=".3">Ehrlich? <u style="--ul:1">B.</u></div>
</div><div class="grain"></div></section>

<section class="scene org3" id="s3" data-s="8.6" data-e="13.35"><div class="cam" id="cam3">
 <div class="t3"><span class="mask"><span data-in="8.7" data-a="up" data-dur=".35">Der erste Eindruck</span></span><span class="mask"><span data-in="8.95" data-a="up" data-dur=".35">hängt am <span>Shirt.</span></span></span></div>
 <div class="macro" data-in="9.0" data-a="pop" data-dur=".4"><div class="weave"></div>
  <svg viewBox="0 0 700 460" width="760" height="500">
   <rect x="60" y="70" width="580" height="320" rx="60" fill="none" stroke="#FF5A1F" stroke-width="10" stroke-dasharray="22 14" id="stitchbox"/>
   <text x="350" y="275" text-anchor="middle" font-family="Inter" font-weight="900" font-size="90" letter-spacing="-2" fill="#FF5A1F" fill-opacity="0" stroke="#FF5A1F" stroke-width="4" id="logotext">EUER LOGO</text>
  </svg><div class="sweep" id="sweep"></div></div>
 <div class="ckrow">
  <div data-in="11.0" data-a="left" data-dur=".3"><div class="ck"></div>Wirkt sofort professionell</div>
  <div data-in="11.45" data-a="left" data-dur=".3"><div class="ck"></div>Schafft Vertrauen an der Tür</div>
  <div data-in="11.9" data-a="left" data-dur=".3"><div class="ck"></div>Werbung auf jeder Baustelle</div>
 </div>
</div><div class="grain"></div></section>

<section class="scene paper" id="s4" data-s="13.0" data-e="17.75"><div class="cam" id="cam4">
 <div class="tag" data-in="13.15" data-a="pop" data-dur=".3">So einfach</div>
 <div class="title" style="top:320px;font-size:88px">{words("Euer Team in *Firmenkleidung:",13.2,.12)}</div>
 <div class="cards">
  <div class="card3" id="c1"><div class="ic">{icon_up}</div><div><h6>Schritt 1</h6><p>Logo schicken</p></div></div>
  <div class="card3" id="c2"><div class="ic">{icon_link}</div><div><h6>Schritt 2</h6><p>Grössen per Link</p></div></div>
  <div class="card3" id="c3"><div class="ic">{icon_bag}</div><div><h6>Schritt 3</h6><p>Einzeln verpackt mit Name</p></div></div>
 </div>
 <div class="pricebar"><div data-in="15.9" data-a="up" data-dur=".3">T-Shirt mit Druck<b>ab ca. CHF 23</b></div><div data-in="16.15" data-a="up" data-dur=".3">Hoodie mit Stick<b>ab ca. CHF 38</b></div></div>
</div><div class="grain"></div></section>

<section class="scene ink" id="s5" data-s="17.4" data-e="99"><div class="cam" data-zoom="17.4,22.5">
 <div class="glow" id="glow"></div>
 {endlogo(17.55)}
 <div style="position:absolute;left:0;right:0;top:820px;text-align:center">
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Arbeitskleidung mit eurem *Firmenlogo.",18.1,.12)}</div>
  <div style="margin-top:80px" data-in="19.2" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.5" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.9" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.3" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''

js = '''
const io=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
function trans(id,a,dur){ // incoming scene slides up with depth
  const s=document.getElementById(id);const p=cl((t_-a)/dur);const e=io(p);
  s.style.transform=`translateY(${(1-e)*100}%)`;s.style.zIndex=10;}
let t_=0;
window.HOOK=function(t){t_=t;
 // scene transitions: push up, previous recedes
 const T=[['s2',3.0],['s3',8.6],['s4',13.0],['s5',17.4]];const ids=['s1','s2','s3','s4','s5'];
 ids.forEach(i=>{const s=document.getElementById(i);s.style.transform='none';s.style.zIndex=1;s.style.filter='none';});
 T.forEach(([id,a],k)=>{if(t>=a&&t<a+.35){trans(id,a,.35);const prev=document.getElementById(ids[k]);const e=io(cl((t-a)/.35));prev.style.transform=`scale(${1-.08*e}) translateY(${-6*e}%)`;prev.style.filter=`brightness(${1-.5*e})`;}});
 // S1: camera push, bell rings, door opens in 3D
 document.getElementById('cam1').style.transform=`scale(${1+0.06*E(cl(t/3))})`;
 [['r1',0.05],['r2',0.35],['r1',0.9],['r2',1.2]].forEach(([id,a])=>{const q=(t-a)/.6;if(q>=0&&q<1){const r=document.getElementById(id);r.style.opacity=1-q;r.style.transform=`scale(${1+q*2.6})`;}});
 const dp=io(cl((t-1.2)/1.1));const d=document.getElementById('door');d.style.transform=`rotateY(${-78*dp}deg)`;d.style.filter=`brightness(${1-.4*dp})`;
 const bob=k=>Math.sin(t*3.2+k)*4;
 document.getElementById('h1a').style.transform=`translateY(${bob(0)}px)`;document.getElementById('h1b').style.transform=`translateY(${bob(1.4)}px)`;
 // S2: walk in, vote, A fades back, B steps forward with spotlight
 const wa=document.getElementById('wa'),wb=document.getElementById('wb');
 const ia=E(cl((t-3.1)/.5)),ib=E(cl((t-3.25)/.5));
 const pick=E(cl((t-5.6)/.5));
 wa.style.transform=`translateX(${(1-ia)*-500}px) translateY(${bob(.3)+pick*40}px) scale(${1-.12*pick})`;wa.style.filter=`grayscale(${pick}) brightness(${1-.25*pick})`;wa.style.opacity=1-.35*pick;
 wb.style.transform=`translateX(${(1-ib)*500}px) translateY(${bob(2)-pick*20}px) scale(${1+.08*pick})`;
 document.getElementById('spot').style.opacity=pick;
 document.getElementById('ul').style.setProperty('--ul',E(cl((t-4.2)/.5)));
 const tap=document.getElementById('tap');const ta=5.3,tq=cl((t-ta)/.45);tap.style.left='800px';tap.style.top='1450px';tap.style.opacity=(t>ta&&t<ta+.45)?(1-tq):0;tap.style.transform=`scale(${.6+tq*.9})`;
 document.getElementById('vfill').style.width=(E(cl((t-5.45)/.6))*100)+'%';
 document.getElementById('cam2').style.transform=`scale(${1+.04*E(cl((t-5.5)/3))})`;
 // S3: stitch draw + logo stroke + light sweep
 const sb=document.getElementById('stitchbox');const per=1800;const sp=cl((t-9.3)/1.0);sb.setAttribute('stroke-dashoffset',(1-sp)*per*0);sb.style.opacity=sp>0?1:0;sb.style.strokeDasharray=`22 14`;sb.style.clipPath=`inset(0 ${100-sp*100}% 0 0)`;
 const lt=document.getElementById('logotext');const lp=cl((t-9.5)/1.1);lt.style.strokeDasharray='900';lt.style.strokeDashoffset=900*(1-lp);lt.setAttribute('fill-opacity',E(cl((t-10.4)/.4)));
 const sw=document.getElementById('sweep');sw.style.left=(-300+1400*E(cl((t-10.6)/.9)))+'px';
 document.getElementById('cam3').style.transform=`scale(${1+.03*cl((t-8.6)/4.4)})`;
 // S4: cards flip in (3D)
 [['c1',13.7],['c2',14.3],['c3',14.9]].forEach(([id,a])=>{const c=document.getElementById(id);const p=cl((t-a)/.45);const e=Bk(p);c.style.opacity=p>0?Math.min(1,p*3):0;c.style.transform=`rotateX(${(1-e)*-85}deg) translateZ(0)`;});
 // S5 glow pulse
 document.getElementById('glow').style.opacity=cl((t-17.6)/.6)*(.7+.3*Math.sin(t*2.4));
 const c=Math.floor(cl((t-19.7)/.8)*4);const ct=document.getElementById('ctext');
 if(c>0){ct.textContent='TEAM'.slice(0,c);ct.className='';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [], 'reel45/r7b/reel.html')
print('ok')
