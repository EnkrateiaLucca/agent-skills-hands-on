# Rate card, formula, and floors

## Where the numbers come from

Everything in the "observed" section below is what Lucas actually quoted to real
sponsors between June and August 2026 — lifted from his sent mail, not invented.
That matters because it's the calibration anchor: any formula that outputs less
than what he already charges is wrong, no matter how principled the CPM math looks.

### Observed quotes (Jun–Aug 2026, ~31K subs)

**USD track — dedicated video** (used with TEC-DO/Tripo3D and MiniMax)

| Line item | Quoted |
|---|---|
| Dedicated video + link in bio (7 or 90-day code) | $3,500 |
| 90-day paid-ad usage rights | $1,500–2,000 |
| Cross-platform usage + editing rights (3 mo) | $1,500 |
| Cross-post add-on, per extra platform | $750 |
| **Totals quoted** | **$5,000** (MiniMax) / **$7,000** (Tripo3D) |

**EUR track — integrated video** (used with Supermemory)

| Line item | Quoted |
|---|---|
| INTEGRATED VIDEO PACKAGE — 2–3 min segment + vertical cut-down + one LinkedIn post at launch, one revision round, permanent placement | €3,000 |
| Paid usage rights, 6 mo, all platforms | €1,500 |
| Category exclusivity, 3 mo | €900 |
| Second video | €2,500 |

**Outbound self-pitch** (Vercel, Aug 2026): $4,000 for one video, "flexible".

## Floors — do not go below these

- Dedicated video: **$3,500 USD**
- Integrated segment: **€3,000 EUR**
- Short-only: **$1,200 USD** (no observed quote; derived, treat as provisional
  and flag it when used)

`rate_calc.py` enforces these. If the CPM math lands under a floor, the floor wins
and the output says so. A floor exists because a rate isn't only a function of
views — it's a function of what Lucas will actually get out of bed for, and of not
resetting his own price anchor downward with every soft month.

## The formula

```
expected_views  = median views of recent mature long-form uploads
                  (mature = published long enough ago to have finished its run;
                   yt_stats.py uses a 30-day cutoff)

base            = expected_views × CPM / 1000
subtotal        = base × (1 + sum of add-on percentages)
quote           = max(subtotal, floor_for_format)
```

### The CPM is anchored, not looked up

Generic creator-sponsorship CPM tables ($20–70 for a dedicated read) badly
underprice this channel. Run the numbers backwards from Lucas's own quotes and the
implied CPM is roughly **$150–200** — several times the general-interest rate.

That is not him overcharging. A viewer evaluating paid developer tooling is worth
far more to a sponsor than a general-interest viewer, because the viewer is either
the buyer or the person who tells the buyer, and one converted account can be worth
five figures a year. B2B dev creators price accordingly.

So `rate_calc.py` derives its CPM from Lucas's observed pricing instead of a table:

```
anchor_cpm  = observed_price / view_median_at_calibration x 1000   # frozen once
base        = today's_view_median x anchor_cpm / 1000
```

Calibrate once (`--calibrate`) and the anchor freezes. Today that reproduces his
current prices almost exactly; as the channel grows the quote grows with it rather
than parking on the floor forever. The generic-CPM number is still printed next to
the result as a cross-check — expect it to look low, that's the point.

Tier multipliers on the anchored CPM: **low ×0.85**, **mid ×1.0** (default),
**high ×1.30**. Use high when the tool is a strong fit and Lucas is keen — a video
he'd half want to make anyway will be better, and is worth more to the sponsor. Use
low only to close something he actively wants, never because the sponsor pushed.

**Validation against real quotes** (at an 18K-view median, illustrative):

| Scope | Formula | Lucas actually quoted |
|---|---|---|
| Dedicated video, bare | $3,500 | $3,500 |
| Dedicated + 90-day usage rights | $5,000 | $5,000 (MiniMax) |
| Dedicated + usage + cross-platform | $6,250 | $7,000 (Tripo3D) |

The Tripo3D gap is real: he priced usage rights there at $2,000 rather than $1,500.
Treat formula output as the floor of a sensible range, not a ceiling.

### Add-ons (percentage of base)

| Add-on | % |
|---|---|
| Paid-ad usage rights, 90 days | +40% |
| Paid usage rights, 6 months, all platforms | +50% |
| Cross-platform usage + editing rights, 3 months | +40% |
| Category exclusivity, 3 months | +30% |
| Each extra platform cross-post (Reel, Short, TikTok) | +20% |
| Rush delivery (under 2 weeks) | +25% |

Usage rights are where creators most often give away real money. When a brand buys
90-day paid-ad rights they are buying ad creative — the same footage they'd pay an
agency five figures to produce — so it is priced as a separate line, never bundled
in silently.

## Sanity check before you send a number

Divide the final quote by expected views × 1000 and look at the implied CPM. If
it lands outside roughly $20–$120, something upstream is wrong — usually a stale
or unrepresentative view median. `rate_calc.py` prints this check automatically.

Also compare against the observed quotes above. At ~31K subs Lucas quoted $5,000
and $7,000 for full dedicated packages. A formula output of $1,800 means the view
median is broken, not that his prices were wrong.

## Negotiation notes

- Lucas holds a **no affiliate-only** line. Base rate first; affiliate percentage
  on top is welcome, not a substitute. He's told sponsors this in writing.
- When a sponsor lowballs, cut scope rather than price: drop usage rights, shorten
  the segment to a mention, remove the LinkedIn post. This protects the price
  anchor for the next deal, and the sponsor usually finds more budget.
- "Bigger budgets on the next one if this performs" is worth nothing. Price this
  deal on this deal.
- Bundle discounts are legitimate: a second video at ~80% of the first is normal
  and Lucas has quoted exactly that (€2,500 against €3,000).
