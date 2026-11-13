---
name: scene-deck
description: Build a talk as one self-contained HTML "scene deck" in the style of Hrishi Olickel's AI Engineer talk, with no slides. Each keypress advances a step, and steps build hand-drawn SVG scenes (strokes trace themselves, words get a marker sweep, wrong ideas get struck through, old content ghosts out). A chapter timeline runs along the bottom with a little mascot walking along it, and you can click or drag it to scrub. Use this whenever the user wants an animated or "interactive" presentation, a talk or video explainer deck that builds as they speak, slides "like that Hrishi talk", a presentation with a timeline at the bottom, a storyboard-style deck to record a YouTube or course video over, or says "scene deck", "not slides, an animation", or "make my talk move". Prefer marp-slides for conventional static slide decks and hyperframes for rendered MP4 video.
---

# Scene deck

A scene deck is a single HTML file that plays a talk as a sequence of **steps** rather than slides. Every step is one beat of narration: one thing appears, draws, highlights, strikes or fades. Scenes are the visual canvases those steps build on. Chapters group scenes, and the bottom timeline places a numbered dot where each chapter starts. Dots sit far apart when a chapter has many steps. An owl mascot waddles to the current step.

The format comes from Hrishi Olickel's "Just-in-Time Ontologies" talk (AI Engineer, 2026). No source for his deck is public, so this skill reconstructs the look and mechanics from the recording. The aesthetic is a white page, a serif voice, mono labels, ink line drawings with a slight hand wobble, one green accent, mint marker highlights, and red strikes for wrong ideas.

## Files

- `assets/template.html`: the engine (CSS + ~100 lines JS) with one placeholder scene. Copy it and replace everything between `SCENES START` and `SCENES END`. Leave the engine alone.
- `references/patterns.md`: copy-paste scenes (statement build, self-drawing chart, chapter map, stepper, pipeline diagram, big number, bars, checklist, code diff, icon kit). Read it before writing scenes.
- `scripts/snapshot.py`: renders each scene at its final step, writes a contact sheet, and flags overflow and console errors. Run it with `uv run`.

## Workflow

### 1. Get the content

Take whatever the user has: a script, an outline, notes, a blog post, a transcript, or just a topic. If they only gave a topic, draft the argument yourself and keep moving. Ask only when the talk's point is unclear. Use sensible defaults for length (about 15 minutes) and audience (technical).

### 2. Write the beat sheet first

Write `<deck-name>-beats.md` next to the deck. It is the storyboard and doubles as speaker notes, so keep it editable:

```markdown
## 1 · Why now
### Scene: infrastructure assumption
1. "All of our data infrastructure is built…" (line 1 visible on entry)
2. "…on the idea that transformation…" (line 2 fades in)
3. "…is expensive." (line 3; marker sweeps "expensive")
4. "That idea is dead." (strike through "transformation is expensive")
```

Each numbered beat is one keypress, so it should match one spoken sentence or clause. This mapping makes the deck feel alive: the picture changes exactly when the speaker's point lands. Rough density: 3–9 steps per scene, 1–4 scenes per chapter, and about 8–12 steps per minute of talk (5–9 chapters for a 15–20 minute talk, 3–4 for a short one).

### 3. Build the deck

