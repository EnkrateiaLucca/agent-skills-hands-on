---
name: anti-ai-writing-slop
description: >-
  Strip the tells of AI-generated prose out of any writing so it reads as human — specific,
  plain, and in the user's own voice. Use this WHENEVER you are drafting or editing prose the
  user will publish or send as their own: blog posts, LinkedIn posts, newsletters, emails,
  video/short scripts, Medium articles, essays, bios, cover letters, documentation, or Obsidian
  notes meant for others. Trigger it even when the user doesn't say "AI slop" — any request like
  "write a post about…", "draft an email…", "make this sound like me", "tighten this up",
  "does this sound like AI?", "de-slop this", or handing over a draft to polish. Also apply it as
  a self-check pass before returning any substantial piece of prose you wrote. Do NOT apply it to
  code, config, data, or when the user explicitly wants a formal/templated register.
---

# Anti-AI-Writing-Slop

## Why this exists

LLMs regress to the mean. Trained on oceans of promotional web copy, they default to prose that is
**simultaneously more exaggerated and less specific** than good human writing — shouting that the
subject is important while the actual facts blur into generic mush. The tells below are the visible
symptoms of that averaging. Removing them isn't cosmetic: each one is a place where a vague claim
should become a concrete fact, or an inflated phrase should become a plain one.

The goal is not "avoid banned words." It's to sound like **a specific person who knows this topic**
saying a **specific thing** — the user, usually. When in doubt, prefer the plainer, more concrete,
more falsifiable sentence.

## The one move that matters most

**Trade significance for specificity.** AI writing tells you something matters ("a pivotal moment,"
"underscores its importance," "a testament to"). Human writing shows the thing itself and lets the
reader judge. Whenever you catch a sentence *asserting* importance, legacy, or broader impact, ask:
*what concrete fact could replace this?* Usually the puffery is hiding the absence of one — so go
find the fact, or cut the sentence.

- ❌ "The 2019 release marked a pivotal moment in the evolution of the framework, reflecting a
  broader shift toward developer-first tooling."
- ✅ "The 2019 release let you deploy from a single config file, and adoption roughly tripled that year."

**The portability test.** If a sentence could move unchanged to another person, company, product, or
country, it is filler. Cut it, or replace it with a fact, mechanism, consequence, or judgment that only
fits this subject.

## The high-value tells to strip

These are the ones that most reliably scream "a bot wrote this." Fix on sight.

1. **AI vocabulary.** A cluster of these in one piece is the single strongest tell. They travel in
   packs — where one appears, others follow. Cut or replace: *delve, intricate, tapestry, testament,
   underscore, showcase, boasts, vibrant, robust, pivotal, crucial, garner, foster, landscape (as
   metaphor), realm, nuanced, meticulous, seamless, leverage, harness, elevate, resonate, align with,
   emphasizing, highlighting, ensuring, enhance, bolster, navigate (as metaphor), a rich history of,
   utilize, facilitate, empower, streamline, cutting-edge, paradigm shift, game changer, this is huge,
   this changes everything, beacon, multifaceted, paramount, transformative, embark, supercharge,
   ever-evolving* and especially sentence-opening **"Additionally,"** / **"Moreover,"** /
   **"Furthermore,"**. These are flags, not bans: density and co-occurrence convict.

2. **Negative parallelism.** The "not X, but Y" family: *"It's not just a tool, it's a movement,"*
   *"not a mirror but a portal,"* *"no fluff, no filler, just results."* This fake-profound contrast
   is maybe the most recognizable AI cadence. Say the positive claim plainly and drop the strawman.

3. **Rule of three.** Reflexive three-item lists — *"fast, reliable, and scalable,"* three parallel
   clauses in a row. One or two concrete items beat three padded ones. Vary your list lengths.

4. **The -ing significance tail.** A participial phrase bolted onto a sentence to editorialize about
   what it means: *"…, highlighting its role in the community,"* *"…, reflecting a broader trend,"*
   *"…, cementing its legacy."* These are almost always unsupported opinion. Cut them.

