const { chromium } = require('playwright');const D=process.argv[2];const fps=30,dur=+process.argv[3];
const only=process.argv[4];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+D+'/reel.html');await p.evaluate(()=>document.fonts.ready);
const times= only? only.split(',').map(Number) : Array.from({length:Math.round(fps*dur)},(_,i)=>i/fps);
let i=0;for(const t of times){await p.evaluate(t=>window.render(t),t);
 await p.screenshot({path:`${D}/${only?'test':'f'}_${String(i).padStart(4,'0')}.png`});i++;}
console.log('frames',i,errs);await b.close();})();
