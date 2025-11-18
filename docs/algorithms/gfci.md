# GFCI — Greedy Fast Causal Inference
**Type:** Hybrid (Score + Constraints)  
**Output:** **PAG**  
**Reference:** *Ogarrio, Spirtes & Ramsey (PGM 2016)*

GFCI is a **hybrid latent-variable causal discovery algorithm** that combines:

- a **score-based CPDAG search** (FGES), and  
- a **constraint-based refinement phase** (FCI-style tests)

to produce a **PAG** that is sound for models containing **latent confounding** and **selection bias**.

It serves as the **parent template** for the other hybrid latent-variable algorithms in Tetrad, including:  
➡️ **BOSS-FCI**, **GRaSP-FCI**, and **FCIT**.

---

## 🔍 Key Idea

GFCI proceeds in **two stages**:

### 1. **Score-Based CPDAG Search (FGES)**  
FGES finds a high-scoring CPDAG using SEM-BIC or another score.  
This provides:
- a good **skeleton**,  
- many **arrow orientations**,  
- and a **search space** strongly biased toward plausible structures.

This dramatically reduces the number of CI tests required in the next stage.

### 2. **FCI-Style Refinement**  
Given the FGES CPDAG, GFCI applies:
- conditional independence tests,
- collider identification logic,
- and PAG orientation rules

to correct mistakes caused by latent variables or selection bias, ultimately producing a **correct PAG** in the large-sample limit.

This refinement step is similar to FCI and RFCI but operates over a much
smaller set of adjacencies—making it faster and more robust.

---

## 🎯 When to Use GFCI

- You expect **latent confounding** or **selection bias**.  
- You want a **PAG** but need more **efficiency** or **robustness** than pure FCI.  
- You trust a **score-based model** (FGES) to find a good CPDAG skeleton.  
- You want a strong hybrid baseline before trying BOSS-FCI, GRaSP-FCI, or FCIT.

GFCI remains one of the most practical algorithms for medium-to-large models with latent structure.

---

## 🧠 Prior Knowledge

**Fully supported.**  
GFCI respects:
- required edges  
- forbidden edges  
- temporal/tier constraints  
- arbitrary `Knowledge` objects  

Knowledge is honored during both FGES and the FCI-style refinement.

---

## ⭐ Strengths

- **Much faster** than FCI on moderate–large data  
- Reduces spurious CI tests by starting from a strong score-based CPDAG  
- Produces high-quality PAGs in many real datasets  
- Template for all modern hybrid latent-variable methods in Tetrad

---

## ⚠️ Limitations

- Inherits FGES’s weaknesses on **dense** or **nonlinear/non-Gaussian** models.  
- Final PAG depends partly on score heuristics from stage 1.  
- Not as aggressive or accurate as FCIT when data are noisy or small-sample.

---

## 🔧 Key Parameters (Tetrad)

| Parameter | Meaning |
|----------|----------|
| `score` | The score used by FGES (SEM-BIC, mixed-BIC, etc.). |
| `faithfulnessAssumed` | If true, FGES may skip some tests and orientations. |
| `maxDegree` | Pruning constraint for FGES; limits parent set size. |
| `numThreads` | Degree of parallelism for FGES scoring. |
| `verbose` | Prints decisions during both stages. |
| `timeLag`, `timeLagReplicatingGraph` | For time-series adaptations. |

(*FGES parameters come directly from FGES; GFCI adds its own CI-test choices for the refinement stage.*)

---

## ⛓ Relation to Other Algorithms

- **FCI** — Constraint-only PAG learning  
- **RFCI** — Faster, more conservative variant  
- **GFCI** — Hybrid: *FGES → FCI refinement*  
- **BOSS-FCI** — Uses **BOSS** instead of FGES  
- **GRaSP-FCI** — Uses **GRaSP** instead of FGES  
- **FCIT** — Uses **targeted testing** guided by scores

GFCI is the **parent template** for the hybrid latent-variable algorithms in Tetrad.

---

## 📚 Reference

Ogarrio, J. M., Spirtes, P., & Ramsey, J. (2016).  
*A hybrid causal search algorithm for latent variable models.*  
In **PGM 2016**, pp. 368–379.