5. **Copula avoidance.** AI dodges plain *is/are/has*, reaching for *serves as, stands as, functions
   as, represents, boasts, features, offers.* Just use *is* and *has*. "X is a Y" is good writing.

6. **Em dashes.** LLMs use " — " as a default rhythm crutch. Short copy (posts, emails, scripts):
   none. Longer drafts: at most 1-2, and only when one clearly beats a comma, period, or parentheses.
   Remove clusters and decorative dashes. (This is a known Claude tendency; watch your own output.)

7. **Promotional / travel-brochure tone.** *"Nestled in the heart of," "boasts a rich cultural
   heritage," "a diverse array of," "groundbreaking," "renowned for."* Neutral it out even when the
   subject is genuinely cool. Enthusiasm should come from the facts, not the adjectives.

8. **Formulaic conclusions.** *"In conclusion / Overall / In summary,"* and especially the
   "Despite its challenges, X continues to thrive…" closer, or tacked-on "Challenges" / "Future
   Outlook" sections. End on a concrete last beat, not a restatement.

9. **Elegant variation.** Straining to never repeat a word, so "the app" becomes "the platform,"
   "the solution," "the offering" in consecutive sentences. Repeating the plain noun is fine and
   clearer.

10. **Vague attribution.** *"Experts argue," "industry reports suggest," "many have noted,"* "studies
    show" with no study. Either name the source or state it as your own claim.

11. **Throat-clearing and faux-insight openers.** *"Here's the thing," "Let me be clear," "I'll be
    honest," "The uncomfortable truth is," "What most people get wrong," "Here's what nobody tells
    you," "The part everyone misses."* These flatter the writer as the lone expert and delay the point.
    Cut the setup; the claim stands alone. "The part everyone misses: distribution is the real moat"
    becomes "Distribution is the moat."

12. **Colon reveals.** A noun phrase, a colon, then a dramatic lowercase reveal: *"The best part: it
    learns." "The detail that makes it work: a separate agent grades it."* Rewrite as a plain sentence.
    Colons are for lists, labels, and quotes, not drama. Sentence case after a colon unless grammar,
    a proper noun, a title, or code requires otherwise.

13. **Interpretive metadiscourse.** Lines that step outside the subject to tell the reader what to
    notice or how much weight to give it: *"That last part matters more than it sounds," "The key
    point is," "As you can see," "This distinction matters," "It's worth noting,"* redundant *"In
    other words."* Show, don't tell the reader what to think. If the prose already shows it, delete the
    aside. If it doesn't, replace the aside with support.

14. **Rhetorical setups and dramatic fragmentation.** *"What if I told you...", "Think about it:",
    "Plot twist:",* self-answered "Question? Answer." pairs. Negative listing: *"Not a X. Not a Y. A
    Z."* Stacked punchy fragments: *"X. And Y. And Z." "That's it. That's the whole thing."* Say Z.
    Use complete sentences. (A single fragment in the writer's natural spoken rhythm is fine; a stack
    of them for effect is the tell.)

15. **Fake-profound kickers.** A closing line that turns the point into a cute metaphor, aphorism, or
    mic drop. Delete it. Do not rewrite it into a better metaphor or preserve its rhythm. End on the
    clearest concrete sentence already in the draft, or add a plain takeaway or next action.

16. **Empty adverbs and filler phrases.** Cut by default: *just, literally, honestly, simply, actually,
    truly, fundamentally, importantly, crucially, inherently, inevitably, very.* Phrases: *it's worth
    noting, it's important to note, at the end of the day, when it comes to, at its core, in today's
    world, in the age of, in the world of, the reality is, the truth is, in terms of, with regard to,
    in order to, the fact that, going forward, in this article, let's dive in.* Keep one only when it
    carries real uncertainty or contrast the sentence needs.

