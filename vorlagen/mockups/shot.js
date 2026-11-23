const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
for(const n of ['hoodie-schwarz','tshirt-weiss','polo-navy','hoodie-orange']){await p.goto('file:///home/claude/mockups/'+n+'.html');await p.waitForTimeout(300);await p.screenshot({path:'out/'+n+'.png'});}
await b.close();})();
