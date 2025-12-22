# Interpreting Results

After exploring your data, choosing methods, systematically searching, and evaluating candidate models  
(see *Data Exploration*, *Algorithm Selection and Assumptions*, *Running Searches*, and *Model Evaluation and Markov Checking*),  
the final step in the causal analysis workflow is **interpreting results responsibly**.

Causal discovery outputs — whether DAGs, CPDAGs, or PAGs — are **not definitive truths**.  
They are *models that fit patterns in the data under specific assumptions*.  
This page explains what you can *reasonably conclude*, how to assess robustness, and how to communicate uncertainty clearly.

---

## 1. What a Discovered Graph Represents

A graph estimated from data is best understood as:

- a **hypothesis** about causal structure,
- consistent with observed conditional independences,
- dependent on modeling assumptions (e.g., causal sufficiency, functional form),
- influenced by algorithm and parameter choices.

It is *not* a guarantee of causal truth.

> **Interpretation is about plausibility under assumptions, not certainty.**

Your conclusions should always be read as conditional statements:
> *“If these assumptions hold, then this structure is plausible.”*

---

## 2. Types of Output and Their Meaning

### 2.1 Fully Directed Acyclic Graphs (DAGs)

A fully oriented DAG proposes causal directions for all adjacencies.

**When they deserve attention:**
- Strong assumptions are made (e.g., no latent confounding)
- Models pass evaluation diagnostics (e.g., Markov checking)
- Results align with domain knowledge

**How to interpret:**
- Directions are *hypotheses*, not proofs
- Emphasize which assumptions support each orientation

---

### 2.2 Completed Partially Directed Acyclic Graphs (CPDAGs)

CPDAGs represent a **Markov equivalence class** of DAGs.

**What you can conclude:**
- Adjacencies are supported by the data
- Some orientations are identifiable
- Unoriented edges indicate directions that cannot be determined from the data and assumptions alone

Unoriented edges are *informative*: they mark genuine limits of identifiability.

---

### 2.3 Partial Ancestral Graphs (PAGs)

PAGs allow for **latent confounders and selection effects**.

They use richer edge markings to represent uncertainty about:
- causal direction
- the presence of latent common causes

**Interpretation focus:**
- Which variables are adjacent
- Which directions are identifiable
- Which relationships remain ambiguous due to latent structure

PAGs are often the most honest representation when causal sufficiency is doubtful.

---

## 3. Interpreting Common Edge Marks

| Mark | Meaning |
|------|--------|
| **A → B** | Oriented edge under stated assumptions |
| **A – B** | Adjacent; direction not identifiable |
| **A o→ B** | Possible direction with latent uncertainty |
| **A ↔ B** | Evidence consistent with latent confounding |
| **A o–o B** | Both direction and confounding unresolved |

> Always explain edge marks in plain language when presenting results — most readers will not know their formal meaning.

---

## 4. Robustness and Stability

Strong conclusions depend on **robustness**, not a single run.

Look for features that persist across:
- algorithms (e.g., PC vs FCI vs score-based),
- parameter settings (α, penalties),
- tests or scores,
- reasonable variations in assumptions.

Edges or orientations that appear only under narrow settings should be treated as **tentative**.

Grid Search is particularly valuable here, as it exposes which features are stable versus fragile.

---

## 5. What You *Can* Say (With Care)

When supported by diagnostics and robustness:

- “**X and Y are adjacent**”
- “**X → Y is plausible under these assumptions**”
- “**This structure is stable across methods**”
- “**Under causal sufficiency, this orientation holds**”

These statements convey *support*, not certainty.

---

## 6. What You Should Avoid Saying Unqualified

Avoid absolute claims such as:

- “This is the true causal graph”
- “This direction is definitely causal”
- “No edge means no causal relationship”

Absence of an edge may reflect:
- limited power,
- violated assumptions,
- inappropriate tests or scores.

---

## 7. Using Background Knowledge

If background knowledge was incorporated (e.g., time tiers, forbidden edges):

- State what constraints were imposed
- Explain how they influenced the results
- Note whether conclusions depend on those constraints

Conflicts between data-driven results and prior knowledge are *important findings*, not failures.

---

## 8. Communicating Uncertainty Clearly

Responsible interpretation includes:

- identifying stable vs unstable features,
- explaining unresolved edges or orientations,
- tying conclusions explicitly to assumptions.

Example phrasing:

> “Across algorithms and parameter settings, X–Y is consistently adjacent; however, its orientation varies, so we refrain from asserting a causal direction.”

This builds credibility rather than weakening conclusions.

---

## 9. Documenting Your Analysis

For transparency and reproducibility, record:

- data exploration findings,
- assumptions made,
- algorithms and parameters explored,
- evaluation results,
- which conclusions are robust,
- which remain tentative.

This documentation is part of doing causal analysis *well*.

---

## 10. Summary

Interpreting causal discovery results requires more than reading a graph:

- Results are conditional on assumptions
- Robustness matters more than single outputs
- Simplicity and consistency are guiding principles
- Uncertainty should be communicated explicitly

Interpretation is where **causal discovery becomes scientific reasoning**, not just graphical output.

---

## 🧭 What’s Next

With careful interpretation in place, you are positioned to:

- report findings responsibly,
- refine models with new assumptions or data,
- integrate results into downstream causal analysis or decision-making.