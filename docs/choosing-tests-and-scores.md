# Choosing Tests & Scores

Selecting the right conditional-independence test or score is one of the most important modeling decisions in Tetrad. Many search algorithms (PC, FGES, BOSS, GFCI, etc.) allow you to choose a test/score tailored to your data type and modeling assumptions.

This page gives practical guidance on which tests and scores to use for:

- Continuous (Gaussian / nearly Gaussian)
- Discrete
- Mixed continuous/discrete
- Non-Gaussian linear models
- Nonlinear models (KCI, basis expansions)
- Latent-variable block-based searches

The goal is not to list every option, but to highlight the ones that **work well in practice** in real causal-discovery workflows.

---

## 1. Continuous, Approximately Gaussian Data

When variables are continuous, roughly symmetric, and well-modelled by linear relationships:

### Recommended Tests

- **[Fisher Z Test](tests-and-scores/fisher-z.md)**  
  The default in Tetrad and the most reliable choice for continuous data.  
  Fast, robust, and statistically well-understood.

- **Partial Covariance / Partial Correlation Tests**  
  Equivalent variants used by some algorithms (conceptually the same family as the Fisher Z / partial-correlation approach).

### Recommended Scores

- **[Sem BIC Score](tests-and-scores/sem-bic-score.md)**  
  The standard linear-Gaussian score.

### Best-Fit Algorithms

- PC, PC-Max, CPC
- FGES (high-dimensional)
- BOSS (small–medium dimensional; often gives better precision than FGES)
- GRaSP
- GFCI / RFCI

**Rule of thumb:**  
If nothing fancy is required, use **Fisher Z** and **Sem BIC**.

---

## 2. Discrete Data (Binary / Ordinal / Categorical)

Discrete CI testing behaves very differently from continuous modeling. Tetrad offers fast standard tests plus Bayesian alternatives.

### Recommended Tests

- **[G²](tests-and-scores/g-square.md) / [Chi-Square Test](tests-and-scores/chi-square.md)**  
  Best for moderate–large samples.

- **“BDeu-style” Bayesian tests**  
  (Logically aligned with the [BDeu Score](tests-and-scores/bdeu-score.md), especially in small-sample / sparse-table settings.)

### Recommended Scores

- **[Discrete BDeu Score](tests-and-scores/bdeu-score.md)**  
  Works well for small–medium models.  
  **Note:** For large numbers of discrete variables, CPTs explode.

### Best-Fit Algorithms

- **BOSS** (preferred for discrete; handles small–medium models extremely well)
- **FGES** (works, but CPT blowup can be prohibitive; use only when p is modest)
- PC / GFCI / RFCI with G² or BDeu-type tests

**Rule of thumb:**  
Finite-state models are rarely high-dimensional; for score-based search on discrete data:  
**BOSS > FGES**.

---

## 3. Mixed Continuous/Discrete Data

Mixed data requires special handling. In Tetrad you have **three practically useful options**:

### A. Conditional Gaussian (CG)

- **CG Independence Test** → **[ConditionalGaussianLrt](tests-and-scores/conditional-gaussian-lrt.md)**
- **CG BIC Score** → **[ConditionalGaussianBicScore](tests-and-scores/conditional-gaussian-bic-score.md)**

Works when continuous variables are approximately Gaussian within levels of discrete parents.  
Statistically principled but slower.

### B. Degenerate Gaussian (DGC)

- **Degenerate Gaussian Test** → **[DegenerateGaussianLrt](tests-and-scores/degenerate-gaussian-lrt.md)**
- **Degenerate Gaussian Score** → **[DegenerateGaussianBicScore](tests-and-scores/degenerate-gaussian-bic-score.md)**

Treats discrete variables as “degenerate Gaussians.”  
Much faster than full CG for large data.

### C. Basis Function (BF) Tests/Scores  **(highly recommended)**

- **Basis Function CI Test** → **[BasisFunctionLrt](tests-and-scores/basis-function-lrt.md)**
- **Basis Function BIC Score** → **[BasisFunctionBicScore](tests-and-scores/basis-function-bic-score.md)**

This approach expands continuous variables using orthogonal polynomials (Legendre/Chebyshev):

- works for mixed data
- handles **nonlinear** relationships
- extremely fast compared to kernel methods
- sample-size scaling ~ constant

**This is the best general-purpose choice** when data includes both continuous and discrete variables.

---

## 4. Non-Gaussian Linear Models

If relationships are linear but noise terms are non-Gaussian (LiNGAM-type models):

### Recommended Tests

- **[Poisson BIC Test](tests-and-scores/poisson-bic-test.md)**  
  Good when non-Gaussianity manifests as asymmetric or skewed distributions.

- **ICA-based independence tests**  
  Used internally by LiNGAM-style methods (not exposed as separate test pages in this manual).

