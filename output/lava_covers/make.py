from playwright.sync_api import sync_playwright
B=[
 ("01","The Belly<br>Fat Lie","Why the belly stays, and what actually helps.","#C13A30","#7d2019","The Belly<br>Fat Lie"),
 ("02","Aging Faster<br>Than You<br>Should","Why you look older than you feel.","#238077","#124a46","Aging Faster<br>Than You Should"),
 ("03","The Caffeine<br>Trap","Why you're still tired after a full night's sleep.","#C27A12","#744507","The Caffeine<br>Trap"),
 ("04","The 3AM<br>Signal","Why you wake up at 3AM, and what to do.","#25508F","#0f2447","The 3AM<br>Signal"),
]
CSS="""*{box-sizing:border-box;margin:0}body{width:1160px;height:464px;overflow:hidden;font-family:'Inter',sans-serif;position:relative}
.bg{position:absolute;inset:0;background:radial-gradient(circle at 78% 45%,%A 0%,%B 100%)}
.left{position:absolute;left:64px;top:0;bottom:0;width:640px;display:flex;flex-direction:column;justify-content:center;color:#fff}
.k{font-size:20px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;opacity:.85;margin-bottom:14px}
h1{font-size:%Tpx;line-height:1.02;font-weight:800;letter-spacing:-.02em;margin-bottom:16px}
.s{font-size:26px;line-height:1.3;font-weight:500;opacity:.95;max-width:560px;margin-bottom:22px}
.pill{display:inline-flex;gap:18px;font-size:18px;font-weight:700;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.4);padding:9px 18px;border-radius:40px;align-self:flex-start}
.book{position:absolute;right:92px;top:50px;width:262px;height:364px;border-radius:6px 14px 14px 6px;background:linear-gradient(145deg,%A,%B);transform:rotate(5deg);box-shadow:-14px 22px 40px rgba(0,0,0,.45),inset 8px 0 0 rgba(0,0,0,.22);padding:34px 28px 28px 38px;color:#fff;display:flex;flex-direction:column;border:2px solid rgba(255,255,255,.28)}
.book .n{font-size:15px;font-weight:800;letter-spacing:.18em;opacity:.8;margin-bottom:16px}
.book .t{font-size:38px;line-height:1.04;font-weight:800;letter-spacing:-.01em}
.book .f{margin-top:auto;font-size:14px;font-weight:700;letter-spacing:.1em;opacity:.8}
.glow{position:absolute;right:40px;top:30px;width:380px;height:400px;background:radial-gradient(circle,rgba(255,255,255,.22),transparent 65%)}
"""
def page(a,b,tsize,inner):
    return "<html><head><meta charset=utf-8><style>"+CSS.replace('%A',a).replace('%B',b).replace('%T',str(tsize))+"</style></head><body><div class=bg></div><div class=glow></div>"+inner+"</body></html>"
pages={}
for n,t,sub,a,b,bt in B:
    ts=64 if t.count('<br>')<2 else 56
    inner=f"<div class=left><div class=k>Guide {n} · PDF</div><h1>{t}</h1><div class=s>{sub}</div><div class=pill><span>Instant PDF</span><span>·</span><span>14-day guarantee</span></div></div><div class=book><div class=n>GUIDE {n}</div><div class=t>{bt}</div><div class=f>THE KIRA METHOD</div></div>"
    pages[f"cover_{n}"]=page(a,b,ts,inner)
# bundle
mini=""
cols=[("#C13A30","#7d2019","The Belly<br>Fat Lie"),("#238077","#124a46","Aging<br>Faster"),("#C27A12","#744507","The Caffeine<br>Trap"),("#25508F","#0f2447","The 3AM<br>Signal")]
for i,(a,b,t) in enumerate(cols):
    mini+=f"<div style='position:absolute;left:{628+i*118}px;top:{74+(i%2)*26}px;width:152px;height:236px;border-radius:4px 10px 10px 4px;background:linear-gradient(145deg,{a},{b});transform:rotate({-8+i*5}deg);box-shadow:-8px 14px 26px rgba(0,0,0,.4),inset 6px 0 0 rgba(0,0,0,.22);border:2px solid rgba(255,255,255,.28);padding:22px 14px 14px 22px;color:#fff;font-weight:800;font-size:22px;line-height:1.05;z-index:{i}'><div style='font-size:11px;letter-spacing:.16em;opacity:.8;margin-bottom:10px'>GUIDE 0{i+1}</div>{t}</div>"
inner=f"<div class=left style='width:560px'><div class=k>Pack of 4 · PDF</div><h1 style='font-size:46px'>Your Body Has Been Trying to Tell You</h1><div class=s style='font-size:26px'>4 short guides + 4 tools, in plain English.</div><div class=pill><span>Instant PDF</span><span>·</span><span>14-day guarantee</span></div></div>{mini}"
pages["cover_bundle"]=page("#2a7a70","#0f3a36",46,inner)
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    for k,h in pages.items():
        pg=br.new_page(viewport={'width':1160,'height':464});pg.set_content(h);pg.wait_for_timeout(400)
        pg.screenshot(path=k+'.png');pg.close()
    br.close()
