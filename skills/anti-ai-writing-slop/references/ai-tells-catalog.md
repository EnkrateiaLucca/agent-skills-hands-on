# AI Writing Tells — Full Catalog

Adapted for general prose (blog posts, LinkedIn, newsletters, scripts, emails) from Wikipedia's
[Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Wikipedia-only
tells (wikitext, categories, DOIs, AfC templates, chatbot citation artifacts like `oaicite`/
`turn0search0`/`[cite: 1]`) are omitted here since they don't apply to human-facing prose — but if
you ever see those literal tokens in a draft, it was pasted straight from a chatbot.

## Table of contents
1. Content & tone tells
2. Language & grammar tells
3. Style & formatting tells
4. Assistant-voice leakage
5. Word-watch lists (by category)
6. AI-vocabulary eras (how the fingerprint shifts over time)
7. Signs of *human* writing (steer toward these)
8. Ineffective tells / false positives

---

## 1. Content & tone tells

**Undue emphasis on significance, legacy, broader trends.** The core AI move: inflating importance
instead of stating facts. *"marks a pivotal moment," "a testament to," "underscores its
significance," "reflects a broader shift," "cementing its legacy," "setting the stage for," "an
indelible mark," "deeply rooted."* Fix: replace the significance claim with the concrete fact it's
standing in for, or cut it. Watch for it even on mundane subjects (population figures, etymology) and
for over-connecting a subject to "broader debates."

**Superficial analysis via -ing tails.** A present-participle phrase glued to the end of a sentence
to editorialize: *"…, highlighting the collaborative nature of the work," "…, contributing to the
region's growth," "…, reflecting its enduring relevance."* Nearly always unsupported opinion. Cut.

**Promotional / advertisement tone.** Even when told to be neutral, AI drifts into brochure copy:
*"nestled in the heart of," "boasts a vibrant," "rich cultural heritage," "a diverse array,"
"groundbreaking," "renowned," "state-of-the-art," "seamless experience."* Especially bad on anything
framed as "heritage" or "culture." Let facts carry enthusiasm.

**Vague attribution / overgeneralized opinion.** *"Experts argue," "observers have noted," "industry
reports," "critics say," "studies show,"* "several sources" when there's one. Presenting one voice as
consensus. Fix: name the source or own the claim.

**Formulaic "challenges & future" conclusions.** *"Despite its [positive], X faces challenges…"*
ending on a vaguely upbeat note, or standalone "Challenges" / "Future Outlook" / "Future Prospects"
sections. It's the rigid template that's the tell, not the mention of difficulty.

**Definition-lead for non-terms.** Opening as if defining a phrase rather than discussing a thing:
*"Productivity hacks refers to…," "The list of best cafés is a curated compilation of…"* Just talk
about the subject.

**"X and Y" catch-all section headers**, especially "Awards and recognition" / "Legacy and impact" —
manifestations of the legacy fixation.

**Throat-clearing and faux-insight setups.** *"Here's the thing," "Let me be clear," "I'll be
honest," "The uncomfortable truth is," "What most people get wrong," "Here's what nobody tells you,"
"The part everyone misses."* Cut the setup; state the claim.

**Colon reveals.** Noun phrase, colon, dramatic reveal: *"The best part: it learns."* Rewrite as a
plain sentence. Colons are for lists, labels, quotes.

**Interpretive metadiscourse.** *"The key point is," "As you can see," "This distinction matters,"
"That last part matters more than it sounds," "It's worth noting,"* redundant *"In other words."*
Show, don't tell the reader what to think. Delete if the prose already shows it.

**Rhetorical setups.** *"What if I told you...", "Think about it:", "Plot twist:",* self-answered
"Question? Answer." pairs.

**Negative listing and dramatic fragmentation.** *"Not a X. Not a Y. A Z."* / *"X. And Y. And Z."* /
*"That's it. That's the whole thing."* Say Z in a complete sentence. One characteristic fragment is
voice; a stack is the tell.

**Fake-profound kickers.** A closing metaphor, aphorism, or mic-drop line. Delete it rather than
rewriting it into a better metaphor; end on the last concrete sentence or a plain next action.

**Weak verb phrases and inanimate agents.** *"made a decision"* → decided; *"has the ability to"* →
can; *"the decision emerged"* → who decided? Human subjects, active voice.

---

## 2. Language & grammar tells

**High density of AI vocabulary.** See §5–6. One word is coincidence; a *cluster* is the strongest
single tell, and they co-occur.

**Copula avoidance.** Replacing *is/are/has* with *serves as, stands as, functions as, operates as,
represents, marks, embodies* — and marketing verbs *features, offers, boasts, provides, delivers* in
place of *has*. A measured >10% drop in "is/are" in post-2023 text. Newer, subtler forms: *"ventured
into politics as a candidate"* for *"was a candidate,"* *"began his career as"* for *"was."* Fix: use
the plain copula. "X is a Y" is good prose.

**Negative parallelism** (the big one). Families:
- *"Not only X, but also Y"* / *"It's not just X, it's Y."*
- *"It's not X, it's Y"* / *"no X, no Y, just Z"* (flatly denies the first trait).
- Reversed, Grok-flavored: *"prioritizing X rather than Y."*
- Across sentences: *"He came from an esteemed family. His life, however, took a different path."*
Reads as debunking a misconception the reader never held. Say the positive claim once, plainly.

**Rule of three.** *"adjective, adjective, adjective"* or three short parallel clauses, used to make
thin analysis feel thorough. Cut to the one or two that carry real content; vary list length.

**Elegant variation.** Repetition-penalty-driven synonym-swapping: *app → platform → solution →
offering* across adjacent sentences. Repeat the plain noun instead. (Caveat: some non-native English
writers are *taught* to avoid repetition, so weight this lightly on its own.)

---

## 3. Style & formatting tells

- **Boldface overuse** — emphasizing a phrase in every bullet, "key takeaways" style. Inherited from
  READMEs, listicles, sales decks. Bold rarely.
- **Inline-header vertical lists** — `- **Thing:** description` repeated down a list. Fine
  occasionally; a wall of them is a tell.
- **Em dashes**, usually **spaced** ( — ), replacing commas/parens/colons for punched-up emphasis.
  A July 2026 study found Claude specifically overuses them vs. professional writers, so self-check.
  Rule: none in short copy; at most 1-2 in long drafts, only when one clearly beats a comma, period,
  or parentheses.
- **Bullets where prose reads better**, and headers over two-sentence sections.
- **Title Case On Every Heading** — use sentence case by default.
- **Emoji as formatting** — 🚀 ✨ 🎯 decorating headers/bullets. Drop unless the user's voice uses them.
- **Thematic-break lines** (`---`) between every section — Markdown-export habit.
- **Curly quotes / smart apostrophes** (“ ” ’) mixed inconsistently — a copy-paste-from-chatbot
  artifact. (Weak on its own: Word, macOS, and real typesetting also produce them.)

---

## 4. Assistant-voice leakage

Text that was meant as chat, not content, pasted in by accident — or generated in a helpful-assistant
register that never belongs in the user's published voice:

- **Collaborative filler:** *"Certainly!," "Of course!," "Great question!," "You're absolutely
  right!," "I hope this helps," "Let me know if…," "Would you like me to…," "Here's a
  breakdown/overview of…," "Let's dive in," "In this article, we will explore…"*
- **Knowledge-cutoff & hedge disclaimers:** *"As of my last update," "up to my knowledge cutoff,"
  "while specific details are limited/scarce," "not widely documented," "based on available
  information,"* and speculative *"they likely…," "maintains a low profile"* filler for unknown facts.
- **Didactic disclaimers (older models):** *"It's important to note that…," "It's worth
  remembering…," "may vary."*
- **Refusal fragments:** *"As an AI language model, I can't…," "I'm sorry, but…"*
- **Placeholder text left unfilled:** `[Insert X here]`, `[Your Name]`, `(Add your URL here)`,
  `2025-XX-XX` dates.

All of these get cut entirely.

---

## 5. Word-watch lists (by category)

Not bans — flags. Density and co-occurrence convict, not a lone instance.

**Significance / legacy:** stands as, serves as, is a testament, is a reminder, plays a crucial/
pivotal/vital/key role, underscores/highlights its importance, reflects broader, symbolizing its
enduring/lasting, contributing to, setting the stage for, marking a shift, a key turning point,
evolving landscape, focal point, indelible mark, deeply rooted, rich history/heritage.

**Superficial-analysis verbs (esp. as -ing tails):** highlighting, underscoring, emphasizing,
ensuring, reflecting, symbolizing, contributing to, fostering, cultivating, encompassing, enhancing,
showcasing; "valuable insights," "align/resonate with."

**Promotional / peacock:** boasts, vibrant, rich, profound, seamless, groundbreaking, renowned,
nestled, in the heart of, natural beauty, diverse array, state-of-the-art, cutting-edge, exemplifies,
commitment to, featuring.

**Vague attribution:** industry reports, observers have cited, experts argue, some critics argue,
several sources/publications (with few cited), studies show, "such as" before an exhaustive list.

**Copula dodges:** serves/stands/functions/operates as, represents, marks, embodies; boasts/features/
maintains/offers/provides/delivers; "refers to" as a lead.

**Connectors overused:** Additionally, Moreover, Furthermore, Notably, Consequently — especially
starting sentences.

**Generic intensifier-nouns:** landscape, realm, tapestry, sphere, world, ecosystem, journey — used
metaphorically.

**Conclusion flags:** In conclusion, In summary, Overall, Ultimately, Despite these challenges, Future
Outlook, a final paragraph that restates the piece.

**Hype / transformation:** cutting-edge, paradigm shift, game changer, this is huge, this changes
everything, transformative, supercharge, ever-evolving, beacon, multifaceted, paramount, empower,
streamline, facilitate, embark.

**Empty adverbs (cut by default):** just, literally, honestly, simply, actually, truly, fundamentally,
importantly, crucially, inherently, inevitably, very.

**Empty phrases (cut by default):** it's worth noting, it's important to note, at the end of the day,
when it comes to, at its core, in today's world, in the age of, in the world of, the reality is, the
truth is, in terms of, with regard to, in order to, the fact that, going forward, in this article,
let's dive in.

---

## 6. AI-vocabulary eras

The fingerprint shifts as models change — useful for dating a draft and for knowing what reads as
"current" AI:

- **2023–mid-2024 (GPT-4):** delve, tapestry, testament, boasts, bolstered, intricate, interplay,
  meticulous, vibrant, pivotal, underscore, garner, "Additionally." ("Delve" peaked here, then fell.)
- **Mid-2024–mid-2025 (GPT-4o):** align with, enhance, fostering, showcasing, highlighting, crucial,
  enduring, pivotal, underscore, vibrant.
- **Mid-2025+ (GPT-5 era):** emphasizing, enhance, highlighting, showcasing — plus heavier "canned
  notability" phrasing ("independent coverage," "active social media presence").
- **Grok** is idiosyncratic: over-uses pseudo-scientific *causal, empirical, correlate*, and keeps
  over-using *underscore*.

Takeaway: don't just memorize one list — the *pattern* (inflated, generic, packing flagged words) is
stable even as the specific words rotate.

---

## 7. Signs of human writing (steer toward these)

Empirically *underproduced* by AI, so they read as authentically human:

- Simple **is/has** constructions: "there is a," "it has a."
- **Plain synonyms** over stiff ones: wrote (not authored), moved (not relocated), used (not
  utilized), tried (not attempted), died (not passed away), about (not regarding/pertaining to).
- **Definite / superlative commitments:** "one of the best," "the first," "the only," "I think this
  is wrong." AI hedges; people commit.
- **Real hedges that carry uncertainty:** "I think," "maybe," "perhaps," "kind of." Keep these when
  they express actual doubt or the writer's spoken rhythm. (The empty adverbs and phrases in §5 are
  a different thing: cut those by default.)
- **Concrete specifics:** numbers, names, dates, mechanisms, one real anecdote.
- **Uneven sentence rhythm** — long then short then fragment. AI is metronomic.
- The user's own idiom. If you have their prior writing, match it above any generic rule here.

---

## 8. Ineffective tells / false positives

Don't accuse (or over-edit) on these alone:

- **Perfect grammar** — lots of humans write cleanly.
- **A single flagged word** — literal uses exist (underscore = a mark, landscape = terrain, robust =
  statistical, "delve" in a real mining piece).
- **Formal / academic / "fancy" prose** — register ≠ authorship. Formal can still be specific and human.
- **One em-dash**, or **curly quotes** — Word/macOS/Chicago style produce these too.
- **Mixed casual + formal register** — often just a real person, or several editors.
- **"Bland" prose** — blandness isn't the same fingerprint as the specific tells above.

Bottom line: it's *clusters* and *co-occurrence* that identify AI text, and the fix is always the
same: trade inflation for specificity, and match the user's real voice.

Sources: Wikipedia's *Signs of AI writing*; Peter Yang's *no-ai-slop* skill
(github.com/petergyang/no-ai-slop).
