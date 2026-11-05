#!/usr/bin/env python3
"""Turn live YouTube stats into a defensible sponsorship quote.

    quote = max( expected_views x CPM/1000 x (1 + add-ons), floor )

The CPM is not taken from a generic industry table, because generic tables badly
underprice this channel. Lucas quotes $3,500 for a dedicated video at his current
size; standard creator CPMs would suggest a fraction of that, and they'd be wrong.
A developer audience evaluating paid dev tools converts at a value per view that
general-interest sponsorship rates don't model.

So the CPM is anchored to his own observed pricing: calibrate once against the
current view median, freeze that CPM, and from then on the quote scales as the
channel grows. Today it reproduces his real numbers; in a year it won't leave money
on the table. The static industry band is still printed alongside as a cross-check.

    python3 scripts/rate_calc.py --stats stats.json --calibrate     # once
    python3 scripts/rate_calc.py --stats stats.json --format dedicated --usage-90d
    python3 scripts/rate_calc.py --views 18000 --format integrated --currency EUR
"""
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path

CALIB = Path(__file__).resolve().parent / "calibration.json"

# Generic creator-sponsorship CPMs, USD. Kept only as a sanity cross-check --
# they systematically underprice a B2B developer audience.
STATIC_CPM = {"dedicated": 55, "integrated": 32, "short": 6}

# Multipliers applied to the anchored CPM.
TIER = {"low": 0.85, "mid": 1.0, "high": 1.30}

FLOORS = {
    "dedicated":  {"USD": 3500, "EUR": 3200},
    "integrated": {"USD": 3300, "EUR": 3000},
    "short":      {"USD": 1200, "EUR": 1100},
}
FLOOR_OBSERVED = {"dedicated": {"USD"}, "integrated": {"EUR"}}

ADDONS = [
    ("usage_90d",       "Paid-ad usage rights, 90 days",              0.40),
    ("usage_6mo",       "Paid usage rights, 6 months, all platforms", 0.50),
    ("cross_platform",  "Cross-platform usage + editing, 3 months",   0.40),
    ("exclusivity_3mo", "Category exclusivity, 3 months",             0.30),
    ("rush",            "Rush delivery (under 2 weeks)",              0.25),
]
CROSS_POST_EACH = 0.20


def money(x, cur):
    return f"{'$' if cur == 'USD' else '€'}{x:,.0f}"


