# FCI-IOD — FCI with Independent Overlapping Datasets

**Type:** Constraint-based (multi-dataset)
**Output:** PAG
**Reference:** Tillman & Spirtes (2011). *Learning equivalence classes of acyclic models with latent and selection variables from multiple datasets with overlapping variables.* AISTATS.

FCI-IOD extends the standard **Fast Causal Inference (FCI)** algorithm to work with **multiple datasets that contain different (but overlapping) subsets of variables**.
It uses the **IOD (Independent Overlapping Datasets)** independence test, which pools CI information across datasets to infer a single PAG over the union of variables.

---

## Key Idea

When multiple datasets each contain only *some* of the variables (e.g., due to study design, missing experimental modules, data collection constraints), standard CI testing cannot be applied directly, because not all conditioning sets are available in every dataset.

FCI-IOD solves this by:

1. **Pooled CI testing (IOD test)**
   - Performs CI tests across all datasets where the relevant variables are jointly observed.
   - Combines their evidence to decide conditional independence or dependence.

2. **Modified FCI search**
   - Uses these pooled CI judgments for adjacency search.
   - Applies the standard FCI orientation rules to produce a PAG representing all models compatible with the (pooled) CI information.

3. **Full union graph**
   - Produces a PAG over **all variables observed in any dataset**, even those never jointly observed in one dataset.

The result is a latent/selection-robust PAG that integrates information across overlapping datasets.

---

## When to Use

Use FCI-IOD when:

- You have **multiple observational datasets** with **partially overlapping variable sets**.
  (e.g., Dataset A has {X, Y, Z}, Dataset B has {Y, Z, W}, etc.)
- Variables may share **latent confounders**.
- Variables may be subject to **selection bias** in some datasets.
- You want a **single, integrated causal model** over all variables.

Typical applications:

- Consortium or multi-site studies where different labs measure different subsets of variables.
- Combining datasets across years where instrument batteries change.
- Merging clinical datasets with heterogeneous measurement panels.

---

## Prior Knowledge Support

FCI-IOD accepts the same background knowledge as FCI:

- **Required edges**
- **Forbidden edges**
- **Temporal / tier constraints**

Knowledge is enforced during adjacency pruning and orientation.

---

## Strengths

- **Integrates multiple datasets** with differing variable sets.
- **Latent-variable and selection-bias robust**, through FCI logic.
- Produces a **single PAG** covering all measured variables.
- Leverages **all available CI information**, even when no dataset contains all variables jointly.

---

## Limitations

- Computational cost grows with:
  - number of datasets
  - size of variable union
  - size of conditioning sets
- Relies on the correctness of the pooled **IOD independence test**.
- Finite-sample instability can propagate across datasets.
- Produces a PAG, which may be highly partially oriented when coverage is sparse.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `independenceTest`    | Should be set to **IndTestIod**, which performs pooled CI tests across datasets. |
| `datasets`            | The list of input datasets (each a DataSet object) with overlapping variable sets. |
| `alpha`               | Significance level for CI testing. |
| `depth`               | Max conditioning-set size. |
| `verbose`             | Whether to print detailed processing logs. |
| `knowledge`           | Background knowledge (required/forbidden edges, tiers). |

---

## Reference

Tillman, R., & Spirtes, P. (2011).
*Learning equivalence classes of acyclic models with latent and selection variables from multiple datasets with overlapping variables.*
In **AISTATS**, pp. 3–15.

---

## Summary

FCI-IOD extends FCI to the setting of **multiple datasets with overlapping variable sets**, pooling CI information through the IOD test to produce a unified, latent-variable–robust PAG over all variables.