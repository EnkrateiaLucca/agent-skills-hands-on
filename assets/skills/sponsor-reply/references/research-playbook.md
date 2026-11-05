# Researching the tool and the company

The output of this phase is a decision Lucas can defend on camera. He's putting his
name on the thing, so "their landing page says it's great" is not research.

## 1. Primary sources

- **Landing page** — what does it claim, in its own words? Copy the specific claims;
  those are what you'll test.
- **Docs / quickstart** — a real product has a quickstart that works. A thin or
  missing one is a signal.
- **Pricing page** — is there a business here? Free-only with no pricing usually
  means pre-revenue or the user is the product.
- **GitHub, if open source** — stars, date of last commit, open vs. closed issue
  ratio, how many distinct contributors. A repo whose last commit was eight months
  ago is a different risk than one shipping weekly.
- **Company basics** — founded when, funding if public, team size, who's behind it.
  LinkedIn and Crunchbase-style listings are enough; don't over-invest here.

## 2. Social perception

You're answering: do real people use this, and what do they say when the marketing
isn't in the room?

- Hacker News (`site:news.ycombinator.com <tool>` or the HN search API)
- Reddit — the subreddits where this audience lives (r/LocalLLaMA, r/ClaudeAI,
  r/devops, r/webdev, whichever fits)
- X/Twitter — developer chatter, not the company's own account
- Product Hunt, Lobsters, dev.to as secondary

Record links. Quote a couple of representative comments, positive and negative.

**Say so when you find nothing.** For an early-stage tool, silence is normal and
not disqualifying — but it changes the video Lucas would make (a "here's something
new" video rather than a "here's the thing everyone's using" video), and he should
know that before agreeing.

## 3. Hands-on test — tiered

Try the tool. A report that says "not tested" is much weaker, and Lucas has told
sponsors he only makes claims about products he's actually used.

**Tier 1 — no gate needed.** Hosted product, free tier, web playground, public API
with a free key, or a documented example you can reason about. Prefer this always.
Sign up with a throwaway if needed; don't use Lucas's personal accounts or pay for
anything without asking.

**Tier 2 — GATE 2, requires approval.** Cloning and running their code locally.
Work through `security-rubric.md`, then ask Lucas explicitly, showing him the
rubric result. If he declines or doesn't answer, fall back to Tier 1 or to docs
review and mark the report "not tested — <reason>". Never silently skip the gate
because the repo looked fine to you.

**What to test:** the specific claims from the landing page or README. If it says
"cuts agent memory costs 10x", try to observe something about cost or latency. If
it says "works with any MCP client", point an MCP client at it. Note what worked,
what didn't, and where you got stuck — the friction is often the most useful part
of the eventual video, and it's the part the sponsor won't tell you about.

## 4. Fit with the channel

Automata Learning Lab's audience: developers and technically curious builders
around AI agents, MCP, Claude Code, context engineering, LLM tooling. Roughly:

- **Bullseye** — agent infrastructure, memory/context tooling, MCP servers,
  coding agents, eval and observability tooling, dev-facing AI APIs.
- **Adjacent** — general dev infra and deployment, data tooling, no-code AI. Can
  work with the right angle.
- **Off-centre** — QA automation, marketing SaaS, consumer AI apps, 3D/video
  generation. Possible, but the video has to be built around a real use case Lucas
  would plausibly have, or it reads as an ad.
- **No** — anything Lucas can't test, anything requiring claims he can't verify,
  anything whose growth model depends on his audience being misled.

Fit is about whether a good video exists here, not whether the cheque clears. A
mediocre sponsored video costs more in audience trust than the sponsorship pays.

## 5. Write it up

Use the report template in SKILL.md. Lead with the verdict — Lucas reads the first
line and decides whether to read the rest. Separate what you verified from what you
inferred, and link your sources so he can check any claim in ten seconds.
