# Hands-On Agent Skills: From Folder to Shippable Expertise

Materials for the O'Reilly live training *Hands-On Agent Skills* (2 hours).

## Contents

- [`presentation/agent-skills-oreilly.pdf`](presentation/agent-skills-oreilly.pdf): the slide deck. All source citations in it are clickable.
- [`notebooks/`](notebooks/): notebooks for the session (empty for now).
- [`assets/skills/`](assets/skills/): the Skills built in class.
  - [`test-skill/`](assets/skills/test-skill/): a minimal Skill that explains what a Skill is.
  - [`sponsor-reply/`](assets/skills/sponsor-reply/): the live-demo Skill. It triages an inbound sponsorship email, researches the company, computes a rate from YouTube stats and drafts a reply.
  - [`packaged/`](assets/skills/packaged/): the same Skills zipped for upload to Claude.ai.
- [`skills/`](skills/): extra Skills to try. Copy any folder into `~/.claude/skills/`.
  - [`scene-deck/`](skills/scene-deck/): a talk as one animated HTML file with a chapter timeline.
  - [`research-report/`](skills/research-report/): a web research report with deep-linked citations.
  - [`grounded-reading-interfaces/`](skills/grounded-reading-interfaces/): HTML study pages built on reading and retention research.
  - [`anti-ai-writing-slop/`](skills/anti-ai-writing-slop/): removes AI tells from prose.
  - [`explain-simply/`](skills/explain-simply/): explanations in Simplified Technical English.
- [`assets/whiteboard/`](assets/whiteboard/): the class whiteboard (Excalidraw). Serve the folder and open `view.html`, or rebuild it with `python build_whiteboard.py`.

## Running the sponsor-reply Skill

Copy `assets/skills/sponsor-reply/` into `~/.claude/skills/` (or a project's `.claude/skills/`). To fetch live YouTube stats, copy `.env.example` to `.env` and fill in `YOUTUBE_API_KEY` and `YOUTUBE_CHANNEL_HANDLE`.
