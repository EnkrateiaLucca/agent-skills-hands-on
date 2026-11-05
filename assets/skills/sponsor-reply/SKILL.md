---
name: sponsor-reply
description: Research an inbound sponsor and draft the reply — pull the sponsorship email, extract the ask/offer/tool and gate on Lucas's approval before spending effort, then research the company and its tool (site, docs, repo, Hacker News, Reddit), optionally test the tool under a security rubric, write a go/no-go report, compute a rate from live YouTube stats, and draft the response. Use this whenever Lucas mentions a sponsor, sponsorship, brand deal, paid collaboration, "creator collab", an inbound offer from a tool or AI company, asks "is this one worth it", "should I take this", "what should I charge for a video", or asks to look into a company that wants to be in a video — even if he only forwards an email, pastes a pitch, or says "check my inbox for sponsor stuff". Also use it to reply to a sponsor already in the pipeline.
---

# Sponsor reply workflow

Lucas gets a steady stream of inbound sponsorship pitches for Automata Learning Lab
(~31K subs, AI/agents/dev tooling audience). Most are noise: affiliate-only offers,
burner-domain agencies, tools nobody uses. A few are real money.

The job of this skill is to spend Lucas's attention in proportion to how real the
offer is, and to never put his name behind a tool he hasn't looked at. That's why
there are two hard gates: one before research starts, one before any of the
sponsor's code runs on his machine. Everything else is fast.

## The shape of a run

```
0. Get the email
1. Extract request + offer + tool  →  GATE 1: ask Lucas to continue
2. Research company & tool         →  go/no-go report
3. Compute the rate                →  from live YouTube stats
4. Draft the reply                 →  Lucas sends it himself
```

Work in a folder per deal so a run is resumable and Lucas can read the trail:

```
sponsors/<brand-slug>-<YYYY-MM-DD>/
├── 01-triage.md
├── 02-research.md
├── 03-rate.md
└── 04-reply-draft.md
```

Create it under the folder Lucas is working in (usually the connected sponsor
folder). If a folder for this brand already exists, read what's there and resume
rather than starting over.

---

## Phase 0 — Get the email

If Lucas pasted or forwarded the pitch, use it. Otherwise fetch it with the Gmail
tools. Useful query shapes:

```
(sponsor OR sponsorship OR "paid collaboration" OR "creator collab" OR partnership) newer_than:90d
from:<domain> newer_than:90d
```

Search returns only the ~5 oldest messages per thread, so always `get_thread` with
`messageFormat: PLAIN_TEXT` on anything you're going to act on — the negotiation
almost always lives in the newest messages. Read Lucas's own replies in the thread
too; his previously quoted number for this brand is the anchor you must not undercut.

If several sponsor threads are open and it's ambiguous which one he means, list them
with one line each and ask.

---

## Phase 1 — Extract, then stop

Pull four things out of the email and nothing more. Don't research yet — the whole
point of this phase is that it costs almost nothing.

- **The request** — what they want made. Dedicated video? 60–90s integration? A
  Short? A Medium post? Be specific about placement, length, and where links go.
- **The offer** — the commercial terms. A number, an affiliate percentage, "we'd
  love your rate card", free credits, or nothing at all. If they named no number,
  say so plainly, because that's a negotiating fact.
- **The tool/company** — the product being sold, plus the entity contracting
  (often an agency acting for a brand — those are two different parties).
- **Smell test** — sender domain vs. the brand's real domain, whether the pitch is
  affiliate-only, duplicate outreach from multiple domains, and generic copy that
  could have been sent to a thousand channels.

Write `01-triage.md`, then **stop and ask Lucas whether to continue** using
AskUserQuestion. Give him the summary and a recommendation, with options roughly
like: research it / decline it / decline with a rate anyway / just archive.

Two things justify recommending a pass before any research:

