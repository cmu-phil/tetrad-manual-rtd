# PCD — PC for Deterministic Relations

**Type:** Constraint-based  
**Output:** CPDAG  
**Reference:**  
Glymour, C. (2007). *Learning the structure of deterministic systems.*  
In **Causal Learning: Psychology, Philosophy, and Computation**, pp. 231–240.

Pcd is a variant of the PC algorithm designed to handle **deterministic** or **near-deterministic functional relationships**—situations where one variable is an exact or almost exact function of others (e.g., sums, ratios, duplicates, encoded transformations). Such relations violate the **faithfulness** assumption underlying PC and can lead to spurious edges.  
Pcd adds safeguards to prevent deterministic relations from corrupting adjacency search and collider orientation.

---

## Key Idea

Determinism breaks the usual CI patterns:

> If \(Y = f(X)\), then \(X\) and \(Y\) are *never* independent—even when conditioning would ordinarily separate them under faithfulness.

To address this, Pcd introduces:

1. **Detection of (near-)deterministic relations**  
   Identifies variables involved in deterministic mappings using heuristic or test-based diagnostics.

2. **Suppression of invalid CI tests**  
   Avoids CI tests that would be misleading under determinism (e.g., tests that *should* show independence but cannot).

3. **Adjusted adjacency pruning**  
   Prevents deterministic variables from forcing large, spurious cliques in the skeleton.

4. **PC-style orientation (CPC-consistent)**  
   Uses standard PC/CPC orientation rules but applied to the *cleaned* skeleton.

The result is a **CPDAG** that more faithfully reflects causal relations even when determinism is present.

---

## When to Use

Use **Pcd** when you suspect or know that:

- Variables include **exact deterministic functions**, such as:
    - sums, differences, averages
    - ratios or percentages
    - logical or categorical encodings

- There is **near-perfect multicollinearity** (correlations ≈ ±1).

- Standard PC produces **large cliques** or **spurious adjacencies** around deterministic chains.

- You want a **PC-like method** that is robust to faithfulness violations induced by determinism.

---

## Prior Knowledge Support

Pcd fully supports Tetrad background knowledge:

- **Required edges**
- **Forbidden edges**
- **Tier/temporal constraints**

All knowledge is respected during both adjacency search and orientation.

---

## Strengths

- **Robust to determinism**  
  Handles exact or near-exact functional dependencies.

- **Cleaner skeletons**  
  Removes artificial cliques introduced by deterministic relations.

- **PC-compatible**  
  Same interface, same parameters, and same interpretation as PC/CPC.

- **Works with all CI tests**  
  Fisher Z, G-test, KCI/RCIT, basis-function tests, etc.

---

## Limitations

- **Does not model latent confounders**  
  (use FCI, RFCI, GFCI, FCIT, etc. for that)

- **Determinism must be detectable**  
  Very subtle determinism can still cause issues.

- **Still a constraint-based method**  
  Thus inherits finite-sample CI-test sensitivity from PC/CPC.

---

## Key Parameters in Tetrad

| Parameter (camelCase)          | Description |
|--------------------------------|-------------|
| `stableFas`                    | Use order-independent adjacency search. |
| `colliderOrientationStyle`     | PC, PC-Max, or CPC-style collider detection. |
| `depth`                        | Maximum conditioning-set size. |
| `fdrQ`                         | Optional FDR control (replaces α). |
| `verbose`                      | Print detailed CI-test and orientation logs. |

---

## Summary

Pcd is a **determinism-aware variant of PC** that prevents faithfulness violations from creating spurious edges. It yields cleaner, more interpretable CPDAGs when datasets include exact or near-exact functional relationships, while retaining the familiar behavior of PC/CPC.