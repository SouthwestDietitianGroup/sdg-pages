// node render.js vision  -> vision.pdf + vision.fields.json (+ overflow report)
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const name=process.argv[2];const b=await chromium.launch();
const p=await b.newPage({viewport:{width:816,height:1056}});
await p.emulateMedia({media:'print'});
await p.goto('file://'+process.cwd()+'/'+name+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const info=await p.evaluate(()=>{
 const sheets=[...document.querySelectorAll('.sheet')];
 const over=sheets.map((s,i)=>{const kids=[...s.children].filter(c=>!c.classList.contains('foot'));const last=kids[kids.length-1];
   const sb=s.getBoundingClientRect(), lb=last.getBoundingClientRect(); const limit=sb.bottom-0.62*96; return lb.bottom>limit?{page:i+1,by:Math.round(lb.bottom-limit)}:null;}).filter(Boolean);
 const f=[...document.querySelectorAll('[data-f]')].map(el=>{const r=el.getBoundingClientRect();const sh=el.closest('.sheet');const sr=sh.getBoundingClientRect();
   return {name:el.dataset.f,type:el.dataset.t,lh:+(el.dataset.lh||0),page:sheets.indexOf(sh),x:r.left-sr.left,y:r.top-sr.top,w:r.width,h:r.height};});
 return {over,f,pages:sheets.length};});
await p.pdf({path:name+'.pdf',preferCSSPageSize:true,printBackground:true});
fs.writeFileSync(name+'.fields.json',JSON.stringify(info.f));
console.log(name,'pages',info.pages,'fields',info.f.length,'overflow',JSON.stringify(info.over));
const dup={};info.f.forEach(x=>dup[x.name]=(dup[x.name]||0)+1);const d=Object.entries(dup).filter(([k,v])=>v>1);if(d.length)console.log('DUP',d);
await b.close();})();
