# Generates protein-plan.html with protein totals computed from the item table (no hand arithmetic).
ITEMS = {  # name: (portion, protein_g)  approximate typical values
 "yogurt": ("Greek yogurt, plain nonfat, 3/4 cup", 16), "egg": ("hard-boiled egg", 6), "eggs2": ("2 scrambled eggs", 12),
 "cheesestick": ("string cheese, 1 stick", 7), "cottage": ("cottage cheese, 1/2 cup", 13), "tuna": ("canned tuna, 3 oz", 20),
 "chicken": ("cooked chicken breast, 3 oz", 26), "salmon": ("cooked salmon, 3 oz", 21), "shrimp": ("cooked shrimp, 3 oz", 20),
 "lentils": ("lentil soup or cooked lentils, 1 cup", 18), "tofu": ("firm tofu, 1/2 cup", 10), "milk": ("milk, 1 cup", 8),
 "kefir": ("kefir, 1 cup", 9), "almonds": ("almonds, 1/4 cup", 7), "pb": ("peanut butter, 2 tbsp", 7), "shake": ("protein shake, 1 scoop powder in water", 22),
 "turkey": ("deli turkey, 2 oz", 10), "edamame": ("shelled edamame, 1/2 cup", 9), "hummus": ("hummus, 1/4 cup", 5),
 "cheddar": ("cheddar cheese, 1 oz", 7), "beans": ("black beans, 1/2 cup", 8),
}
DAYS = [
 ("Day 1", [("Breakfast", ["yogurt","almonds"], "yogurt with almonds and berries"), ("Lunch", ["tuna"], "on toast or greens"),
            ("Afternoon", ["egg","egg","cheesestick"], "two hard-boiled eggs and a cheese stick"), ("Dinner", ["chicken"], "with vegetables")]),
 ("Day 2", [("Breakfast", ["eggs2","cheesestick"], "scrambled eggs and a cheese stick"), ("Lunch", ["lentils","hummus"], "lentil soup with hummus and veggies"),
            ("Afternoon", ["cottage","almonds"], "cottage cheese with fruit and almonds"), ("Dinner", ["salmon"], "with greens")]),
 ("Day 3", [("Breakfast", ["shake"], "sip slowly over 20 minutes"), ("Lunch", ["turkey","hummus","cheddar"], "turkey, hummus and cheese in a wrap"),
            ("Afternoon", ["yogurt","almonds"], "yogurt with almonds"), ("Dinner", ["shrimp"], "with rice or vegetables")]),
 ("Day 4", [("Breakfast", ["yogurt","pb"], "yogurt with peanut butter and oats"), ("Lunch", ["tuna"], "tuna salad"),
            ("Afternoon", ["kefir","egg","egg"], "kefir and two hard-boiled eggs"), ("Dinner", ["tofu","edamame","pb"], "tofu and edamame stir-fry with peanut sauce")]),
 ("Day 5", [("Breakfast", ["eggs2","cheesestick"], "scrambled eggs with spinach and a cheese stick"), ("Lunch", ["beans","cheddar","turkey"], "bean, cheese and turkey bowl"),
            ("Afternoon", ["shake"], "sip slowly"), ("Dinner", ["chicken"], "chicken soup or roast")]),
 ("Day 6", [("Breakfast", ["cottage","almonds"], "cottage cheese with berries and almonds"), ("Lunch", ["salmon"], "on greens or toast"),
            ("Afternoon", ["milk","egg","cheesestick"], "a glass of milk, an egg and a cheese stick"), ("Dinner", ["lentils","egg"], "lentil stew topped with an egg")]),
 ("Day 7", [("Breakfast", ["yogurt","almonds"], "yogurt with almonds"), ("Lunch", ["chicken"], "cold chicken with vegetables"),
            ("Afternoon", ["cheesestick","egg","milk"], "a cheese stick, an egg and a glass of milk"), ("Dinner", ["shrimp"], "shrimp with vegetables")]),
]
def row_items(keys): return " + ".join(ITEMS[k][0] for k in keys), sum(ITEMS[k][1] for k in keys)
out=[]
shop=set()
for d, meals in DAYS:
    rows=[]; total=0
    for t, keys, note in meals:
        txt, g = row_items(keys); total+=g
        shop.update(keys)
        rows.append(f'<tr><td>{t}</td><td>{txt}{(" — "+note) if note else ""}</td><td>~{g} g</td></tr>')
    out.append(f'<div class="nobreak"><h3>{d} &nbsp;·&nbsp; about {total} g protein</h3><table><tr><th style="width:18%">Stop</th><th>What</th><th style="width:14%">Protein</th></tr>{"".join(rows)}</table></div>')
    print(d, total)
cheat="".join(f'<tr><td>{v[0].capitalize()}</td><td>~{v[1]} g</td></tr>' for k,v in sorted(ITEMS.items(), key=lambda kv:-kv[1][1]))
html=open('20-gram-rule.template.html').read().replace('{{DAYS}}',"\n".join(out)).replace('{{CHEAT}}',cheat)
open('20-gram-rule.html','w').write(html)
