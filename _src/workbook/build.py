"""Builds the two 2027 patient documents as HTML (one letter-size .sheet per page).
Elements with data-f="name" data-t="text|multi|check" become form fields in the fillable copy."""
import base64, html

F = '/tmp/claude-0/-home-claude/1d1455d7-db0b-5af3-a31d-367b13a3ce8a/scratchpad/fonts'
def font(p): return 'data:font/woff2;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
cg = F + '/fontsource-cormorant-garamond-5.0.13/files/cormorant-garamond-latin-'
js = F + '/fontsource-josefin-sans-5.0.17/files/josefin-sans-latin-'
mu = F + '/fontsource-mulish-5.0.17/files/mulish-latin-'
LOGO = 'data:image/png;base64,' + base64.b64encode(open('/home/claude/sdg-pages/assets/sdg-logo-rust.png', 'rb').read()).decode()
CS = 'https://sdgprograms.com/'
RES = 'https://sdgprograms.com/posts/patient-resource-library-2027-goal-planning-and-14-day-reset-resources'

CSS = f"""
@font-face{{font-family:CG;src:url({font(cg+'500-normal.woff2')});font-weight:500}}
@font-face{{font-family:CG;src:url({font(cg+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:CG;src:url({font(cg+'500-italic.woff2')});font-weight:500;font-style:italic}}
@font-face{{font-family:JS;src:url({font(js+'600-normal.woff2')});font-weight:600}}
@font-face{{font-family:MU;src:url({font(mu+'400-normal.woff2')});font-weight:400}}
@font-face{{font-family:MU;src:url({font(mu+'400-italic.woff2')});font-weight:400;font-style:italic}}
@font-face{{font-family:MU;src:url({font(mu+'700-normal.woff2')});font-weight:700}}
@page{{size:letter;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:MU,Arial,sans-serif;font-size:10.5pt;line-height:1.5;color:#2a1520;background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.sheet{{width:8.5in;height:11in;padding:.62in .75in .8in;position:relative;overflow:hidden;break-after:page}}
.sheet:last-child{{break-after:auto}}
.foot{{position:absolute;left:.75in;right:.75in;bottom:.4in;display:flex;justify-content:space-between;font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#a08a90}}
.eye{{font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:#964527;margin-bottom:4pt}}
h1{{font-family:CG;font-weight:500;font-size:54pt;line-height:.98;color:#31091C}}
h1 em{{font-style:italic;color:#964527}}
h2{{font-family:CG;font-weight:500;font-size:28pt;line-height:1.05;color:#31091C;margin-bottom:8pt}}
h3{{font-family:CG;font-weight:600;font-size:14.5pt;color:#964527;margin:12pt 0 3pt}}
p{{margin-bottom:7pt;text-wrap:pretty}}
a{{color:#964527;text-decoration:underline;text-underline-offset:2px}}
.top{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.5in}}
.top img{{height:46px}}
.tag{{font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:#31091C;background:#F2B574;padding:6pt 12pt;border-radius:99pt}}
.lab{{font-family:JS;font-weight:600;font-size:7.5pt;letter-spacing:.18em;text-transform:uppercase;color:#964527;margin:10pt 0 2pt}}
.ln{{border-bottom:1px solid #cbbcb4;height:24pt}}
.lines{{background:repeating-linear-gradient(to bottom,transparent 0,transparent 23pt,#cbbcb4 23pt,#cbbcb4 24pt);}}
.box{{border:1.5px solid #e1d4cc;border-radius:8pt}}
.name{{display:flex;gap:8pt;align-items:flex-end;margin-top:14pt}}
.name span{{font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:#964527;white-space:nowrap;padding-bottom:4pt}}
.name div{{flex:1;border-bottom:1.5px solid #964527;height:24pt}}
.toc{{margin-top:22pt;border-top:2px solid #F2B574;padding-top:12pt}}
.toc li{{list-style:none;display:flex;gap:10pt;align-items:baseline;padding:5pt 0;border-bottom:1px solid #eee4de}}
.toc li b{{font-family:JS;font-weight:600;font-size:9pt;color:#964527;width:18pt}}
.toc li span{{font-family:CG;font-weight:600;font-size:14pt;color:#31091C}}
table.t{{width:100%;border-collapse:collapse;margin:4pt 0 6pt}}
table.t th{{background:#964527;color:#fff;font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.14em;text-transform:uppercase;text-align:left;padding:6pt 7pt}}
table.t td{{border-bottom:1px solid #cbbcb4;height:26pt;padding:0 7pt;vertical-align:middle}}
table.t tr.ex td{{color:#a08a90;font-style:italic;height:22pt;font-size:9.5pt}}
.quote{{border-left:5px solid #964527;background:#fdf3e8;padding:10pt 16pt;border-radius:0 8pt 8pt 0;margin:8pt 0}}
.quote .q{{font-family:CG;font-style:italic;font-weight:500;font-size:17pt;color:#31091C;line-height:1.25}}
.pills{{display:flex;flex-wrap:wrap;gap:5pt;margin:4pt 0 8pt}}
.pills span{{background:#eef0e2;border:1px solid #ACB574;border-radius:99pt;padding:2pt 9pt;font-size:9.5pt;color:#3e4320}}
.aff{{border:2px solid #964527;border-radius:10pt;padding:12pt 16pt;margin-top:8pt}}
.aff .start{{font-family:CG;font-style:italic;font-size:20pt;color:#964527}}
.steps{{display:grid;gap:9pt}}
.st{{display:grid;grid-template-columns:24pt 1fr;gap:9pt}}
.st .n{{width:24pt;height:24pt;border-radius:50%;background:#964527;color:#fff;font-family:JS;font-weight:600;font-size:11pt;display:grid;place-items:center;padding-top:2pt}}
.st h4{{font-family:CG;font-weight:600;font-size:14pt;color:#31091C;line-height:1.15;margin-bottom:2pt}}
.st p{{margin-bottom:4pt;font-size:10pt}}
.prompt{{background:#f6f4ee;border:1px dashed #ACB574;border-radius:7pt;padding:6pt 10pt;font-size:9.5pt;font-style:italic;margin:2pt 0 4pt;color:#3a2a30}}
.note{{background:#eef0e2;border:1.5px solid #ACB574;border-radius:9pt;padding:8pt 12pt;font-size:9.5pt;margin:6pt 0 10pt}}
.note b{{color:#5d6430}}
/* HOW page */
.howsvg{{margin:12pt auto 10pt;max-width:5.6in}} .howsvg svg{{width:100%;height:auto;display:block}} .howsvg text{{font-family:CG;font-weight:600}}
.how-rows{{display:grid;gap:8pt;margin:6pt 0 4pt}}
.how-rows .hr{{display:grid;grid-template-columns:12pt 1fr;gap:8pt;align-items:start}}
.how-rows .dot{{width:10pt;height:10pt;border-radius:50%;margin-top:4pt}}
.along{{background:#eef0e2;border:1.5px solid #ACB574;border-radius:9pt;padding:11pt 14pt 5pt;margin-top:14pt}}
.along b{{color:#5d6430}}
/* community */
.comm{{display:grid;grid-template-columns:34pt 1fr;gap:12pt;padding:10pt 0;border-bottom:1px solid #e6dcd6;break-inside:avoid}}
.comm .ic{{width:30pt;height:30pt;border-radius:50%;background:#F2B574;display:grid;place-items:center;font-family:JS;font-weight:600;font-size:12pt;color:#31091C;padding-top:2pt}}
.comm h4{{font-family:CG;font-weight:600;font-size:14pt;color:#31091C;margin-bottom:2pt}}
.comm p{{font-size:10pt;margin-bottom:5pt}}
.comm .gk{{background:#fdf3e8;border-radius:7pt;padding:6pt 10pt 3pt;margin:2pt 0 6pt;font-size:9.3pt}}
.comm .gk .k{{font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:#964527;margin-bottom:2pt}}
.comm ul{{padding-left:14pt;margin-bottom:4pt;font-size:9.8pt}} .comm li{{margin-bottom:2pt}}
.coming{{margin-top:14pt;background:#31091C;color:#fff;border-radius:10pt;padding:13pt 18pt 7pt}}
.coming .k{{font-family:CG;font-weight:600;font-size:18pt;margin-bottom:3pt;color:#F2B574}}
.close{{text-align:center;margin-top:20pt}}
.close .q{{font-family:CG;font-style:italic;font-weight:500;font-size:16pt;color:#31091C;line-height:1.35;max-width:5.6in;margin:0 auto;text-wrap:balance}}
.close .s{{font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:#964527;margin-top:8pt}}
/* planning */
.mhead{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #F2B574;padding-bottom:6pt;margin-bottom:6pt}}
.mhead h2{{margin:0}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:4pt 18pt}}
.ck{{display:inline-block;width:10pt;height:10pt;border:1.4px solid #964527;border-radius:2pt;vertical-align:-1pt;margin-right:5pt}}
.checks{{display:grid;gap:5pt;margin-top:10pt;font-size:10pt}}
.week td,.week th{{border:1px solid #d9ccc5}}
table.week{{width:100%;border-collapse:collapse;margin-top:6pt}}
table.week th{{background:#964527;color:#fff;font-family:JS;font-weight:600;font-size:7pt;letter-spacing:.14em;text-transform:uppercase;padding:5pt 6pt;text-align:left}}
table.week td{{height:66pt;vertical-align:top;padding:4pt 6pt;font-family:JS;font-weight:600;font-size:7.5pt;letter-spacing:.12em;color:#964527}}
table.habit{{width:100%;border-collapse:collapse;margin-top:8pt;table-layout:fixed}}
table.habit th{{font-family:JS;font-weight:600;font-size:6.5pt;color:#7a6168;padding:3pt 0;text-align:center}}
table.habit th.h{{text-align:left;width:1.6in;font-size:7pt;letter-spacing:.14em;text-transform:uppercase;color:#964527}}
table.habit td{{border:1px solid #d9ccc5;height:30pt;padding:0}}
table.habit td.h{{padding:0 5pt}}
"""

