# Decision Making Toolkit

A compressed, actionable reference for quantitative decision analysis.

**Source:** [Decision Analysis Module 1, FGCU](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm)

---

## Quick Reference

| Situation | Tool | Section |
|-----------|------|---------|
| No probability data | Maximax, Maximin, Minimax Regret | §2 |
| Can estimate probabilities | Expected Value (EV) | §3 |
| Unsure if choice is robust | Sensitivity Analysis | §4 |
| Considering paying for info | EVPI / EVSI | §5 |

---

## §1. The Decision Worksheet (5-Step Core)

Use this structure for any decision with uncertain outcomes:

| Step | Action |
|------|--------|
| 1 | [Identify and define the problem](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Identify%20and%20define%20the%20problem) |
| 2 | [Determine the set of alternative solutions](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Determine%20the%20set%20of%20alternative%20solutions) |
| 3 | [Determine the criterion that will be used to evaluate the alternatives](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Determine%20the%20criterion%20or%20criteria%20that%20will%20be%20used%20to%20evaluate%20the%20alternatives) |
| 4 | [Evaluate the alternatives using an appropriate quantitative method](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Evaluate%20the%20alternatives) |
| 5 | [Choose an alternative](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Choose%20an%20alternative) |

Then: implement + evaluate results.

### Structure First: Build a Payoff Table

Before calculating anything, [structure forces you to explicitly consider alternatives and states](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=selecting%20an%20option%20or%20alternative%20course%20of%20action):

|  | State 1 | State 2 | ... |
|--|---------|---------|-----|
| **Decision A** | V₁₁ | V₁₂ | ... |
| **Decision B** | V₂₁ | V₂₂ | ... |

