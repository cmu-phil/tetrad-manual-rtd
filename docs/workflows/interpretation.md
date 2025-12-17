# Interpreting Results

After exploring your data, choosing methods, systematically searching, and evaluating candidate models (see *Data Exploration*, *Algorithm Selection*, *Running Searches*, and *Model Evaluation and Markov Checking*), the final step in the causal analysis workflow is **interpreting your results responsibly**.

Causal discovery outputs — whether DAGs, CPDAGs, or PAGs — are not definitive “truths.” They are **models that fit patterns in the data under specific assumptions**. This page helps you understand what you can *reasonably conclude* from such outputs, and how to communicate uncertainty and robustness.

---

## 1. What Your Target Graph Represents

A causal graph estimated from data is **a hypothesis about causal relationships** that:

- is consistent with the data’s conditional independence structure,
- reflects the assumptions made (e.g., causal sufficiency, linearity),
- and is influenced by method and parameter choices.

It is *not* a guaranteed causal truth.

Thus:

> **Interpretation is about plausible conclusions, not certainties.**

---

## 2. Types of Output and What They Mean

### 2.1. Fully Directed Acyclic Graphs (DAGs)

A fully oriented DAG implies causal directions for all adjacencies.

**When to trust:**
- Strong assumptions (e.g., causal sufficiency)
- Good model evaluation support (e.g., Markov consistency)
- Supporting domain knowledge

**What to report:**
- Directed edges with supporting tests
- Explicit assumptions under which those directions hold
- Notes on edges that are borderline uncertain

---

### 2.2. Completed Partially Directed Acyclic Graphs (CPDAGs)

CPDAGs represent an **equivalence class**, where:
- Some edge orientations are identified
- Others remain ambiguous

**What you can conclude:**
- Adjacencies are robust under the given assumptions
- Some directions are invariant across the equivalence class
- Unoriented edges mean *direction is not identifiable* from the data and assumptions

---

### 2.3. Partial Ancestral Graphs (PAGs)

PAGs allow for latent confounders and present multiple edge marks:
- `→`, `←` for oriented relationships
- `o→`, `o–o`, etc. for uncertain orientations with latent possibilities

**What to report:**
- Which adjacencies are robust
- Which orientations are identified
- Which relationships remain ambiguous due to potential latent confounding

---

## 3. How to Interpret Common Edge Marks

| Symbol | Interpretation |
|--------|----------------|
| **A → B** | Oriented edge (under assumptions and given test/score) |
| **A – B** | Adjacent, orientation not identified |
| **A o→ B** | Orientation with uncertainty or latent possibility |
| **A ↔ B** | Possible latent confounder implied |
| **A o–o B** | Both orientation and latent presence uncertain |

> Always explain what assumptions underlie the interpretation of each mark. A casual reader will not know this by default.

---

## 4. Robustness and Stability

Strong conclusions rest on **robust pattern recovery** across:

- Different algorithms (e.g., PC vs FCI vs score-based)
- Different parameter settings (e.g., α or penalty)
- Different tests/scores
- Minor data perturbations (e.g., subsampling or bootstrap)

If a structure (edge or orientation) is only produced under narrow settings, treat it as *tentative*.

---

## 5. What You *Can* Say (When Appropriate)

- “**X is adjacent to Y**” — if the edge appears robustly across methods/settings.
- “**X → Y** is plausible” — when orientations are stable and evaluated models pass diagnostics.
- “**This edge pattern persists** across tests/scores” — conveys stability, not certainty.
- “**Under assumption set A** this direction holds” — anchors claims in assumptions.

---

## 6. What You *Should Not* Say Without Qualification

- “**This is the true causal graph**” — causal discovery does not prove truth.
- “**This orientation is definitely causal**” — unless supported by interventions or strong background knowledge.
- “**No edges = no causation**” — absence may reflect lack of power, misspecification, or violations of assumptions.

Always qualify structural claims with assumptions and diagnostic results.

---

## 7. Incorporating Background Knowledge

When you included background knowledge (e.g., time tiers, forbidden edges, prior causal claims):

- Explain what constraints were used
- Clarify how they influenced search and orientation
- Discuss whether results are consistent with that knowledge

If results conflict with prior knowledge, that’s important to investigate — it could suggest:
- Data issues
- Inappropriate assumptions
- Genuine novel insights

---

## 8. Communicating Uncertainty

A mature interpretation includes:

- **Admitted uncertainty** where models disagree
- **Highlighting stable features** (edges/orientations that persist)
- **Explaining why some features are unresolved**
- **Linking back to assumptions**

Example phrasing:

> “Under assumptions of causal sufficiency and linearity, the edge X–Y is consistently found; however, its orientation varies across settings, so we refrain from asserting a causal direction.”

---

## 9. Documenting Your Interpretation

Good documentation benefits both *yourself* and *your audience*. For each analysis, record:

- Data exploration findings
- Assumptions made
- Algorithms and parameters used
- Evaluation results (Markov and others)
- Which features of the graph you interpret with confidence
- Which features remain tentative

This makes your conclusions transparent and reproducible.

---

## 10. Summary

Interpreting causal discovery results is not a matter of reading a graph at face value. It requires:

- Understanding algorithmic limitations
- Tying claims to assumptions and diagnostics
- Emphasizing robustness
- Communicating uncertainty clearly

Interpretation is where *causal modeling becomes scientific reasoning*, not just graphical output.

---

## 🧭 What’s Next

With interpretive grounding in place, users are equipped to:

- Report results responsibly
- Investigate further with interventions or experiments
- Integrate discovered structure into downstream modeling or decision-making