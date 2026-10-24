from playwright.sync_api import sync_playwright
cols=[("#C13A30","#7d2019","The Belly<br>Fat Lie"),("#238077","#124a46","Aging<br>Faster"),("#C27A12","#744507","The Caffeine<br>Trap"),("#25508F","#0f2447","The 3AM<br>Signal")]
mini=""
for i,(a,b,t) in enumerate(cols):
    mini+=f"<div style='position:absolute;left:{540+i*116}px;top:{40+(i%2)*18}px;width:118px;height:196px;border-radius:4px 9px 9px 4px;background:linear-gradient(145deg,{a},{b});transform:rotate({-7+i*4}deg);box-shadow:-7px 12px 22px rgba(0,0,0,.45),inset 5px 0 0 rgba(0,0,0,.22);border:2px solid rgba(255,255,255,.28);padding:18px 11px 11px 18px;color:#fff;font-weight:800;font-size:17px;line-height:1.05;z-index:{i}'><div style='font-size:10px;letter-spacing:.16em;opacity:.8;margin-bottom:8px'>GUIDE 0{i+1}</div>{t}</div>"
html=f"""<html><head><meta charset=utf-8><style>
*{{box-sizing:border-box;margin:0}}body{{width:1160px;height:464px;overflow:hidden;font-family:'Inter',sans-serif;position:relative;color:#fff}}
.bg{{position:absolute;inset:0;background:radial-gradient(circle at 75% 40%,#2a7a70 0%,#0f3a36 100%)}}
.left{{position:absolute;left:60px;top:0;bottom:0;width:470px;display:flex;flex-direction:column;justify-content:center}}
.k{{font-size:18px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;opacity:.85;margin-bottom:12px}}
h1{{font-size:56px;line-height:1.02;font-weight:800;letter-spacing:-.02em;margin-bottom:12px}}
h1 span{{color:#FFD65A}}
.s{{font-size:23px;line-height:1.3;font-weight:500;opacity:.95;margin-bottom:20px}}
.pill{{display:inline-flex;gap:14px;font-size:17px;font-weight:700;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.4);padding:8px 16px;border-radius:40px;align-self:flex-start}}
.bonus{{position:absolute;left:560px;top:252px;width:560px;border-radius:16px;background:linear-gradient(135deg,#FFE27A,#F2B632);color:#3a2a00;padding:14px 20px 14px;box-shadow:0 12px 30px rgba(0,0,0,.4);z-index:9}}
.bonus .bt{{font-weight:800;font-size:19px;letter-spacing:.12em;margin-bottom:8px}}
.bonus .grid{{display:grid;grid-template-columns:1fr 1fr;gap:5px 14px;font-size:16px;font-weight:700}}
.badge{{position:absolute;left:1010px;top:226px;z-index:10;background:#D8322B;color:#fff;font-weight:800;font-size:16px;letter-spacing:.08em;padding:6px 14px;border-radius:30px;transform:rotate(-4deg);box-shadow:0 4px 12px rgba(0,0,0,.4)}}
</style></head><body><div class=bg></div>
<div class=left><div class=k>Bundle · PDF</div><h1>4 Guides<br>+ <span>BONUS</span></h1><div class=s>Your Body Has Been Trying to Tell You</div><div class=pill><span>Instant PDF</span><span>·</span><span>14-day guarantee</span></div></div>
{mini}
<div class=badge>INCLUDED</div>
<div class=bonus><div class=bt>BONUS: 4 TOOLS</div><div class=grid><span>1. Start Here</span><span>3. Doctor's Brief</span><span>2. 14-Day Body Log</span><span>4. 3 Questions For Your Doctor</span></div></div>
</body></html>"""
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium');pg=br.new_page(viewport={'width':1160,'height':464});pg.set_content(html);pg.wait_for_timeout(400);pg.screenshot(path='cover_bundle_bonus.png');br.close()
