# PcMb — PC Markov Blanket Search

**Type:** Constraint-based (local)  
**Output:** CPDAG (local to a target variable)

PcMb is a **local variant of PC/CPC** designed to recover the **Markov blanket of a single target variable** rather than the entire graph.  
Given a target T, PcMb uses conditional independence tests to construct a **local CPDAG** whose structure encodes **all Markov blankets of T** that are compatible with the CI information.

---

## Key Idea

PcMb applies PC-style conditional independence reasoning but **restricted to the target T**.

A Markov blanket of T is any set of variables that renders T independent of all others when conditioned on.  
PcMb identifies:

- which variables remain adjacent to T after CI pruning, and
- which orientations around T are required or possible.

The resulting **local CPDAG** describes the entire family of Markov blankets consistent with the CI information.

---

## When to Use

Use PcMb when:

- You care about a **single target variable** (e.g., an outcome or label).
- You want a **constraint-based Markov blanket** without learning the full graph.
- The number of variables is large and a full CPDAG or PAG is too expensive.
- You want **all possible Markov blankets**, not one heuristic choice.

PcMb is especially helpful for:

- **Feature selection** or classification
- **High-dimensional** settings
- Comparing constraint-based and score-based MB learners (PcMb vs FgesMb)

---

## Prior Knowledge Support

PcMb respects all Tetrad background knowledge:

- **Required edges**
- **Forbidden edges**
- **Tier / temporal constraints**

All knowledge is enforced during adjacency pruning and orientation.

---

## Strengths

- Efficient when focusing on **one target**
- Returns **all** possible Markov blankets (via the local CPDAG)
- Conservative collider handling (CPC-style) reduces false positive orientations
- Fully compatible with Tetrad knowledge constraints
- Uses standard CI tests (Fisher Z, G-test, KCI, RCIT, BF tests, etc.)

---

## Limitations

- Can still be CI-test intensive when T has many neighbors
- Sensitive to finite-sample CI errors (as with PC/CPC)
- Must be run separately for each target if many MBs are desired
- Does not produce a full-graph CPDAG or MAG/PAG

---

## Key Parameters in Tetrad

All parameters appear in the GUI (camelCase form) and scripting interfaces.

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `target`               | The distinguished variable T. |
| `independenceTest`    | CI test used (Fisher Z, G-test, KCI, RCIT, basis-function tests, etc.). |
| `significanceLevel`   | Alpha level for CI tests. |
| `depth`               | Maximum conditioning-set size. |
| `colliderOrientationStyle` | PC, PC-Max, or CPC-style collider logic. |
| `stableFas`           | Use order-independent adjacency search. |
| `verbose`             | Print detailed logs. |

---

## Reference

Bai, X., Padman, R., Ramsey, J., & Spirtes, P. (2008).  
*Tabu search-enhanced graphical models for classification in high dimensions.*  
INFORMS Journal on Computing, 20(3), 423–437.

---

## Summary

PcMb is a **local PC/CPC-style Markov blanket learner** for a single target T.  
It builds a **local CPDAG** encoding all Markov blankets of T consistent with the observed CI structure and any supplied background knowledge.