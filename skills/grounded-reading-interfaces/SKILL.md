---
name: grounded-reading-interfaces
description: Build HTML "learning artifacts" — pages engineered to hold attention and maximize retention when someone reads and tries to learn dense material onscreen. Encodes research-grounded rules for typography, scanning behavior, cognitive load (Mayer), and active-recall/retention interactions, each traced to its source. Use whenever the user asks to turn a book, paper, article, transcript, research report, course, or "knowledge base" into an HTML page, reader, explainer, primer, study guide, or artifact — or asks for a "well-designed", "readable", "easy to digest", "focused", or "made to actually learn from" version of dense content, even if they don't name design rules. Do NOT use for dashboards, data-viz-primary artifacts, marketing/landing pages, or short single-fact answers with no real reading.
---

# Grounded Reading Interfaces

## What this skill is for

**Build HTML pages that survive how people actually read onscreen — which is badly.** Most "make it look nice" instincts are aesthetic guesses. This skill encodes a small set of rules that trace to real studies in typography, eye-tracking UX, and cognitive/learning psychology. Each rule names its source, so you and the user can tell "empirically grounded" from "stylistic choice."

**The core problem you are fighting is not ugliness — it is shallow processing.** Three converging findings define the enemy:
- Users **scan, they don't read**: ~79% scan any new page; a reader consumes only **20–28% of the words** on a first pass (NN/g, Morkes & Nielsen 1997).
- Screens produce a small-but-real **comprehension penalty** vs paper (g ≈ −0.21), concentrated in exactly the profile of a learning artifact: **long, expository, scrolling text** (Delgado et al. 2018; Kong et al. 2018).
- The penalty is **metacognitive, not visual**: onscreen readers feel they understood (overconfidence) while performing worse, because smooth rereading creates a **fluency illusion** (Ackerman & Goldsmith 2011; Bjork).

So a great learning artifact does two jobs, in this priority order: **(1) make the text effortless to read and scan** (typography + structure), then **(2) force small effortful acts of retrieval and generation** that break the fluency illusion (active learning). The draft version of this skill only did job 1. Job 2 is the higher-leverage half — do not skip it.

**Be honest about grounding.** These studies were done on general reading, web scanning, and (often narrated) multimedia learning — not on AI-generated HTML artifacts. Applying them here is a literature-informed analogy, not a validated claim that this format was tested. If asked, say so plainly.

## Before you build: process the content, don't just paste it

The rules only pay off if the content is already well-organized. Before writing any HTML, extract:
1. **The single most important takeaway** (goes top AND bottom — primacy/recency).
2. **3–6 natural sections**, each reducible to one topic sentence.
3. **Which visuals are load-bearing** (convey information) vs decorative (cut them — Coherence).
4. **The 5–15 facts/claims worth retaining** — these become retrieval prompts, not just prose.
5. **Reader level**: novice or expert? This flips several rules (see Expertise Reversal below).

Cut the draft to ~50% of its word count. Concise + scannable + objective writing drove a **124% usability gain** in controlled testing (Morkes & Nielsen). Every sentence must survive being skipped.

---

## Pillar 1 — Typography: make reading effortless

Full copy-paste stylesheet in `references/reading-column.css`. The numbers:

| Lever | Rule | CSS | Source |
|---|---|---|---|
| **Line length** | 50–75 chars/line (~66 ideal); never >80 | `max-width: 65ch` on the prose column | Nanavati & Bias 2005 (Visible Language); Baymard; WCAG 1.4.8 |
| **Font size** | ≥16px body (18px for long-form); use `rem` not `px` | `font-size: 1.0625rem` | Industry consensus / WCAG 1.4.4 |
| **Line height** | 1.5–1.6 body; more (1.6–1.8) as lines widen | `line-height: 1.6` (unitless) | WCAG 1.4.8; Butterick |
| **Paragraph spacing** | ≥1.5× line spacing; margin on one side only | `p { margin: 0 0 1.5em }` | WCAG 1.4.8 |
| **Contrast** | ≥4.5:1 (AA); but avoid pure #000-on-#fff | `#1a1a1a` on `#fbfbf9` | WCAG 1.4.3; comfort refinement |
| **Dark mode** | Never #fff on #000 (halation) | `#e0e0e0` on `#121212` | Halation/astigmatism evidence |
| **Alignment** | Left / ragged-right — never justified on web | `text-align: left` | WCAG 1.4.8 (no browser hyphenation engine) |
| **Weight** | 400 body; never <400 for reading text | `font-weight: 400` | Rendering/anti-alias legibility |
| **Serif vs sans** | Either works if well-rendered on modern displays | pick per rendering, not category | Meta-analyses: no general winner |

