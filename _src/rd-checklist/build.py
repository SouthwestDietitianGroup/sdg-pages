import base64, html
F='/tmp/claude-0/-home-claude/1d1455d7-db0b-5af3-a31d-367b13a3ce8a/scratchpad/fonts'
def f(p): return 'data:font/woff2;base64,'+base64.b64encode(open(p,'rb').read()).decode()
cg=F+'/fontsource-cormorant-garamond-5.0.13/files/cormorant-garamond-latin-'; js=F+'/fontsource-josefin-sans-5.0.17/files/josefin-sans-latin-'; mu=F+'/fontsource-mulish-5.0.17/files/mulish-latin-'
logo='data:image/png;base64,'+base64.b64encode(open('/home/claude/sdg-pages/assets/sdg-logo-rust.png','rb').read()).decode()
S=[
("Housekeeping",["Insurance updates, or cash pay for 2027","Referral?","Overview page: address, phone, and email correct? Update the overview page and tags.","Card on file up to date and not expired?"]),
("2026",["<q>What are you most proud of?</q>","Your recap for them!","<q>What did you learn?</q>","<q>Who did you become this year?</q>","<q>What were 2026’s biggest obstacles?</q>"]),
("2027",["Your goals: get clear numbers. Where they are, the target, and by when.",
 "If you have time, <b>a day in the life of future you:</b><div class='script'>“Take me through a day in the life of future you. Pretend for a moment and use your imagination. Imagine you have reached [all of their goals] and kept them for a full year. Tell me about her. What is her day like in her new life? What are her everyday emotions and feelings? How does she think? What does she do?”</div><b>Capture EMOTIONS for Heidi.</b> Say them back as a positive affirmation."]),
("The plan",["<q>Your written plan will be in your portal within 72 business hours. Here’s an example!</q> Show the sample plan.",
 "Build what you can: Investigation, The Work, Maintenance. Do the rest after the session and use the 24-hour billing period.",
 "If you have time, show the HOW process (screen share). Obstacles WILL happen.",
 "SDG support? GLP-1 Program, Accountability Program, Emotional Eating Class, Events and Connection, Dr. Reker hormones, Taylor gut health. Can be done after."]),
("Before the next visit",["Labs, DEXA, anything else?","Choose the lab route together."]),
("Holidays",["<q>Any holiday concerns? An event you’re nervous about?</q>"]),
("The 14-Day Reset",["Show them where it is in Connection Space.","<q>Do you want to do it?</q>","<q>When do we start? When is our next appointment? Should those line up?</q>","<q>How do we change it for you?</q>"]),
("Wrap up",["Wait for your plan, do your steps, and join a Kickoff Class with Maya: Sat Jan 9 or Sat Jan 16.","Remind them they can schedule, reschedule, or cancel in the portal.","Book the next appointment. Hugs and high fives ❤️"]),
]
def sec(i,t,items):
    li=''.join(f'<li>{x.replace("<q>","“").replace("</q>","”")}</li>' for x in items)
    return f'<section><h2><span>{i}</span>{t}</h2><ul>{li}</ul></section>'
body=''.join(sec(i+1,t,it) for i,(t,it) in enumerate(S))
css=f"""
@font-face{{font-family:CG;src:url({f(cg+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:CG;src:url({f(cg+'500-normal.woff2')});font-weight:500}}
@font-face{{font-family:JS;src:url({f(js+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:MU;src:url({f(mu+'400-normal.woff2')});font-weight:400}}
@font-face{{font-family:MU;src:url({f(mu+'700-normal.woff2')});font-weight:700}}
@font-face{{font-family:MU;src:url({f(mu+'400-italic.woff2')});font-weight:400;font-style:italic}}
@page{{size:letter;margin:.5in .55in .55in}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:MU,Arial,sans-serif;font-size:9.3pt;line-height:1.42;color:#2a1520;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
header{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #F2B574;padding-bottom:8pt;margin-bottom:10pt}}
header img{{height:34px}}
.ti .e{{font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:#964527}}
.ti h1{{font-family:CG;font-weight:600;font-size:21pt;line-height:1.05;color:#31091C;margin:2pt 0 0}}
.cols{{column-count:2;column-gap:20pt}}
section{{break-inside:avoid;margin-bottom:9pt}}
h2{{font-family:CG;font-weight:600;font-size:13.5pt;color:#31091C;margin:0 0 3pt;display:flex;align-items:center;gap:7pt;border-bottom:1px solid #ACB574;padding-bottom:2pt}}
h2 span{{font-family:JS;font-size:8.5pt;width:16pt;height:16pt;border-radius:50%;background:#964527;color:#fff;display:grid;place-items:center;padding-top:1.5pt;flex:none}}
ul{{list-style:none;margin:0;padding:0}}
li{{position:relative;padding-left:15pt;margin:0 0 3pt;text-wrap:pretty}}
li:before{{content:"";position:absolute;left:0;top:2.5pt;width:8pt;height:8pt;border:1.3px solid #964527;border-radius:2pt}}
.script{{background:#fdf3e8;border-left:3px solid #964527;border-radius:0 6pt 6pt 0;padding:5pt 8pt;margin:3pt 0;font-family:CG;font-weight:500;font-size:10.5pt;line-height:1.3;color:#31091C}}
footer{{margin-top:6pt;border-top:1px solid #e6dcd6;padding-top:6pt;font-size:8.5pt;color:#5a4048}}
footer b{{color:#964527}}
"""
doc=f"""<!doctype html><html><head><meta charset="utf-8"><title>2027 Goal Planning Session Checklist</title><style>{css}</style></head><body>
<header><div class="ti"><div class="e">RD in-session checklist</div><h1>2027 Goal Planning Session</h1></div><img src="{logo}"></header>
<p style="margin:0 0 9pt"><b>Open with:</b> “Here’s what we’re going to do today! Some housekeeping, a look back at 2026, a plan forward into 2027, what to do now before the end of the year, any holiday concerns, the 14-Day Reset, and we’ll set up your first 2027 appointment!”</p>
<div class="cols">{body}</div>
<footer><b>After the session:</b> add your brain dump to the Heidi note, then build the plan at <b>go.southwestdietitiangroup.com/plan</b> in Chrome. Upload to the portal within 72 business hours, then delete the PDF from Downloads.</footer>
</body></html>"""
open('checklist.html','w').write(doc)
