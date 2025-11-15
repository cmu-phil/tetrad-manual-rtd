# Graph Types and Formats

Tetrad works with several types of causal graphs and provides multiple ways to
save and load them. This page explains:

- what the main graph types mean (DAG, CPDAG, MAG, PAG), and
- how Tetrad represents and exports them
- (NEW) how to interpret **PAG edge-specialization markings**

The goal is to clarify **what a graph is telling you** and how it is serialized
when you save or share it.

```{contents}
:local:
:depth: 2
```

---

## 1. Core Graph Types in Tetrad

Tetrad’s search algorithms output four main kinds of graphs:

- **DAG** – Directed Acyclic Graph
- **CPDAG** – Completed Partially Directed Acyclic Graph
- **MAG** – Maximal Ancestral Graph
- **PAG** – Partial Ancestral Graph

Each type makes different claims about ancestors, descendants, hidden variables, and
selection.

---

### 1.1 DAG — Directed Acyclic Graph

A **DAG** is a graph with only directed edges and **no directed cycles**.

- `X → Y` means *X is (possibly indirectly) a cause of Y*.
- No bidirected edges, undirected edges, or circles.
- Represents **one specific causal model**, not an equivalence class.

Common sources in Tetrad:
- FGES, BOSS, GRaSP
- Manual graph editing
- SEM simulation tools

---

### 1.2 CPDAG — Completed Partially Directed Acyclic Graph

A **CPDAG** represents a **Markov equivalence class** of DAGs.

- `X → Y` = direction is **invariant**
- `X — Y` = direction is **ambiguous**
- No circles (`o`)

Common outputs:
- PC, PC-Max
- FGES, BOSS
- Some score-based hybrids

---

### 1.3 MAG — Maximal Ancestral Graph

A **MAG** encodes structure with **latent confounding** and possibly **selection bias**.

Edges may be:
- `X → Y` (directed)
- `X ↔ Y` (bidirected; latent confounder)
- `X — Y` (undirected; selection structure)

A MAG represents **one fully specified causal structure** with latents/selection.

---

### 1.4 PAG — Partial Ancestral Graph

A **PAG** represents an **equivalence class of MAGs** compatible with the observed data.

Edges use endpoint marks:

- **Tail**: `-`
- **Arrowhead**: `>`
- **Circle**: `o` (undetermined endpoint)

Examples:
- `X → Y` (tail–arrowhead)
- `X o→ Y` (circle–arrowhead)
- `X o–o Y` (circle–circle)
- `X ↔ Y` (arrowhead–arrowhead)
- `X — Y` (tail–tail; selection effect)

PAGs are produced by:
- FCI
- RFCI
- GFCI
- BOSS-FCI
- FCIT (targeted-testing hybrid)

---

## 2. Endpoint Marking System

Tetrad uses these endpoint symbols:

| Endpoint | Meaning |
|----------|---------|
| `-` (tail) | This endpoint **could** be an ancestor |
| `>` (arrowhead) | This endpoint is **not** an ancestor |
| `o` (circle) | Uncertain: could be `-` or `>` in some MAGs |

---

## 3. PAG Edge Specialization Markup (Optional GUI Feature)

When PAG edge-specialization markup is enabled in the GUI, **directed edges in a PAG** may carry additional stylistic cues. These annotations make explicit what the algorithm infers about **visibility** and **directness**.

These decorations are for visualization only — they do **not** change the PAG’s semantics.

### 3.1 Two Independent Attributes

PAG directed edges may vary along **two independent dimensions**:

---

### **(A) Visibility**
This concerns **whether a latent confounder could exist** for this directed edge.

- **Solid**: *Visible*
    - No latent confounder
    - Estimable coefficient (in linear SEMs)

- **Dashed**: *Possibly invisible*
    - Latent confounding may be present
    - Coefficient may **not** be identifiable

This corresponds to the classical FCI notion of *visible* vs. *invisible* edges.

---

### **(B) Directness**

This indicates whether the edge is **definitely direct** across all MAGs, or could be part of a longer directed path.

- **Thick**: *Definitely direct*
    - Must be a direct parent in all compatible MAGs

- **Thin**: *Possibly indirect*
    - Could have intermediates in some MAGs of the equivalence class

---

### 3.2 The Four Directed-Edge Types

Since visibility and directness are independent, PAG directed edges can take one of
**four** forms:

| Visibility | Directness | Appearance | Meaning |
|-----------|------------|------------|---------|
| **Solid** | **Thick** | Solid + Thick | Visible and definitely direct |
| **Solid** | Thin | Solid + Thin | Visible but possibly indirect |
| **Dashed** | Thick | Dashed + Thick | Possibly confounded but definitely direct |
| **Dashed** | Thin | Dashed + Thin | Possibly confounded and possibly indirect |

These stylizations help interpret complex PAG output:

- solid = **no latent confounder**
- dashed = **may be latent confounder**
- thick = **direct**
- thin = **possibly indirect**

---

### 3.3 Undirected Edges Represent Selection Bias

In PAGs, the edge type:

```
X — Y    (tail–tail)
```

indicates a **selection effect** (a latent common child):

```
X → L ← Y   where L is unmeasured
```

This is *not* an adjacency in the causal graph, but a constraint induced by conditioning/selection.

---

## 4. Saving and Loading Graphs

Tetrad supports:

- Plain-text graph formats
- Graph exports embedded in session files
- JSON-based formats (GUI + programmatic)
- Programmatic construction (Java, Py-Tetrad, RPy-Tetrad)

### 4.1 Conceptual Plain-Text Format

A minimal conceptual export resembles:

```text
# Nodes
X, Y, Z

# Edges
X --> Y
Y o-> Z
X <-> Z
```

Exact formatting varies depending on GUI/CLI options, but semantics are consistent.

---

## 5. Graphs and Data: Name Matching

Graphs refer to variables by **name**, so:

- Node names must match dataset column names
- Renaming variables in the data requires renaming nodes in the graph

Avoid unusual characters or whitespace in names.

---

## 6. Summary

- **DAG**: Directed, no cycles, no latents.
- **CPDAG**: Equivalence class of DAGs.
- **MAG**: Allows latent confounders and selection; fully oriented.
- **PAG**: Equivalence class of MAGs; uses tails, arrowheads, and circles.
- **PAG Markup**: Solid/dashed (visibility) × thick/thin (directness).

This page provides the conceptual foundation needed to interpret Tetrad graphs and use them correctly across GUI, Python, R, and Java interfaces.