# Security rubric — before running a sponsor's code locally

This is GATE 2. It exists because a sponsorship pitch is an unusually effective
delivery mechanism for malware: it arrives unsolicited, it comes with a plausible
reason to run unfamiliar code, and it's flattering. Never clone-and-run because the
README looked professional.

Nothing here runs until Lucas says yes, and Lucas can't say a meaningful yes
without seeing the rubric result. Work through it, paste the result, then ask.

## Screen before you clone

| # | Check | Blocks if |
|---|---|---|
| 1 | **Provenance** — is this repo linked from the company's real domain? | The URL came only from the email, or the org name doesn't match the brand |
| 2 | **Age & activity** — first commit, last commit, contributor count | Created in the last few weeks, or a single anonymous contributor |
| 3 | **Reach** — stars, forks, dependent projects, package registry presence | Zero external footprint for something claiming to be widely used |
| 4 | **Install path** — what does setup actually do? | Any `curl … \| sh`, install script needing sudo, or a prebuilt binary with no source |
| 5 | **Postinstall hooks** — `package.json` scripts, `setup.py`, `build.rs`, Makefile targets | Anything executing on install rather than on run |
| 6 | **Network calls** — grep for hardcoded hosts, telemetry, phone-home | Beaconing to hosts unrelated to the product |
| 7 | **Credential access** — grep for `~/.ssh`, `~/.aws`, `.env`, keychain, browser profile paths | Any read of credential stores the product has no reason to touch |
| 8 | **Dependencies** — scan the lockfile for typosquats and unmaintained packages | Obvious typosquat, or a dependency pulled from a personal fork |
| 9 | **Obfuscation** — minified/encoded blobs, base64 payloads, eval of remote content | Any of it. There is no benign reason in a dev tool |

Useful greps once the repo is fetched (fetch is fine; **running** is the gated part):

```bash
grep -rnE "curl .*\| *(ba)?sh|wget .*\| *(ba)?sh" .
grep -rnE "~/\.(ssh|aws|config/gcloud)|\.env|keychain|Login Data" .
grep -rnE "eval\(|exec\(|base64 -d|atob\(" . --include=*.{js,ts,py,sh}
jq '.scripts' package.json 2>/dev/null
```

## Verdict

- **Any blocker hit** → don't run it. Report the specific finding to Lucas; that
  finding is itself a strong sponsorship signal.
- **Clean** → present the rubric result and ask permission. Then run it the safe
  way: a throwaway directory, a fresh virtualenv or container, no credentials
  mounted, no access to `~/.ssh` or `~/.aws`, and remove it afterward. Prefer
  Docker or a disposable VM when the project offers one.
- **Unclear** → treat as blocked. "I couldn't tell what the install script does"
  is a no, not a maybe.

## Always

- Never install globally (`npm i -g`, `pip install` outside a venv, `brew install`
  of the vendor's tap) for an evaluation.
- Never paste Lucas's real API keys into a sponsor's tool. Use throwaway keys with
  spend limits, or skip the test and say why.
- Never write anything into the connected sponsor folder except the report itself.
- Clean up when you're done and say what you removed.
