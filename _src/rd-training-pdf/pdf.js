const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/guide.html');await p.waitForTimeout(500);
await p.pdf({path:'SDG RD Training - How to Run the 2027 Goal Planning Session.pdf',preferCSSPageSize:true,printBackground:true});await b.close();})();
