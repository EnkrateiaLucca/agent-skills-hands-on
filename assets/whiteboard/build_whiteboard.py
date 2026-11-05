# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Build agent-skills-whiteboard.excalidraw: a class map + 8 slide frames.

Run: uv run build_whiteboard.py
"""
import json
import random
import textwrap
from pathlib import Path

random.seed(7)

# Semantic palette, same meaning on every slide (see legend on the class map)
INK, GRAY, MUTED = "#1e1e1e", "#868e96", "#495057"
USER = ("#1971c2", "#d0ebff")
AI = ("#6741d9", "#e5dbff")
TOOL = ("#e8590c", "#ffe8cc")
SKILL = ("#0c8599", "#c3fae8")
PROBLEM = ("#e03131", "#ffe3e3")
FIX = ("#2f9e44", "#d3f9d8")
KEY = ("#f08c00", "#fff3bf")
NEUTRAL = ("#495057", "#f1f3f5")
DARK = "#1e1e1e"

FW, FH, GAP = 1600, 1000, 250
CHAR_W = {5: 0.48, 6: 0.5, 3: 0.6}

elements: list[dict] = []
_frame = {"id": None, "ox": 0, "oy": 0, "children": []}


def _id():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=16))


def _base(kind, x, y, w, h, stroke, bg="transparent", **kw):
    el = {
        "id": _id(), "type": kind,
        "x": x + _frame["ox"], "y": y + _frame["oy"], "width": w, "height": h,
        "angle": 0, "strokeColor": stroke, "backgroundColor": bg,
        "fillStyle": kw.pop("fill", "solid"), "strokeWidth": kw.pop("sw", 2),
        "strokeStyle": kw.pop("style", "solid"), "roughness": kw.pop("rough", 1),
        "opacity": 100, "groupIds": [], "frameId": _frame["id"],
        "roundness": kw.pop("roundness", None),
        "seed": random.randint(1, 2**31), "version": 1,
        "versionNonce": random.randint(1, 2**31), "isDeleted": False,
        "boundElements": [], "updated": 1, "link": None, "locked": False,
    }
    el.update(kw)
    (_frame["children"] if _frame["id"] else elements).append(el)
    return el


def _wrap(s, width, fs, ff):
    per_line = max(4, int(width / (fs * CHAR_W[ff])))
    return "\n".join(
        "\n".join(textwrap.wrap(p, per_line)) if p else "" for p in s.split("\n")
    )


def _dims(s, fs, ff):
    lines = s.split("\n")
    # overestimate width: the renderer clips text to its box, centering stays exact
    return max(len(l) for l in lines) * fs * CHAR_W[ff] * 1.3, len(lines) * fs * 1.25


def text(x, y, s, fs=20, color=INK, align="left", ff=5, wrap=None):
    if wrap:
        s = _wrap(s, wrap, fs, ff)
    w, h = _dims(s, fs, ff)
    if align == "center":
        x -= w / 2
    return _base("text", x, y, w, h, color, text=s, originalText=s, fontSize=fs,
                 fontFamily=ff, textAlign=align, verticalAlign="top",
                 containerId=None, lineHeight=1.25, autoResize=True)


def shape(kind, x, y, w, h, colors=NEUTRAL, label=None, fs=20, tcolor=None,
          ff=5, align="center", valign="middle", **kw):
    stroke, bg = colors
    if kind == "rectangle":
        kw.setdefault("roundness", {"type": 3})
    elif kind != "frame":
        kw.setdefault("roundness", {"type": 2})
    el = _base(kind, x, y, w, h, stroke, bg, **kw)
    if label:
        pad = 0.62 if kind in ("ellipse", "diamond") else 0.9
        s = _wrap(label, w * pad - 10, fs, ff)
        tw, th = _dims(s, fs, ff)
        tx = x + (w - tw) / 2 if align == "center" else x + 12
        ty = y + (h - th) / 2 if valign == "middle" else y + 12
        t = _base("text", tx, ty, tw, th, tcolor or stroke, text=s, originalText=s,
                  fontSize=fs, fontFamily=ff, textAlign=align, verticalAlign=valign,
                  containerId=el["id"], lineHeight=1.25, autoResize=True)
        el["boundElements"].append({"id": t["id"], "type": "text"})
    return el


def rect(*a, **k): return shape("rectangle", *a, **k)
def ellipse(*a, **k): return shape("ellipse", *a, **k)
def diamond(*a, **k): return shape("diamond", *a, **k)


def arrow(pts, color=INK, head="arrow", kind="arrow", **kw):
    kw.setdefault("roundness", {"type": 2})
    x0, y0 = pts[0]
    rel = [[px - x0, py - y0] for px, py in pts]
    xs, ys = [p[0] for p in rel], [p[1] for p in rel]
    return _base(kind, x0, y0, max(xs) - min(xs), max(ys) - min(ys), color,
                 points=rel, lastCommittedPoint=None, startBinding=None,
                 endBinding=None, startArrowhead=None,
                 endArrowhead=head if kind == "arrow" else None, elbowed=False, **kw)


def placeholder(x, y, w, h, what):
    rect(x, y, w, h, (GRAY, "#f8f9fa"), f"[ screenshot ]\n{what}", fs=18,
         tcolor=GRAY, style="dashed")


def dark_box(x, y, w, h, s, fs=16):
    rect(x, y, w, h, (DARK, DARK), s, fs=fs, tcolor="#f8f9fa", ff=6,
         align="left", valign="top", roundness={"type": 3})


class Frame:
    def __init__(self, col, row, name):
        self.name, self.ox, self.oy = name, col * (FW + GAP), row * (FH + GAP)

    def __enter__(self):
        _frame.update(id=_id(), ox=self.ox, oy=self.oy, children=[])
        return self

    def __exit__(self, *exc):
        fid = _frame["id"]
        elements.extend(_frame["children"])  # children sit below their frame
        _frame.update(id=None, ox=0, oy=0, children=[])
        _base("frame", self.ox, self.oy, FW, FH, "#bbb", roundness=None,
              name=self.name, id=fid)


def header(num, part, title, question):
    ellipse(50, 35, 84, 84, (DARK, DARK), str(num), fs=40, tcolor="#ffffff")
    text(155, 28, part, fs=18, color=GRAY)
    text(155, 52, title, fs=46)
    text(155, 115, question, fs=24, color=MUTED)


def key_idea(s):
    rect(60, 880, 1480, 84, KEY, f"Key idea: {s}", fs=26, tcolor=INK, sw=3)


P1, P2, P3 = ("PART 1 · HOW LLMs READ TEXT", "PART 2 · AGENT SKILLS",
              "PART 3 · USING IT WELL")

# ------------------------------------------------------------------ class map
with Frame(0, 0, "0 · Class map"):
    text(60, 50, "Agent Skills Hands-On", fs=64)
    text(60, 135, "Class map · the story runs left to right", fs=28, color=MUTED)
    parts = [
        ("PART 1 · The constraint", "How LLMs read text", [
            "1 · It's all text (and tokens)", "2 · What fills the context window",
            "3 · What happens when it's full", "4 · Context rot & how to fight it"]),
        ("PART 2 · The solution", "Agent Skills", [
            "5 · A skill is just a directory", "6 · Progressive disclosure"]),
        ("PART 3 · Using it well", "Products & prompts", [
            "7 · Product > Harness > Model", "8 · Prompting that works"]),
    ]
    for i, (tag, sub, slides) in enumerate(parts):
        x = 60 + i * 510
        rect(x, 210, 450, 110, (DARK, "#ffffff"), f"{tag}\n{sub}", fs=28, tcolor=INK, sw=3)
        for j, s in enumerate(slides):
            rect(x + 25, 345 + j * 82, 400, 64, NEUTRAL, s, fs=22, tcolor=INK)
        if i < 2:
            arrow([(x + 455, 265), (x + 505, 265)], sw=3)
    rect(60, 690, 1480, 70, KEY,
         "Context is limited  →  skills load expertise only when needed  →  "
         "pick the right product & prompt well", fs=26, tcolor=INK, sw=3)
    text(60, 800, "Color code used on every slide", fs=24, color=MUTED)
    legend = [("You / user", USER), ("AI / model", AI), ("Tools & connectors", TOOL),
              ("Skills", SKILL), ("Problem", PROBLEM), ("Fix", FIX), ("Key idea", KEY)]
    for i, (lbl, c) in enumerate(legend):
        rect(60 + i * 212, 845, 195, 60, c, lbl, fs=20, tcolor=INK)

# ------------------------------------------------------------------ slide 1
with Frame(1, 0, "1 · It's all text"):
    header(1, P1, "It's all text", "What does an LLM actually see and produce?")
    # a. text in, text out
    text(60, 180, "a · Text in, text out", fs=22, color=MUTED)
    rect(80, 230, 170, 70, USER, "You", fs=28)
    rect(430, 230, 170, 70, AI, "AI", fs=28)
    arrow([(255, 250), (425, 250)], USER[0], sw=2)
    text(340, 218, "input text", fs=18, color=USER[0], align="center")
    arrow([(515, 305), (340, 345), (165, 305)], AI[0], sw=2)
    text(340, 350, "output text", fs=18, color=AI[0], align="center")
    # b. tokens
    text(60, 410, "b · It writes one token at a time", fs=22, color=MUTED)
    rect(60, 455, 150, 60, NEUTRAL, "your text", fs=20)
    arrow([(215, 485), (265, 485)])
    rect(270, 455, 110, 60, AI, "LLM", fs=24)
    arrow([(385, 485), (430, 485)])
    for i, tok in enumerate(["The", "cat", "sat"]):
        rect(435 + i * 58, 463, 52, 44, AI, tok, fs=18)
    text(612, 470, "…", fs=28, color=AI[0])
    rect(60, 540, 580, 100, NEUTRAL,
         "1 token ≈ a word or a piece of a word (~¾ of a word)\n"
         "\"unbelievable\" → un · believ · able", fs=20, tcolor=INK)
    # c. scale
    text(60, 670, "c · How big is 1 million tokens?", fs=22, color=MUTED)
    for i, (x, w, s) in enumerate([(60, 150, "1M tokens"), (250, 170, "~750k words"),
                                   (460, 180, "~1,500 pages")]):
        rect(x, 715, w, 70, NEUTRAL, s, fs=22, tcolor=INK)
        if i:
            text(x - 22, 727, "≈", fs=32)
    text(60, 800, "(at ~500 words per page)", fs=16, color=GRAY)
    # context window
    rect(700, 172, 850, 62, NEUTRAL,
         "Context window = the max amount of text an LLM can process at once",
         fs=24, tcolor=INK, sw=3)
    text(722, 252, "context window", fs=20, color=MUTED)
    text(935, 252, "128k · 200k · 1M tokens", fs=20, color=INK)
    rect(720, 285, 400, 550, (INK, "transparent"), style="dashed", sw=2)
    y = 300
    for lbl, c, h in [("system message", NEUTRAL, 55), ("user msg", USER, 50),
                      ("AI msg", AI, 70), ("user msg", USER, 50),
                      ("tool call", TOOL, 50), ("tool output", TOOL, 110),
                      ("AI msg", AI, 70)]:
        rect(745, y, 350, h, c, lbl, fs=20)
        y += h + 10
    rect(1160, 290, 390, 140, KEY,
         "Every time it answers, the LLM re-reads ALL of this, from the very "
         "first message.", fs=22, tcolor=INK)
    arrow([(1155, 360), (1125, 360)], KEY[0], sw=3)
    diamond(1170, 470, 180, 120, PROBLEM, "over the limit?", fs=18)
    arrow([(1345, 510), (1395, 475)], FIX[0])
    arrow([(1345, 550), (1395, 600)], FIX[0])
    text(1352, 462, "yes", fs=16, color=GRAY)
    rect(1400, 445, 150, 55, FIX, "start fresh", fs=18)
    rect(1400, 575, 150, 75, FIX, "carry over outputs", fs=18)
    rect(1160, 690, 390, 140, PROBLEM,
         "Long before the limit: the longer the text, the harder it is to "
         "connect every piece to every other piece.", fs=20, tcolor=INK)
    key_idea("LLMs only see text. Messages, replies and tool results pile up "
             "in one limited window that is re-read every turn.")

# ------------------------------------------------------------------ slide 2
with Frame(2, 0, "2 · What fills the window"):
    header(2, P1, "What fills the context window", "Anatomy of one real chat")
    # token gauge
    text(60, 180, "tokens used", fs=18, color=MUTED)
    rect(80, 220, 90, 600, (INK, "transparent"), roundness=None)
    arrow([(70, 235), (180, 235)], PROBLEM[0], kind="line", style="dashed", sw=3)
    text(185, 222, "limit", fs=20, color=PROBLEM[0])
    y = 820
    for lbl, c, h in [("system", NEUTRAL, 30), ("user", USER, 25), ("thinking", AI, 55),
                      ("AI msg", AI, 70), ("search\nresults", TOOL, 210)]:
        y -= h
        rect(82, y, 86, h, (c[0], c[1]), roundness=None, sw=1,
             fill="hachure" if lbl == "thinking" else "solid")
        text(180, y + h / 2 - 10, lbl, fs=16, color=c[0])
    # the window
    rect(320, 185, 800, 655, (INK, "#ffffff"), sw=3)
    text(340, 195, "context window", fs=20, color=MUTED)
    rect(350, 235, 570, 130, (USER[0], "transparent"), sw=3)
    dark_box(368, 250, 534, 100,
             "Hi! What do you think everyone should know about AI to use it well "
             "on a day-to-day basis? Like non-technical folks who want to level up?")
    rect(350, 385, 570, 220, (AI[0], "transparent"), sw=3)
    dark_box(368, 400, 534, 190,
             "I'll share what I think matters for non-technical folks using AI "
             "daily, but I want to flag upfront that some of this is [inference]...\n\n"
             "Mental models that seem to help:\n"
             "1. AI is a thinking partner, not an oracle. People often treat AI "
             "like a search engine (\"give me the answer\")…")
    rect(350, 625, 570, 195, (TOOL[0], "transparent"), sw=3)
    dark_box(368, 640, 534, 165,
             "✻ Thinking about synthesizing core AI literacy concepts…\n\n"
             "I need to search for top AI concepts from academic papers and "
             "reputable substacks…\n\n⊕ Searching the web")
    text(945, 270, "user msg", fs=32, color=USER[0])
    text(945, 425, "AI msg", fs=32, color=AI[0])
    text(945, 475, "+ hidden thinking\ntokens take space\ntoo", fs=17, color=AI[0])
    text(945, 650, "search\ntool use", fs=30, color=TOOL[0])
    text(945, 735, "results land in\nthe window too", fs=17, color=TOOL[0])
    text(1160, 230, "There is a limit\nto this window", fs=36)
    rect(1160, 380, 390, 190, (USER[0], "#ffffff"),
         "Ask the class: which of the three parts eats the most tokens? "
         "(Hint: check the bar on the left.)", fs=22, tcolor=INK, style="dashed")
    rect(1160, 610, 390, 160, PROBLEM,
         "You never see most of it: thinking and search results fill the window "
         "silently.", fs=21, tcolor=INK)
    key_idea("Every message, every hidden thinking step and every tool result "
             "costs space in the same window.")

# ------------------------------------------------------------------ slide 3
with Frame(0, 1, "3 · When the window gets full"):
    header(3, P1, "When the window gets full",
           "Three things that happen as context piles up")
    rect(480, 185, 640, 110, (INK, "#ffffff"),
         "How much can we put inside the context window, and what does it cost us?",
         fs=26, tcolor=INK, sw=3)
    arrow([(620, 300), (260, 395)], PROBLEM[0], sw=3)
    arrow([(800, 300), (800, 395)], PROBLEM[0], sw=3)
    arrow([(980, 300), (1340, 395)], PROBLEM[0], sw=3)
    cards = [
        ("Gets lost", "Too many instructions at once: it quietly drops some of them."),
        ("Hallucinates more", "More context makes it more likely to invent details "
                              "or mix up sources."),
        ("Slower & costlier", "Time to the first answer token grows, because it must "
                              "process the whole window first. Every turn re-consumes "
                              "all those tokens."),
    ]
    for i, (h, b) in enumerate(cards):
        x = 60 + i * 540
        rect(x, 400, 400, 240, PROBLEM)
        text(x + 200, 418, h, fs=30, color=PROBLEM[0], align="center")
        text(x + 25, 475, b, fs=24, wrap=350)
    rect(200, 680, 1200, 150, (PROBLEM[0], "#ffc9c9"),
         "One chat for everything? One never-ending chat for a whole project?\n"
         "Period. You're using AI wrong!", fs=32, tcolor=INK, sw=4)
    key_idea("More context isn't free: quality drops, errors rise and every "
             "reply gets slower.")

# ------------------------------------------------------------------ slide 4
with Frame(1, 1, "4 · Context rot"):
    header(4, P1, "Context rot", "Why long chats get worse, and what to do about it")
    rect(60, 180, 500, 310, NEUTRAL)
    arrow([(110, 205), (110, 455), (530, 455)], INK, kind="line",
          roundness=None, sw=2)
    text(70, 190, "perf", fs=20)
    text(400, 462, "input size →", fs=18)
    arrow([(125, 225), (170, 235), (205, 230), (250, 290), (290, 280), (340, 350),
           (380, 340), (430, 405), (500, 430)], PROBLEM[0], sw=3)
    text(230, 200, "with nuance: varies by model & task", fs=16, color=GRAY)
    text(60, 505, "Context rot = quality decays as the input grows", fs=22,
         color=PROBLEM[0])
    text(60, 570, "How much can we really use?", fs=22, color=MUTED)
    rect(60, 610, 250, 55, FIX, "sweet spot ~70k?", fs=18, roundness=None)
    rect(310, 610, 150, 55, KEY, "120–150k", fs=18, roundness=None)
    rect(460, 610, 100, 55, PROBLEM, "limit", fs=18, roundness=None)
    text(60, 690, "1 token ≈ ¾ of a word", fs=22)
    text(60, 725, "→ 70k tokens ≈ 52k words ≈ a short novel", fs=18, color=MUTED)
    placeholder(600, 180, 370, 260, "plans & their context limits")
    placeholder(600, 480, 370, 260, "web search results: they occupy a lot of space!")
    arrow([(975, 240), (1005, 240)], FIX[0], sw=3)
    text(1010, 180, "What can we do about context rot?", fs=30, color=FIX[0])
    fixes = [
        ("1 · Carry over outputs", "Ask for a summary of the conversation, then "
                                   "paste it into a brand-new chat."),
        ("2 · Use Projects", "Keep shared files and instructions in a Project, so "
                             "each chat stays short and focused."),
        ("3 · Leave breadcrumbs", "Copy the link to a chat and paste it into the "
                                  "relevant doc: a session trace you can return to."),
    ]
    for i, (h, b) in enumerate(fixes):
        y = 250 + i * 195
        rect(1010, y, 540, 170, FIX)
        text(1035, y + 15, h, fs=28, color=FIX[0])
        text(1035, y + 62, b, fs=21, wrap=490)
    key_idea("Treat chats as disposable: keep them short and focused, and carry "
             "over only what matters.")

# ------------------------------------------------------------------ slide 5
with Frame(2, 1, "5 · Agent Skill = a directory"):
    header(5, P2, "Why Agent Skills?",
           "How do we give an agent real domain expertise?")
    ellipse(60, 170, 640, 240, (GRAY, "#f8f9fa"),
            "How do we bring domain expertise into an agent so it can use it "
            "to execute the task?", fs=24, tcolor=INK)
    arrow([(380, 410), (380, 445)], SKILL[0], sw=3)
    text(760, 175, "Why?", fs=40)
    for x, c, h, b in [(760, PROBLEM, "Without skills", "You re-explain your expertise "
                        "in every chat, and it fills up the context window."),
                       (1170, FIX, "With skills", "Write your expertise once. The "
                        "agent loads it only when the task needs it.")]:
        rect(x, 235, 380, 180, c)
        text(x + 190, 250, h, fs=26, color=c[0], align="center")
        text(x + 22, 295, b, fs=21, wrap=340)
    arrow([(1143, 325), (1167, 325)], sw=3)
    text(60, 450, "Agent Skill = a directory", fs=40, color=SKILL[0])
    rect(60, 510, 1000, 210, (DARK, DARK))
    items = [("SKILL.md", "instructions\n(the recipe)", FIX[0]),
             ("references/", "reference files\n(read when needed)", TOOL[0]),
             ("scripts/", "code to execute\nspecific actions", PROBLEM[0]),
             ("assets/", "files to reuse in the\noutput (templates, logos)", USER[0])]
    for i, (name, desc, color) in enumerate(items):
        cx = 185 + i * 250
        if i == 0:
            rect(cx - 40, 535, 80, 100, ("#dee2e6", "#f8f9fa"), roundness=None)
        else:
            rect(cx - 55, 545, 45, 18, ("#1971c2", "#4dabf7"))
            rect(cx - 55, 555, 110, 80, ("#1971c2", "#74c0fc"))
        text(cx, 655, name, fs=22, color="#ffffff", align="center")
        text(cx, 740, desc, fs=20, color=color, align="center")
    text(60, 815, "only SKILL.md is required", fs=16, color=GRAY)
    text(1100, 440, "peek inside SKILL.md", fs=18, color=MUTED)
    rect(1100, 470, 450, 360, (DARK, DARK),
         "---\nname: pdf\ndescription: Use this skill\n  whenever the user wants\n"
         "  to do anything with PDFs\n---\n# PDF processing\n"
         "1. Check what the user needs\n2. Forms? read\n   references/forms.md\n"
         "3. Run scripts/fill_form.py", fs=20, tcolor="#f8f9fa", ff=3,
         align="left", valign="top")
    key_idea("A skill is a folder of instructions, references, scripts and assets "
             "the agent can pick up when a task calls for it.")

# ------------------------------------------------------------------ slide 6
with Frame(0, 2, "6 · Progressive disclosure"):
    header(6, P2, "Progressive disclosure",
           "How can an agent have many skills without filling its context?")
    levels = [("Level 1 · Metadata", "name + description, always in the system prompt",
               "~100 tokens per skill", "#e6fcf5"),
              ("Level 2 · Full SKILL.md", "loaded when the skill is triggered",
               "usually < 5k tokens", "#c3fae8"),
              ("Level 3+ · Linked files", "references & scripts, read only as needed",
               "only what's needed", "#96f2d7")]
    for i, (h, b, cost, bg) in enumerate(levels):
        x = 60 + i * 560
        rect(x, 180, 360, 170, (SKILL[0], bg), sw=3)
        text(x + 180, 195, h, fs=26, color=SKILL[0], align="center")
        text(x + 25, 245, b, fs=21, wrap=310)
        text(x + 180, 362, cost, fs=18, color=SKILL[0], align="center")
    for x, q in [(425, "skill relevant?"), (985, "need more detail?")]:
        arrow([(x, 265), (x + 190, 265)], SKILL[0], sw=3)
        text(x + 95, 228, q, fs=18, color=MUTED, align="center")
    text(60, 418, "What's in the context window, step by step", fs=24, color=MUTED)
    base = [("system prompt", NEUTRAL, 40), ("skill metadata", SKILL, 30),
            ("user msg", USER, 30)]
    steps = [("1. Session starts", []),
             ("2. Reads SKILL.md", [("SKILL.md", SKILL, 55)]),
             ("3. Reads extra files", [("SKILL.md", SKILL, 55),
                                       ("references/forms.md", ("#0c8599", "#96f2d7"), 45)]),
             ("4. Executes task", [("SKILL.md", SKILL, 55),
                                   ("references/forms.md", ("#0c8599", "#96f2d7"), 45),
                                   ("script output", TOOL, 35), ("AI answer", AI, 40)])]
    for i, (cap, extra) in enumerate(steps):
        x = 110 + i * 360
        text(x + 110, 462, cap, fs=22, align="center")
        rect(x, 500, 220, 330, (INK, "#ffffff"), sw=2)
        text(x + 110, 515, "free space", fs=16, color=GRAY, align="center")
        y = 825
        for lbl, c, h in base + extra:
            y -= h
            rect(x + 8, y, 204, h - 3, c, lbl, fs=14, ff=6, tcolor=INK, roundness=None,
                 sw=1)
        if i < 3:
            arrow([(x + 228, 665), (x + 352, 665)], sw=2)
    key_idea("Skills cost almost nothing until needed: only name + description are "
             "always loaded; everything else arrives on demand.")

# ------------------------------------------------------------------ slide 7
with Frame(1, 2, "7 · Product > Harness > Model"):
    header(7, P3, "Product > Harness > Model",
           "What are you actually talking to when you open an AI app?")
    rect(60, 180, 700, 650, USER, sw=3)
    text(85, 195, "Product", fs=34, color=USER[0])
    text(245, 205, "chatgpt.com · claude.ai", fs=22, color=USER[0])
    rect(105, 260, 610, 540, TOOL, sw=3)
    text(130, 275, "Harness", fs=34, color=TOOL[0])
    text(285, 287, "features around the model", fs=20, color=TOOL[0])
    for i, chip in enumerate(["file uploads", "web search", "projects",
                              "connectors", "memory", "skills"]):
        c = SKILL if chip == "skills" else (TOOL[0], "#ffffff")
        rect(135 + (i % 3) * 190, 335 + (i // 3) * 52, 175, 42, c, chip, fs=18)
    rect(160, 460, 500, 310, AI, sw=3)
    text(185, 475, "Model", fs=34, color=AI[0])
    text(300, 487, "gpt-5.5 · Fable 5", fs=22, color=AI[0])
    placeholder(190, 535, 440, 210, "model picker inside the app")
    explain = [("Model = the brain", "Predicts text, token by token. "
                "Examples: gpt-5.5, Fable 5.", AI, 140),
               ("Harness = everything built around the brain",
                "Uploading files, searching the web, projects, connectors, memory, "
                "and skills.", TOOL, 160),
               ("Product = the app you actually open", "chatgpt.com, claude.ai", USER, 120)]
    y = 185
    for h, b, c, hh in explain:
        rect(820, y, 720, hh, c)
        text(845, y + 15, h, fs=26, color=c[0])
        text(845, y + 60, b, fs=21, wrap=670)
        y += hh + 20
    rect(820, 690, 720, 140, KEY,
         "Same model + different harness = different results.\n"
         "Skills live in the harness.", fs=26, tcolor=INK, sw=3)
    key_idea("When you compare AI apps, compare the harness too, not just the model.")

# ------------------------------------------------------------------ slide 8
with Frame(2, 2, "8 · Prompting"):
    header(8, P3, "Prompting that works",
           "What makes a prompt easy for the model to get right?")
    text(60, 170, "5 principles", fs=24, color=MUTED)
    principles = [("context", "Give it the relevant stuff, and only that."),
                  ("clear goal", "Define the goal concretely: what does a great "
                                 "output look like?"),
                  ("examples", "Show examples instead of describing them."),
                  ("output format", "Ask for a format that's easy to verify."),
                  ("break it down", "Split big jobs into tasks that each fit one "
                                    "focused context window.")]
    for i, (h, b) in enumerate(principles):
        x = 60 + i * 302
        hot = h == "break it down"
        rect(x, 210, 280, 220, KEY if hot else USER, sw=3 if hot else 2)
        rect(x + 20, 225, 240, 52, (INK, "#ffffff"), h, fs=24, tcolor=INK)
        text(x + 25, 295, b, fs=20, wrap=235)
        if hot:
            text(x + 140, 438, "↩ the fix for context rot", fs=16, color=KEY[0],
                 align="center")
    text(60, 462, "Worked example: one prompt, read the way the AI reads it", fs=24,
         color=MUTED)
    chunks = [("Pull from my calendar", "Google Calendar connector", TOOL, 235),
              ("all the stuff I got lined up for the next 2 weeks",
               "context: what + time window", NEUTRAL, 325),
              ("and create a task list database", "Notion connector (creates "
               "the database)", TOOL, 280),
              ("on a new Notion page for me", "Notion connector: where the "
               "output goes", TOOL, 260),
              ("to help me keep track of getting those things done.",
               "the goal: leaves the model room to decide how (Fable 5 is very "
               "good at this)", FIX, 320)]
    x = 60
    for chunk, note, c, w in chunks:
        rect(x, 505, w, 90, USER, chunk, fs=20, tcolor=INK)
        arrow([(x + w / 2, 600), (x + w / 2, 635)], c[0], sw=2)
        rect(x, 640, w, 110, c, note, fs=18, tcolor=INK)
        x += w + 15
    rect(60, 775, 1480, 75, (GRAY, "#ffffff"),
         "Build intuition for: which words trigger which tools · how much to spell "
         "out vs. leave to the model · when to start a new chat", fs=20,
         tcolor=INK, style="dashed")
    key_idea("Good prompt = relevant context + a clear goal + examples + a "
             "verifiable format, split into chunks that fit one focused chat.")

out = Path(__file__).with_name("agent-skills-whiteboard.excalidraw")
out.write_text(json.dumps({
    "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
    "files": {},
}, ensure_ascii=False, indent=1))
print(f"wrote {out} ({len(elements)} elements)")
