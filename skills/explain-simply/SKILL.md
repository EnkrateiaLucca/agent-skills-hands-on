---
name: explain-simply
description: Explain anything (a system, codebase, script, concept, architecture, error, or process) as a short numbered breakdown written in ASD-STE100 Simplified Technical English (Issue 9). Each item has a bold topic sentence and plain STE elaboration, and the breakdown ends with a short analogy that maps real components. Use whenever the user says "explain simply", "/explain-simply", "break this down", "how does this work in simple terms", "explain like the remote app explanation", "explain in STE", or asks for an intuitive or simple explanation of something technical.
---

# Explain Simply (ASD-STE100)

Produce a breakdown in the format below, written in ASD-STE100 Simplified Technical English (STE), Issue 9. The target reader is smart but new to the topic. After one read, that reader can explain it again to a friend.

An explanation is **descriptive writing** in STE terms (Section 6). It gives information, not instructions.

## The format

1. **Lead-in line.** Write one short sentence that names the subject and ends with a colon: "The app has five parts:". A vertical list has a lead-in that ends with a colon (R4.3).
2. **Numbered list, usually 4–6 items.** Each item has one topic (R6.5) and this shape:
   `**Bold topic sentence.** One to four elaboration sentences.`
   - The bold part is a complete STE sentence that ends with a period. It is the topic sentence of the item (R6.4). Write "**The QR code is the Wi-Fi address of your laptop.**", not "**QR code**". A reader who reads only the bold sentences must get the full story.
   - Each item has a maximum of 6 sentences (R6.6), bold sentence included.
3. **Order the items from parts to flow.** Start with what exists and what each part is. Then show how the parts connect. Then show what occurs from start to end when it operates.
4. **Close with an analogy of 2–3 short sentences, after the list, as its own paragraph.** Map 2–3 real components to everyday objects:
   "The phone is the remote control. The laptop is the TV. The QR code gives the address of the TV to the remote control."
   Everyday objects are technical nouns in STE (R1.5 categories: personal effects, machines, tools, parts of the body). Thus, *remote control*, *TV*, *bookmark* and *finger* are permitted.
5. **Nothing after the analogy.** One natural follow-up question is optional. Write no headers, no intro paragraph and no summary.
6. **Length.** Keep the explanation under ~220 words. STE does not let you drop words to save space (R4.2), so cut elaboration sentences, not items.

## STE rules for every sentence

**Words**
- Use only approved dictionary words (R1.1), technical nouns (R1.5) and technical verbs (R1.12). Use each approved word only with its approved meaning and part of speech (R1.2, R1.3). For example, TAP is a verb only, so "a tap" is not STE. NUMBER is a noun only, so "numbered" is not STE. WHICH is a pronoun only, so "which branch" is not STE.
- Technical nouns are names from the subject: `server`, `port`, `router`, `QR code`, file names, commands, error codes. Technical verbs are subject-field processes: `click`, `scroll`, `download`, `install`, `boot`. Use an approved verb when one works (R1.12).
- Use the same name for the same thing every time (R1.11, R6.2). If item 1 says "server", no later item says "backend" or "service".
- Explain each technical noun that is new to the reader in its own short sentence. Write "A port is a door on a computer, and each port has a number." Do not add a gloss after a dash.
- Keep multi-word nouns to 3 words or fewer (R2.1). Use prepositions to break longer stacks.
- Use no Latin abbreviations (*e.g.*, *i.e.*, *etc.*). Write FOR EXAMPLE (GR-6).

**Verbs**
- Use only these forms: simple present, simple past, simple future (WILL), the infinitive, and the past participle as an adjective (R3.2, R3.3).
- Use no perfect or progressive forms: no "has sent", "had started", "is sending" (R3.4).
- Use *-ing* words only inside a technical noun, such as `routing table` (R3.5).
- Use the active voice. The passive voice is permitted only when the agent is unknown (R3.6).
- Use a verb for an action, not a noun phrase. Write "the server checks", not "the server does a check of" (R3.7).
- Use no phrasal verbs (R9.3). "sends back" becomes "sends ... to", and "sets up" becomes "prepares" or "installs".
- Use CAN for possibility and ability, not *may*, *might*, *could* or *would*. Use MUST, not *should*.
- Explanations do not use the imperative, because explanations are descriptive (Section 6).

**Sentences**
- Write a maximum of 25 words in each sentence (R6.3). Give each sentence only one subject (R6.1). Split "X is A, and Y is B" into two sentences.
- Do not leave out words, and do not use contractions (R4.2). "No internet, no cloud." becomes "The data does not go through the internet."
- Put an article or *this/these* before nouns when applicable (R4.5).
- Connect related sentences with AND, BUT, THEN, THUS, AS A RESULT (R4.4).
- Do not use semicolons (R8.1). Dashes, colons and parentheses are permitted.

