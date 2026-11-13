# Scene patterns

Copy-paste building blocks. Every snippet works with `assets/template.html` as-is.
Coordinates assume the 1600×900 stage: a scene's content box starts at (90, 64) and is about 1420×670. The timeline owns the bottom 100px.

## Contents
1. Statement build — lines appear, highlight, strike, ghost, follow-up
2. Chart that draws itself
3. Chapter map / agenda
4. Process stepper
5. Pipeline diagram (boxes + arrows)
6. Big number + ladder
7. Bar comparison
8. Numbered checklist (two columns)
9. Code / diff panel
10. Icon kit
11. Byline header, citation, ambient motion

---

## 1. Statement build

The workhorse. One clause per step, then the payoff word gets a marker sweep, then a wrong idea gets struck, then the whole thing ghosts so the next thought can sit under it.

```html
<section class="scene" data-chapter="Why now">
  <p class="lede">
    <span data-dim="5">All of our data infrastructure is built</span><br>
    <span data-step="1" data-dim="5">on the idea that <s data-fx="4">transformation</s></span><br>
    <span data-step="2" data-dim="5"><s data-fx="4">is <mark data-fx="3">expensive</mark>.</s></span>
  </p>
  <p class="lede" data-step="5" style="margin-top:60px">What if everybody had a <mark>transformer</mark>?</p>
</section>
```

Keep each `<s>` on one line (it is `nowrap`). A `<mark>` inside a `data-step` element sweeps in when its parent appears; give it its own `data-fx` to sweep later.

## 2. Chart that draws itself

Axes trace first, the curve next, then labelled points pop in one at a time. Swap an axis label by fading one out (`data-out`) while another fades in (`data-step`) on the same step.

```html
<section class="scene">
  <h1>The final bottleneck in transformation: <mark data-step="3">judgement</mark></h1>
  <svg class="sketch" width="1100" height="540" viewBox="0 0 1100 540">
    <g class="draw">
      <path class="ink" d="M60 20 V480 H1040"/>
      <path class="ink" d="M50 32 L60 20 L70 32 M1028 470 L1040 480 L1028 490"/>
    </g>
    <text x="74" y="34" class="t-it" font-size="17" data-out="3">capability ↑</text>
    <text x="74" y="34" class="t-it" font-size="17" data-step="3">judgement ↑</text>
    <text x="1040" y="512" class="t-it" font-size="17" text-anchor="end">cost →</text>
    <path class="ink draw" data-step="1" d="M130 470 C 210 250, 430 130, 980 80"/>
    <g data-step="4" class="pop"><circle cx="140" cy="440" r="8" class="fill-acc"/><text x="158" y="462" font-size="20" class="accent">Cheap model</text></g>
    <g data-step="5" class="pop"><circle cx="420" cy="170" r="7" class="fill-paper ink"/><text x="400" y="150" font-size="18" text-anchor="end">Mid model</text></g>
    <g data-step="6" class="pop"><circle cx="960" cy="83" r="7" class="fill-paper ink"/><text x="960" y="60" font-size="18" text-anchor="middle">Frontier</text></g>
    <text x="900" y="140" class="t-it accent" font-size="17" data-step="7">the Pareto frontier</text>
  </svg>
  <p class="src">pricing as of Oct 2026 · illustrative</p>
</section>
```

For real data, compute the path `d` from the numbers (a few lines of JS in a scratch script, or by hand for < 10 points) and paste the literal path. Keep charts sparse: one line, a handful of labelled points.

## 3. Chapter map / agenda

Each chapter appears as a small drawn thumbnail + timestamp kicker + title. Use it at the start, and reuse it between chapters: give the other cards `data-dim="1"` and swap the current card's `<mark>` in with `data-fx="1"`.

```html
<section class="scene">
  <div class="row" style="gap:40px;margin-top:120px">
    <div class="col" data-step="1" style="width:300px">
      <svg class="draw sketch" data-step="1" width="300" height="160" viewBox="0 0 300 160">
        <rect class="ink" x="10" y="10" width="130" height="80"/><rect class="ink" x="150" y="10" width="130" height="80"/>
        <circle class="ink acc" cx="145" cy="110" r="34"/><text x="145" y="116" text-anchor="middle" font-size="16">23 °C</text>
      </svg>
      <span class="label">§2 · 1:48</span>
      <span class="body" style="font-size:22px">Why single <mark>ontologies</mark> always fail</span>
    </div>
    <div class="col" data-step="2" style="width:300px">
      <!-- next chapter card: same shape -->
    </div>
  </div>
</section>
```

## 4. Process stepper

Numbered circles on a line. The current phase is filled with the accent and the detail for it builds underneath. Duplicate the scene per phase, changing which circle is `hi` and what builds below.

