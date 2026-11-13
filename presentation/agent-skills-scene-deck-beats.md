# Agent Skills, intuitively: beat sheet

Storyboard and speaker notes for `agent-skills-scene-deck.html`. Each numbered beat is one keypress. Beat 0 is what the scene shows on entry.

Controls: `→` / space / clicker next, `←` back, `1`–`9` jump to a chapter, click or drag the timeline to scrub, `f` fullscreen.

Sources: the class whiteboard (frames 1–7 plus the hand-drawn agent loop and skill-activation sketches) and `agent-skills-oreilly.pdf`.

## 1 · A folder

### Scene: the nine-second definition
0. "A Skill is a folder…" (byline on top)
1. The folder draws itself. "folder" gets the marker.
2. "…with a markdown file in it." SKILL.md slides into the folder.
3. "That's it. That's the whole form factor."
4. "So why a folder?" The definition ghosts out. The rest of the talk answers this.

## 2 · It's all text

### Scene: what the model sees
0. "An LLM only ever sees text." Empty context window.
1. "Everything piles up in one place: the context window." System prompt lands first.
2. Your message.
3. Hidden thinking, then the reply.
4. Tool call and tool output: the biggest block. "You never see most of it."
5. "Every turn, the model re-reads all of it, from the very first message."
6. "And the window has a limit." 128k, 200k, 1M tokens. 1M tokens ≈ 750k words ≈ 1,500 pages.

### Scene: the agent loop
0. "An agent is that same model, in a loop with tools." You and the LLM.
1. You send a prompt. It lands in the window.
2. The model decides: tool? Yes, run the tool. The call lands in the window.
3. The tool's output goes back in. Output is the wide block.
4. More laps: call, output, call, output.
5. No more tools: final answer back to you.
6. "Every lap lands in the same window. Agents fill it fast."

## 3 · Context rot

### Scene: more context isn't free
0. Axes: answer quality against how much is in the window.
1. The curve falls.
2. "Context rot": quality decays as the input grows. Sweet spot on the left, limit on the right.
3. It gets lost: too many instructions, it quietly drops some.
4. It hallucinates more: invents details, mixes up sources.
5. It gets slower and costlier: every turn re-reads the whole window.
6. "So keep the window short and focused." This is the constraint every Skill design choice follows from.

## 4 · Expertise

### Scene: one email, three setups
0. A real sponsorship email. "Could you please share your pricing?" is the task.
1. Chat: has the email, nothing else.
2. It writes fluent prose that breaks my rules in sentence one. Good writing was never the bottleneck.
3. Cowork: gains tools. Finds the thread, reads the negotiation, drafts in place.
4. Still missing the process. Nothing tells it how this job is done here.
5. Cowork + Skill: a written-down workflow. Same model, same tools, one folder added to disk.
6. "Agency gets you there faster. Expertise gets you somewhere right."

### Scene: how do we bring our expertise into an agent?
0. The question.
1. Naive answer: load all of it, always. The window fills with expertise.
2. 50 Skills ≈ 30–50k tokens before anyone speaks. 10 Skills ≈ 6–10k tokens every turn.
3. The user asks "capital of Portugal?" on top of all that. Worse, not just pricier.
4. Strike the naive answer.
5. With Skills: write your expertise once. The window stays almost empty.
6. The agent loads it only when the task needs it.

## 5 · The folder

### Scene: anatomy
0. "An Agent Skill is a directory." `sponsor-reply/`
1. `SKILL.md`: the recipe. Judgment in prose. The only file that must exist.
2. `references/`: depth. Read before a step, to shape it.
3. `scripts/`: repetition. The code runs, only its output enters context.
4. `assets/`: templates, fonts, logos that end up in the output.
5. "Judgment in prose · depth on demand · arithmetic in scripts."
6. "Three kinds of knowing, three homes."

### Scene: where the human sits
0. "Two gates, written as prose."
1. Get email, extract.
2. Gate 1: before research is spent. Most pitches die right here.
3. Research, then gate 2: before their code runs on my machine.
4. Rate, draft.
5. Send is my thumb, never its own. Nothing sends.
6. The gates are two paragraphs. No gate-handling code exists.