Copy the template to the destination (the user's folder, or the current project if none is named), set `<title>`, and write scenes using the patterns. The engine's whole vocabulary:

| Attribute / class | Effect |
|---|---|
| `<section class="scene" data-chapter="Title">` | A scene. `data-chapter` starts a new chapter dot on the timeline. Scenes without it continue the current chapter. |
| `data-step="n"` | Hidden until local step *n*, then fades up. Step 0 means "visible as the scene enters". |
| `data-fx="n"` | Always visible; its effect fires at *n*: a `<mark>` sweeps, an `<s>` strikes, a `.glow` turns accent. |
| `data-dim="n"` | Ghosts to 18% opacity at *n*. Use it to keep context on screen while the next idea builds under it. |
| `data-out="n"` | Disappears at *n*. Pair it with a `data-step` at the same *n* to swap one thing for another. |
| `.draw` | On any SVG shape or group: strokes trace themselves, children stagger, fills and `<text>` fade in after. |
| `.sketch` | Hand-drawn wobble filter for an `<svg>` or group. Leave it off text-heavy SVGs. |
| `.pop` | Scale-in instead of fade-up (labelled points, stamps). |
| `.spin` / `.float` | Ambient motion that loops while you talk. Use it sparingly, for "repeat" or "alive" ideas. |
| `.ink` (+ `.acc` `.warn` `.thin` `.faint`) | SVG line style. `fill-acc` `fill-soft` `fill-paper` `fill-ink` set fills. `.accent` `.muted` `.warn` colour SVG text. |
| `.glow` + `data-fx="n"` | Turns text, borders or strokes accent at *n*. |
| `.lede` `.body` `.small` `.label` `.kicker` `h1` `.src` | Type scale. `.src` is the italic citation pinned bottom-left. |
| `.row` `.col` `.card` `.abs` | Layout helpers. `.abs` + `style="left:…;top:…"` positions freely on the stage. |

A scene's step count is the highest number used in it. Number steps per scene, starting at 1. Gaps are fine but waste a keypress.

### 4. Check it

```bash
uv run ~/.claude/skills/scene-deck/scripts/snapshot.py path/to/deck.html
```

Read `contact.png` (and any single shot that looks off). Fix every overflow the script reports and every console error. Then look for the design failures the script can't see: crowded scenes, text colliding with drawings, a scene showing everything at step 0, unreadable small text. Add `--all-steps` to inspect one scene's build closely.

### 5. Open it

`open path/to/deck.html`. Tell the user the controls: → / space / clicker next, ← back, 1–9 jump to chapter, click or drag the timeline to scrub, `f` fullscreen. The URL hash holds the step, so reloading after an edit keeps their place.

## Style: what makes it look like this

- **One idea per scene, built in public.** Never show the finished scene on entry. The audience should watch the argument assemble. Step 0 is usually just a title or the first clause.
- **Draw it instead of listing it.** Turn bullets into a diagram, a chart, boxes and arrows, a row of icons. Text-only scenes are reserved for statements set in large `.lede` serif.
- **Color carries meaning.** Ink for neutral, the green accent for "the thing we're recommending / the current position", mint `<mark>` for the word to remember, red `<s>` for the idea being retired. Keep everything else grey.
- **Ghost, don't delete.** When the next point builds on the last one, `data-dim` the old content and put the new line underneath.
- **Real numbers, cited.** Concrete figures beat adjectives. Put the source in `.src` at the bottom-left.
- **Quiet layout.** Lots of white, left-aligned, small mono labels, thin lines. Most scenes use under half the canvas.
- **Motion is a verb.** Each step's animation should mean something (a line draws because the process flows, a strike lands because the idea is wrong). The engine's default easing is enough. Skip fancy entrances.

## Theming

Default to the original look above. Swap the `:root` tokens only when the user asks for their brand. Example: the Automata Learning Lab brand uses:

```css
--paper:#ffffff; --ink:#111111; --accent:#0B6E4F; --accent-soft:#e2f0ea; --mark:#bfe6d4; --warn:#C8102E;
--serif:'Archivo',system-ui,sans-serif; --mono:'IBM Plex Mono',ui-monospace,monospace;
```

and change the Google Fonts link to `family=Archivo:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500`. Replace the owl in `#mascot` with any ~32×32 inline SVG. The whole mascot waddles while it moves, and anything with `class="eye"` blinks.

## Gotchas

- `data-step` on inline `<span>`s fades but can't slide (inline elements ignore transforms). This is expected.
- Keep each `<s>` within one line, because it doesn't wrap.
- A `.draw` group with dozens of shapes staggers up to 1.4s. Split it, or set `style="--i:0"` on shapes that should draw together.
- Everything must fit the 1420×670 content box (x 90–1510, y 64–736 on the 1600×900 stage; the timeline owns the bottom 100px). The snapshot script flags anything more than 15px outside it. `.src` citations may sit in the bottom padding.
- `.ink` sets `fill:none` in CSS, so for a filled box use `ink fill-paper` (or `style="fill:…"`). A `fill=` attribute won't work there.
- `.ink` also sets `stroke-width` in CSS, so a `stroke-width=` attribute is ignored on `.ink` shapes. Use `style="stroke-width:3"`.
- A `.draw` with no `data-step` draws at step 0. If its parent appears later, the drawing happens while hidden. Give the `.draw` the same `data-step` as its parent so it traces when it appears.
- The deck needs network access only for Google Fonts. Offline, it falls back to Georgia and Menlo.

## Recording a video over it

Present it full-screen in Chrome and record with a screen recorder plus a webcam overlay (Screen Studio, OBS, or Loom), the way the original talk was recorded. Advance on the beat each time a sentence lands. Use `<deck>-beats.md` as the teleprompter.
