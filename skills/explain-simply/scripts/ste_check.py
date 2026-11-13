# /// script
# requires-python = ">=3.10"
# ///
"""Mechanical ASD-STE100 (Issue 9) checks for descriptive text.

Usage: ste_check.py [FILE] [--tn port,router]   (reads stdin without FILE)   |   ste_check.py --selftest
--tn lists the words you use as technical nouns/verbs (R1.5, R1.12). The check skips them.
Exit 1 when a hard rule fails. "REVIEW" words do not fail the check.
Not checked: approved meaning / part of speech, imperatives, topic sentences.
"""
import argparse
import re
import sys
from pathlib import Path

REF = Path(__file__).resolve().parent.parent / "references"
MAX_WORDS, MAX_SENTENCES = 25, 6  # R6.3, R6.6 (descriptive writing)
NUMBER_WORDS = set("zero one two three four five six seven eight nine ten eleven twelve twenty thirty forty fifty hundred thousand million".split())


def load_dictionary():
    approved, unapproved, phrases = {}, {}, {}  # approved: word -> parts of speech
    for line in (REF / "dictionary-approved.md").read_text().splitlines():
        if m := re.match(r"^([A-Z][A-Z '\-]*?) \((\w+)\)", line):
            for w in m[1].lower().split():
                approved.setdefault(w, set()).add(m[2])
            forms = re.match(r".*?\[([A-Z][^;\]]*)", line)  # "[SENDS, SENT, SENT; ...]", not "[other meanings: ...]"
            for w in re.findall(r"\b[A-Z]{2,}\b", forms[1] if forms else ""):
                approved.setdefault(w.lower(), set()).add("form")
    for line in (REF / "dictionary-unapproved.md").read_text().splitlines():
        if m := re.match(r"^([a-z].*?) \((\w+)\.?\) -> (.+)$", line):
            head = re.sub(r"\s*\(.*?\)", "", m[1]).strip()
            (phrases if " " in head else unapproved).setdefault(head, f"({m[2]}) -> {m[3]}")
    unapproved = {w: alt for w, alt in unapproved.items() if w not in approved}
    return approved, unapproved, phrases


VERB, ADJ = {"v", "form"}, {"adj", "adv", "form"}
SUFFIXES = (("ies", "y", None), ("es", "", None), ("s", "", None), ("ied", "y", VERB), ("ed", "", VERB), ("d", "", VERB), ("er", "", ADJ), ("est", "", ADJ))


def stems(w):
    """(stem, required part of speech) pairs: 'numbered' -> ('number', verb), so noun-only NUMBER fails."""
    out = [(w, None)]
    for suf, rep, pos in SUFFIXES:
        if w.endswith(suf) and len(w) > len(suf) + 2:
            out.append((w[: -len(suf)] + rep, pos))
    if re.search(r"(\w)\1ed$", w):
        out.append((w[:-3], VERB))  # stopped -> stop
    return out


def is_approved(w, approved):
    return any(s in approved and (pos is None or approved[s] & pos) for s, pos in stems(w))


def clean(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "CODE", text)  # quoted text = 1 word (R8.6)
    text = re.sub(r"https?://\S+", "URL", text)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = re.sub(r"^\s*(\d+\.|[-*])\s+", "\n\n", text, flags=re.M)  # each list item = own unit
    return re.sub(r"[*_#]", "", text)


