---
name: research-report
description: Generate focused research reports from web sources with deep-linked citations. Delivers a self-contained HTML report (sticky TOC, tier badges, one-click Export .md) whose clickable references navigate directly to specific passages in source articles. Use it when user requests research reports, deep linked reports, overview of a research field, topic or domain.
---

# Research Report Generator with Deep-Linked Sources

Create actionable, compressed research reports backed by **high-quality, verified sources**. Every non-trivial claim links directly to the exact supporting passage via W3C Text Fragment URLs, and every source is graded against an explicit quality rubric before it is allowed into the report.

This skill has two modes:
- **From URLs the user supplies** — synthesize directly from those.
- **From a topic the user supplies** — perform multi-agent discovery first, vet sources against the quality rubric, then synthesize.

## When to Use This Skill

- "Create a research report on X"
- "Build a toolkit / reference guide from these articles"
- "Deep-linked overview of [field/domain]"
- "Summarize with verifiable source links"

---

## Part 1 — Source Quality System (NEW, mandatory)

Bad sources poison the whole report. Every source that ends up cited MUST be graded with the rubric below. Reject anything that scores < 7/12, unless the user explicitly accepts it.

### 1.1 Source Quality Rubric (12 points total)

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Authority** — who wrote/published it | Anonymous / SEO farm | Generic blog, no author bio | Named practitioner / known publication | Primary source: official docs, the team that built it, peer-reviewed |
| **Evidence depth** — claims are backed by | Pure opinion | Anecdote / one example | Multiple examples or data | Reproducible code, benchmarks, empirical study, or first-hand build |
| **Recency** — for fast-moving topics (LLMs, frameworks) | > 24 mo old | 12–24 mo | 6–12 mo | ≤ 6 mo, or evergreen + still maintained |
| **Specificity** — actionable vs hand-wavy | Marketing fluff | High-level overview | Concrete patterns/examples | Code, configs, decision rules, named tradeoffs |

**Scoring gates:**
- **10–12:** Tier-A — quote freely, lead with this source.
- **7–9:** Tier-B — use, but cross-check key claims against another source.
- **< 7:** Reject. Do not cite.

### 1.2 Preferred source types (in order)

1. **Primary docs** from the team that built the thing (Anthropic docs, official spec, repo README/CHANGELOG).
2. **Engineering blog posts** by the team or experienced practitioners with shown code.
3. **Peer-reviewed papers / well-cited preprints** (for research-flavored topics).
4. **Conference talks / video transcripts** by domain experts.
5. **Curated awesome-lists / cookbooks** maintained by reputable orgs.
6. **High-signal community posts** (HN threads, Reddit) — only as Tier-B and only when the comment chain itself contains the evidence.

### 1.3 Sources to actively avoid

- AI-generated SEO content with no author.
- Tutorials older than the major version they describe.
- "Top 10 X" listicles with no original analysis.
- Vendor marketing pages mistaken for docs.

---

## Part 2 — Multi-Agent Research Phase (NEW, for topic-mode requests)

When the user gives a **topic** (not URLs), do NOT do a single WebSearch and call it done. Spin up **3–5 parallel research sub-agents** so coverage is broad and angles are diverse.

### 2.1 Sub-agent dispatch pattern

Send a **single message with multiple `Agent` tool calls in parallel**. Default fleet (adapt to the topic):

1. **`primary-docs` agent** — find the canonical/official documentation, specs, repos. Goal: ground truth.
2. **`practitioner-patterns` agent** — find engineering blog posts and case studies showing real-world patterns, with code.
3. **`critique-and-pitfalls` agent** — find posts, threads, and talks describing what *doesn't* work, anti-patterns, gotchas, failure modes.
4. **`recent-developments` agent** — find anything from the last 3–6 months: new releases, changelogs, recent talks.
5. **(Optional) `academic` agent** — for research-y topics, find papers / preprints.

Use `subagent_type: web-search-researcher` (or `general-purpose` if unavailable). Each agent prompt MUST include:

- The exact topic and the user's stated goal.
- The Source Quality Rubric (paste it in).
- Instruction: return **5–10 candidate sources**, each with URL, 1-line summary, **rubric score with justification**, and **2–4 verbatim quotes** (with exact wording, suitable for deep-linking).
- Instruction: reject sources scoring < 7 unless the angle is otherwise uncovered.

### 2.2 Triage step (after agents return)

After agents come back, do this BEFORE writing the report:

