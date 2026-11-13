# Evidence base

The sourced grounding behind every rule in this skill: the study, the effect size, how strong the evidence is, and honest caveats. Read this when the user challenges a rule, wants citations, or asks "is this actually real?"

**Scope honesty (say this if asked):** these studies were run on general reading, web-content scanning, and (frequently narrated) multimedia learning — *not* on AI-generated HTML artifacts. Applying them to this format is a literature-informed analogy, not a validated claim that this exact format was tested. Effect sizes (Cohen's *d* / Hedges' *g*) are directional strength indicators, not precise universals; many come from lab studies with student subjects.

---

## Pillar 1 — Typography

| Rule | Finding | Evidence strength | Source |
|---|---|---|---|
| Line length 50–75 cpl (~66), never >80 | Both too-long and too-short lines disrupt eye-movement, hurting speed/comprehension | **High** — literature review of controlled reading studies (but itself synthesizes print-era work; screen-specific RCTs sparse) | Nanavati & Bias 2005, *Visible Language* 39(2); Baymard; WCAG 1.4.8 (80-char ceiling) |
| Body ≥16px (18px long-form), use `rem` | 16px = calibrated to visual acuity at typical viewing distance | Convention, well-corroborated (not one RCT) | Industry consensus; WCAG 1.4.4 (resize to 200%) |
| Line height 1.5–1.6, unitless | ≥1.5 within paragraphs | Standard (testable) + convention | WCAG 1.4.8; Butterick |
| Paragraph spacing ≥1.5× line spacing | Precise, testable multiplier | **Standard** | WCAG 1.4.8 |
| Contrast ≥4.5:1 (AA), 7:1 (AAA); avoid pure #000/#fff | 4.5:1 calibrated to ~20/40 vision; max contrast self-reported as glare over long reads | Standard (floor) + practitioner comfort refinement | WCAG 1.4.3/1.4.6 |
| Dark mode: off-white on dark-gray, not #fff/#000 | "Halation" — bright text on pure black glows/bleeds, worse with astigmatism (~47% of people) | Documented phenomenon, multi-source; not one large RCT | Halation/polarity literature |
| Left-aligned, never justified on web | Browsers lack print-grade hyphenation → "rivers of white" | **Standard** is the decisive reason; comprehension studies are mixed | WCAG 1.4.8 |
| Weight ≥400 for reading text | Light weights thin under anti-aliasing, undercutting effective contrast even when ratio passes | Practitioner/accessibility consensus | Penn State A11y; A11Y Collective |
| Letter- + word-spacing move together | Increasing letter-spacing *without* word-spacing slows reading | **Controlled study** | PMC dyslexia spacing study; WCAG 1.4.12 |
| Serif vs sans: no general winner | Most studies show no legibility/comprehension difference on modern displays; sans better for low-vision specifically | **Meta-analysis level** | Multiple reviews |

---

## Pillar 2 — Scanning & structure (NN/g eye-tracking corpus)