**Word-count rules (R8.4–R8.7).** Each of these counts as 1 word: a number, a code span, an abbreviation, a proper noun, a hyphenated group, and all text in parentheses. Text in parentheses also counts as its own sentence.

## Word swaps that come up in explanations

These pairs come from the Issue 9 dictionary. Before you use a word you are not sure of, look it up:
`grep -i "^word " references/dictionary-approved.md references/dictionary-unapproved.md`

| Not STE | STE |
|---|---|
| just, basically, really, actually, simply | delete the word |
| explain / describe | TELL / GIVE |
| need | NECESSARY ("A key is necessary") |
| run (a program) | OPERATE, START |
| talk to | SPEAK, or SEND DATA TO |
| happen | OCCUR |
| every / both | EACH, ALL / THE TWO |
| kind / way | TYPE / PROCEDURE, or rewrite |
| job | TASK |
| allow, enable / provide / display | LET / GIVE, SUPPLY / SHOW |
| reach, arrive / exist | GET / BE |
| store, save / take / bring | KEEP / GET, REMOVE / MOVE, PUT |
| match / link / call | AGREE / CONNECT / TELL |
| big, huge / little, tiny | LARGE / SMALL |
| like (comparison) / similar | THE SAME AS / ALMOST THE SAME, EQUIVALENT |
| difficult / whole / several / various | NOT EASY / FULL, ALL / SOME / DIFFERENT |
| however / therefore / since (reason) | BUT / THUS, AS A RESULT / BECAUSE |
| whether / via / within / due to / prior to | IF / THROUGH / IN / BECAUSE OF / BEFORE |
| may, might, could, would / should | CAN / MUST |
| ensure / utilize / consist of | MAKE SURE / USE / HAVE |

When a word swap gives a bad sentence, change the sentence construction (R9.1).

## Canonical example

This is the target output. It explains a phone app that controls a laptop:

> The app has five parts:
>
> 1. **Your laptop has a small web server.** The server is one Python script that waits for messages on port 7777. A port is a door on a computer, and each port has a number. The server has two tasks: it sends a web page, and it starts Mac commands.
> 2. **The QR code is the Wi-Fi address of your laptop.** The address is `http://192.168.1.221:7777`. When your phone reads the QR code, the phone goes to this address. The phone and the laptop are on the same Wi-Fi network. The data does not go through the internet.
> 3. **The page with four buttons is on the laptop.** When your phone goes to the address, the server sends this small HTML page to the phone.
> 4. **When you tap a button, your phone sends a message to the laptop.** Each button sends a different message, for example `POST /run/disco`.
> 5. **For each message, the server starts one Mac command.** The video message starts `open <url>`. The voice message starts `say`. The server accepts only these four messages. For all other messages, the server sends a 404 error.
>
> The phone is the remote control. The laptop is the TV. The QR code gives the address of the TV to the remote control.

Item 2 has one negative sentence ("The data does not go through the internet."). That sentence stops a misconception the reader is likely to have. Use one such sentence per explanation, not more.

## Process

1. If the user does not say what to explain, explain the most recent artifact or topic in the conversation.
2. Read the actual source (code, doc, error) before you write. Use the real names, numbers and commands from it.
3. Draft the list in STE.
4. Write the draft to `explain.md` in your scratchpad directory, and run the checker on it. Use `--tn` to list the words you use as technical nouns or verbs (singular is enough, plurals match):
   ```bash
   uv run ~/.claude/skills/explain-simply/scripts/ste_check.py <scratchpad>/explain.md --tn port,router
   ```
   - Fix each `FAIL` line, then run the checker again. A FAIL word can be a technical noun in your text, for example "file" (FILE is not approved as a verb). In that case, add the word to `--tn`.
   - Each `REVIEW` word must be a technical noun or technical verb. Replace each word that is not.
   - The checker prints the total word count. Keep it under ~220.
5. Do the checks that the script cannot do:
   - Each word keeps its approved meaning and part of speech.
   - The text has no imperatives.
   - The bold sentences alone tell the full story.
   - The analogy maps real components.
6. Show only the final explanation to the user. Do not show the checker output.

## References

- `references/writing-rules.md`: all 53 Issue 9 rules, with examples. Read it for edge cases, such as hyphens (R8.2) and the 7 permitted uses of parentheses (R8.3).
- `references/dictionary-approved.md`: the 875 approved words, each with its approved meaning and part of speech.
- `references/dictionary-unapproved.md`: about 1,270 words that are not approved, with their STE alternatives.
- `scripts/ste_check.py`: mechanical checks for sentence length, paragraph length, dictionary words, verb forms, semicolons, contractions and Latin abbreviations. `--selftest` runs its own test.

The reference files come from an extraction of ASD-STE100 Issue 9 by Cainã Costa ([cfcosta/writing-styles](https://github.com/cfcosta/writing-styles), MIT, see `references/LICENSE.md`). ASD gives the official standard free of charge at https://www.asd-ste100.org/STE_downloads.html.
