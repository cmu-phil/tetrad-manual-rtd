# Search Algorithms

Tetrad provides a wide range of causal discovery algorithms. This page gives a **curated, expert-guided overview** of the algorithms most users should try first.

## 🔍 Choosing an Algorithm

Tetrad’s algorithms for generating DAGs, CPDAGs, or PAGs fall into two broad categories depending on whether you assume  
**no hidden confounders (DAG/CPDAG target)** or  
**possible hidden confounders (PAG target)**.

### **If you assume *no hidden confounders* (DAG target):**
Start with one of these:
- **FGES** — fast, scalable, score-based default
- **BOSS** — order-based; often finds sharper orientations
- **PC / PC-Max** — constraint-based; explicitly tuned by α

---

### **If hidden confounders are possible (PAG target):**
Use one of:
- **FCI** — canonical method for latent confounding / selection bias
- **BOSS-FCI** — score-assisted hybrid improving precision
- **FCIT** — experimental targeted-testing method; guarantees legal PAGs

---

## 🏆Some Recommended Algorithms (With Descriptions)

These are the algorithms most users should consider first.

---

### **PC — Peter–Clark Algorithm**

**Type:** Constraint-based  
**Output:** CPDAG

PC begins with a **complete undirected graph** over all variables. It then systematically removes edges by testing for **conditional independence** over increasing conditioning-set sizes. When two variables become independent given some set S, the edge is removed and S is recorded as a separating set.

After the adjacency phase, PC orients edges by:

1. **Identifying unshielded colliders**  
   If X and Z are nonadjacent but both adjacent to Y, and Y is *not* in the separating set of X and Z, then the triple is oriented:  
   `X → Y ← Z`.

2. **Applying propagation rules**  
   Additional orientations are added (R1–R3) as long as they do not create new unshielded colliders or directed cycles.

The final result is a **CPDAG** representing the Markov equivalence class of DAGs consistent with the detected independence relations.

**When to use PC:**
- You want explicit statistical control through **α**, the significance level for CI tests
- CI test assumptions (e.g., Gaussianity for Fisher Z) fit your data
- You prefer a method grounded directly in conditional independence theory

**Variant:** **PC-Max**, which improves orientation precision by choosing separating sets with **maximum p-value** when multiple valid sets exist.

---

### **FGES — Fast Greedy Equivalence Search**

**Type:** Score-based  
**Output:** CPDAG (assumes no hidden confounders)

FGES starts from an empty graph and greedily **adds edges** that improve the BIC score until no further improvement is possible. It then performs a second, greedy **edge-removal** phase, again optimizing BIC, to produce a final CPDAG.

**When to use FGES:**
- Continuous, discrete, or mixed data
- Hidden confounding is unlikely
- You want speed, scalability, and a clear score-based objective

**Strengths:** Extremely fast and parallelizable; uses an interpretable score (BIC).  
**Limitations:** Assumes **causal sufficiency**—no unmeasured confounders of any variable pair.

---

### **BOSS — Best Order Score Search**

**Type:** Score-based  
**Output:** CPDAG

BOSS searches over **variable orders**, scoring parent sets consistent with each order. It usually yields more accurate graphs (improved precision/recall for both adjacencies and orientations) than FGES or PC.

**When to use:**
- Same settings as FGES
- As a strong alternative CPDAG search or as the score engine for hybrids (e.g., FCIT, BOSS-FCI)

---

### **FCI — Fast Causal Inference**

**Type:** Constraint-based  
**Output:** PAG (allows latent confounders and selection bias)

FCI begins with the **same adjacency search as PC**, producing an undirected skeleton and separating sets.  
It then performs two additional phases:

1. **Extra-edge removal**  
   Uses “possible-d-separation” sets to remove edges that PC cannot detect due to latent confounding.

2. **Orientation phase**  
   Applies an extended set of orientation rules (R0–R10, including collider orientation, discriminating paths, and visible/invisible-edge rules) to produce a **provably correct PAG** under an independence oracle.

The resulting PAG:
- Correctly reflects which adjacencies *must* or *may* be present across all MAGs compatible with the CI oracle
- Correctly marks endpoints (tail, arrowhead, circle) indicating ancestral and non-ancestral constraints
- Gives the **most informative graph possible** assuming only conditional-independence information

**When to use FCI:**
- Hidden confounders **may** exist
- Selection bias **may** exist
- You want a **PAG**, the correct representational target for such settings

**Strengths:**
- **Provably sound and complete** for PAG identification with an oracle
- Handles both latent confounding **and** selection bias
- Modern Tetrad implementation is **fast and optimized** (early “slow FCI” concerns no longer apply)

**Notes:**
- FCI does *not* “miss” orientations; PAGs purposely avoid over-committing to a single MAG.
- For large problems, variants such as RFCI, GFCI, and FCIT can provide speed/precision trade-offs.

---

### **GFCI — Greedy Fast Causal Inference**

**Type:** Hybrid (score + CI tests)  
**Output:** PAG