## 6 · Progressive disclosure

### Scene: the description is the router
0. The frontmatter of `sponsor-reply`.
1. The user types "what should I charge for this video?"
2. The agent only sees the small descriptions: always loaded, ~100 tokens each.
3. One matches. Its SKILL.md body enters context, once.
4. A working description has What, When, Key functionalities. The When is the hard part: write the words a user actually types.
5. "A Skill that never fires can't be wrong about anything else."

### Scene: three levels
0. System prompt in an otherwise empty window.
1. Level 1: name + description, always in context.
2. The user's message arrives.
3. Level 2: the SKILL.md body loads when the Skill triggers. Usually under 5k tokens.
4. Level 3: a linked file loads only if a step needs it. Here, the rate card.
5. The script runs outside. Only its output comes in: €3,000. Then the draft.
6. `security-rubric.md` never loads on a deal that never gets tested.
7. "The file system becomes just-in-time knowledge retrieval. That's why a Skill is a folder."

## 7 · The harness

### Scene: what are you actually talking to?
0. Model = the brain. Predicts text, token by token.
1. Harness = everything built around it: files, search, projects, connectors, memory.
2. Skills sit there too.
3. Product = the app you actually open.
4. "Same model + different harness = different results."
5. "Skills live in the harness: one component, swappable and portable."

### Scene: Skill vs. instruction
0. An instruction is a sentence.
1. Six turns.
2. It rides along every turn, forever. No version, nothing to hand over.
3. A Skill is a folder. Same six turns.
4. It loads only on the turn that matches. Versioned, portable, shareable.
5. The stack: prompt, CLAUDE.md, project, Skill, subagent, MCP.
6. "Layers, not substitutes." Most disappointment with Skills is misattribution.

## 8 · A good Skill

### Scene: the 85/15 split
0. Licklider, 1960: "About 85 per cent of my 'thinking' time was spent getting into a position to think."
1. 85%: setup. Search, transform, format, retrieve. What a Skill can carry.
2. 15%: judgment, taste, goal-setting. What stays yours.
3. Automation asks how to get a machine to do what I do. Decomposition asks which parts are mine.
4. A bad Skill goes after the wrong 85%, or tries the 15% and ships something beige.

### Scene: the order we build in is the lesson
1. Brain dump: dictate it, don't organize it.
2. skill-creator: scaffolding, not authorship. It returns a straw man.
3. Name the artifact. Can't name it? You're not ready to write.
4. Write the trigger: the words you actually type. Aim for ~90% on 10–20 queries.
5. Test against a baseline, same turn.
6. Iterate: ask for the ugly version, then fix the Skill.
7. "Fix the Skill, not the output."

### Scene: the "and" test
0. Describe the Skill in one sentence, with no "and".
1. "Creates Anki cards from any input": one Skill.
2. "Creates Anki cards and posts summaries to Notion."
3. Two Skills in one hat. A Frankenstein Skill (Chris Butler).
4. Six qualities: clear success criteria, single responsibility, defined inputs and outputs, stateless, progressive disclosure, easily verifiable.
5. "Verification must be cheaper than generation, or the Skill saved you nothing."
6. The rubric is the ceiling: your 15% is the part you cannot write down.

## 9 · Ship it

### Scene: scope
0. "Decide the scope before you write."
1. Personal: you, on your machine. `~/.claude/skills/`
2. Project: anyone in this repo. `.claude/skills/`
3. Plugin: anyone who installs it. Versioned, opt-in.
4. Organization: everyone, via managed settings.
5. A hardcoded `/Users/lucas/...` is fine personally, a tripwire in a repo, broken in a plugin.
6. Version the description: it is the public interface.
7. Installing someone else's? Read the SKILL.md first. It is instructions someone else wrote, executed with your access.

### Scene: takeaways
0. A Skill is a folder because the context window is finite.
1. Agency gets you there faster. Expertise gets you somewhere right.
2. Build one when the work is in the 85% and your judgment about it is reusable.
3. Judgment in prose · depth on demand · arithmetic in scripts.
4. Verification must stay cheaper than generation.
5. "Now go ship one." Questions.
