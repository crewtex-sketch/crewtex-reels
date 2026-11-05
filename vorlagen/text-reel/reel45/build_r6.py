exec(open(__file__.replace('build_r6.py', 'common.py')).read())
# REEL 6: WhatsApp-Chaos vs. 1 Link (Vereine)
msgs = [
    ("Sandro", "Ich nimm M", 0), ("Lena", "Gits die au in Grau?", 1), ("Sandro", "nei doch L", 0),
    ("Marco", "Wer zahlt das eigentlich?", 1), ("Jil", "bin bis Sunntig i de Ferie", 0), ("Lena", "Was isch mit em Logo??", 1),
    ("Timo", "M oder L, weiss nöd", 0), ("Nadia", "Hät öpper d Liste?", 1), ("Marco", "welli Liste", 0),
    ("Jil", "ich nimm 2", 1), ("Sandro", "doch M", 0), ("Lena", "???", 1),
]
bub = ''.join(
    f'<div class="bb {"r" if s else "l"}" data-in="{3.15 + i * 0.42:.2f}" data-a="pop" data-dur=".22"><b>{n}</b>{m}</div>'
    for i, (n, m, s) in enumerate(msgs))
hookbub = ''.join(
    f'<div class="hb" style="left:{x}px;top:{y}px" data-in="{a:.2f}" data-a="pop" data-dur=".2">{m}</div>'
    for (x, y, a, m) in [(80, 1320, .05, "Ich nimm M"), (520, 1420, .35, "nei doch L"), (140, 1540, .65, "wer zahlt??"),
                         (560, 1640, .95, "Logo?"), (90, 1740, 1.25, "hät öpper d Liste"), (600, 1250, 1.55, "???"),
                         (430, 1180, 1.85, "M oder L")])
names = [("Sandro", "M"), ("Lena", "S"), ("Marco", "L"), ("Jil", "M"), ("Timo", "XL"), ("Nadia", "S"), ("Luca", "L"), ("Mia", "XS")]
rows = ''.join(f'<div class="nm" data-in="{10.05 + i * 0.2:.2f}" data-a="right" data-dur=".22"><b>{n}</b><span>{s}</span><i class="okd"></i></div>'
               for i, (n, s) in enumerate(names))
bags = ''.join(f'<div class="bag" data-in="{13.25 + i * 0.15:.2f}" data-a="drop" data-dur=".4" data-rot="{rt}deg" style="left:{x}px;top:{y}px"><span>{n}</span><em>{s}</em></div>'
               for i, (x, y, rt, n, s) in enumerate([(110, 1300, -2, "Sandro", "M"), (400, 1300, 1, "Lena", "S"), (690, 1300, -1, "Marco", "L"),
                                                    (255, 1070, 2, "Jil", "M"), (545, 1070, -2, "Timo", "XL"), (400, 840, 0, "Nadia", "S")]))