17. **Weak verbs and inanimate agents.** *"Made a decision"* is *"decided."* *"Has the ability to"*
    is *"can."* Use active voice with human subjects: *"The team shipped it Tuesday,"* not *"the
    decision emerged."* Never let inanimate things do human verbs.

## Formatting tells (for anything with structure)

- **Boldface spam** — bolding a key phrase in every bullet, "key-takeaways" style. Bold sparingly.
- **Title Case Headings** — use sentence case unless the user's house style says otherwise.
- **Emoji as bullets/section markers** (🚀 ✨ 🎯) — drop them unless the user's voice actually uses them.
- **Bullets where prose reads better**, and headers over two-sentence sections. Format follows the
  content; it does not decorate it.
- **Collaborative-assistant filler** leaking into the text: *"Certainly!," "I hope this helps,"
  "Would you like me to…," "Here's a breakdown of…," "Let's dive in."* Never ships in the user's voice.
- **Knowledge-cutoff / hedge disclaimers**: *"As of my last update," "while specific details are
  limited," "based on available information."* Cut entirely.

## What good human writing actually looks like

Steer *toward* these — they're what AI text underproduces, so they read as authentically human:

- Plain **is/has** sentences; short words over stiff synonyms (*use* not *utilize*, *wrote* not
  *authored*, *died* not *passed away*, *about* not *regarding*).
- **Concrete, checkable specifics** — numbers, names, dates, mechanisms, one real example.
- **A definite point of view** — "this is the best way to do X," "I was wrong about Y." AI hedges;
  people commit. (Keep it honest, but don't sand off the opinion.)
- **Uneven rhythm** — mix long and short sentences. AI prose is metronomic; real writing lurches.
- The user's actual idioms and asymmetries. If you have samples of their writing (their blog posts,
  LinkedIn, notes), match those over any generic "good writing."

## Editing someone's draft: the minimum effective edit

When the user hands over a draft rather than asking for one, you are an editor, not a rewriter.

- First notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and
  level of polish. Those traits survive the edit.
- Fix AI patterns, errors, repetition, and tangled passages. Leave strong human sentences alone. Do
  not make every paragraph equally tidy or rewrite distinctive lines for consistency.
- Keep opinions, blunt language, profanity, self-interruptions, and honest admissions that belong
  to the writer. Do not swap them for safer wording.
- Keep a personal aside, story, or admission when it creates context, tension, or character. Cut
  only generic throat-clearing.
- Keep the structure unless it hurts the piece. Front-load the point only where that helps.
- Never invent claims, examples, stats, or opinions. If a weasel attribution has no source, ask
  rather than inventing one.
- Cutting should be proportional to the actual slop. Aggressive compression that strips character
  is its own failure.

## Detect mode

When the user asks "does this sound like AI?", or to audit, scan, or flag a draft without rewriting:
name each pattern from this skill that appears, quote the line, and give the fix in a few words. Do
not rewrite, do not score the draft, and do not guess whether AI wrote it. Detectors guess; named
patterns are evidence the user can check. Offer to edit afterward.

## Don't overcorrect

Naturalness is the goal, not word-avoidance. Guard against these failure modes:

- A single "crucial" is **not** slop. It's *density* and *co-occurrence* that convict. Don't mangle a
  good sentence to dodge one flagged word.
- These words have honest literal uses — *underscore* (a mark), *landscape* (actual terrain),
  *robust* (statistics). Context matters.
- Formal or academic prose isn't automatically AI. If the user wants a formal register, give it to
  them; just keep it specific and copula-friendly.
- Don't strip real enthusiasm or real structure to pass a detector. The target is a human reader,
  not GPTZero.

## Full catalog

For the complete word-watch lists, era-by-era vocabulary shifts, worked before/after examples, and
the finer-grained tells (leads-as-definitions, "not just… but," reversed parallelisms, etc.), read
`references/ai-tells-catalog.md`. Pull it in when you're doing a careful de-slop pass on an important
piece or when you want to explain *why* a specific sentence reads as AI.