| Rule | Finding / number | Strength | Source |
|---|---|---|---|
| Design for scanning, not reading | 79% scan; only 16% read word-for-word; reader consumes ~20–28% of words per pass | **Strong** — large field study | NN/g "How Users Read"; "How Little Do Users Read" |
| Concise + scannable + objective | −50% words, +formatting, +objective tone = **124% usability gain** (159% in a follow-up) | **Strong** — controlled experiment | Morkes & Nielsen 1997 |
| Layer-cake > F-pattern | F-pattern appears with *unformatted walls* + low commitment; it's a failure mode. Bold, distinct subheadings produce layer-cake scanning — "by far the most effective" | **Strong** — eye-tracking | NN/g F-pattern (2006) & Layer-Cake |
| Front-load headings/sentences/bullets | Headline = conclusion; first sentence = point; first 2 words = keyword | Strong (eye-tracking + consensus) | NN/g Inverted Pyramid; Morkes & Nielsen |
| TL;DR in first screenful | ~57% of viewing time above fold; 74% in first two screenfuls | **Strong** | NN/g Scrolling and Attention |
| Chunk into ~3–5 ideas | Focus-of-attention capacity ≈ 4 chunks (contested 3–5) | **Strong** (Cowan reconsideration of Miller's rhetorical 7±2) | Cowan 2001, *BBS* 24 |
| Bold ≤30%, key phrases only | Over-emphasis self-cancels | Practitioner consensus | NN/g Formatting Long-Form |
| Callouts must not look ad-like | Banner blindness — users skip ad-shaped/peripheral boxes regardless of content | **Strong, 3 decades** | NN/g Banner Blindness |
| Progressive disclosure, ≤2 levels | 3+ disclosure levels degrade usability | Strong | NN/g Progressive Disclosure |

---

## Pillar 3 — Cognitive load (Mayer's CTML)

Theory rests on: dual-channel, limited capacity, transient storage, active processing (select→organize→integrate). **Key caveat for a silent page:** the dual-channel assumption is *auditory vs visual* — on a silent HTML page, text AND images both hit the visual channel and compete. That's why several principles need translation.

Effect sizes are commonly-cited figures from Mayer/Clark's syntheses (mostly narrated-animation lab studies) — directional, not gospel.

| # | Principle | Static-HTML status | Effect | Source |
|---|---|---|---|---|
| 1 | **Coherence** — cut extraneous words/images/sounds | Full ✅ (highest leverage here) | d≈0.70 | Mayer; 2025 meta-analysis flags "remove seductive detail" among largest effects |
| 2 | **Signaling** — cue essential material + structure | Full ✅ | d≈0.46 | Mayer |
| 3 | **Redundancy** — don't duplicate identical words across channels | Reinterpreted ⚠️ → don't caption a diagram with what its own labels already say | d≈0.87 (narration studies) | Mayer |
| 4 | **Spatial contiguity** — text near its referent | Full ✅ (translates literally to layout) | d≈0.79 | Mayer |
| 5 | **Temporal contiguity** — words + visuals simultaneous | Reinterpreted ⚠️ → only for scroll/step reveals; else collapses into spatial | d≈1.30 (narration) | Mayer |
| 6 | **Segmenting** — learner-paced chunks | Full ✅ | ~d≈0.9 | Mayer |
| 7 | **Pre-training** — teach key terms first | Full ✅ (skip for experts) | d≈0.75+ | Mayer |
| 8 | **Modality** — words as narration frees visual channel | **Does NOT apply ❌** (no audio channel) — don't cargo-cult "add narration" | strong in source | Mayer |
| 9 | **Multimedia** — words + pictures > words alone | Full ✅ (foundational; only when visual carries real info) | d≈1.5+ | Mayer/Clark |
| 10 | **Personalization** — conversational register | Full ✅ | d≈0.79 | Mayer |
| 11 | **Voice** — human > synthetic narration | **Does NOT apply ❌** (no audio) | moderate | Mayer |
| 12 | **Image** — talking-head face doesn't reliably help | Partial → caution: decorative author photo mid-content = wasted Coherence | weak/null | Mayer |
| 13 | **Embodiment** — informative gesture directs attention | Partial → converges with Signaling: arrows, numbered pins | medium | Kalyuga/Cambridge Handbook |
| 14 | **Immersion** — 3D/VR not automatically better | Caution, not a build directive — reserve 3D for spatial content | mixed/null | Mayer |
| 15 | **Generative activity** — self-explain/test/draw | Full ✅ (see Pillar 4) | among largest | 2025 meta-analysis |
| 16 | **Guided discovery** — exploration + hints/feedback | Interactive widgets only; guided > unguided | strong | Mayer |

**Three loads → levers:** extraneous (kill clutter, proximity), intrinsic (segment, pre-train), germane (generative activities). Mantra: minimize extraneous, manage intrinsic, spend freed capacity on germane.

**Expertise reversal (Kalyuga):** scaffolds that help novices *hurt* experts — for high-knowledge readers, integrated text+diagram can underperform diagram-alone because the text becomes redundant load. → Novice mode = max scaffolding; expert mode = stripped. Progressive disclosure (`<details>`) resolves it.

---

## Pillar 4 — Screen penalty & retention

### The screen-vs-paper gap
| Study | Finding | Strength |
|---|---|---|
| **Kong, Seo & Zhai 2018**, *Computers & Education* 123 (the linked paper) | Meta-analysis, 17 studies: comprehension better on paper (≈ g −0.21); no reading-speed difference; moderators n.s. (underpowered) | Peer-reviewed, modest k |
| **Delgado et al. 2018**, *Educational Research Review* (171,055 participants, 54 studies) | **g = −0.21** paper > screen; penalty **larger under time pressure**, **for expository (not narrative) text**, and **growing over time** | Best-powered — lean on this for moderators |
| **Singer & Alexander 2017** | Medium doesn't matter for gist; print wins for deep/inferential comprehension; penalty grows with length + scrolling | Systematic review |
| **Ackerman & Goldsmith 2011**, *JEP:Applied* | Gap is **metacognitive** — screen readers are *overconfident* and under-regulate study time | Controlled — the "why" |
| Mangen et al. 2013 | Randomized: print group scored higher on expository comprehension | Clean causal study |
| Media Psychology 2022 | **No** screen penalty for narrative text | Meta-analysis (scope limiter) |

**Correct scope statement:** the penalty is real, small-to-moderate (g≈−0.20 to −0.25), and concentrated in **long, expository, scrolling, time-pressured or self-paced** reading — exactly a dense learning artifact. The fix is interaction (force pacing + retrieval), not typography alone.

### Learning techniques (Dunlosky et al. 2013 utility ratings)
| Technique | Effect | Utility | Source |
|---|---|---|---|
| **Retrieval practice** | g≈0.61 | **HIGH** | Roediger & Karpicke 2006; Adesope et al. 2017 |
| **Spaced/distributed practice** | robust across 317 experiments | **HIGH** (but a static page can only *nudge*, not enforce) | Cepeda et al. 2006 |
| **Self-explanation** | g≈0.55 | Moderate | Bisra et al. 2018 |
| **Elaborative interrogation** ("why?") | g≈0.56 | Moderate | Dunlosky et al. |
| **Generation effect** | d≈0.40 | Moderate | Slamecka & Graf 1978; Bertsch et al. |
| **Interleaving** | up to 2× next-day scores, but fragile/implementation-dependent | Moderate | Rohrer & Taylor 2007 |
| **Dual coding / multimedia** | median gain ~89%, d>1; spatial contiguity alone d≈0.72 | Strong | Clark & Mayer 2016 |
| **Worked examples + fade** | strong for novices; reverses with expertise | Strong (CLT) | Sweller/Kalyuga |
| **Desirable difficulties / anti-fluency** | retrieval/spacing/variation feel harder but retain better; combats fluency illusion | High (framework) | Bjork & Bjork; Kornell & Bjork 2007 |
| **Summarization** | inconsistent without training | **LOW** — convert to "write your own before revealing" | Dunlosky et al. |
| **Rereading / highlighting** | small, non-generalizing — yet 76% of students rely on them | **LOW** — the fluency-illusion trap | Kornell & Bjork 2007 |
| **Concept maps** | small-to-large; **construction > viewing** | Better than free summary | Nesbit & Adesope 2006 |
| Primacy/recency | first + last items best recalled | Classical, high internal validity; directional for prose | Murdock 1962 |

**Honest ceiling of one static page** — CAN: prompt single-pass retrieval, prompt generation, scaffold worked examples, front/end-load, dual-code visuals, nudge via localStorage, export to Anki. CANNOT: enforce multi-day spacing, interleave across sessions, adapt to measured expertise, or grade self-explanations.

---

## Pillar 5 — Focus & distraction

| Rule | Finding | Source |
|---|---|---|
| No autoplay/ambient motion near text | Peripheral vision involuntarily locks onto motion; 32-study meta-analysis found background motion degrades comprehension (worse for older readers) | PMC 2025 distraction meta-analysis; NN/g Animation |
| Animation only for functional feedback | Motion should confirm state changes, not decorate | NN/g Role of Animation |
| Honor `prefers-reduced-motion` | Accessibility + focus | WCAG / platform standard |
| One continuous document | Longer text + more scrolling/pagination widens the screen penalty | Singer & Alexander 2017 |

---

## Debunked — do NOT cite these

- **"8-second attention span / goldfish" and "90-second attention span"** — fabricated marketing claims traced to a Microsoft Canada report citing a non-existent "Statistic Brain" source. No peer-reviewed basis. Use Cowan's ~4-chunk working-memory limit and NN/g scanning data for chunking rationale instead.
- **"Reduces eye strain by 30%" / "improves accuracy by up to 20%"** typography stats — circulate on SEO/marketing blogs, never traceable to a citable study.
- **"Serif is inherently harder to read on screen"** — a low-DPI-era convention superseded by high-res displays; meta-analyses show no general difference.
- **"7±2 is a hard memory limit"** — Miller 1956 explicitly offered it as a rhetorical heuristic; Cowan's ~4 is the rigorous figure. Also: don't misapply "7 items" to cap *visible* nav/content (it applies only to what must be held in memory).
- **Overstating the screen penalty** — it's g≈−0.2, absent for narrative text, and has failed to replicate in some follow-ups (Clinton's own included). Real but fragile; don't call screens "bad for reading" wholesale.

