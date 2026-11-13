const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('file://'+process.cwd()+'/checklist.html');await p.waitForTimeout(400);
await p.pdf({path:'SDG 2027 Goal Planning Session - RD Checklist.pdf',preferCSSPageSize:true,printBackground:true});await b.close();})();