def main():
    p = argparse.ArgumentParser()
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--stats", help="stats.json from yt_stats.py")
    src.add_argument("--views", type=int, help="expected views, set by hand")
    p.add_argument("--format", choices=STATIC_CPM, default="dedicated")
    p.add_argument("--tier", choices=TIER, default="mid",
                   help="mid by default; high for a strong fit Lucas is keen on")
    p.add_argument("--cpm", type=float, help="override the anchored CPM (USD)")
    p.add_argument("--currency", choices=["USD", "EUR"], default="USD")
    p.add_argument("--fx", type=float, default=0.92, help="USD->EUR, verify before sending")
    p.add_argument("--calibrate", action="store_true",
                   help="freeze the anchor to the current view median, then exit")
    p.add_argument("--recalibrate", action="store_true", help="overwrite an existing anchor")
    for flag, label, _ in ADDONS:
        p.add_argument("--" + flag.replace("_", "-"), action="store_true", help=label)
    p.add_argument("--cross-post", type=int, default=0, metavar="N",
                   help="extra platform cut-downs, +20%% each")
    p.add_argument("--round-to", type=int, default=250)
    p.add_argument("--out", help="write the breakdown as JSON here")
    a = p.parse_args()

    cal = json.loads(CALIB.read_text(encoding="utf-8"))

    if a.stats:
        s = json.loads(Path(a.stats).read_text(encoding="utf-8"))
        block = s["shorts"] if a.format == "short" else s["long_form"]
        views = block.get("median_views")
        if not views:
            sys.exit("No median views in the stats file for that format.")
        basis = (f"median of {block.get('sample_size')} mature "
                 f"{'Shorts' if a.format == 'short' else 'long-form uploads'}")
        channel = s.get("channel", {}).get("title", "channel")
    else:
        views, basis, channel = a.views, "supplied by hand", "channel"

    # --- calibration -------------------------------------------------------
    if a.calibrate or a.recalibrate:
        if cal["anchor_median_views"] and not a.recalibrate:
            sys.exit(f"Already calibrated at {cal['anchor_median_views']:,} views on "
                     f"{cal['calibrated_at']}. Use --recalibrate to overwrite.")
        if not a.stats:
            sys.exit("Calibrate from real stats: --stats <file> --calibrate")
        cal["anchor_median_views"] = s["long_form"]["median_views"]
        cal["anchor_median_views_shorts"] = s.get("shorts", {}).get("median_views")
        cal["calibrated_at"] = datetime.now(timezone.utc).date().isoformat()
        CALIB.write_text(json.dumps(cal, indent=2), encoding="utf-8")
        print(f"Anchored to {cal['anchor_median_views']:,} long-form median views"
              + (f" / {cal['anchor_median_views_shorts']:,} Shorts median."
                 if cal["anchor_median_views_shorts"] else " (no Shorts sample)."))
        print("Implied CPMs now:")
        for f, price in cal["anchors_usd"].items():
            av = (cal["anchor_median_views_shorts"] if f == "short"
                  else cal["anchor_median_views"])
            if not av:
                print(f"  {f:<11} no baseline views — cannot anchor")
                continue
            print(f"  {f:<11} ${price:,} / {av:,} views = ${price / av * 1000:,.0f} CPM")
        print("\nFrozen. Quotes scale from here as the channel grows.")
        return

    anchor_views = (cal.get("anchor_median_views_shorts") if a.format == "short"
                    else cal.get("anchor_median_views"))
    if not anchor_views:
        sys.exit("Not calibrated yet. Run once with --stats <file> --calibrate so the "
                 "CPM is anchored to what Lucas actually charges, then quote.")

    anchor_cpm = cal["anchors_usd"][a.format] / anchor_views * 1000
    cpm = a.cpm if a.cpm else anchor_cpm * TIER[a.tier]

    base_usd = views * cpm / 1000
    applied = [(lbl, pct) for flag, lbl, pct in ADDONS if getattr(a, flag)]
    if a.cross_post:
        applied.append((f"Cross-post to {a.cross_post} extra platform(s)",
                        CROSS_POST_EACH * a.cross_post))
    uplift = sum(pct for _, pct in applied)

    subtotal_usd = base_usd * (1 + uplift)
    subtotal = subtotal_usd if a.currency == "USD" else subtotal_usd * a.fx
    floor = FLOORS[a.format][a.currency]
    quote = round(max(subtotal, floor) / a.round_to) * a.round_to
    if quote < floor:  # rounding must never dip below the floor
        quote = -(-floor // a.round_to) * a.round_to

    w = 46
    print(f"\n{channel} — {a.format} quote in {a.currency}")
    print("=" * 64)
    print(f"{'Expected views':<{w}} {views:>12,}")
    print(f"  basis: {basis}")
    print(f"{'Anchored CPM (from ' + money(cal['anchors_usd'][a.format], 'USD') + ' @ ' + format(anchor_views, ',') + ' views)':<{w}} {'$' + format(anchor_cpm, ',.0f'):>12}")
    if a.tier != "mid" or a.cpm:
        print(f"{'CPM used (' + (a.tier if not a.cpm else 'override') + ')':<{w}} {'$' + format(cpm, ',.0f'):>12}")
    print(f"{'Base = views x CPM / 1000':<{w}} {money(base_usd, 'USD'):>12}")
    for lbl, pct in applied:
        print(f"{'  + ' + lbl:<{w}} {'+' + format(pct, '.0%'):>12}")
    if applied:
        print(f"{'Subtotal (USD)':<{w}} {money(subtotal_usd, 'USD'):>12}")
    if a.currency == "EUR":
        print(f"{'Converted at ' + str(a.fx) + ' USD->EUR':<{w}} {money(subtotal, 'EUR'):>12}")
    obs = a.currency in FLOOR_OBSERVED.get(a.format, set())
    print(f"{'Floor (' + ('observed' if obs else 'derived') + ')':<{w}} {money(floor, a.currency):>12}")
    print("-" * 64)
    print(f"{'QUOTE':<{w}} {money(quote, a.currency):>12}")
    print("=" * 64)

    growth = views / anchor_views - 1
    static = views * STATIC_CPM[a.format] / 1000 * (1 + uplift)
    notes = []
    if abs(growth) < 0.03:
        notes.append(f"Views are level with the {anchor_views:,} calibration baseline, "
                     f"so this reproduces Lucas's current pricing by design.")
    else:
        notes.append(f"Views are {growth:+.0%} vs the {anchor_views:,} baseline — the "
                     f"quote tracks the channel instead of sitting on the floor.")
    notes += [
        f"Generic creator-CPM math would say {money(static, 'USD')} — it underprices a "
        f"B2B dev audience, which is why the anchor exists. Shown only as a cross-check.",
    ]
    if subtotal < floor:
        notes.append(f"Formula gave {money(subtotal, a.currency)}, under the "
                     f"{money(floor, a.currency)} floor — quoting the floor. Check whether "
                     f"the view median is representative.")
    if not obs:
        notes.append(f"The {a.format}/{a.currency} floor is derived, not a number Lucas "
                     f"has actually quoted. Provisional.")
    if a.currency == "EUR":
        notes.append(f"FX assumed at {a.fx} USD->EUR. Verify before sending.")
    notes.append("Check the thread: never quote under a number already given to this "
                 "brand. If they lowball, cut scope, not price.")
    print("\nNotes:")
    for n in notes:
        print(f"  • {n}")

    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(json.dumps({
            "format": a.format, "currency": a.currency, "tier": a.tier,
            "expected_views": views, "basis": basis,
            "anchor_views": anchor_views, "anchor_cpm_usd": round(anchor_cpm, 2),
            "cpm_used_usd": round(cpm, 2), "base_usd": round(base_usd, 2),
            "addons": [{"label": l, "pct": pct} for l, pct in applied],
            "uplift": uplift, "subtotal": round(subtotal, 2),
            "floor": floor, "floor_observed": obs, "quote": quote,
            "static_cpm_crosscheck_usd": round(static, 2), "notes": notes,
        }, indent=2), encoding="utf-8")
        print(f"\nWrote {a.out}")


if __name__ == "__main__":
    main()
