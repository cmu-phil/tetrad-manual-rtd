# Factor Analysis

**Category:** Latent Structure / Measurement Models  
**Type:** Classical factor analysis (linear-Gaussian)

Factor Analysis is the standard statistical method for learning continuous
measurement models. It assumes that each observed variable is a linear
combination of one or more latent factors plus independent Gaussian noise.
Tetrad provides a lightweight wrapper so that factor-analysis results can be
integrated into causal discovery workflows.

---

## Purpose

Use FactorAnalysis when you want a traditional **measurement model** for forming
latent variables prior to structural modeling.

It estimates:
- latent factors,
- loadings of indicators on each factor,
- unique variances,
- and covariances among factors.

The resulting latent variables can then be handed off to FGES, PC, GFCI, or any
other Tetrad algorithm.

---

## When to Use

- You want a **classical** factor model (linear, continuous, Gaussian).
- You believe variables load cleanly onto latent factors.
- You need latent scores for downstream causal modeling.
- You prefer parametric estimation over trek-separation clustering.

---

## How It Works (Conceptual)

1. Compute the covariance matrix of the observed variables.
2. Estimate loadings that best explain this covariance using linear factor
   decomposition.
3. Determine factor scores (latent-variable estimates) via regression or ML.
4. Return a measurement model where latent variables are linked to their
   indicators.

---

## Strengths

- Widely used and well-understood.
- Produces interpretable loadings and factor scores.
- Integrates naturally with SEM and MIM-building workflows.

---

## Limitations

- Assumes **linearity** and **Gaussian noise**.
- Sensitive to model misspecification.
- Does not identify clusters automatically—you must choose the number of factors.

### Parameters

| Parameter (camelCase)       | Description |
|-----------------------------|-------------|
| `fa_threshold`              | Non-negative double. Threshold used when deciding which factor loadings are considered “large enough” to be substantive. Typical values are small (e.g., 0.1–0.4). |
| `numFactors`                | Integer ≥ 1. The number of latent factors to extract. If set incorrectly, factors may be under- or over-extracted. |
| `useVarimax`                | Boolean. If `true`, applies Varimax rotation to the loading matrix, producing a more interpretable factor structure. If `false`, uses the raw (unrotated) solution. |
| `convergenceThreshold`      | Small positive double. Iterative fitting stops when the change in log-likelihood or parameter estimates falls below this threshold. Typical values: 1e-4 to 1e-8. |
| `verbose`                   | Boolean. If `true`, prints detailed progress messages during factor extraction and rotation. |

---

## Relation to Other Latent Tools

- For *pure-cluster discovery*, use **TSC**, **FOFC**, **FTFC**, **GFFC**, or **BPC**.
- For automated latent construction after clustering, see **MimbuildBollen** or **MimbuildPca**.
- For non-Gaussian or nonlinear latent orientation, see **GIN**.

---

## References

- Classical SEM / factor-analysis literature (Harman 1976; Bollen 1989).

## Summary

Factor Analysis extracts a classical linear-Gaussian measurement model in
which observed variables load on a small number of latent factors. It provides
interpretable loadings, latent scores, and unique variances, and integrates
smoothly with downstream causal discovery (e.g., FGES, PC, GFCI, MIM-building).
It is best suited to continuous data with approximately linear structure and is
limited when indicators exhibit strong nonlinearity, non-Gaussianity, or
complex latent clustering patterns.