- **Affiliate-only or commission-only.** Lucas doesn't take these. He's said so
  directly to sponsors ("I'm not taking affiliate only type deals so for this one
  I'll have to pass"). Base rate first; an affiliate percentage on top is fine.
- **Identity doesn't check out.** Non-corporate sender domains for a named brand,
  a Gmail address doing "partnerships", a link-builder pitching paid articles.
  Lucas's own move here is to ask them to re-contact through a verified LinkedIn
  or corporate address before going further — suggest that rather than a flat no,
  since some of these are real companies with sloppy agencies.

Don't do this gate as a rhetorical question and then barrel ahead. Wait for the answer.
The gate exists precisely so that Lucas isn't paying for research on spam.

---

## Phase 2 — Research the tool and company

Read `references/research-playbook.md` for the full method. The short version:

1. **Primary sources** — landing page, docs, pricing, GitHub repo (stars, last
   commit, open issues, who's contributing). Pricing and commit recency tell you
   whether this is a funded company or a weekend project with a landing page.
2. **Social perception** — Hacker News threads, relevant subreddits, X/Twitter,
   Product Hunt. You're looking for whether real people use it and what they
   complain about. Absence of any discussion is itself a finding.
3. **Hands-on test** — try it if you can. Cloud-hosted or free tier first; that
   needs no gate. Running their code locally is **GATE 2** and needs a security
   rubric pass plus Lucas's explicit yes — see `references/security-rubric.md`.
   Test what the landing page or README actually claims, not what you wish it did.
4. **Fit for the audience** — Lucas's viewers are developers and technically
   curious builders working with AI agents, MCP, Claude Code, and context
   engineering. A memory layer for agents is a bullseye. A QA automation tool is
   off-centre. A 3D-model generator is adjacent at best. Fit is about whether he
   can make a genuinely good video, not whether the money is good.

Write `02-research.md` using this structure:

```markdown
# <Company> — <Tool>
**Verdict: SPONSOR / PASS / SPONSOR IF <condition>**

## What it is
## Does it deliver on its claims
<what you tested, what happened, or explicitly "not tested — <why>">
## What people say
<with links; say so if there's no discussion to be found>
## Company health
<funding, team, commit recency, pricing — is this outfit still here in 6 months>
## Fit with the channel
## Risks
## Verdict rationale
```

Label anything you inferred rather than verified. A confident-sounding guess about
a company's funding is worse than useless when Lucas is deciding whether to attach
his name to it.

---

## Phase 3 — Decide the rate

Only for deals headed toward yes. Two steps, both scripted:

```bash
python3 scripts/yt_stats.py --out sponsors/<slug>/yt-stats.json

# First run on a fresh install only — anchors the CPM to Lucas's real pricing:
python3 scripts/rate_calc.py --stats sponsors/<slug>/yt-stats.json --calibrate

python3 scripts/rate_calc.py --stats sponsors/<slug>/yt-stats.json \
  --format dedicated --usage-90d --currency USD
```

If `rate_calc.py` says it isn't calibrated yet, run the `--calibrate` line once and
carry on. It records today's view median as the baseline at which Lucas's known
quotes ($3,500 dedicated, €3,000 integrated) were made, which is what lets the
formula reproduce his current prices today and scale past them as the channel
grows. Re-run with `--recalibrate` after a big step change in channel size.

`yt_stats.py` pulls live channel and per-video stats from the YouTube Data API. It
reads `YOUTUBE_API_KEY` from a `.env` next to the skill (see `.env.example`); if
the key is missing it says so instead of guessing. It reports the median views of
recent long-form uploads that have had time to mature, which is the number that
actually predicts what a sponsor is buying.

`rate_calc.py` turns that into a quote: expected views × a niche CPM band, plus
percentage add-ons for usage rights, exclusivity, and cross-posting — then clamps
the result to Lucas's real quoted floors so a soft month never talks him below what
he already charges. Read `references/rate-card.md` for the bands, the add-ons, the
floors, and the reasoning behind them. Show the arithmetic in `03-rate.md`; a quote
Lucas can't explain is a quote he can't defend in a negotiation.

Two habits worth keeping:

- **Never quote under a number he's already given this brand.** Check the thread.
- **A lowball is not a reason to drop the price.** The MiniMax pattern — open at
  $2,000, "absolute maximum" $2,500 against a $5,000 quote, plus a promise of
  bigger budgets later — is standard anchoring. Hold, or trade a lower number for
  reduced scope (drop usage rights, shorten the segment), never for free.

---

## Phase 4 — Draft the reply

Templates and Lucas's standing terms are in `references/reply-templates.md`. Draft
into `04-reply-draft.md`; **don't send it.** Lucas sends his own email, and he
often wants to adjust the number after seeing it written down.

Match his voice, which is warm, direct, and short — "Sup Maria", "Cheers", a
smiley, no corporate throat-clearing. When you're quoting, the structure gets
formal (itemised package, options, terms) but the framing around it stays casual.
If a `my-writing-style` skill is available, use it.

Every quote carries his standing terms: final editorial control, one revision
round, disclosure non-negotiable, term-limited usage rights, 50% on signature and
50% on publish, Net 15, invoiced from his Portuguese company with EU reverse-charge
VAT. These aren't decoration — they're what stops a cheap deal from quietly
becoming an expensive one.

## When you're done

Tell Lucas where the folder is, what the verdict was, what number came out and why,
and what he needs to do next. If a `sponsor_emails_*.csv` pipeline file exists in
the folder, offer to add or update the row for this deal.