css = '''
.hb{position:absolute;background:#fff;color:var(--ink);font-size:44px;font-weight:800;padding:20px 34px;border-radius:40px;box-shadow:0 14px 30px rgba(0,0,0,.35)}
.chat{position:absolute;left:150px;top:420px;width:780px;height:1330px;border-radius:70px;background:#ECE5DA;border:14px solid #2A2724;overflow:hidden}
.chat .top{position:relative;z-index:2;background:var(--ink);color:var(--paper);padding:56px 44px 30px;display:flex;align-items:center;gap:24px}
.chat .top i{width:80px;height:80px;border-radius:50%;background:var(--acc);flex:none}
.chat .top b{font-size:42px;display:block}.chat .top small{font-size:28px;opacity:.7}
.chat .top em{margin-left:auto;font-style:normal;background:var(--acc);color:var(--ink);font-weight:900;font-size:34px;border-radius:999px;padding:8px 22px;min-width:110px;text-align:center}
.feed{position:absolute;left:0;right:0;top:190px;padding:20px 30px;display:flex;flex-direction:column;gap:14px}
.bb{max-width:560px;font-size:38px;font-weight:700;padding:16px 26px 20px;border-radius:30px;background:#fff;color:var(--ink);line-height:1.15}
.bb b{display:block;font-size:26px;color:var(--acc);margin-bottom:4px}
.bb.r{align-self:flex-end;background:#DCEFD0}
.bb.l{align-self:flex-start}
.over{position:absolute;left:60px;right:60px;top:760px;background:var(--ink);color:var(--paper);border-radius:40px;padding:50px 50px;text-align:center;font-weight:900;font-size:84px;line-height:1;letter-spacing:-.03em;box-shadow:0 30px 80px rgba(0,0,0,.4);z-index:5}
.over span{color:var(--acc);display:block;margin-top:14px}
.phone{position:absolute;left:190px;top:560px;width:700px;height:1160px;border-radius:70px;background:var(--paper);border:14px solid #2A2724;overflow:hidden;color:var(--ink)}
.phone .hd{padding:64px 50px 26px;font-weight:900;font-size:60px;letter-spacing:-.03em;line-height:.95;text-transform:uppercase}
.phone .hd span{color:var(--acc);display:block}
.cnt{margin:0 50px 22px;font-size:34px;font-weight:800;color:#6B665F}.cnt b{color:var(--ink)}
.bar{margin:0 50px 26px;height:18px;border-radius:9px;background:#E2DBCD;overflow:hidden}.bar i{display:block;height:100%;background:var(--acc);width:0}
.list{margin:0 34px}
.nm{display:grid;grid-template-columns:1fr auto 56px;gap:20px;align-items:center;background:#fff;border-radius:26px;padding:18px 26px;margin-bottom:12px;font-size:40px;font-weight:800}
.nm span{background:var(--ink);color:var(--paper);border-radius:999px;padding:4px 20px;font-size:32px}
.okd{width:44px;height:44px;border-radius:50%;background:var(--acc);position:relative}
.okd::after{content:"";position:absolute;left:15px;top:8px;width:10px;height:20px;border-right:6px solid var(--ink);border-bottom:6px solid var(--ink);transform:rotate(45deg)}
.bag{position:absolute;width:280px;height:210px;background:var(--paper);border-radius:22px;color:var(--ink);box-shadow:0 18px 30px rgba(0,0,0,.35)}
.bag::before{content:"";position:absolute;left:24px;top:24px;width:20px;height:20px;border-radius:50%;background:var(--acc)}
.bag span{position:absolute;left:26px;bottom:60px;font-size:48px;font-weight:900}
.bag em{position:absolute;left:26px;bottom:22px;font-style:normal;font-size:30px;font-weight:800;color:var(--acc)}
.cbox{display:flex;align-items:center;gap:22px;margin:0 auto;width:820px;background:#26231F;border-radius:999px;padding:22px 26px 22px 40px;font-size:50px;font-weight:800;color:var(--paper);text-align:left}
.cbox i{width:70px;height:70px;border-radius:50%;background:var(--acc);flex:none}
.cbox .ph{opacity:.45}.cbox .ty{color:var(--paper)}
.caret{display:inline-block;width:5px;height:54px;background:var(--acc);vertical-align:middle;margin-left:4px}
.price{position:absolute;left:90px;right:90px;top:1590px;font-size:44px;font-weight:800;opacity:.85}
.price b{color:var(--acc)}
'''
body = f'''
<section class="scene ink" data-s="0" data-e="3.0"><div class="cam" data-zoom="0,3.0">
 <div class="tag" data-in="0" data-a="pop" data-dur=".25">POV</div>
 <div class="title" style="top:330px;font-size:104px;line-height:.98">{words("Du musst *25 Hoodies für den Verein bestellen.",0.05,.13)}</div>
 {hookbub}
</div><div class="grain"></div></section>

<section class="scene paper" data-s="3.0" data-e="9.0"><div class="cam" data-zoom="3.0,9.0">
 <div class="chat" data-in="3.0" data-a="rise" data-dur=".35">
  <div class="top"><i></i><div><b>Vorstand Hoodies</b><small>14 Mitglieder</small></div><em id="unr">34</em></div>
  <div class="feed" id="feed">{bub}</div>
 </div>
 <div class="over" data-in="7.75" data-a="stamp" data-dur=".35">147 Nachrichten.<span>0 Bestellungen.</span></div>
</div><div class="grain"></div></section>

<section class="scene org" data-s="9.0" data-e="12.9"><div class="cam" data-zoom="9.0,12.9">
 <div class="title" style="top:200px;font-size:110px;text-transform:uppercase;line-height:.92">{words("Oder: *1 Link.",9.05,.16)}</div>
 <div class="phone" data-in="9.3" data-a="rise" data-dur=".4">
  <div class="hd">Hoodies <span>Grössen</span></div>
  <div class="cnt"><b id="cn">0</b> von 25 eingetragen</div>
  <div class="bar"><i id="bar"></i></div>
  <div class="list">{rows}</div>
 </div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="12.9" data-e="17.2"><div class="cam" data-zoom="12.9,17.2">
 <div class="title" style="top:240px;font-size:88px">{words("Jedes Teil *einzeln verpackt. Mit Name und Grösse.",12.95,.11)}</div>
 {bags}
 <div class="price" data-in="15.4" data-a="up" data-dur=".3">Zum Beispiel: Hoodie mit gesticktem Logo <b>ab ca. CHF 38</b></div>
</div><div class="grain"></div></section>

<section class="scene ink" data-s="17.2" data-e="99"><div class="cam" data-zoom="17.2,22.5">
 {endlogo(17.25)}
 <div style="position:absolute;left:0;right:0;top:820px;text-align:center">
  <div class="title" style="position:static;font-size:76px;line-height:1.02">{words("Teamkleidung mit eurem Logo. Wir *organisieren alles.",17.9,.1)}</div>
  <div style="margin-top:80px" data-in="19.2" data-a="pop" data-dur=".3"><div class="cbox"><i></i><span id="ctext" class="ph">Kommentieren ...</span><span class="caret" id="caret"></span></div></div>
  <div style="margin-top:46px;font-size:52px;font-weight:900" data-in="20.4" data-a="up" data-dur=".3">Schreib <span style="color:var(--acc)">TEAM</span> in die Kommentare</div>
  <div style="margin-top:20px;font-size:40px;font-weight:700;opacity:.75" data-in="20.8" data-a="up" data-dur=".3">und wir melden uns mit einem Angebot.</div>
  <div style="margin-top:56px" data-in="21.2" data-a="pop" data-dur=".3"><span class="pill" style="font-size:60px;padding:20px 46px">crewtex.ch</span></div>
 </div>
</div><div class="grain"></div></section>
'''
js = '''
window.HOOK=function(t){
 const n=Math.round(34+113*E(cl((t-3.1)/4.6)));document.getElementById('unr').textContent=n;
 const vis=[...document.querySelectorAll('#feed .bb')].filter(b=>t>=+b.dataset.in).length;
 document.getElementById('feed').style.transform=`translateY(${-Math.max(0,vis-8)*92}px)`;
 const k=Math.round(25*E(cl((t-9.9)/2.6)));document.getElementById('cn').textContent=k;document.getElementById('bar').style.width=(k/25*100)+'%';
 const full='TEAM';const c=Math.floor(cl((t-19.6)/.8)*4);const ct=document.getElementById('ctext');
 if(c>0){ct.textContent=full.slice(0,c);ct.className='ty';}else{ct.textContent='Kommentieren ...';ct.className='ph';}
 document.getElementById('caret').style.opacity=(Math.floor(t*3)%2)?1:0;
};
'''
page(css, body, js, [3.0, 9.0, 12.9, 17.2], 'reel45/r6/reel.html')
print('ok')
