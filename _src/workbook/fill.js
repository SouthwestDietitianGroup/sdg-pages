// node fill.js vision "My 2027 Vision - Fillable.pdf"
const {PDFDocument,StandardFonts,rgb}=require('pdf-lib');const fs=require('fs');
(async()=>{const [name,out]=process.argv.slice(2);
const pdf=await PDFDocument.load(fs.readFileSync(name+'.pdf'));const form=pdf.getForm();
const helv=await pdf.embedFont(StandardFonts.Helvetica);
const fields=JSON.parse(fs.readFileSync(name+'.fields.json'));const pages=pdf.getPages();
const PT=0.75, LINE=24/0.75; // a ruled line is 24pt = 32px
const ink=rgb(0.17,0.08,0.13);
const opts=(x,y,w,h)=>({x,y,width:w,height:h,borderWidth:0,textColor:ink,font:helv});
let n=0;
for(const f of fields){const pg=pages[f.page];const H=pg.getHeight();
 const X=f.x*PT, W=f.w*PT;
 if(f.type==='check'){const s=Math.min(f.w,f.h)*PT;const cb=form.createCheckBox(f.name);
   cb.addToPage(pg,{x:X+(W-s)/2,y:H-(f.y+f.h/2)*PT-s/2,width:s,height:s,borderWidth:0,textColor:rgb(0.59,0.27,0.15)});n++;continue;}
 const L=f.lh?f.lh/PT:LINE;
 if(f.type==='multi' && f.lh){
   const k=Math.round(f.h/L);
   for(let i=0;i<k;i++){const tf=form.createTextField(k===1?f.name:`${f.name}_${i+1}`);
     const top=f.y+i*L; tf.addToPage(pg,opts(X,H-(top+L)*PT+1.5,W,L*PT-2));tf.setFontSize(10.5);n++;}
   continue;}
 const tf=form.createTextField(f.name);
 if(f.type==='multi'){tf.enableMultiline();}
 tf.addToPage(pg,opts(X+2,H-(f.y+f.h)*PT+1,W-4,f.h*PT-2));tf.setFontSize(f.type==='multi'?9:10.5);n++;}
form.updateFieldAppearances(helv);
fs.writeFileSync(out,await pdf.save());console.log(out,'fields',n);})();