GFCI is a **hybrid extension of FCI** that starts by learning a **Markov CPDAG** with a score-based search (FGES), then upgrades that result to a **PAG** using FCI-style reasoning. Concretely:

1. **Score phase:**  
   Run FGES to obtain a CPDAG that (approximately) maximizes a score such as BIC.

2. **Latent-variable/PAG phase:**  
   Treat the CPDAG as the starting graph and:
    - remove extra edges using conditional-independence tests (including possible-d-separation sets), then
    - apply FCI orientation rules (R0–R10) to obtain a PAG that accounts for possible latent confounders and selection bias.

The result is a PAG that reflects **both** the score structure (from FGES) and the CI structure (from the independence test).

**When to use GFCI:**
- Latent confounding and/or selection bias may be present
- You want a **PAG** but prefer a **hybrid baseline** that combines score and test information
- You are interested in the classical hybrid that underlies newer methods (BOSS-FCI, GRaSP-FCI, FCIT)

**Strengths:**
- Combines FGES scalability with FCI’s latent-variable semantics
- Often more stable than pure-FCI in finite samples
- Introduces the hybrid design pattern that later algorithms (BOSS-FCI, GRaSP-FCI, FCIT) refine and extend

**Notes:**  
In modern Tetrad, GFCI is best thought of as the **foundational hybrid**; empirically, newer hybrids like **BOSS-FCI**, **GRaSP-FCI**, and especially **FCIT** often outperform it.

---

### **BOSS-FCI — BOSS-Guided Fast Causal Inference**

**Type:** Hybrid (score + CI tests)  
**Output:** PAG

BOSS-FCI follows the **same overall template as GFCI**, but substitutes **BOSS** for FGES in the score phase.  
This gives a sharper initial CPDAG, often with more accurate orientations, which then feeds into the FCI upgrade.

Pipeline:

1. **Score phase (BOSS):**  
   Run BOSS to obtain a CPDAG that typically has:
    - fewer false-positive adjacencies,
    - stronger orientation accuracy,
    - high stability even in nonlinear or non-Gaussian settings.

2. **Latent-variable/PAG phase:**  
   Apply the standard FCI-style steps:
    - remove extra edges using CI tests (including possible-d-separation),
    - apply FCI orientation rules to produce a PAG.

The result is a **PAG** that integrates:
- BOSS’s high-quality score-based structure, and
- FCI’s correctness guarantees for latent confounding and selection.

**When to use BOSS-FCI:**
- You want a PAG
- Latent confounding is plausible
- You prefer a more accurate or sharper starting point than FGES (i.e., sharper than GFCI)

**Strengths:**
- Typically improves adjacencies and orientations compared to GFCI
- Reduces false positives from the score stage
- High precision, especially in moderate-to-large sample sizes

### **FCIT — FCI with Targeted Testing**

**Type:** Hybrid (score-guided CI testing)  
**Output:** PAG (guaranteed legal)

FCIT follows the same broad architecture as **GFCI**, but replaces GFCI’s exhaustive CI-testing steps with a **targeted, score-informed testing strategy**.  
A score engine (typically **BOSS**) identifies which adjacencies are most plausible, and FCIT then performs **only the CI tests that matter**, avoiding low-value or misleading tests that often cause false independences.

Algorithmically, FCIT:

1. **Uses BOSS (or another score) to guide adjacency priorities**  
   → identifies promising edges early  
   → deprioritizes noisy or low-information CI tests

2. **Runs a targeted version of the FCI pruning/orientation steps**  
   → dramatically reduces spurious independences  
   → avoids pathological test sequences

3. **Guarantees a legal PAG**  
   → incorporates an explicit PAG-repair step when needed

Compared to FCI and GFCI, FCIT typically yields:

- **Fewer false-positive independences**
- **Sharper and more stable PAGs**
- **Better orientations**, especially in moderate–large sample sizes
- **Better scalability**, since many CI tests are skipped entirely

**When to use FCIT:**
- You want a PAG
- Hidden confounders are expected
- FCI or GFCI seem unstable or overly noisy
- You have medium–large datasets
- You prefer a **legal-by-construction** PAG
- You’re comfortable using a *new, pre-publication* method

---

## 🎛 Choosing CI Tests & Scores

A quick rule-of-thumb:

- **Continuous Gaussian-ish:** Fisher Z test; SEM-BIC score
- **Discrete:** G-test or Chi-square; BDeu/BIC scores
- **Mixed / nonlinear:** KCI or RCIT (slower); basis-function methods are also available and are more scalable.
- **Covariance-only:** Use algorithms supporting covariance + N (e.g., BOSS with SEM-BIC)

---

## ⚠️ Common Pitfalls

- **Too many edges:** Lower α (constraint-based) or increase penalty (score-based)
- **Too few edges:** Raise α or decrease score penalty
- **Odd orientations:** Try BOSS or PC-Max or add minimal prior knowledge
- **Slow runtime:** Limit depth; try RFCI or FCIT; increase threads

---

## 🧩Full Algorithm List

For the full catalog—including specialized, legacy, and experimental methods—see:

👉 **[Full Algorithm List](search.algorithms.full)**