1. **Dedupe** sources across agents.
2. **Re-score** anything borderline yourself.
3. **Coverage check** — does every major sub-topic have at least one Tier-A or two Tier-B sources?
4. **Gap-fill** — if a sub-topic is thin, dispatch one more targeted agent.
5. Produce an internal **Source Ledger** (kept in working memory, surfaced in the report's appendix): `URL | Tier | Score | Why it earned that score | What it's cited for`.

### 2.3 When to skip multi-agent mode

- User provided URLs directly → just vet those against the rubric.
- User explicitly says "quick" or "rough" → 1–2 agents fine, but still apply rubric.

---

## Part 3 — Citation & Claim Linking System (UPGRADED)

The old rule was "every section has a link." The new rule is stricter:

### 3.1 Claim-level linking rule

> **Every non-trivial claim must carry an inline citation whose deep link lands on a verbatim passage that directly supports the claim.**

"Non-trivial" = anything a skeptical reader could reasonably ask "says who?" about. Definitions, rules, numbers, named patterns, tradeoffs, recommendations — all need links. Generic connective prose does not.

### 3.2 Citation density target

- Aim for **1 citation per 2–4 sentences** of substantive content.
- Sections with zero citations are a smell — either cut them or find support.
- Conversely: don't pile 4 citations on one sentence; pick the strongest.

### 3.3 Deep-link quality rules

A deep link is only valid if ALL of these hold:

1. **Verbatim match** — the `text=` payload is copied character-for-character from the page (no paraphrasing, no normalized punctuation).
2. **Uniqueness** — the chosen 5–15 word phrase appears only once on the page. If not, use the `textStart,textEnd` range form.
3. **Direct support** — the highlighted passage, read on its own, would convince a skeptic of the claim. No "supports the spirit of" links.
4. **Source-tier annotation** — each citation indicates the source's tier inline (see template below) so readers see at a glance how trusted it is.

### 3.4 W3C Text Fragment refresher

```
https://example.com/page#:~:text=URL%20encoded%20unique%20phrase
https://example.com/page#:~:text=Start%20of%20passage,end%20of%20passage
```

Encoding: spaces → `%20`, `,` → `%2C`, `(` → `%28`, `)` → `%29`, `'` → `%27`, `%` → `%25`, `&` → `%26`, `+` → `%2B`, `=` → `%3D`. Use `encodeURIComponent` semantics (NOT `+` for spaces).

### 3.5 Verification pass (mandatory before delivery)

Run this checklist over the finished draft:

- [ ] Every non-trivial claim has at least one citation.
- [ ] Every cited URL exists in the Source Ledger with tier ≥ B.
- [ ] Every `text=` payload was actually quoted by an agent or by WebFetch (no hallucinated quotes — if uncertain, drop to a page-level link and flag it).
- [ ] At least one **independent** corroborating source exists for every Tier-B-only claim.
- [ ] No claim cites a source that doesn't discuss that claim.
- [ ] Quick-Reference table and Source Ledger are present.

If any item fails, fix or remove the claim. Do not ship.

---

## Part 4 — Report Structure (updated template)

Author the report as **markdown** using the template below — it is the single source of truth. Part 4.1 then wraps it in the HTML deliverable; the markdown is embedded verbatim inside the HTML, so the **Export .md** button hands the reader back exactly this file.

```markdown
# [Report Title]

[2–3 sentence framing: what this report covers and who it's for.]

**Topic / goal:** [user's stated goal, verbatim]
**Sources vetted:** N candidates → M cited (see Source Ledger at end)
**Best-supported in:** Chrome / Edge / Brave (text-fragment links)

---

## Quick Reference

[Compact table of the top-level patterns/rules/concepts.]

---

## §1. [Section Title]

### [Concept name](deep-link-to-verbatim-passage) <sup>[A]</sup>

Short explanation in your own words. The actionable claim sits here ([source](deep-link) <sup>[A]</sup>), and a corroborating angle sits here ([source](deep-link) <sup>[B]</sup>).

> [Optional pull-quote, itself a deep link.](deep-link)

**When to apply:** …
**Tradeoff / pitfall:** … ([source](deep-link) <sup>[B]</sup>)

---

## §N. …

---

## Cross-cutting tradeoffs

[Brief synthesis: where do sources agree, where do they disagree? Disagreements are surfaced, not hidden.]

---

## Source Ledger

| # | Source | Tier | Score | Cited for |
|---|--------|------|-------|-----------|
| 1 | [Title](url) | A | 11/12 | §1 definition, §3 pattern |
| 2 | [Title](url) | B | 8/12 | §2 pitfall |
| … | | | | |

**Tier legend:** A = primary/expert + reproducible evidence; B = solid but cross-checked; rejected sources are not listed.

---

*Generated [DATE]. Deep links use W3C Text Fragments — best in Chrome/Edge/Brave.*
```

The `<sup>[A]</sup>` / `<sup>[B]</sup>` annotations are the tier markers — they let readers spot uncited-only-by-Tier-B claims at a glance, and the HTML shell renders them as colored badges (green = A, amber = B, red = unverified).

### 4.1 HTML deliverable (the thing you actually ship)

The final artifact is a **single self-contained HTML file**, not a bare `.md`. Build it:

```bash
~/.claude/skills/research-report/assets/build_report.py <report>.md
# writes <report>.html next to it AND opens it in the default browser
# pass --no-open to suppress that (headless/cron runs)
```

What the shell adds, for free, with no extra authoring:

- Rendered report with a **sticky TOC** (auto-built from `##`/`###`) and scroll-spy.
- **Tier badges** styled from the `<sup>[A]</sup>` markers.
- Deep-link citations get a `↗` affordance so text-fragment links are visibly different from plain links.
- Light theme only (dark was hard to read), and a print stylesheet.
- **Export .md** button → downloads the original markdown verbatim. **Copy Markdown** button → same content to clipboard.
- **Copy section** button on every `##` heading → copies just that section's raw markdown (deep links included) so the reader can paste one section into a draft without the rest. Hovering a paragraph shows a **Copy** button that copies just that paragraph's markdown. Each section and paragraph also has a **Delete** button: it removes the block from the page, the TOC, and what Copy Markdown / Export .md produce, so the reader can trim the report to the parts they want (reload restores everything). A **Hide TOC** header button collapses the sidebar so the text takes the full width.

Rules when building:

- Keep the `.md` next to the `.html`. The markdown is the source you edit; **re-run the build after any edit** — the HTML does not update itself.
- Write the markdown to the current project folder (`<topic>_report.md`) unless the user names another location; the HTML sits beside it.
- Markdown-in-HTML rendering uses marked from a CDN. Offline, the page falls back to showing the raw markdown — still readable, and Export still works.
- Do **not** hand-write the HTML or duplicate the report body into it. One source, one build step.

---

## Part 5 — End-to-End Workflow

### Topic mode (user gave a topic, no URLs)

1. **Clarify goal.** One sentence back to the user if the topic is ambiguous; otherwise proceed.
2. **Dispatch 3–5 research sub-agents in parallel** (Part 2.1). One message, multiple `Agent` tool calls.
3. **Triage** returns into the Source Ledger; gap-fill if needed (Part 2.2).
4. **Outline** sections from the Ledger — organize by concept, not by source.
5. **Draft** with claim-level citations (Part 3).
6. **Verification pass** (Part 3.5).
7. **Write** the markdown file. Default location: the current project folder unless they specify otherwise. Filename: `topic_report.md`.
8. **Build the HTML** — `assets/build_report.py <file>.md` (Part 4.1). This is the deliverable. It opens in the browser automatically, so the user never has to go hunting for the file.
9. **Report back** to the user: path to the `.html` (note it is already open in the browser, the `.md` sits beside it, and the page has an Export .md button) + 1-paragraph summary + count of sources vetted vs cited.

### URL mode (user gave URLs)

1. **WebFetch each URL**, requesting verbatim passages for key concepts.
2. **Score each source** against the rubric. Warn the user about anything < 7.
3. **Draft → verify → write → build HTML** as above.

---

## Part 6 — Examples and Patterns

### Inline claim citation (preferred)

```markdown
Agents should expose **narrow, composable tools** rather than one
mega-tool ([Anthropic engineering](https://…#:~:text=narrow%2C%20composable%20tools) <sup>[A]</sup>).
```

### Disagreement surfaced

```markdown
One school argues for stateless agents ([X](link) <sup>[A]</sup>); another
finds short-term scratchpads materially improve multi-step tasks
([Y](link) <sup>[B]</sup>). Pick based on task horizon.
```

### Pull quote as deep link

```markdown
> ["the model is most reliable when each tool does exactly one thing"](link)
> — Source title <sup>[A]</sup>
```

---

## Part 7 — Failure Modes & Recovery

- **Agent returns weak sources** → re-dispatch with a sharper angle, do not lower the rubric.
- **Verbatim quote can't be found on page** → drop to a page-level link AND flag the claim with `<sup>[unverified]</sup>` or cut the claim.
- **Topic is too broad** → split into Part 1 / Part 2 reports rather than thinning citations.
- **Only Tier-B sources available** → say so explicitly in the framing paragraph; do not pretend the evidence is stronger than it is.

---

## Reference Example

See `./EXAMPLE.md` for the prior format. The current format adds: Source Ledger, tier markers (`<sup>[A]</sup>`), claim-level citation density, the verification pass, and the HTML deliverable (Part 4.1).

## Tips for Success

- **Sources first, prose second.** Build the Source Ledger before writing any paragraphs.
- **Never invent a quote.** If you can't find it verbatim, you can't deep-link it.
- **Surface disagreement.** A report where all sources agree is either a trivial topic or a biased selection — check which.
- **Tier markers are a feature.** They let the reader trust the report without re-reading every source — and the HTML turns them into badges.
- **Ship the HTML, keep the markdown.** The export button means the reader never loses the plain-text version.
