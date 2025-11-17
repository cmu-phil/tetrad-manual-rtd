# Algorithm: <NAME>

## Overview

<One paragraph giving a high-level description.
What does the algorithm assume? What graph does it output?
Where does it fit in the Tetrad ecosystem?>

---

## Outputs

- **Graph type:** `<DAG / CPDAG / MAG / PAG>`
- **Handles hidden confounding?** `Yes/No/Partially`
- **Handles selection bias?** `Yes/No/With assumptions`

---

## Assumptions

State the minimal assumptions:

- **Causal sufficiency?**
- **No selection bias?**
- **Linearity / Gaussianity?**
- **Faithfulness?**
- **Independent errors?**

If assumptions vary with options, list them.

---

## How the Algorithm Works (Intuition)

A few short bullets describing the intuitive steps, accessible to users without needing the full technical paper.

Example format:

1. **Initialize** from <empty graph, complete graph, score model, etc.>.
2. **Search stage** (e.g., adjacency reduction via CI tests; greedy additions; score-based search).
3. **Orientation stage** (colliders, rules R1–R4, Meek rules, FCI rules, etc.).
4. **Finalization** (repair to PAG, refine CPDAG, prune false positives, etc.).

*Keep this section high-level; technical detail belongs in the next section.*

---

## How the Algorithm Works (Technical)

A more complete list of steps for advanced users.

- Mathematical criteria (e.g., maximizing BIC score, using sepsets)
- Orientation rules used (Meek, Zhang 2008, special-case rules)
- Use of background knowledge
- Order-independence or dependence
- Data-type compatibility (continuous/discrete/mixed)
- Complexity notes (optional but helpful)

This section can be as detailed as needed; users who don’t want it will skip it.

---

## Strengths

Bullets focusing on advantages:

- Scalability
- Precision/recall characteristics
- Handles large p, large n, mixed data
- Good orientation quality
- Robustness

Make these grounded, not marketing-speak.

---

## Limitations and Failure Modes

Bullets on known caveats:

- When it fails (e.g., dense graphs, small sample sizes)
- Sensitivity to depth
- CI test issues
- Score degeneracy
- Latent confounding sensitivity
- Computational bottlenecks

This section builds trust.

---

## Key Parameters in Tetrad

List major parameters and short meanings.

Example:

- **alpha** — significance threshold for CI tests
    - **depth** — maximum size of conditioning sets
- **numThreads** — parallelization
- **score penalty (c)** — BIC weight

Keep each one short; users can click through to full parameter definitions.

---

## Recommended Use-Cases

Practical guidance:

- “Use PC when…”
- “Use BOSS when…”
- “Use FCIT when…”

Make these concrete so users can choose algorithms confidently.

---

## Variants and Related Algorithms

List siblings or variations:

- PC ↔ PC-Max
- FGES ↔ GES ↔ BOSS ↔ BOSS-FCI
- FCI ↔ RFCI ↔ GFCI ↔ BOSS-FCI ↔ GRaSP-FCI ↔ FCIT

A short description of how this algorithm fits in the family is extremely helpful.

---

## References

Use formal citations (IEEE or APA — whichever the rest of the manual uses). Include:

- Original paper(s)
- Major follow-up papers
- Links to proofs if they exist (Zhang 2008, etc.)

---

## Optional: Example Workflow

A short “How to run this in Tetrad” block:

1. Add a **Search box**
2. Choose `<algorithm>`
3. Attach **Data box** (+ **Knowledge box** if applicable)
4. Set parameters
5. Run search

This section is optional but helpful for newcomers.