def sheet(inner, footer, n, cls=''):
    return f'<section class="sheet {cls}">{inner}<div class="foot"><span>{footer}</span><span>{n}</span></div></section>'

def lines(name, n, h=24):
    bg = f"background:repeating-linear-gradient(to bottom,transparent 0,transparent {h-1}pt,#cbbcb4 {h-1}pt,#cbbcb4 {h}pt)"
    return f'<div class="lines" data-f="{name}" data-t="multi" data-lh="{h}" style="height:{n*h}pt;{bg}"></div>'

def ln(name):
    return f'<div class="ln" data-f="{name}" data-t="text"></div>'

def doc(title, pages):
    return f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

# ======================= MY 2027 VISION =======================
def vision():
    FT = 'Southwest Dietitian Group  &middot;  My 2027 Vision'
    P = []
    P.append(sheet(f'''<div class="top"><img src="{LOGO}" alt="Southwest Dietitian Group"><span class="tag">2027</span></div>
<h1>My <em>2027</em> Vision</h1>
<div class="name"><span>This vision belongs to</span><div data-f="name" data-t="text"></div></div>
<p style="margin-top:22pt;font-size:11.5pt;line-height:1.6">This is where your 2027 starts: your goals in numbers, the feelings you’re choosing, and a clear picture of a day in your new life. Fill it in, keep it where you’ll see it, and come back to it any time you need a reminder of where you’re going.</p>
<ul class="toc">
<li><b>01</b><span>My goals in numbers</span></li>
<li><b>02</b><span>My 2027 affirmation</span></li>
<li><b>03</b><span>A day in my new life</span></li>
<li><b>04</b><span>A day in my new life, with AI</span></li>
<li><b>05</b><span>Obstacles are expected in 2027</span></li>
<li><b>06</b><span>Get connected</span></li>
</ul>''', FT, 1))

    rows = ''.join(f'<tr><td data-f="g{i}_goal" data-t="text"></td><td data-f="g{i}_now" data-t="text"></td><td data-f="g{i}_target" data-t="text"></td><td data-f="g{i}_when" data-t="text"></td></tr>' for i in range(1, 6))
    P.append(sheet(f'''<div class="eye">01</div><h2>My goals in numbers</h2>
<p>Write each goal with a number: where you are now, where you’re going, and by when. Not sure of a number? Ask your dietitian. Numbers are how we’ll both see your progress.</p>
<table class="t"><tr><th style="width:34%">My goal</th><th>Where I am now</th><th>My target</th><th>By when</th></tr>
<tr class="ex"><td>Example: average blood sugar</td><td>165</td><td>under 130</td><td>June 2027</td></tr>{rows}</table>
<div class="lab">Why these goals matter to me</div>{lines("why", 4)}
<div class="lab">What I need to see to stay with my plan</div>{lines("needtosee", 3)}
<div class="lab">How I’ll celebrate when I get there</div>{lines("celebrate", 2)}''', FT, 2))

    words = ['encouraged', 'motivated', 'calm', 'confident', 'energized', 'strong', 'proud', 'in control', 'peaceful', 'capable', 'hopeful', 'joyful', 'steady', 'free', 'nourished', 'rested', 'light', 'focused']
    P.append(sheet(f'''<div class="eye">02</div><h2>My 2027 affirmation</h2>
<p>Your affirmation is how you choose to feel, every day, in 2027. Write it in the present tense, as if it’s already true. Use only the feelings you want. Leave the ones you’re leaving behind out of it.</p>
<div class="quote"><div class="q">“In 2027, I feel encouraged and motivated.”</div></div>
<div class="lab">Feeling words to choose from</div>
<div class="pills">{"".join(f"<span>{w}</span>" for w in words)}</div>
<div class="aff"><div class="start">In 2027, I feel</div>{lines("affirmation", 3, 26)}</div>
<div class="lab">Where I’ll put it so I see it every day</div>{ln("where")}
<p style="margin-top:10pt;font-size:9.5pt;color:#7a6168">Ideas: your bathroom mirror, your phone lock screen, the fridge, your car dashboard.</p>
<div class="lab">How I’ll know I’m living it</div>{lines("living", 3)}''', FT, 3))

    prompts = [('wake', 'When I wake up, I feel'), ('morning', 'My morning looks like'), ('eat', 'What I eat, and how I eat it'),
               ('move', 'How I move my body'), ('hard', 'When a hard moment comes, I'), ('evening', 'My evening, and how I rest'),
               ('emotions', 'My everyday emotions are')]
    body = ''.join(f'<div class="lab">{t}</div>{lines("day_"+k, 2)}' for k, t in prompts)
    P.append(sheet(f'''<div class="eye">03</div><h2>A day in my new life</h2>
<p>Imagine you’ve reached your goals and kept them for a full year. Close your eyes for a minute and picture yourself. Then write about your day in the present tense, as if you’re already living it.</p>
{body}''', FT, 4))

    P.append(sheet(f'''<div class="eye">04</div><h2>A day in my new life, with AI</h2>
<p>Want to go deeper? This version uses an AI assistant, like Claude, to turn your vision into a story you can see and feel, and then into a plan for your week.</p>
<div class="note"><b>Keep it about your life.</b> Write about your days, your habits, and your feelings. You don’t need to share medical details or anything private.</div>
<div class="steps">
<div class="st"><div class="n">1</div><div><h4>Brain dump your new life</h4><p>Write down everything you want your life to look and feel like one year from now, with your goals reached and kept. The big things, the small things, even the parts that feel too good to be true. Nobody reads this but you.</p></div></div>
<div class="st"><div class="n">2</div><div><h4>Ask AI to write the story</h4><p>Copy this in, then paste your brain dump underneath:</p><div class="prompt">“Based on this description, write a detailed story of one day in my life one year from now, after I’ve reached my health goals and kept them for a full year. Be specific. What does my morning look like? What do I eat? How do I move? How do I feel in my body? How do I handle stress? Who am I with? Write it like a scene from my day, not a summary.”</div></div></div>
<div class="st"><div class="n">3</div><div><h4>Read it, picture it, feel it</h4><p>Read it slowly. Notice what makes you smile and what gets you excited. Close your eyes and picture it clearly, and let yourself feel it. This is the person you’re becoming.</p></div></div>
<div class="st"><div class="n">4</div><div><h4>Find the gap</h4><div class="prompt">“Compare that future day to how I’m living right now. What is the biggest gap? What is the one thing I keep almost doing but haven’t started? Be specific and kind.”</div><p>This step can land hard. Take a breath with it. Seeing the gap is the first step to closing it, and you don’t have to close it alone.</p></div></div>
<div class="st"><div class="n">5</div><div><h4>Ask for your week</h4><div class="prompt">“Build me a simple weekly plan that bridges my life now to that future day. Keep it realistic for my schedule. Tell me what I could let go of to make room, and name the ONE thing to do this week that would make the biggest difference.”</div><p>Your dietitian’s plan comes first. Use this to support it, and bring what you find to your next visit.</p></div></div>
</div>
<div class="lab">My ONE thing this week</div>{ln("onething")}''', FT, 5))

    P.append(sheet(f'''<div class="eye">05 &middot; The HOW process</div><h2>Obstacles are expected in 2027</h2>
<p>Every plan hits bumps: a busy week, a holiday, a number that won’t move. That is normal. It does not mean the plan is broken or that you did something wrong. We plan for it with the HOW process.</p>
<div class="howsvg"><svg viewBox="0 0 772 320" role="img" aria-label="The HOW process"><defs><marker id="ha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#A4753D"/></marker></defs>
<g fill="none" stroke="#A4753D" stroke-width="2"><path d="M526 50H630V198" marker-end="url(#ha)"/><path d="M480 240H300" marker-end="url(#ha)"/><path d="M142 198V50H246" marker-end="url(#ha)"/></g>
<rect x="246" y="16" width="280" height="68" rx="12" fill="#964527"/><text x="386" y="60" text-anchor="middle" font-size="30" fill="#fff">The Work</text>
<rect x="480" y="202" width="290" height="76" rx="12" fill="#fff" stroke="#F2B574" stroke-width="3"/><text x="625" y="250" text-anchor="middle" font-size="28" fill="#31091C">Obstacle Management</text>
<rect x="2" y="202" width="298" height="76" rx="12" fill="#fff" stroke="#ACB574" stroke-width="3"/><text x="151" y="249" text-anchor="middle" font-size="26" fill="#31091C">Reflect &amp; Course Correct</text></svg></div>
<div class="how-rows">
<div class="hr"><span class="dot" style="background:#964527"></span><div><b>The Work.</b> You do your steps, one at a time.</div></div>
<div class="hr"><span class="dot" style="background:#F2B574"></span><div><b>Obstacle Management.</b> Something gets in the way. Pause, name it, and tell your dietitian. Don’t wait for your next visit.</div></div>
<div class="hr"><span class="dot" style="background:#ACB574"></span><div><b>Reflect &amp; Course Correct.</b> Together, we look at what happened, adjust what needs adjusting, and you get back to the work.</div></div>
</div>
<div class="along"><p><b>You are not doing this alone.</b> Your dietitian is part of every loop. Send us a portal message any time something gets in the way.</p></div>''', FT, 6))

    a = lambda url, t: f'<a href="{url}">{t}</a>'
    items = [
        ('Join Connection Space', f'<p>Our private community, where your 2027 Workbook, the 14-Day Reset guide, meal plans, and class replays live. You’ll also find community events, meal planning club, patient-only resources, and more. <b>Click here to SIGN UP or LOG IN:</b> {a(CS,"sdgprograms.com")}</p><div class="gk"><div class="k">Good to know</div><ul><li>After you sign up, we approve your account. This can take up to 48 business hours.</li><li>Connection Space is for active patients and clients, meaning at least one scheduled visit per quarter. We review membership each quarter, and members without a scheduled appointment that quarter are removed.</li></ul></div>'),
        ('RSVP for the 2027 Kickoff Class with Maya', f'<p>Live on <b>Saturday, January 9</b> or <b>Saturday, January 16, 2027</b>. Both classes are the same, so pick the one that fits your schedule. You’ll find them in Connection Space under <b>Events and Meet Ups</b>.</p><p><b>January 9:</b> {a("https://sdgprograms.com/events/kickoff-class-with-maya","RSVP here")} &nbsp;&middot;&nbsp; <b>January 16:</b> {a("https://sdgprograms.com/events/kickoff-class-with-maya-110064261","RSVP here")}</p><p>Can’t make either? Watch the replay in Connection Space.</p>'),
        ('Get your 2027 resources', f'<p>Inside Connection Space, go to the <b>Patient Resource Library</b>. The first section is <b>2027 Goal Planning and 14-Day Reset Resources</b>, with your reset guide, daily tracker, suggested meal plans, recipes, grocery list, and 2027 planning pages, all free.</p><p><b>Go straight there:</b> {a(RES,"2027 Goal Planning and 14-Day Reset Resources")}</p>'),
        ('Get new recipes every Friday', f'<p>Join our SDG mailing list and receive new recipes every Friday morning, plus community news. Be sure to add us to your contacts so we don’t land in your spam folder. You can unsubscribe at any time.</p><p><b>Sign up here:</b> {a("https://southwestdietitiangroup.kit.com/","southwestdietitiangroup.kit.com")}</p>'),
        ('Your patient portal: book, reschedule, and message your dietitian', f'<p>Your patient portal is your home base with SDG. Log in any time to:</p><ul><li><b>Schedule, reschedule, or cancel</b> your appointments with your dietitian, on your own time.</li><li><b>Message your dietitian</b> between visits.</li><li><b>Share documents</b> like labs, food logs, and tracking PDFs.</li><li><b>Update your card on file</b> and your information, and so much more.</li></ul><p>We know medical portals are no fun, but for now they are how we keep your information safe and follow HIPAA privacy laws. Bookmark the link below. You’ll also find it inside your SDG Connection Space.</p><div class="gk"><div class="k">Try it today</div><p style="margin:0 0 3pt">Log in, find your next appointment with your dietitian, and bookmark the page.</p></div><p><b>Patient portal:</b> {a("https://sdg.intakeq.com/portal","sdg.intakeq.com/portal")}</p>'),
    ]
    comm = ''.join(f'<div class="comm"><div class="ic">{i+1}</div><div><h4>{h}</h4>{b}</div></div>' for i, (h, b) in enumerate(items))
    intro = 'Welcome to the community at Southwest Dietitian Group, SDG for short. SDG is a heart-centered company. We put people over profits, and we commit deeply to supporting our communities, both in their food needs and in connecting them. Real health changes require a healthy nervous system, and a healthy nervous system is supported through safe, supportive connections. That is what our community is built to offer. We go together, we grow together, and that includes YOU.'
    coming = 'What about the moments in between visits? Real life happens there. You’re at the grocery store and the goal slips your mind. It’s a busy Wednesday night and you don’t know what to make for dinner. Or you just don’t feel motivated. We’re building something special for exactly those moments: a new accountability tool and program to support you between visits. Watch your email and Connection Space for more.'
    closing = 'Every BODY is different, and this is YOUR body’s plan. All you need to do is show up and take the right next step. And when you forget what that step is or feel lost, we’re here to help, every step of the way.'
    # community spans two sheets: intro + items 1-3, then 4-5 + coming + closing
    split = comm.split('<div class="comm">')
    first = '<div class="comm">'.join(split[:4]) ; second = '<div class="comm">' + '<div class="comm">'.join(split[4:])
    P.append(sheet(f'''<div class="eye">06 &middot; Your community</div><h2>Get connected</h2><p>{intro}</p><p><b>Here’s what’s available to you now, and what’s on our 2027 roadmap for you.</b></p>{first}''', FT, 7))
    P.append(sheet(f'''{second}<div class="coming"><div class="k">Coming in 2027</div><p>{coming}</p></div>
<div class="close"><div class="q">{closing}</div><div class="s">Your SDG team</div></div>''', FT, 8))
    return doc('My 2027 Vision', P)

