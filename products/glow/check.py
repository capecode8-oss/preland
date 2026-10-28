import pdfplumber,sys
p=pdfplumber.open(sys.argv[1]);print(sys.argv[1],'pages',len(p.pages))
for i,pg in enumerate(p.pages):
    ws=pg.extract_words()
    body=[w for w in ws if w['bottom']<pg.height-62]
    bottom=max([w['bottom'] for w in body] or [0])
    first=' '.join(w['text'] for w in body[:7])
    print(f"{i+1:>2} fill={bottom/pg.height:.2f} words={len(ws):>3}  {first}")