### Recommended Scores

- **“Poisson BIC”–type scores** → **[PoissonPriorScore](tests-and-scores/poisson-prior-score.md)**  
  (Score for linear non-Gaussian models with Poisson-like or skewed noise.)

### Best-Fit Algorithms

- DirectLiNGAM
- ICA-LiNGAM, ICA-LiNG-D
- FASK / FASK-Vote
- Pairwise Skewness

**Rule of thumb:**  
If your data has visible skew or heavy tails, consider Poisson or ICA-based methods.

---

## 5. Nonlinear Models

Tetrad provides three practically useful nonlinear CI tests.

### A. Kernel Conditional Independence Test (**KCI**) — *Recommended*

- **[KCI](tests-and-scores/kci-test.md)**

Captures **arbitrary nonlinear** dependencies.  
Very powerful but computationally expensive for large N.  
Best for small–medium datasets.

### B. Basis Function Test / Score (**Recommended for scalability**)

- **[Basis Function CI Test](tests-and-scores/basis-function-lrt.md)**
- **[Basis Function BIC Score](tests-and-scores/basis-function-bic-score.md)**

- Nonlinear via polynomial/orthogonal expansions.
- Post-nonlinear models.
- Often matches or outperforms KCI on large N due to superior speed.

### C. CCI (Conditional Correlation Independence) — *Minimal recommendation*

- **[CCI Test](tests-and-scores/cci-test.md)**

- Fast additive-noise model test.
- Works only when the model is truly additive.
- Empirically weaker and more restrictive than KCI or BF.

**Rule of thumb:**

| Goal | Recommended |
|------|-------------|
| Best accuracy for nonlinear CI | **[KCI](tests-and-scores/kci-test.md)** |
| Best speed + strong accuracy | **[Basis Function Test](tests-and-scores/basis-function-lrt.md)** / **[Basis Function BIC](tests-and-scores/basis-function-bic-score.md)** |
| Additive-noise special case | **[CCI](tests-and-scores/cci-test.md)** (if you must) |

---

## 6. Latent Variable Workflows (Block-Based Search)

When you run latent clustering (TSC, FOFC, FTFC, GFFC, BPC), you obtain **clusters → latent nodes**.  
You can then run structure discovery over those latent nodes.

### Block-Based Tests/Scores

- **Blocks-Test-TS**  
  Trek-separation test on clusters.

- **Blocks-BIC Score**  
  A block-aware score for FGES, BOSS, GRaSP, SP, etc.

(These are not yet documented as separate test/score pages in this manual.)

### Compatible Algorithms

Any algorithm that accepts a test and/or score:

- PC (default choice)
- GFCI / RFCI
- FGES (when clusters are few)
- BOSS (very strong for moderate-sized latent structures)
- GRaSP or SP (if small)

### Typical Workflow

1. Run clustering (e.g., TSC)
2. Convert clusters → latent variables
3. Choose Blocks-Test-TS or Blocks-BIC
4. Run PC, GFCI, BOSS, FGES, or others

This is the recommended approach for **latent causal structure without specifying measurement models**.

---

## Summary Table (Practical Defaults)

| Setting | Test | Score | Algorithms |
|--------|------|--------|-----------|
| Continuous linear | [Fisher Z](tests-and-scores/fisher-z.md) | [Sem BIC](tests-and-scores/sem-bic-score.md) | PC, FGES, BOSS, GFCI |
| Discrete | [G²](tests-and-scores/g-square.md) or BDeu-style tests | [BDeu](tests-and-scores/bdeu-score.md) | BOSS\*, FGES, PC |
| Mixed | [Basis Function Test](tests-and-scores/basis-function-lrt.md) | [Basis Function BIC](tests-and-scores/basis-function-bic-score.md) | PC, FGES, BOSS, GFCI |
| Linear non-Gaussian | [Poisson BIC Test](tests-and-scores/poisson-bic-test.md) or ICA-based | [PoissonPriorScore](tests-and-scores/poisson-prior-score.md) | LiNGAM, FASK |
| Nonlinear | [KCI](tests-and-scores/kci-test.md) | (none / kernel-based) | PC+KCI, CAM |
| Nonlinear scalable | [Basis Function Test](tests-and-scores/basis-function-lrt.md) | [Basis Function BIC](tests-and-scores/basis-function-bic-score.md) | PC+BF, GFCI+BF |
| Latent blocks | Blocks-Test-TS | Blocks-BIC | PC, GFCI, FGES, BOSS |

\* **BOSS is recommended over FGES** unless p is very large.

---

## Next Steps

- **[Tests & Scores Catalog](tests-and-scores-catalog.md)**
- **[Search Algorithms — Short List](search-algorithms-short-list.md)**
- **[Latent Clustering](algorithms/latent-cluster.md)**
- Per-algorithm documentation for parameter definitions