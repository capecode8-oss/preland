import sys, json
sys.path.insert(0, "tools/carousel")
import gen_atlas_five as g
from PIL import Image
OUT = "carousels/2026/10/til8"
B1="""I spent years doing everything right. Less food. More walking. Nothing moved.

Then I found out what actually happens inside a woman's body after 40. It's not about calories. It's not about willpower. My body was fighting against me — and I had no idea why.

I put together everything I found — the research nobody explains at the doctor's office, what's actually causing the belly that won't move, and what changed when I finally understood it."""
B2="""I looked in the mirror one morning and didn't recognize myself. Not old. Just... less. Less bright. Less firm. Less me.

I started researching what actually happens to a woman's skin after 40 — not the creams, not the treatments. What's happening on the inside. What you're eating that's speeding it up. What your body is missing that nobody mentions.

I pulled it all together. What I found changed how I eat, how I sleep, how I think about my body."""
B3="""I kept thinking it was just aging. The belly. The skin. Waking up at 3AM. Not feeling like myself anymore.

It wasn't aging. My body had been sending signals for years. I just didn't know how to read them.

I collected everything — the belly fat research, what's aging your skin faster than years, the 3AM signals, the caffeine truth. Four books. Everything in one place."""
CTA="""👇 HOW TO GET IT: 👇
• FOLLOW this account 🔒
• COMMENT GLOW below 💬
I'll send it straight to your DMs."""
P=[
("til_nonenal","a woman in her forties looking at herself in a bathroom mirror in soft morning light, thoughtful, face in the upper half of the frame",
 ["A 2001 study found a skin chemical that only showed up after age 40.","Later research disagrees. Here's what actually holds up →"],
"""A study in 2001 tested shirts worn by people of different ages. The researchers found a chemical called 2-nonenal only on shirts from people aged 40 and older. They linked it to the faint "old person smell."

Here's the part that rarely gets said. It was a small study, just 22 people. Later work didn't always back it up. A team at the Monell Center, which studies smell, reported that it couldn't find the chemical on older people at all. Other studies found different compounds instead.

What did hold up? In a 2012 study, people could tell the body odor of people over 75 from people under 55. But they couldn't tell people in their 20s from people aged 45 to 55. In another Monell study, volunteers rated older people's odor as neutral, not unpleasant.

So here's what we know. Body odor does change with age. The details are still argued about. The "40" comes from one small study.

Your skin changes too. Nobody explains why.""",
 "A fact can sound settled and still be a lot less certain than the headline. Skin is the same.", B2, "📌 Save this before you believe the next \"science says\" post."),
("til_estranged","an empty holiday dinner table set for six with one chair pushed back, family photos on the wall, warm window light, room in the upper half of the frame",
 ["27% of American adults say they've cut off a family member.","Most say it still hurts. Here's who it happens between →"],
"""Cornell professor Karl Pillemer surveyed more than 1,300 American adults. 27% said they were estranged from a family member right now.

Most of the people who reported a rift said it upset them.

The breakdown: 10% were estranged from a parent or a child. 8% from a sibling. 9% from extended family.

Pillemer says the real number is probably higher, because some people don't want to admit it. A 2025 YouGov poll, reported by one outlet, put it at 38%. That used a different method, so the two numbers can't be compared directly.

It isn't a rare family secret. It's in a lot of houses. Maybe yours. Maybe the one down the street.

If you've ever held a phone with a name you couldn't call, you are not the only one.""",
 "Most of us who carry a family rift still show up for everyone else.", "I gave my family everything and kept nothing for my own body. When I finally listened to it, I wrote down what it had been telling me for years.", "📌 Save this for the next time someone says \"family is everything.\""),
("til_twins","two tiny pairs of newborn baby socks laid side by side on a hospital blanket next to a bright window, soft light, objects in the upper half of the frame",
 ["A mother gave birth to one twin in June. The other was born in August.","87 days apart. This is how it happened →"],
"""In June 2012, Maria Jones-Elliott from Waterford, Ireland, went into labor at 23 weeks. Her first twin, Amy, was born weighing about 1 pound 3 ounces.

Then her contractions stopped.

Doctors tried to induce labor again. It didn't work. The second twin, Katie, stayed inside.

Katie was born on August 27, 2012, at 36 weeks. That was 87 days after her sister. Coverage at the time said it would likely be a Guinness World Record, beating the previous record of 84 days. I couldn't find confirmation of the final ruling.

Doctors called it extraordinary. Katie was at risk of infection while she waited, and the couple chose to let nature take its course.

A woman's body can do things like this. Most of us were never told how much it does quietly, every day.""",
 "I read stories like this and realize how little I knew about my own body.", B3, "📌 Save this for the friend who needs a reminder of what bodies can do."),
("til_guardrail","an empty rural highway at golden hour with a curved metal guardrail along the shoulder and green Tennessee hills, wide road in the upper half of the frame",
 ["His daughter died in a crash. Then he got a $3,000 bill for the guardrail.","The bill was a mistake. What he did next is bigger than the bill →"],
"""In November 2016, 17-year-old Hannah Eimers died in a car crash on I-75 in Tennessee. A Highway Patrol report cited by local news said a guardrail piece went into the car.

Her father, Steve Eimers, later received a bill for about $3,000 to replace the guardrail. It was sent by mistake.

He didn't stay quiet. He sued the maker of the guardrail end, a model called X-LITE, and pushed states to take it off the road. He refused to sign a settlement that came with a gag order.

His push helped put language into the 2021 infrastructure bill. The Senate passed its version that August.

Whatever you think of the case, one thing is clear. He turned the worst day of his life into a way to look at something we drive past every day.

I read stories like this and wonder what else sits right next to us that we never look at.""",
 "Warning signs are everywhere. We just learn to stop seeing them.", "I learned to read every warning sign except the ones my body sends.", "📌 Save this before your next road trip."),
("til_eu261","rows of empty airport gate seats at night with a large window showing a parked airplane, tired atmosphere, seats in the upper half of the frame, no text",
 ["Your flight in Europe lands 3 hours late. The airline may owe you cash.","Up to €600. Most people never ask →"],
"""If you fly in Europe, there's a rule most people never use. Under EU Regulation 261/2004, you may be owed money when your flight reaches its final destination 3 hours or more late.

The amount depends on distance. €250 for trips up to 1,500 km. €400 for longer trips inside the EU and for flights of 1,500 to 3,500 km. €600 for trips over 3,500 km between an EU airport and a non-EU airport, where the delay threshold is 4 hours.

Two things people miss. First, arrival time is counted when the aircraft door opens, not when it touches down. Second, airlines don't have to pay if the delay came from "extraordinary circumstances." Weather and air traffic control generally count. Mechanical problems and crew issues generally don't.

The rule covers flights leaving the EU, and flights arriving in the EU on an EU airline. Check the details for your own trip, and know that rules can change. You can make a claim straight to the airline.""",
 "Every trip showed me what travel does to a woman's body after 40.", "On the road I noticed things about my body I used to blame on age. They weren't age.\n\nI wrote down all of it, in one place.", "📌 Save this before your next flight."),
("til_meds","a kitchen counter with a weekly pill organizer, a handwritten notebook page with blurred lines of writing and a pen, soft morning light, objects in the upper half of the frame",
 ["If an ambulance came tonight, could you hand over this one page?","EMS programs across the US ask every household to keep one →"],
"""Imagine an ambulance is at your door right now. The paramedic asks three things. What medications do you take? Do you have allergies? What's your medical history?

If you can't answer, who can?

Programs run by fire departments and EMS in many US towns ask households to keep one page ready for exactly this. It's often called a Vial of Life. The page lists conditions, allergies, current medications and an emergency contact. Many programs say to keep it where responders can find it, often the fridge, and to date it so they know how current it is.

One paramedic quoted in coverage said many relatives don't know the patient's medical history or daily medications.

It takes ten minutes. Write it once. Update it when anything changes. Make a copy for everyone in the house.

If you live alone, it matters even more.""",
 "I think about how many women walk into a doctor's office and can't remember the list.", "My answer is in the Health Bundle: a Doctor's Brief, a 14-Day Body Log and 3 questions to ask your doctor. Four short books and four tools about what your body has been trying to tell you.", "📌 Save this before your next doctor visit."),
("til_milk","a vintage glass milk bottle with bluish-white milk standing on a wooden crate on an old cobblestone New York street, bottle in the upper half of the frame, no text",
 ["In the 1850s New York sold bluish milk as \"Pure Country Milk.\"","What was really in the bottle took a journalist to expose →"],
"""In the 1850s, a lot of New York's milk came from cows kept in stables next to whiskey distilleries and fed the leftover mash. The milk came out thin and bluish.

Dairymen fixed the look with additives. Sources list water, chalk, flour, starch, eggs, molasses and plaster of Paris. It was sold as "Pure Country Milk."

Journalist Frank Leslie exposed it in 1858. The New York legislature passed milk rules in 1862. A contemporary estimate, repeated in later accounts, put infant deaths from this milk around 8,000 a year. That's a number from the era, not a verified count.

It took years of pressure, railroads that brought milk from real farms, and pasteurization to fix it. The federal Pure Food and Drug Act came in 1906.

Today we think of milk as simple. It wasn't always. The label said one thing. The bottle said another.""",
 "The label said one thing. The bottle said another. I think about that with everything we put in our bodies.", "We check labels, bills and fine print. I started reading what my body had been trying to tell me.", "📌 Save this before your next grocery trip."),
("til_skeletons","a dim pirate cave interior with a skeleton pirate prop sitting on a treasure chest lit by a glowing lantern, dramatic but bright, subject in the upper half of the frame, no text",
 ["The skeletons in Disneyland's Pirates ride were once real.","How they got them, and what Disney says happened next →"],
"""When Disneyland's Pirates of the Caribbean opened in 1967, the designers wanted the skeletons to look real. The fake bones of the 1960s didn't convince them.

According to former Disney producer Jason Surrell, the team got real remains from the anatomy departments at UCLA's medical school.

Disney's position, as paraphrased in coverage, is that the real bones were later swapped for fakes and returned to their source for proper burial.

Some people say a skull or two might still be in the ride. That part is unverified. I found no primary source, like a Disney statement or medical school records, that confirms it.

Whatever is in the ride today, the story is a good reminder: sometimes the thing that looks most fake is the real one.""",
 "Funny how much we don't notice until someone points it out. Bodies are like that.", B3, "📌 Save this before your next theme park trip."),
]
sheet=[]
for slug,prompt,blocks,story,pivot,bridge,save in P:
    bg=g.flux(prompt); bg.save(f"{OUT}/{slug}_bg.jpg",quality=92)
    g.cover_sans(bg,blocks,f"{OUT}/{slug}.jpg")
    cap=f"{story}\n\n{pivot}\n\n{bridge}\n\n{save}\n\n{CTA}"
    open(f"{OUT}/{slug}_caption.txt","w").write(cap)
    print(slug,len(cap),"free" in cap.lower(),"#" in cap)
    sheet.append(Image.open(f"{OUT}/{slug}.jpg").resize((405,506)))
sh=Image.new("RGB",(405*4,506*2))
for i,im in enumerate(sheet): sh.paste(im,((i%4)*405,(i//4)*506))
sh.save("/tmp/claude-0/-home-user-preland/060f7d12-589c-5001-aaab-eefd926c8c4c/scratchpad/til8_sheet.jpg",quality=88)
