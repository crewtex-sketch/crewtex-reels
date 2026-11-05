import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
P = json.load(open('logo/parts.json')); font = open('font.css').read(); L = json.load(open('logo/logo.json'))

def endlogo(t0):
    r = L['dot'][2]; dcy = L['dot'][1]; prev = None; letters = []
    for k, ((x1, x2), d) in enumerate(zip(L['boxes'], L['letters'])):
        w = x2 - x1; ml = (x1 - (prev if prev is not None else 2 * r)) / 164
        letters.append(f'<svg class="il" data-in="{t0+0.3+k*0.06:.2f}" data-a="blurin" data-dur=".4" style="width:{w/164:.4f}em;margin-left:{ml:.4f}em" viewBox="{x1} -8 {w} 164"><g fill="currentColor"><path d="{d}"/></g></svg>')
        prev = x2
    return f'<div class="endlogo"><i class="edot" data-in="{t0:.2f}" data-a="fly" data-dur=".45" style="width:{2*r/164:.4f}em;height:{2*r/164:.4f}em;margin-top:{(dcy-r+8)/164:.4f}em"></i>{"".join(letters)}</div>'

def words(txt, t0, step=.12, cls='kw'):
    out = []
    for i, w in enumerate(txt.split(' ')):
        hl = ' hl' if w.startswith('*') else ''
        w = w.lstrip('*')
        out.append(f'<span class="{cls}{hl}" data-in="{t0+i*step:.2f}" data-a="word" data-dur=".28">{w}</span>')
    return ' '.join(out)

BASE_CSS = '''
:root{--acc:#FF5A1F;--ink:#121110;--paper:#F3EFE6;--panel:#1C1A18;--line:#D8D1C4}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif;background:var(--ink)}
.scene{position:absolute;inset:0;overflow:hidden;opacity:0}
.cam{position:absolute;inset:0;transform-origin:50% 45%}
.ink{background:var(--ink);color:var(--paper)} .paper{background:var(--paper);color:var(--ink)} .org{background:var(--acc);color:var(--ink)}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.06;background-image:radial-gradient(currentColor 1px,transparent 1.2px);background-size:6px 6px;z-index:9}
[data-in]{opacity:0}
.tag{position:absolute;left:90px;top:230px;background:var(--acc);color:var(--ink);font-weight:900;font-size:40px;letter-spacing:.08em;padding:12px 26px;border-radius:999px;text-transform:uppercase}
.org .tag{background:var(--ink);color:var(--acc)}
.title{position:absolute;left:90px;right:90px;top:320px;font-weight:900;font-size:92px;letter-spacing:-.04em;line-height:1.02}
.kw{display:inline-block} .kw.hl{color:var(--acc)} .org .kw.hl{color:var(--paper)}
.sub{position:absolute;left:90px;right:90px;font-size:48px;font-weight:700;line-height:1.25}
.endlogo{position:absolute;left:50%;top:600px;transform:translateX(-50%);display:flex;align-items:flex-start;height:1em;line-height:0;font-size:96px;color:var(--paper)}
.endlogo .il{display:block;height:1em;flex:none;overflow:visible}
.edot{border-radius:50%;background:var(--acc);display:block;flex:none}
.pill{display:inline-block;background:var(--acc);color:var(--ink);font-weight:900;font-size:76px;letter-spacing:-.03em;padding:26px 56px;border-radius:999px}
.wipe{position:absolute;left:50%;top:50%;width:200px;height:200px;margin:-100px 0 0 -100px;border-radius:50%;background:var(--acc);z-index:50;transform:scale(0)}
.tap{position:absolute;width:90px;height:90px;border-radius:50%;border:8px solid var(--ink);opacity:0;z-index:20}
.ck{width:96px;height:96px;border-radius:50%;background:var(--ink);position:relative;flex:none}
.ck::after{content:"";position:absolute;left:33px;top:18px;width:22px;height:44px;border-right:11px solid var(--acc);border-bottom:11px solid var(--acc);transform:rotate(45deg)}
'''

BASE_JS = '''
const E=x=>1-Math.pow(1-x,3),Bk=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)},cl=x=>Math.max(0,Math.min(1,x));
window.render=function(t){
 document.querySelectorAll('.scene').forEach(s=>{s.style.opacity=(t>=+s.dataset.s&&t<+s.dataset.e)?1:0;});
 document.querySelectorAll('[data-zoom]').forEach(c=>{const [a,b]=c.dataset.zoom.split(',').map(Number);const p=cl((t-a)/(b-a));c.style.transform=`scale(${1+0.05*p})`;});
 document.querySelectorAll('[data-in]').forEach(el=>{
  const a=+el.dataset.in,d=+(el.dataset.dur||.35);if(t<a){el.style.opacity=0;return;}
  const p=cl((t-a)/d),e=E(p);let tf='',op=Math.min(1,p*1.8),f='none';const rot=el.dataset.rot||'0deg';
  switch(el.dataset.a){
   case 'up':tf=`translateY(${(1-e)*60}px)`;break;
   case 'word':tf=`translateY(${(1-e)*50}px) rotate(${(1-e)*4}deg)`;f=`blur(${(1-e)*8}px)`;break;
   case 'left':tf=`translateX(${(1-e)*-140}px)`;break;
   case 'right':tf=`translateX(${(1-e)*140}px)`;break;
   case 'pop':tf=`scale(${0.4+0.6*Bk(p)})`;break;
   case 'rise':tf=`translateY(${(1-e)*500}px) rotate(${(1-e)*-6}deg)`;op=1;break;
   case 'card':tf=`translateX(${(1-e)*900}px) rotate(${(1-e)*8}deg)`;op=1;break;
   case 'drop':{const b=p<.75?E(p/.75):1+Math.sin((p-.75)/.25*Math.PI)*.04;tf=`translateY(${(1-Math.min(1,b))*-1300}px) rotate(${rot})`;op=1;break;}
   case 'stamp':tf=`scale(${1+(1-Bk(p))*1.6}) rotate(-12deg)`;op=Math.min(1,p*3);break;
   case 'fly':tf=`translateX(${(1-e)*-900}px) scaleX(${1+0.6*(1-e)})`;f=`blur(${(1-e)*10}px)`;op=1;break;
   case 'blurin':tf=`translateX(${(1-e)*-130}px) skewX(${(1-e)*-18}deg)`;f=`blur(${(1-e)*12}px)`;break;
  }
  el.style.opacity=op;el.style.transform=tf;el.style.filter=f;});
 if(window.HOOK)window.HOOK(t);
 const w=document.getElementById('wipe');let s=0;
 for(const c of window.CUTS){const a=c-.28,b=c+.22;if(t>=a&&t<c)s=E((t-a)/.28)*14;else if(t>=c&&t<b)s=(1-E((t-c)/.22))*14;}
 w.style.transform=`scale(${s})`;w.style.background=window.WIPECOL?window.WIPECOL(t):'var(--acc)';
};
'''

def page(css, body, js, cuts, out):
    html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{font}{BASE_CSS}{css}</style></head><body>{P['SYMBOL']}
{body}
<div class="wipe" id="wipe"></div>
<script>window.CUTS={json.dumps(cuts)};{BASE_JS}{js}
window.render(0);</script></body></html>'''
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