# ======================= 2027 PLANNING PAGES =======================
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
def planning():
    FT = 'Southwest Dietitian Group  &middot;  My 2027 Planning Pages'
    P = []; n = 1
    P.append(sheet(f'''<div class="top"><img src="{LOGO}" alt="Southwest Dietitian Group"><span class="tag">2027</span></div>
<h1>My <em>2027</em><br>Planning Pages</h1>
<div class="name"><span>Name</span><div data-f="name" data-t="text"></div></div>
<div class="aff" style="margin-top:20pt"><div class="lab" style="margin-top:0">My 2027 affirmation</div><div class="start">In 2027, I feel</div>{lines("affirmation", 2, 26)}</div>
<h3>How to use these pages</h3>
<ul class="toc" style="margin-top:4pt;border-top:0;padding-top:0">
<li><b>12</b><span style="font-family:MU;font-size:10.5pt;font-weight:400;color:#2a1520"><b style="color:#31091C;width:auto;font-family:MU;font-size:10.5pt">Monthly check-ins.</b> At the end of each month, look back at your wins and numbers and choose your next step.</span></li>
<li><b>4</b><span style="font-family:MU;font-size:10.5pt;font-weight:400;color:#2a1520"><b style="color:#31091C;width:auto;font-family:MU;font-size:10.5pt">Quarterly reflections.</b> Fill one in before each quarterly visit and bring it with you.</span></li>
<li><b>+</b><span style="font-family:MU;font-size:10.5pt;font-weight:400;color:#2a1520"><b style="color:#31091C;width:auto;font-family:MU;font-size:10.5pt">Weekly planner and habit tracker.</b> At the back. Print or copy as many as you need.</span></li>
</ul>''', FT, n))
    def month(i, m):
        k = f'm{i+1}'
        rows = ''.join(f'<tr><td data-f="{k}_n{j}_what" data-t="text"></td><td data-f="{k}_n{j}_start" data-t="text"></td><td data-f="{k}_n{j}_end" data-t="text"></td></tr>' for j in range(1, 4))
        return f'''<div class="mhead"><div><div class="eye">Monthly check-in</div><h2>{m} 2027</h2></div></div>
<div class="lab">My focus this month (my current step)</div>{lines(k+"_focus", 2)}
<div class="lab">My numbers</div>
<table class="t"><tr><th style="width:44%">What I’m tracking</th><th>Start of month</th><th>End of month</th></tr>{rows}</table>
<div class="lab">My wins this month</div>{lines(k+"_wins", 5)}
<div class="grid2"><div><div class="lab">What got in the way</div>{lines(k+"_obst", 4)}</div><div><div class="lab">How I’ll course correct</div>{lines(k+"_cc", 4)}</div></div>
<div class="lab">What I want to remember</div>{lines(k+"_notes", 2)}
<div class="lab">My next step</div>{ln(k+"_next")}
<div class="checks"><div><span class="ck" data-f="{k}_msg" data-t="check"></span>I messaged my dietitian when I needed help</div>
<div style="display:flex;align-items:flex-end;gap:6pt"><span><span class="ck" data-f="{k}_booked" data-t="check"></span>My next appointment is booked:</span><div style="flex:1;border-bottom:1px solid #cbbcb4;height:16pt" data-f="{k}_appt" data-t="text"></div></div></div>'''
    def quarter(q, span):
        k = f'q{q}'
        rows = ''.join(f'<tr><td data-f="{k}_n{j}_what" data-t="text"></td><td data-f="{k}_n{j}_start" data-t="text"></td><td data-f="{k}_n{j}_now" data-t="text"></td><td data-f="{k}_n{j}_target" data-t="text"></td></tr>' for j in range(1, 4))
        return f'''<div class="mhead"><div><div class="eye">Quarterly reflection &middot; {span}</div><h2>Quarter {q} reflection</h2></div></div>
<div class="note" style="margin:4pt 0 2pt"><b>Bring this page to your quarterly visit.</b> &nbsp;My visit date: <span style="display:inline-block;width:1.6in;border-bottom:1px solid #ACB574;height:12pt;vertical-align:-2pt" data-f="{k}_date" data-t="text"></span></div>
<div class="lab">My biggest wins this quarter</div>{lines(k+"_wins", 4)}
<div class="lab">My numbers</div>
<table class="t"><tr><th style="width:34%">What I’m tracking</th><th>Where I started</th><th>Now</th><th>My target</th></tr>{rows}</table>
<div class="grid2"><div><div class="lab">What I learned</div>{lines(k+"_learn", 2)}</div><div><div class="lab">Who I’m becoming</div>{lines(k+"_becoming", 2)}</div></div>
<div class="lab">What got in the way, and how I handled it</div>{lines(k+"_obst", 3)}
<div class="lab">My focus for next quarter</div>{lines(k+"_focus", 3)}
<div class="lab">Questions for my dietitian</div>{lines(k+"_q", 3)}'''
    spans = {3: 'January to March', 6: 'April to June', 9: 'July to September', 12: 'October to December'}
    for i, m in enumerate(MONTHS):
        n += 1; P.append(sheet(month(i, m), FT, n))
        if i + 1 in spans:
            n += 1; P.append(sheet(quarter((i + 1) // 3, spans[i + 1]), FT, n))
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    wrows = ''.join(f'<tr><td style="width:.95in;font-size:8pt">{d}</td><td data-f="w_{d[:3].lower()}_meals" data-t="multi"></td><td data-f="w_{d[:3].lower()}_move" data-t="multi"></td><td data-f="w_{d[:3].lower()}_step" data-t="multi"></td></tr>' for d in days)
    n += 1
    P.append(sheet(f'''<div class="mhead"><div><div class="eye">Print or copy as many as you need</div><h2>Weekly planner</h2></div>
<div style="display:flex;align-items:flex-end;gap:6pt;font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:#964527">Week of <div style="width:1.4in;border-bottom:1px solid #cbbcb4;height:16pt" data-f="w_week" data-t="text"></div></div></div>
<div class="lab">My ONE thing this week</div>{ln("w_onething")}
<table class="week"><tr><th></th><th>Meals and prep</th><th>Movement</th><th>My step and notes</th></tr>{wrows}</table>
<div class="lab">Grocery and prep list</div>{lines("w_grocery", 3)}''', FT, n))
    hrows = ''.join(f'<tr><td class="h" data-f="h{r}_name" data-t="text"></td>' + ''.join(f'<td data-f="h{r}_d{d}" data-t="check"></td>' for d in range(1, 32)) + '</tr>' for r in range(1, 11))
    n += 1
    P.append(sheet(f'''<div class="mhead"><div><div class="eye">Print or copy as many as you need</div><h2>Habit tracker</h2></div>
<div style="display:flex;align-items:flex-end;gap:6pt;font-family:JS;font-weight:600;font-size:8pt;letter-spacing:.18em;text-transform:uppercase;color:#964527">Month <div style="width:1.4in;border-bottom:1px solid #cbbcb4;height:16pt" data-f="h_month" data-t="text"></div></div></div>
<p style="font-size:9.5pt;margin-top:4pt">Write the habits from your current step on the left, then check off each day you do them. Ideas: water goal, protein at breakfast, 10-minute walk after dinner, logged my food, in bed by 10.</p>
<table class="habit"><tr><th class="h">Habit</th>{"".join(f"<th>{d}</th>" for d in range(1, 32))}</tr>{hrows}</table>
<div class="lab">What I noticed this month</div>{lines("h_notice", 7)}''', FT, n))
    return doc('My 2027 Planning Pages', P)

if __name__ == '__main__':
    open('vision.html', 'w').write(vision())
    open('planning.html', 'w').write(planning())