---

## Primary sources (URLs)

- Nanavati & Bias 2005, Optimal Line Length — https://journals.uc.edu/index.php/vl/article/view/5765
- Baymard, Line Length & Readability — https://baymard.com/blog/line-length-readability
- WCAG 1.4.8 Visual Presentation — https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html
- NN/g F-Shaped Pattern — https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content-discovered/
- NN/g Layer-Cake Pattern — https://www.nngroup.com/articles/layer-cake-pattern-scanning/
- Morkes & Nielsen 1997 — https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/
- Mayer's Principles (summary) — https://educationaltechnology.net/mayers-principles-of-multimedia-learning/
- Mayer 2023, Past/Present/Future of CTML — https://link.springer.com/article/10.1007/s10648-023-09842-1
- 2025 Mayer meta-analysis (boundary conditions) — https://www.sciencedirect.com/science/article/pii/S1747938X25000673
- Kong, Seo & Zhai 2018 (screen vs paper) — https://www.sciencedirect.com/science/article/abs/pii/S0360131518301052
- Delgado et al. 2018 — https://www.sciencedirect.com/science/article/pii/S1747938X18300101
- Ackerman & Goldsmith 2011 — https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/Ackerman-Goldsmith-2011-JEP-AppliedMetacognitive-Regulation-of-Text-Learning-on-Screen-vs-on-Paper.pdf
- Dunlosky et al. 2013 (learning techniques) — https://pubmed.ncbi.nlm.nih.gov/26173288/
- Roediger & Karpicke 2006 (testing effect) — https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x
- Cepeda et al. 2006 (spacing) — https://augmentingcognition.com/assets/Cepeda2006.pdf
- Bisra et al. 2018 (self-explanation) — https://link.springer.com/article/10.1007/s10648-018-9434-x
- Cowan 2001 (magical number 4) — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/44023F1147D4A1D44BDC0AD226838496/S0140525X01003922a.pdf
- Kornell & Bjork 2007 (fluency illusion) — https://sanlab.psych.ucla.edu/wp-content/uploads/sites/13/2016/07/RBjork_Dunlosky_Kornell_2012.pdf
- Distraction meta-analysis 2025 — https://pmc.ncbi.nlm.nih.gov/articles/PMC12684101/