**Use `ch` for the column width, not `px`** — `ch` scales with font size, so the character-count stays correct when text zooms. This is the single most robust typographic choice you can make.

**Common violations:** full-bleed text on wide monitors (100–150+ chars/line — the #1 mistake), light-gray body text (#999 fails AA), `font-weight: 300` "modern" body copy, justified text without hyphenation ("rivers of white").

---

## Pillar 2 — Structure for scanning: design for layer-cake, not F

Users default to an **F-shaped scan** (top sweep, shorter second sweep, then a vertical run down the left edge) **only when text is an unformatted wall** — the F-pattern is a *failure mode*, not a target. Good formatting replaces it with the **layer-cake pattern** (eyes hop cleanly across bold subheadings), which NN/g calls "by far the most effective way to scan."

**Build the whole skeleton for layer-cake:**
- **Never let body copy run >3–4 lines without a structural break** — heading, bullet, bold lead-in, or callout.
- **Front-load everything.** Heading = the conclusion, not a teaser ("Retry with exponential backoff" not "A note on retries"). First sentence of every paragraph = its point. First 2–3 words of every bullet/sentence = the information-carrying keyword, never filler ("There are…", "It is important…").
- **Every section is independently scannable** — a reader who jumps to section 4 gets the gist without 1–3.
- **TL;DR block in the first screenful.** ~57% of viewing time is above the fold; 74% in the first two screenfuls. Get a bulleted "Key takeaways" box in within ~600–800px — before any decorative hero.
- **Chunk into ~3–5 ideas per section** (Cowan's ~4-item working-memory limit — *not* the fabricated "8-second attention span," which is a debunked marketing myth; don't cite it).
- **Auto-generate a table of contents** from `<h2>/<h3>` for anything past 2–3 screens — that's what the vertical scan hunts for.

**Bold ≤30% of any paragraph, only the exact load-bearing phrase.** Over-bolding self-cancels ("if everything is emphasized, nothing is").

**Callouts must not look like ads** — banner blindness makes readers unconsciously skip bright boxes in the periphery or right rail. Keep callouts inline, subtly tinted, never carousel/auto-rotating.

---

## Pillar 3 — Manage cognitive load (Mayer's multimedia learning)

Full principle-by-principle table with effect sizes in `references/evidence-base.md`. The principles that **transfer strongly to a silent HTML page**, by leverage:

- **Coherence (d≈0.70)** — cut everything that doesn't carry information. No decorative icons, stock photos, gradients, ambient animation, "seductive detail." On a text-dense page, every non-functional pixel taxes the visual channel. *Highest-leverage principle for this medium.*
- **Spatial contiguity (d≈0.79)** — keep text next to what it refers to. Labels ON the diagram, not in a legend below; code output directly under the code; a caption adjacent to its figure. Never make the reader hold something in working memory while scrolling to hunt its referent.
- **Signaling (d≈0.46)** — bold/headers/callouts mark *structure and key claims*, not decoration. Arrows and numbered pins pointing at diagram parts count too (the static analog of Mayer's Embodiment).
- **Multimedia (d≈1.5+)** — pair non-trivial concepts with a diagram/annotated screenshot/table *when the visual genuinely adds what words can't*. Don't add an image just because "there should be one" (that's pure Coherence cost).
- **Segmenting** — break long content into learner-paced chunks (`<details>`, tabs, numbered stages). If a section takes >~90s to read, find a split.
- **Pre-training** — front-load a short glossary/legend of key terms before a dense diagram or walkthrough (skip for experts — see below).
- **Personalization (d≈0.79)** — write in conversational register ("you'll notice…", "here's why this matters"), not formal passive voice. Register, *not* filler ("Hey friend, let's dive in!").

**Do NOT cargo-cult these — they don't apply to a silent page:**
- **Modality & Voice** assume a *narration* channel. There's no audio on a silent page, so "add narration" advice is structurally inapplicable. All your text is visual and competes with your images for one channel — which is *why* Coherence matters more here, not less.
- **Redundancy** (classically: don't duplicate audio + captions) → translates to: don't write a caption that just re-states what the diagram's own labels already show.
- **Temporal contiguity** → only matters if you use scroll/step reveals; then sync the text and the visual change to the same trigger. On a plain page it collapses into Spatial contiguity.
- **Immersion / 3D** — reserve WebGL/heavy interactivity for genuinely *spatial* content (a molecule, an architecture). For propositional content it adds extraneous load for no gain.

**Three loads, one mantra:** minimize *extraneous* (kill clutter, enforce proximity), manage *intrinsic* (sequence via segmenting/pre-training), spend the freed capacity on *germane* (the active-learning interactions in Pillar 4).

---

## Pillar 4 — Force active processing (the half the draft was missing)

This is where retention is won. A beautiful, readable page still loses to the fluency illusion unless it makes the reader *do* something effortful. Copy-paste widgets in `references/learning-widgets.html`.

- **Retrieval practice — strongest evidence (g≈0.61; rated "high utility" by Dunlosky et al. 2013).** After every conceptual chunk, add a hide-answer prompt phrased as a *question*, so the reader attempts recall before revealing:
  ```html
  <details><summary>Q: Why does exponential backoff beat a fixed retry delay?</summary>
    <p>Because it spreads retries out as failures persist, preventing a thundering-herd…</p>
  </details>
  ```
  Native `<details>` = zero JS, keyboard/screen-reader accessible. Prefer a question in the `<summary>` over a statement.
- **Generation & self-explanation (g≈0.40–0.56).** Instead of stating a fact, prompt the reader to produce it first: fill-in-the-blank, "predict what happens if X, then reveal," or a standing "Why is this true? (explain before revealing)" `<details>`. Always pair with a model answer for self-comparison — a page can prompt generation but can't grade it.
- **Fight the fluency illusion (desirable difficulties; Bjork).** *Resist frictionless design.* Don't pre-highlight everything so the eye glides fluently; force a small click-to-reveal at exactly the points where the reader thinks "I've got this." Avoid glossy "review complete!" summary boxes right after new content — they *manufacture* false confidence. Calibrate: friction at chunk boundaries and key claims, not every sentence (over-gating causes abandonment).
- **Worked examples + fade (expertise reversal).** For procedural content: full worked example → partially-faded "try it" → unscaffolded practice. Let advanced readers collapse the scaffolding.
- **Primacy/recency.** Put the top takeaway both at the top (TL;DR) and restated at the bottom (recap) — deliberately, because the middle is least remembered.
- **Spacing — be honest about the ceiling.** True spaced repetition (the other "high utility" technique) needs the reader to *return over days*, which one static page cannot enforce. It CAN nudge: a `localStorage` "you last reviewed this N days ago — quick self-test?" banner on revisit, an **"export to Anki/flashcards" button** that turns the `<details>` Q&A into importable cards (hands spacing to purpose-built software), and a printed cadence suggestion (day 1/3/7/21). Say which you did and don't over-claim.

**Match intensity to the material.** The screen penalty and these heavy techniques target *dense, technical, expository* content. Don't bolt retrieval quizzes onto narrative or low-stakes reading — reserve them for material genuinely worth retaining.

---

## Pillar 5 — Kill distraction, sustain focus

The attention enemy after clutter is **motion**. Peripheral vision is evolutionarily tuned to movement — any animation near text involuntarily captures attention and is hard to disengage; a 32-study meta-analysis found background motion measurably degrades comprehension.

- **No autoplay video/GIF/looping/ambient animation anywhere near reading content.** Zero exceptions. Highest-leverage focus rule.
- **Animation only for functional feedback** — a `<details>` opening, a state change — never decorative. Keep transitions ~150–300ms.
- **Always honor `prefers-reduced-motion`** and offer nothing that moves on its own.
- **Reading-progress bar** (thin fixed top bar) for long artifacts — knowing "how much is left" reduces perceived cost and sustains reading (information-foraging).
- **Sticky headers**: minimize height, opaque background, don't animate on every scroll.
- **One continuous document.** Don't split a coherent argument across pages/tabs the reader must click through; don't require horizontal scrolling. This directly compensates for the screen comprehension gap by removing navigation friction.

---

## Pillar 6 — Visual craft: beautiful without breaking Coherence

**"Cut decoration" (Coherence) is not "make it plain."** The other five pillars guarantee a page is *legible and learnable*; they do not make it *beautiful*, and a page can nail every reading rule while still looking like an unstyled boilerplate default. Ugliness is itself a cost: it reads as low-effort, erodes trust in the content, and subtly discourages sustained attention. Beauty here comes from **craft and restraint** — refined typography, a coherent color system, spacing rhythm, and precise detailing — none of which add ornament. Every rule below still serves reading.

**Honesty flag:** unlike Pillars 1–4, this pillar is **craft and taste, not research-grounded**. Treat it as a strong default aesthetic, not an empirical claim. It stays subordinate to Coherence: if a flourish doesn't serve reading, cut it.

**Design with tokens, never ad-hoc values.** Define CSS custom properties for the whole system and reuse them — a page whose colors, spacing, and radii are all derived from a small token set looks *designed*; one with sprinkled one-off hex codes and pixel values looks improvised. Ship: a color ramp, a spacing scale, one radius scale, one shadow, a type scale.

- **Color — a real system, not "system-blue on gray."** The single biggest driver of the "boilerplate" look is (a) pure `#000`/`#fff`, (b) the default browser-blue accent, and (c) flat mid-gray boxes. Instead:
  - **Warm or cool your neutrals deliberately.** A warm off-white paper (`#faf8f4`) with a warm near-black ink (`#232025`) already looks more considered than `#fff`/`#000`. Pick one temperature and hold it across bg, surface, border, and text.
  - **One accent, used sparingly, as signal.** Prefer a *deeper, slightly desaturated* accent (e.g. deep indigo `#3730a3`) over a bright saturated one — it pairs better with warm paper and doesn't shout. Use it for links, rules, small labels, and the *one* thing per section that matters — not for filling boxes.
  - **Derive tints, don't invent them.** Surface and callout backgrounds should be low-chroma tints of the neutral or accent, not random grays. Keep contrast within WCAG (Pillar 1) — beauty never overrides the 4.5:1 floor.
- **Typography — pick a quality pairing (system fonts only for Artifacts).** The Artifact CSP blocks web fonts, so choose *good OS-shipped* faces, not `Georgia`/`Times` by reflex. Excellent screen serifs already on Apple/Windows: `Charter`, `"Sitka Text"`, `Cambria`, `"Iowan Old Style"`, `"Palatino"`. For sans: the system stack (`ui-sans-serif, -apple-system, "Segoe UI", Roboto`). An editorial pairing (quality serif body + serif or sans display headings) beats the default serif-body/Helvetica-heading combo. Add craft details: `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs, and `font-variant-numeric: tabular-nums` on any stats/tables so figures align.
- **A modular type scale with real contrast.** Timid scales (h1 barely bigger than body) look flat. Use a clear ratio (~1.25–1.4): e.g. body 1.0625rem → h3 1.25 → h2 1.75 → h1 2.5rem. Tighten letter-spacing slightly on large display headings (`-0.02em`).
- **Spacing on one rhythm.** Base everything on a single scale (a 0.5rem / 8px step). Generous, *consistent* whitespace is the cheapest way to look premium — and it reinforces Pillar 3 segmenting. Vary space to signal structure (big gap before an `h2`, tight gap after it to its first line).
- **One radius, one shadow, hairline borders.** Consistency reads as intent. Pick a radius scale (e.g. 8px controls, 12px cards) and *one* very soft shadow token for the rare element that should lift (the TL;DR). Prefer hairline 1px borders in a tinted neutral over heavy dark rules. Don't mix five border weights.
- **Detailing is where "designed" lives.** Small, cheap moves with outsized payoff: an eyebrow label (letterspaced, uppercase, accent, small) above a title; a styled section numeral instead of "1." inline; an accent hairline under the masthead; `:focus-visible` rings that match the accent; considered hover states on links/buttons; differentiated callout treatments (key vs warning) by color, not just a label. **Give distinct components distinct surfaces** — don't paint the TL;DR, every callout, every diagram, and every table the same flat gray; that monotony is what read as "ugly."
- **Both themes, deliberately.** Design the dark theme as its own object (warm-tinted dark `#1a1713`, not `#000`; softened accent), not a mechanical inversion. Honor `prefers-color-scheme` and the viewer's toggle.

**The failure mode to recognize:** default serif body + Helvetica headings + one saturated system-blue + every box the same flat gray + uniform 1px borders + timid type scale. That's "technically follows the reading rules but looks like a 2005 print stylesheet." The fix is never ornament — it's a coherent token system and precise detailing.

Ready-made token themes in `references/aesthetic-themes.css` (Editorial-warm, Technical-cool, Notebook) — drop one in and the structural CSS inherits it.

---

## Expertise reversal: the toggle that flips half these rules

Scaffolding that **helps novices actively hurts experts** (Kalyuga). For high-knowledge readers, integrated labels, pre-training glossaries, and heavy signaling become redundant clutter they must suppress — diagram-alone can *beat* diagram-plus-text for them.

- **Novice-facing artifact:** maximal signaling, pre-training glossary, integrated labels, worked examples, guided prompts.
- **Expert-facing reference:** strip labels, let diagrams stand alone, collapse explanatory scaffolding by default.
- **Progressive disclosure resolves the conflict cleanly** — put scaffolding inside `<details>` so the expert clicks past it and the novice expands it. Ask the user which audience if it's not obvious.

---

## What one static HTML page genuinely cannot do

State these limits honestly rather than implying the page "makes you learn":
- **CAN:** prompt single-pass retrieval, prompt generation/self-explanation, scaffold worked examples, chunk and front/end-load by primacy-recency, integrate dual-coded visuals, avoid fluency-illusion traps, nudge review via `localStorage`, export to Anki.
- **CANNOT (without extra infrastructure):** enforce true multi-day spaced repetition, interleave across sessions, adapt to the reader's *measured* expertise (only self-selected proxies), or grade/evaluate self-explanations (only self-comparison).

---

## Pre-ship checklist

**Read (Pillar 1–2):**
1. Prose column has `max-width` in `ch` (60–75), body ≥16px, line-height ≥1.5, left-aligned, near-black on off-white.
2. Every heading/paragraph/bullet is front-loaded with its keyword/conclusion.
3. No body copy runs >3–4 lines without a structural break; sections independently scannable.
4. TL;DR bulleted box in the first screenful, before any hero.
5. Bold ≤30%, load-bearing phrases only. Callouts inline, not ad-like.

**Load (Pillar 3):**
6. Zero decorative visuals near the reading column (Coherence).
7. Every figure/label/caption sits adjacent to what it explains (Spatial contiguity).
8. No section takes >~90s to read without a segment break.
9. No "add narration/modality" cargo-culting on a silent page.

**Learn (Pillar 4–5):**
10. Retrieval prompt (question-form `<details>`) after each key chunk — **not optional for dense material.**
11. At least one generation/self-explanation prompt with a model answer.
12. No fluency-illusion "review complete" false-confidence boxes.
13. Top takeaway appears at top AND bottom.
14. Zero autoplay/ambient motion; `prefers-reduced-motion` honored.
15. Reads as one continuous document — no needless pagination/click-throughs.
16. Reader level chosen (novice scaffolds vs expert-stripped); scaffolding in `<details>` if mixed.
17. If you claim "spaced review," you actually shipped a `localStorage` nudge or Anki export — no empty claims.

**Craft (Pillar 6):**
18. Colors/spacing/radii/type come from a **token set**, not ad-hoc values; neutrals are deliberately warm or cool (no pure `#000`/`#fff`), accent is deep-not-bright and used sparingly.
19. Quality OS-shipped font pairing (not reflexive `Georgia`+Helvetica); type scale has real contrast; stats/tables use `tabular-nums`.
20. Distinct components have **distinct surfaces** (TL;DR ≠ callout ≠ table ≠ diagram); hairline borders, one radius scale, one soft shadow; masthead has an eyebrow/rule/meta treatment.
21. Dark theme designed as its own object, not an inversion. Does it look *designed*, or like a boilerplate default? If the latter, fix the tokens — never by adding ornament.

---

## Reference files

- **`references/reading-column.css`** — full copy-paste stylesheet: reading column, type scale, light/dark themes, callouts, figure-with-context, TOC, `prefers-reduced-motion` guard. Adapt colors/fonts to the artifact's theme; keep the structural choices (ch-width, spacing rhythm, contrast).
- **`references/learning-widgets.html`** — copy-paste Pillar-4/5 patterns: retrieval `<details>`, self-explanation prompt, section quiz, reading-progress bar, auto-TOC, `localStorage` review nudge, and an "export to Anki" button. All zero- or minimal-JS, accessible.
- **`references/evidence-base.md`** — the sourced evidence: every rule's study, effect size, evidence strength, and honest caveats — plus a "debunked, do not cite" list (goldfish/8-second attention span, unsourced "reduces eye strain 30%" stats). Read this when the user challenges a rule or wants citations.
- **`references/aesthetic-themes.css`** — three ready-made Pillar-6 token themes (Editorial-warm, Technical-cool, Notebook): color ramp, spacing scale, radius/shadow, and a system-font pairing per theme, all as CSS variables. Drop one `:root` block in and the structural CSS in `reading-column.css` inherits it. This is the fastest path from "readable but plain" to "looks designed."
