## Example: Algorithm Selection for the Auto MPG Example

A key modeling decision in causal discovery is whether to **allow for latent (unmeasured) variables** or to assume **causal sufficiency** — that all relevant common causes of the measured variables are included in the dataset.

### 1. Latent Variables vs. Causal Sufficiency

Before selecting an algorithm, ask:

> *Do we believe there are important unmeasured common causes among these variables?*

There are two broad options in Tetrad:

#### Option A: Assume Causal Sufficiency
- All relevant variables are measured.
- The true causal structure can be represented by a **DAG** (or its equivalence class, a CPDAG).
- Algorithms may orient edges more aggressively under this assumption.

**Typical algorithms:**
- BOSS
- GES
- GRaSP
- PC

This assumption is often reasonable for **well-studied, low-dimensional datasets** where the main variables of interest are known and measured.

---

#### Option B: Allow for Latent Variables
- Some common causes may be unobserved.
- The appropriate target is a **PAG**, which explicitly represents latent confounding and orientation uncertainty.

**Typical algorithms:**
- FCI and its variants
- Score-based methods adapted to PAGs (e.g., BOSS-FCI, GRaSP-FCI)

This option is more conservative but typically yields less oriented graphs.

---

### 2. Choice for the Auto MPG Analysis

For the Auto MPG example, we proceed under the **causal sufficiency assumption**:

- The variables represent well-defined mechanical and design features.
- The dataset is relatively small and interpretable.
- Our goal is to illustrate a clear, approachable workflow.

Accordingly, we use **BOSS** as the primary search algorithm.

BOSS is a **score-based search** that:
- Optimizes a global objective
- Balances model fit and complexity
- Works well in continuous and mixed-data settings when paired with an appropriate score

---

### 3. Score Choice: Degenerate Gaussian BIC

Based on data exploration:

- Relationships appear largely linear
- The data include both continuous variables and a discrete variable (`origin`)
- No strong evidence suggests a need for nonlinear modeling

We therefore use the **Degenerate Gaussian BIC score**, which:

- Extends Gaussian likelihood-based scoring to mixed data
- Is appropriate when discrete variables have a small number of categories
- Naturally penalizes overly complex models

This score choice is **consistent with the observed structure** in the plot matrix and provides a principled baseline for comparison.

---

### 4. Summary of Choices

For this example, we adopt the following modeling decisions:

- **Latent variables:** *Not allowed* (assume causal sufficiency)
- **Search algorithm:** BOSS
- **Score:** Degenerate Gaussian BIC
- **Rationale:** Matches data type, observed structure, and pedagogical goals

These choices are not claimed to be “true,” but they form a **coherent, defensible starting point** that can later be relaxed or challenged using alternative assumptions and diagnostics.