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
- **Fisher Z Test**  
  The default in Tetrad and the most reliable choice for continuous data.  
  Fast, robust, and statistically well-understood.

- **Partial Covariance / Partial Correlation Tests**  
  Equivalent variants used by some algorithms.

### Recommended Scores
- **Sem BIC Score**  
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
- **G² / Chi-Square Test**  
  Best for moderate–large samples.

- **Discrete BDeu Test**  
  Bayesian alternative better for smaller samples or sparse contingency tables.

### Recommended Scores
- **Discrete BDeu Score**  
  Works well for small–medium models.  
  **Note:** For large numbers of discrete variables, CPTs explode.

### Best-Fit Algorithms
- **BOSS** (preferred for discrete; handles small–medium models extremely well)
- **FGES** (works, but CPT blowup can be prohibitive; use only when p is modest)
- PC / GFCI / RFCI with G² or BDeu tests

**Rule of thumb:**  
Finite-state models are rarely high-dimensional; for score-based search on discrete data:  
**BOSS > FGES**.

---

## 3. Mixed Continuous/Discrete Data

Mixed data requires special handling. In Tetrad you have **three practically useful options**:

### A. Conditional Gaussian (CG)
- **CG Independence Test**
- **CG BIC Score**

Works when continuous variables are approximately Gaussian within levels of discrete parents.  
Statistically principled but slower.

### B. Degenerate Gaussian (DGC)
- **Degenerate Gaussian Test**
- **Degenerate Gaussian Score**

Treats discrete variables as “degenerate Gaussians.”  
Much faster than full CG for large data.

### C. Basis Function (BF) Tests/Scores  **(highly recommended)**
- **Basis Function CI Test**
- **Basis Function BIC Score**

This approach expands continuous variables using orthogonal polynomials (Legendre/Chebyshev):  
✓ works for mixed data  
✓ handles **nonlinear** relationships  
✓ extremely fast compared to kernel methods  
✓ sample-size scaling ~ constant

**This is the best general-purpose choice** when data includes both continuous and discrete variables.

---

## 4. Non-Gaussian Linear Models

If relationships are linear but noise terms are non-Gaussian (LiNGAM-type models):

### Recommended Tests
- **Poisson BIC Test**  
  Good when non-Gaussianity manifests as asymmetric or skewed distributions.

- **ICA-based independence tests**  
  Used internally by LiNGAM-style methods.

### Recommended Scores
- **Poisson BIC Score**

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
- Captures **arbitrary nonlinear** dependencies.
- Very powerful but computationally expensive for large N.
- Best for small–medium datasets.

### B. Basis Function Test / Score (**Recommended for scalability**)
- Nonlinear via polynomial expansions.
- Post-nonlinear models.
- Often matches or outperforms KCI on large N due to superior speed.

### C. CCI (Conditional Correlation Independence) — *Minimal recommendation*
- Fast additive-noise model test.
- Works only when the model is truly additive.
- Empirically weaker and more restrictive than KCI or BF.

**Rule of thumb:**

| Goal | Recommended |
|------|-------------|
| Best accuracy for nonlinear CI | **KCI** |
| Best speed + strong accuracy | **Basis Function Test/BIC** |
| Additive-noise special case | CCI (if you must) |

---

## 6. Latent Variable Workflows (Block-Based Search)

When you run latent clustering (TSC, FOFC, FTFC, GFFC, BPC), you obtain **clusters → latent nodes**.  
You can then run structure discovery over those latent nodes.

### Block-Based Tests/Scores
- **Blocks-Test-TS**  
  Trek-separation test on clusters.

- **Blocks-BIC Score**  
  A block-aware score for FGES, BOSS, GRaSP, SP, etc.

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
| Continuous linear | Fisher Z | Sem BIC | PC, FGES, BOSS, GFCI |
| Discrete | G² or BDeu | BDeu | BOSS*, FGES, PC |
| Mixed | BF Test | BF BIC | PC, FGES, BOSS, GFCI |
| Linear non-Gaussian | Poisson or ICA | Poisson BIC | LiNGAM, FASK |
| Nonlinear | **KCI** | (none / kernel-based) | PC+KCI, CAM |
| Nonlinear scalable | **Basis Function Test** | BF BIC | PC+BF, GFCI+BF |
| Latent blocks | Blocks-Test-TS | Blocks-BIC | PC, GFCI, FGES, BOSS |

\* **BOSS is recommended over FGES** unless p is very large.

---

## Next Steps

- **[Tests & Scores Catalog](tests-and-scores-catalog.md)**
- **[Search Algorithms — Short List](search-algorithms-short-list.md)**
- **[Latent Clustering](algorithms/latent-cluster.md)**
- Per-algorithm documentation for parameter definitions