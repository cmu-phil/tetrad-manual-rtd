# Search Algorithms

Tetrad provides a wide range of causal discovery algorithms. This page gives a **curated, expert-guided overview** of the algorithms most users should try first.

## 🔍 Choosing an Algorithm

Tetrad’s algorithms fall into two broad categories depending on whether you assume  
**no hidden confounders (DAG/CPDAG target)** or  
**possible hidden confounders (PAG target)**.

### **If you assume *no hidden confounders* (DAG target):**
Start with one of these:
- **FGES** — fast, scalable, score-based default
- **BOSS** — order-based; often finds sharper orientations
- **PC / PC-Max** — constraint-based; explicitly tuned by α

> GRaSP can provide complementary insight to BOSS, though it is not as scalable.

---

### **If hidden confounders are possible (PAG target):**
Use one of:
- **FCI** — canonical method for latent confounding / selection bias
- **BOSS-FCI** — score-assisted hybrid improving precision
- **FCIT** — experimental targeted-testing method; guarantees legal PAGs

RFCI is a speed-optimized alternative when FCI is too slow.

---

## 🏆Some Recommended Algorithms (With Descriptions)

These are the algorithms most users should consider first.

---

### **FGES — Fast Greedy Equivalence Search**

**Type:** Score-based  
**Output:** CPDAG (assumes no hidden confounders)

FGES performs greedy hill-climbing over equivalence classes of DAGs using a penalized score (typically SEM-BIC). It is extremely fast and effective for medium to large datasets.

**When to use:**
- Continuous or discrete data
- No major latent confounding expected
- You want speed and a clear objective score

**Strengths:** Highly scalable, parallelizable, interpretable score.  
**Limitations:** Assumes causal sufficiency.

---

### **BOSS — Best Order Score Search**

**Type:** Score-based  
**Output:** CPDAG

BOSS searches over **variable orders**, scoring parent sets consistent with each order. Often yields more decisive orientations than structure-only hill-climbing.

**When to use:**
- Same settings as FGES
- As a strong alternative or as the score engine for hybrids (e.g., FCIT, BOSS-FCI)

---

### **PC — Peter–Clark Algorithm**

**Type:** Constraint-based  
**Output:** CPDAG

PC identifies adjacencies through conditional independence tests, then orients using standard PC rules.

**When to use:**
- You want explicit statistical control via α
- CI test assumptions match your data

**Notable variant:** **PC-Max**, which improves orientation precision.

---

### **FCI — Fast Causal Inference**

**Type:** Constraint-based  
**Output:** PAG (allows latents + selection bias)

FCI is the standard algorithm for discovering causal structure when unmeasured confounders or selection bias may be present.

**When to use:**
- You need a PAG
- Latent confounding is plausible

**Limitations:** Runs many CI tests; can be conservative or slow.

---

### **RFCI — Really Fast Causal Inference**

**Type:** Constraint-based  
**Output:** PAG

RFCI uses more aggressive pruning than FCI, trading some completeness for significant gains in speed.

**When to use:**
- High-dimensional data
- FCI is too slow
- Preliminary latent-variable structure discovery

---

### **GFCI — Greedy Fast Causal Inference**

**Type:** Hybrid (score + CI tests)  
**Output:** PAG

GFCI combines score-based search (e.g., FGES) with FCI-style pruning/orientation. Often the strongest general-purpose method for latent-variable cases.

**When to use:**
- Latent confounding expected
- You want higher precision/recall than FCI alone

---

### **BOSS-FCI — BOSS-Score Hybrid for FCIs**

**Type:** Hybrid  
**Output:** PAG

Uses the BOSS score engine to propose a structure, followed by FCI-style testing and orientation. Often improves orientations and reduces false positives.

---

### **FCIT — FCI with Targeted Testing**

**Type:** Hybrid  
**Output:** PAG (guaranteed legal)

*FCIT is an experimental, not-yet-published enhancement of FCI.*  
It uses score information (typically from BOSS) to **prioritize CI tests**, steering the search away from low-value or misleading independence tests.

Compared to FCI or GFCI:

- **Produces a guaranteed legal PAG**
- Reduces spurious independences
- Often runs faster on medium–large datasets
- Provides cleaner, more stable latent-variable structure

**When to use:**
- Medium–large datasets
- FCI or GFCI appear unstable or noisy
- You want a certified-legal PAG
- You are comfortable using an experimental method

---

## 🎛 Choosing CI Tests & Scores

A quick rule-of-thumb:

- **Continuous Gaussian-ish:** Fisher Z test; SEM-BIC score
- **Discrete:** G-test or Chi-square; BDeu/BIC scores
- **Mixed / nonlinear:** KCI or RCIT (slower); basis-function methods may help
- **Covariance-only:** Use algorithms supporting covariance + N (e.g., FGES with SEM-BIC)

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

[//]: # (---)

[//]: # ()
[//]: # (## 📄 Algorithm Parameters)

[//]: # ()
[//]: # (All algorithm parameters are documented here:)

[//]: # ()
[//]: # (👉 [`parameter.definitions.md`]&#40;./parameter.definitions.md&#41;)

[//]: # ()
[//]: # (Machine-readable source:)

[//]: # ()
[//]: # (👉 [`parameter.definitions.txt`]&#40;./_static/manual/parameter.definitions.txt&#41;)