```html
<section class="scene" data-chapter="The six phases">
  <h1>The six phases</h1>
  <svg width="1400" height="160" viewBox="0 0 1400 160">
    <line class="ink thin" x1="60" y1="60" x2="1340" y2="60"/>
    <g font-size="18" text-anchor="middle">
      <circle class="ink fill-paper" cx="80"  cy="60" r="22"/><text x="80"  y="66">1</text><text x="80"  y="116">Spec and split</text>
      <circle class="ink acc fill-soft" cx="330" cy="60" r="26"/><text x="330" y="66" class="accent">2</text><text x="330" y="116">Decide the</text><text x="330" y="140">failure surface</text>
      <circle class="ink faint fill-paper" cx="580" cy="60" r="22"/><text x="580" y="66" class="muted">3</text><text x="580" y="116" class="muted">Bounded pilots</text>
      <!-- … -->
    </g>
  </svg>
  <div class="row" style="margin-top:50px" data-step="1">
    <div class="card" style="width:420px;height:150px"></div>
    <span class="label" style="margin-top:20px">— 200 held-out families</span>
  </div>
</section>
```

## 5. Pipeline diagram

Boxes trace in, then each arrow draws, then labels land. Put the arrowhead in the same path as its shaft (`M… H… M… L… L…`) so it draws last. Stagger with `--i` when a single `.draw` group holds many shapes.

```html
<section class="scene">
  <h1>Just-in-time ontologies</h1>
  <svg class="sketch" width="1400" height="420" viewBox="0 0 1400 420">
    <g class="draw"><circle class="ink" cx="120" cy="180" r="56"/><path class="ink" d="M120 145 L130 172 L157 180 L130 188 L120 215 L110 188 L83 180 L110 172 Z"/></g>
    <text x="120" y="275" text-anchor="middle" font-size="20">intelligence</text>
    <path class="ink draw" data-step="1" d="M190 180 H440 M428 172 L440 180 L428 188"/>
    <g class="draw" data-step="2">
      <rect class="ink acc" x="460" y="80" width="300" height="200"/>
      <rect class="ink thin" x="500" y="110" width="90" height="40"/><rect class="ink thin" x="630" y="110" width="90" height="40"/>
      <rect class="ink thin" x="565" y="200" width="90" height="40"/>
      <path class="ink thin" d="M590 130 H630 M545 150 V220 H565"/>
    </g>
    <text x="610" y="310" text-anchor="middle" font-size="20" data-step="2"><tspan class="accent">ontology</tspan></text>
    <path class="ink draw" data-step="3" d="M780 180 H1030 M1018 172 L1030 180 L1018 188"/>
    <g class="draw" data-step="4"><path class="ink" d="M1060 110 H1150 L1180 140 V260 H1060 Z M1150 110 V140 H1180"/><path class="ink acc" d="M1090 200 L1110 220 L1150 175"/></g>
    <text x="1120" y="300" text-anchor="middle" font-size="20" data-step="4">result</text>
  </svg>
</section>
```

## 6. Big number + ladder

A headline number on the left, a ladder of tiers on the right that climbs one rung per step.

```html
<section class="scene">
  <div class="row" style="gap:120px;margin-top:20px">
    <div class="col" style="width:380px">
      <span style="font:400 64px/1 var(--serif)">203,317</span>
      <span class="body" style="font-size:22px">cases, each labelled with what its answer rests on</span>
      <span class="body accent" style="font-size:22px" data-step="6">18,374 checked by a second model</span>
    </div>
    <div class="col" style="gap:26px">
      <div data-step="5"><b class="accent" style="font-weight:500">Frontier</b><br><span class="label">335 settled · the last word</span></div>
      <div data-step="4"><b style="font-weight:500">Mid tier</b><br><span class="label">12,112 cases settled</span></div>
      <div data-step="3"><b style="font-weight:500">Cheap second opinion</b><br><span class="label">20,280 second opinions</span></div>
      <div data-step="2"><b style="font-weight:500">Cheap first pass</b><br><span class="label">first answer · 146,759 cases</span></div>
      <div data-step="1"><b style="font-weight:500">Rules in code</b><br><span class="label">bundles duplicates · guards every answer</span></div>
    </div>
  </div>
</section>
```

## 7. Bar comparison

Hatched bars grow from the left (`.draw` on a `rect` with a hatch fill traces the outline, then the fill fades in). A rubber-stamp label lands on the failures.

```html
<section class="scene">
  <div class="row" style="justify-content:space-between"><h1>Big migrations</h1><span class="label">bar lengths illustrative</span></div>
  <svg width="1400" height="420" viewBox="0 0 1400 420" class="sketch">
    <g font-size="20">
      <text x="0" y="40">Lidl → SAP</text><text x="0" y="64" class="t-mono">~€500M · 2011–2018</text>
      <rect class="ink draw" data-step="1" x="420" y="22" width="820" height="34" style="fill:url(#hatch)"/>
      <g data-step="2" class="pop"><rect x="1000" y="26" width="140" height="26" class="ink warn thin fill-paper"/><text x="1070" y="45" text-anchor="middle" class="t-mono warn" font-size="13">ABANDONED</text></g>
      <!-- repeat rows at y += 90 -->
    </g>
  </svg>
</section>
```