- **Rows:** Your decision alternatives
- **Columns:** States of nature (future scenarios you don't control)
- **Cells:** Payoffs (profit, cost, utility — pick one consistent unit)

---

## §2. Decision Making WITHOUT Probabilities

Use when you cannot reliably estimate likelihoods. Practice using all three to see how they differ.

### A) [Maximax (Optimistic)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=the%20decision%2Dmaker%20evaluates%20each%20decision%20alternative%20in%20terms%20of%20the%20best%20payoff%20that%20can%20occur)

**Rule:** [Select the decision alternative associated with the maximum of the maximum payoffs](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=maximum%20of%20the%20maximum%20payoffs)

```
For each option → Find BEST payoff → Pick the option with the HIGHEST best
```

**When to use:** You accept large losses for a shot at large gains.

---

### B) [Maximin (Conservative)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=the%20decision%2Dmaker%20evaluates%20each%20decision%20alternative%20in%20terms%20of%20the%20worst%20payoff%20that%20can%20occur)

**Rule:** [Select the decision alternative associated with the maximum of the minimum payoffs](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=maximum%20of%20the%20minimum%20payoffs)

```
For each option → Find WORST payoff → Pick the option with the HIGHEST worst
```

**When to use:** Avoiding large downside is the priority.

---

### C) [Minimax Regret](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=converting%20the%20payoff%20table%20into%20a%20regret%20table)

**The "minimize future regret" tool.** Build a regret table by asking: [if I knew ahead of time that state s₁ will occur, what would I do?](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=if%20I%20knew%20ahead%20of%20time%20that%20state%20of%20nature%20s1%20will%20occur)

**How to build a regret table:**

1. For each state, find the **best payoff achievable** if you had known that state in advance
2. **Regret = Best payoff in that state − Your payoff in that state**
3. For each decision, find its **maximum regret** across all states
4. [Select the decision with the minimum of the maximum regrets](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=minimum%20of%20the%20maximum%20regrets)

```
Build Regret Table → Find MAX regret per option → Pick MIN of those
```

**Practice prompt:** "If each scenario happens, how much will I kick myself? Which choice minimizes my worst regret?"

---

## §3. Decision Making WITH Probabilities

### [Expected Value (EV)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=the%20sum%20of%20weighted%20payoffs%20for%20the%20decision%20alternative)

**Formula:**
```
EV(d) = Σ [P(sⱼ) × Vᵢⱼ]
```

Or expanded: [EV(d₁) = P(s₁) × V₁₁ + P(s₂) × V₁₂](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=EV%20%28d1%29%20%3D%20%5BP%20%28s1%29%20*%20V11%5D%20%2B%20%5BP%20%28s2%29%20*%20V12%5D)

**Rule:** Choose the alternative with the highest EV.

**Interpretation:** EV represents [the long run outcome of repeated experiments](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=the%20long%20run%20outcome%20of%20repeated%20experiments) — what you'd average over many similar decisions.

### Probability Hygiene

Your probabilities must satisfy these requirements ([source](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=each%20probability%20must%20be%20a%20real%20number%20between%200%20and%201)):

- Each P(sⱼ) ∈ [0, 1]
- Σ P(sⱼ) = 1.0
- [States must be mutually exclusive and exhaustive](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=mutually%20exclusive%20and%20exhaustive)

If you forgot a state, add it and assign probability.

---

## §4. Sensitivity Analysis

Ask: [How sensitive is my solution to changes in data input?](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=how%20sensitive%20is%20my%20solution%20to%20changes%20in%20data%20input)

### The 5% Rule

[If a decision strategy changes based on a five or less percent change to an input, the solution is very sensitive to change](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=if%20a%20decision%20strategy%20changes%20based%20on%20a%20five%20or%20less%20percent%20change%20to%20an%20input) — invest in refining that input before deciding.

### Break-Even Method

To find when you're indifferent between two decisions:

```
Set: EV(Option A) = EV(Option B)
Solve for: the uncertain variable (probability or payoff)
```

**Example:**
- At P(s₁) = 0.35 → "Make" is better
- At P(s₁) = 0.40 → Indifferent
- At P(s₁) > 0.40 → "Buy" is better

**Practice prompt:** "What input value would flip my choice? Am I confident we're not near that threshold?"

---

## §5. Valuing Information

### [Expected Value of Perfect Information (EVPI)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=the%20difference%20between%20the%20expected%20value%20with%20perfect%20information%20and%20the%20expected%20value%20without%20perfect%20information)

**What it answers:** Maximum you should pay for ANY information source.

**Formula:**
```
EVPI = EV(with perfect info) − EV(without info)
```

**How to calculate EV with perfect info ("crystal ball"):**

1. For each state, identify the best decision you'd make if you knew that state would occur
2. Multiply that best payoff by the state's probability
3. Sum across all states

**Example:**
```
If I KNEW s₁ (unfavorable) → Best = Buy ($10,000)
If I KNEW s₂ (favorable)   → Best = Make ($90,000)

EV w/ PI = (0.35 × $10,000) + (0.65 × $90,000) = $62,000
EV w/o PI = $51,500

EVPI = $62,000 − $51,500 = $10,500
```

**Rule:** [EVPI is an upper bound](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=EVPI%20%3D%20EV%20w%20PI%20-%20EV%20w/o%20PI) — never pay more than this for research, forecasts, or consultants.

---

### [Expected Value of Sample Information (EVSI)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=expected%20value%20with%20sample%20information)

For *imperfect* information (market research, consultants, tests):

```
EVSI = EV(with sample info) − EV(without info)
```

### Updating Probabilities with a Track Record (Bayes)

When you have:
- **Prior:** P(sⱼ) — your initial estimates
- **Track record:** P(Iₖ | sⱼ) — how often the source predicts Iₖ when state sⱼ actually occurs

Calculate ([source](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=prior%20probabilities%20times%20the%20consultant%20track%20record%20probabilities)):

1. **Joint:** P(Iₖ and sⱼ) = P(sⱼ) × P(Iₖ | sⱼ)
2. **Marginal:** P(Iₖ) = Σⱼ P(Iₖ and sⱼ)
3. **Posterior:** [P(sⱼ | Iₖ) = Joint / P(Iₖ)](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=conditional%20probabilities%20in%20the%20last%20column%20are%20computed%20by%20dividing%20the%20joint%20probabilities)

Then recalculate EV using posteriors for each indicator scenario.

---

### [Efficiency of Sample Information](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=Efficiency%20%3D%20EVSI%20/%20EVPI)

**Formula:**
```
Efficiency = EVSI / EVPI
```

[The closer this number is to 100%, the better](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=The%20closer%20this%20number%20is%20to%20100%25%2C%20the%20better) — it measures how close your imperfect source is to a crystal ball.

**Example:** Efficiency = 6,900 / 10,500 = 65.7%

**Use in negotiations:** EVPI/EVSI = your "price ceiling" for research, pilots, or expert advice.

---

## §6. Decision Trees

For complex sequential decisions, [draw a decision tree](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=decision%20tree):

- □ **Decision node:** You choose among branches
- ○ **Chance node:** Probability determines which branch occurs
- **Terminal nodes:** Final payoffs

### Solving a Decision Tree

[Start at the right of the tree, move left, pruning branches as we go](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm#:~:text=start%20at%20the%20right%20of%20the%20tree%2C%20move%20left%2C%20pruning%20branches):

1. At **chance nodes:** Calculate EV (probability-weighted average of branches)
2. At **decision nodes:** Select the branch with highest EV
3. **Prune** inferior branches as you work backward

---

## §7. 10-Minute Practice Loop

For any real decision:

1. **List 2-5 alternatives** and **2-5 states of nature** (keep it small)
2. **Fill a payoff table** (use one consistent unit: €, hours, stress, etc.)
3. **Run minimax regret** (even if you have probabilities — it surfaces different insights)
4. **If you have probabilities:** Compute EV for each option
5. **Sensitivity check:** Set EVs equal, solve for the break-even input
6. **If sensitive:** Compute EVPI/EVSI to decide if more info is worth buying

---

## Formula Cheat Sheet

| Concept | Formula |
|---------|---------|
| Expected Value | `EV = Σ [P(sⱼ) × Vᵢⱼ]` |
| Regret | `Best payoff in state − Your payoff` |
| EVPI | `EV(perfect info) − EV(no info)` |
| EVSI | `EV(sample info) − EV(no info)` |
| Efficiency | `EVSI / EVPI` |
| Posterior | `P(s|I) = [P(I|s) × P(s)] / P(I)` |
| Break-even | `Set EV_A = EV_B, solve for unknown` |

---

## Decision Criteria Summary

| Criterion | Selects | Mindset |
|-----------|---------|---------|
| Maximax | Max of max payoffs | Optimistic risk-taker |
| Maximin | Max of min payoffs | Conservative loss-avoider |
| Minimax Regret | Min of max regrets | Regret minimizer |
| Expected Value | Highest EV | Long-run optimizer |

---

*Source: [Decision Analysis Module 1, FGCU](https://ruby.fgcu.edu/Courses/ekirche/MSci/modules/6603/m1_notes.htm)*
