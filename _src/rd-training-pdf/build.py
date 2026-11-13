import re, base64, markdown, html
md = open('guide.md').read()
md = md.replace('****','').replace('&#91;','[').replace('&#32;','').replace('\\[','[').replace('\\]',']').replace('\\_','_')
md = re.sub(r'^##\s*$\n?', '', md, flags=re.M)
# title + lead pulled out for the cover band
lines = md.split('\n')
title = lines[0].lstrip('# ').strip()
body = '\n'.join(lines[1:])
# nested lists: docs export uses 2-space indents; python-markdown needs 4
body = re.sub(r'^  (- )', r'    \1', body, flags=re.M)
h = markdown.markdown(body, extensions=['tables','sane_lists'])
h = h.replace('<li>[ ] ','<li class="ck">').replace('<li>[x] ','<li class="ck done">')
h = re.sub(r'<ul>(\s*<li class="ck)', r'<ul class="cl">\1', h)
F='/tmp/claude-0/-home-claude/1d1455d7-db0b-5af3-a31d-367b13a3ce8a/scratchpad/fonts'
def f(p): return 'data:font/woff2;base64,'+base64.b64encode(open(p,'rb').read()).decode()
cg=F+'/fontsource-cormorant-garamond-5.0.13/files/cormorant-garamond-latin-'; js=F+'/fontsource-josefin-sans-5.0.17/files/josefin-sans-latin-'; mu=F+'/fontsource-mulish-5.0.17/files/mulish-latin-'
logo='data:image/png;base64,'+base64.b64encode(open('/home/claude/sdg-pages/assets/sdg-logo-rust.png','rb').read()).decode()
css=f"""
@font-face{{font-family:CG;src:url({f(cg+'500-normal.woff2')});font-weight:500}}
@font-face{{font-family:CG;src:url({f(cg+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:CG;src:url({f(cg+'500-italic.woff2')});font-weight:500;font-style:italic}}
@font-face{{font-family:JS;src:url({f(js+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:MU;src:url({f(mu+'400-normal.woff2')});font-weight:400}}
@font-face{{font-family:MU;src:url({f(mu+'400-italic.woff2')});font-weight:400;font-style:italic}}
@font-face{{font-family:MU;src:url({f(mu+'700-normal.woff2')});font-weight:700}}
@page{{size:letter;margin:.7in .8in .8in;
 @bottom-left{{content:"Southwest Dietitian Group  \\00b7  RD Training  \\00b7  Internal use only";font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.16em;text-transform:uppercase;color:#a08a90}}
 @bottom-right{{content:counter(page);font-family:JS;font-weight:600;font-size:7pt;color:#a08a90}}}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:MU,Arial,sans-serif;font-size:10.5pt;line-height:1.55;color:#2a1520;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:22pt}}
.top img{{height:44px}}
.tag{{font-family:JS;font-weight:600;font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;background:#F2B574;color:#31091C;padding:6pt 12pt;border-radius:99pt}}
h1{{font-family:CG;font-weight:500;font-size:34pt;line-height:1.05;color:#31091C;margin:0 0 10pt}}
.lead{{font-size:11.5pt;color:#5a4048;border-bottom:2px solid #F2B574;padding-bottom:14pt;margin-bottom:6pt}}
h2{{font-family:CG;font-weight:600;font-size:21pt;color:#31091C;border-bottom:1.5px solid #ACB574;padding-bottom:3pt;margin:22pt 0 8pt;break-after:avoid}}
h3{{font-family:CG;font-weight:600;font-size:15.5pt;color:#964527;margin:16pt 0 4pt;break-after:avoid}}
p{{margin:0 0 7pt;text-wrap:pretty}}
ul,ol{{margin:0 0 8pt;padding-left:18pt}}
li{{margin-bottom:3pt;text-wrap:pretty}}
li::marker{{color:#964527}}
ul.cl{{list-style:none;padding-left:4pt}}
li.ck{{position:relative;padding-left:18pt}}
li.ck:before{{content:"";position:absolute;left:0;top:3.5pt;width:9pt;height:9pt;border:1.5px solid #964527;border-radius:2pt}}
blockquote{{margin:6pt 0 10pt;background:#fdf3e8;border-left:4px solid #964527;border-radius:0 8pt 8pt 0;padding:9pt 14pt 3pt;break-inside:avoid}}
blockquote em{{font-family:CG;font-size:13pt;line-height:1.35;color:#31091C}}
em{{color:#4a2a35}}
strong{{color:#31091C}}
table{{width:100%;border-collapse:collapse;margin:6pt 0 12pt;font-size:9.5pt;break-inside:avoid}}
th{{background:#964527;color:#fff;font-family:JS;font-weight:600;font-size:7.5pt;letter-spacing:.14em;text-transform:uppercase;text-align:left;padding:7pt 8pt}}
td{{border-bottom:1px solid #e6dcd6;padding:6pt 8pt;vertical-align:top}}
tr:nth-child(even) td{{background:#faf7f5}}
a{{color:#964527}}
"""
lead_m = re.match(r'\s*\n(.+?)\n', body)
lead=''
m = re.search(r'^\s*(?!#)(.+)$', body, flags=re.M)
if m: lead = m.group(1).strip(); h = h.replace('<p>'+markdown.markdown(lead)[3:-4]+'</p>','',1)
doc=f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{css}</style></head><body>
<div class="top"><img src="{logo}"><span class="tag">RD Training</span></div>
<h1>{html.escape(title)}</h1><p class="lead">{markdown.markdown(lead)[3:-4]}</p>
{h}</body></html>"""
open('guide.html','w').write(doc)