def check(text, tn=frozenset()):
    approved, unapproved, phrases = load_dictionary()
    hard, review, total = [], set(), 0
    body = clean(text)
    low = body.lower()
    if ";" in body:
        hard.append("semicolon (R8.1)")
    for m in re.finditer(r"\b\w+(n['’]t|['’](re|ve|ll|d|m))\b|\b(it|that|there|what|here|let|who|where)['’]s\b", low):
        hard.append(f"contraction '{m[0]}' (R4.2)")
    for m in re.finditer(r"\b(e\.g\.|i\.e\.|etc\b|vs\.)", low):
        hard.append(f"Latin abbreviation '{m[0]}' (GR-6)")
    for m in re.finditer(r"\b(has|have|had)\s+(been|\w+ed|done|gone|made|sent|shown|given|known|found)\b", low):
        hard.append(f"perfect tense '{m[0]}' (R3.4)")
    for m in re.finditer(r"\b(am|is|are|was|were|be|been)\s+(\w+ing)\b", low):
        if m[2] not in approved:
            hard.append(f"progressive tense '{m[0]}' (R3.4)")
    for m in re.finditer(r"\b(is|are|was|were|be|been|being)\s+\w+\s+by\b", low):
        hard.append(f"passive with agent '{m[0]}' (R3.6)")
    for p, alt in phrases.items():
        if re.search(rf"\b{re.escape(p)}\b", low):
            hard.append(f"'{p}' not approved {alt}")

    for unit in filter(str.strip, re.split(r"\n\s*\n", body)):
        parens = re.findall(r"\(([^()]*)\)", unit)
        unit = re.sub(r"\([^()]*\)", " PAREN ", unit)  # parentheses = 1 word (R8.5)
        sentences = [s for s in re.split(r"(?<=[.!?:])\s+", " ".join(unit.split())) if s.strip()]
        if len(sentences) > MAX_SENTENCES:
            hard.append(f"{len(sentences)} sentences in one paragraph/item, max {MAX_SENTENCES} (R6.6): '{sentences[0][:50]}…'")
        for s in sentences + parens:
            words = [w for w in s.split() if re.search(r"\w", w)]
            total += len(words) if s in sentences else 0
            if len(words) > MAX_WORDS:
                hard.append(f"{len(words)} words, max {MAX_WORDS} (R6.3): '{s[:60]}…'")
            for i, raw in enumerate(words):
                w = re.sub(r"['’]s$", "", raw.strip(".,:!?\"'’“”—()[]"))  # possessive OK (GR-8)
                if not w or re.search(r"\d", w) or w.isupper() or (i and w[0].isupper()) or w.lower() in NUMBER_WORDS:
                    continue  # ponytail: caps = abbreviation/proper noun/quoted text, may hide a capitalized non-STE word
                for part in w.lower().split("-"):
                    if w.lower() in tn or any(st in tn for st, _ in stems(part)):
                        continue
                    if part in unapproved:
                        hard.append(f"'{part}' not approved {unapproved[part]}")
                    elif part.endswith("ing") and part not in approved:
                        review.add(f"{part} (-ing form: only inside a technical noun, R3.5)")
                    elif part and not is_approved(part, approved):
                        if alt := next((unapproved[s] for s, _ in stems(part) if s in unapproved), None):
                            hard.append(f"'{part}' not approved {alt}")
                        else:
                            review.add(part)
    return list(dict.fromkeys(hard)), sorted(review), total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--tn", default="", help="comma-separated technical nouns/verbs")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        bad = "We utilize it; it's basically prior to the start. The page is being loaded by the server, e.g. now."
        h, r, _ = check(bad)
        joined = " ".join(h)
        for needle in ("utilize", "semicolon", "contraction", "prior to", "Latin", "progressive", "passive"):
            assert needle in joined, needle
        assert "basically" in r
        assert "numbered" in check("A port is a numbered door.")[1]
        assert not check("The part moved. It stopped.")[1]
        good = "1. **The laptop has a small web server.** The server waits for messages on port 7777."
        h, r, n = check(good)
        assert h == ["'port' not approved (adj) -> LEFT (adj)"] and n == 15, (h, n)
        h, r, _ = check(good + " The ports open.", {"port"})
        assert not h, h
        assert r == ["laptop", "messages", "server", "web"], r
        print("selftest OK")
        return
    text = Path(args.file).read_text() if args.file else sys.stdin.read()
    hard, review, total = check(text, {w.strip().lower() for w in args.tn.split(",") if w.strip()})
    for h in hard:
        print("FAIL  ", h)
    if hard:
        print("       A FAIL word that is a technical noun/verb here goes in --tn.")
    if review:
        print("REVIEW (keep only if a technical noun/verb, else replace):", ", ".join(review))
    print(f"{total} words")
    if not hard:
        print("OK: no hard STE rule failures")
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()
