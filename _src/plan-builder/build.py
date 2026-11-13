import base64
F='/tmp/claude-0/-home-claude/1d1455d7-db0b-5af3-a31d-367b13a3ce8a/scratchpad/fonts'
cg=F+'/fontsource-cormorant-garamond-5.0.13/files/cormorant-garamond-latin-'
js=F+'/fontsource-josefin-sans-5.0.17/files/josefin-sans-latin-'
mu=F+'/fontsource-mulish-5.0.17/files/mulish-latin-'
m={'__CG500__':cg+'500-normal.woff2','__CG600__':cg+'600-normal.woff2','__CG500I__':cg+'500-italic.woff2','__JS600__':js+'600-normal.woff2','__MU400__':mu+'400-normal.woff2','__MU700__':mu+'700-normal.woff2','__LOGO__':'/home/claude/sdg-pages/assets/sdg-logo-rust.png'}
s=open('template.html').read()
for k,p in m.items():
    mt='image/png' if p.endswith('png') else 'font/woff2'
    s=s.replace(k,'data:%s;base64,%s'%(mt,base64.b64encode(open(p,'rb').read()).decode()))
open('sdg-plan-builder.html','w').write(s)
print(len(s)//1024,'KB')