## 8. Numbered checklist

Two columns of numbered items, each item = title + one muted line. Reveal items one per step only if you'll talk to each one; otherwise reveal the whole list in one step.

```html
<section class="scene">
  <h1>Ten useful checks</h1>
  <div class="row" style="gap:90px">
    <ol class="col" style="list-style:none;gap:22px;width:600px">
      <li data-step="1" class="row" style="gap:22px"><span class="label accent">1</span><div><b style="font-weight:500;font-size:21px">look before you transform</b><div class="small" style="font-size:17px">List each column's real values before writing code for them.</div></div></li>
      <!-- … -->
    </ol>
    <ol class="col" style="list-style:none;gap:22px;width:600px"><!-- 6–10 --></ol>
  </div>
</section>
```

## 9. Code / diff panel

Mono text on a faint panel. Removed lines get a pink wash, added lines a green wash. Two panels side by side compare iterations.

```html
<section class="scene">
  <h1>The resolving step, two iterations</h1>
  <div class="row" style="gap:30px">
    <pre data-step="1" style="flex:1;font:14px/1.7 var(--mono);background:#f4f4f1;padding:18px 20px;white-space:pre-wrap">
<span style="background:#f6dede;display:block">- MODEL cheap-model FRESH</span>  PROMPT prompt.txt
<span style="background:#f6dede;display:block">-   MAX $0.75</span></pre>
    <pre data-step="2" style="flex:1;font:14px/1.7 var(--mono);background:#f4f4f1;padding:18px 20px;white-space:pre-wrap">
<span style="background:var(--accent-soft);display:block">+ MODEL set-per-session FRESH</span>  PROMPT prompt.txt
<span style="background:var(--accent-soft);display:block">+   MAX $1.00</span></pre>
  </div>
</section>
```

## 10. Icon kit

Draw icons as a few `.ink` strokes inside a `.draw` group so they trace themselves. Keep them geometric and 40–120px. Starters (each assumes its own `<svg viewBox="0 0 100 100">`):

```html
<!-- database -->   <g class="draw"><ellipse class="ink" cx="50" cy="20" rx="35" ry="10"/><path class="ink" d="M15 20 V80 A35 10 0 0 0 85 80 V20 M15 50 A35 10 0 0 0 85 50"/></g>
<!-- document -->   <g class="draw"><path class="ink" d="M25 10 H65 L80 25 V90 H25 Z M65 10 V25 H80 M35 45 H70 M35 58 H70 M35 71 H58"/></g>
<!-- loop arrow --> <g class="draw spin"><path class="ink" d="M80 50 A30 30 0 1 1 65 24 M58 14 L67 24 L55 30"/></g>
<!-- gear -->       <g class="draw"><circle class="ink acc" cx="50" cy="50" r="14"/><path class="ink acc" d="M50 18 V28 M50 72 V82 M18 50 H28 M72 50 H82 M27 27 L34 34 M66 66 L73 73 M27 73 L34 66 M66 34 L73 27"/><circle class="ink acc" cx="50" cy="50" r="26"/></g>
<!-- person -->     <g class="draw"><circle class="ink" cx="50" cy="30" r="14"/><path class="ink" d="M22 88 C22 62 78 62 78 88"/></g>
<!-- check -->      <path class="ink acc draw" d="M22 52 L42 72 L80 30"/>
<!-- question -->   <g class="draw"><circle class="ink thin" cx="50" cy="50" r="38" stroke-dasharray="4 5"/><text x="50" y="58" text-anchor="middle" class="t-it" font-size="24">?</text></g>
```

A shape with an authored `stroke-dasharray` (like the dashed circle) keeps its dashes and fades in instead of tracing.

## 11. Byline header, citation, ambient motion

```html
<!-- byline: top-left of the opening scene; paste a copy of the #mascot <svg> markup in place of the comment -->
<div class="row" style="gap:12px;align-items:center;margin-bottom:24px">
  <!-- mascot svg copy, width="32" height="32" -->
  <span class="label">Your Name · Your Company</span>
</div>

<!-- citation: bottom-left of any scene that shows a number or a borrowed idea -->
<p class="src">source: Southbridge · run logs, 16–27 Sep 2026</p>

<!-- motion that keeps going while you talk -->
<g class="spin">…</g>   <div class="float">…</div>
```

Pattern fills: `.ink` sets `fill:none` in CSS, which beats a `fill="…"` attribute. Put pattern or colour fills in `style="fill:…"` or use the `fill-*` classes. On `<text>`, `fill=` and `font-size=` attributes work; the `accent`/`muted`/`warn` classes colour text only.
