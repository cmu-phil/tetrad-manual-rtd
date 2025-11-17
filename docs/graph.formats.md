# Graph Types and Formats

Tetrad works with several types of causal graphs and provides multiple ways to
save and load them. This page explains:

- What the main graph types mean (DAG, CPDAG, MAG, PAG)
- How Tetrad represents and exports them
- How to interpret **PAG edge-specialization markings**

The goal is to clarify **what a graph is telling you** and how it is serialized
when you save or share it.

```{contents}
:local:
:depth: 2
```

---

## 1. Core Graph Types in Tetrad

Tetrad’s search algorithms output four main graph types:

- **DAG** – Directed Acyclic Graph
- **CPDAG** – Completed Partially Directed Acyclic Graph
- **MAG** – Maximal Ancestral Graph
- **PAG** – Partial Ancestral Graph

Each type expresses different assumptions about ancestors, descendants, hidden
variables, and selection.

---

### 1.1 DAG — Directed Acyclic Graph

A **DAG** contains only directed edges and **no directed cycles**.

- `X → Y` means *X is (possibly indirectly) a cause of Y*.
- No bidirected edges, no undirected edges, no circle endpoints.
- A DAG represents **one specific causal model**, not an equivalence class.

Most Tetrad algorithms output **equivalence classes**, but some (e.g.,
LiNGAM, DAGMA) output actual DAGs.

DAGs are often used as inputs as well; you can create them by editing a Graph Box
or loading them from a file.

---

### 1.2 CPDAG — Completed Partially Directed Acyclic Graph

A **CPDAG** represents a **Markov equivalence class of DAGs** that share the same
conditional independence structure.

- `X → Y` — the orientation is **invariant** across all DAGs in the class
- `X — Y` — orientation is **ambiguous**, meaning it could be `X → Y` or `X ← Y`
- No circle endpoints (`o`)

Common CPDAG outputs include:

- PC, PC-Max
- FGES, BOSS
- Several score-based hybrids

---

### 1.3 MAG — Maximal Ancestral Graph

A **MAG** encodes causal structure with **latent confounding** and possibly
**selection bias**.  
Edges may be:

- `X → Y` — directed
- `X ↔ Y` — bidirected (latent confounder)
- `X — Y` — undirected (selection structure)

A MAG represents **one fully specified causal structure** involving latent and/or
selection variables.

---

### 1.4 PAG — Partial Ancestral Graph

A **PAG** represents an **equivalence class of MAGs** consistent with the observed
data.

The edge endpoints can be:

- **Tail**: `-`
- **Arrowhead**: `>`
- **Circle**: `o` (undetermined endpoint)

Examples:

- `X → Y` (tail–arrowhead)
- `X o→ Y` (circle–arrowhead)
- `X o–o Y` (circle–circle)
- `X ↔ Y` (arrowhead–arrowhead)
- `X — Y` (tail–tail; selection structure)

PAGs are produced by:

- FCI
- RFCI
- GFCI
- BOSS-FCI
- FCIT (targeted-testing hybrid)

---

## 2. Endpoint Marking System

Tetrad uses the following endpoint symbols:

| Endpoint | Meaning |
|----------|---------|
| `-` (tail) | This endpoint **could** be an ancestor |
| `>` (arrowhead) | This endpoint is **not** an ancestor |
| `o` (circle) | Uncertain: could be tail or arrowhead in some MAGs |

These markings summarize what is invariant across the entire equivalence class.

---

## 3. PAG Edge-Specialization Markup (Optional GUI Feature)

When edge-specialization markup is enabled in the GUI, **directed edges in a PAG**
may carry additional visual cues to indicate two independent properties:
**visibility** and **directness**.

### 3.1 Two Independent Attributes

PAG directed edges may vary along two independent dimensions:

---

### **(A) Visibility**

“Visibility” is a technical notion introduced by **Jiji Zhang (2008)** in his paper  
*“On the Completeness of Orientation Rules for Causal Discovery in the Presence of Latent Confounding.”*

Visibility describes whether a directed edge **must** represent a *direct causal influence*
that is **not explainable by a latent confounder** in any compatible MAG.

- **Solid arrow**: *Visible edge*
    - Cannot be explained away by a latent confounder
    - Corresponds to an identifiable causal effect in linear SEMs

- **Dashed arrow**: *Possibly invisible*
    - A latent confounder may exist
    - The direct effect may be non-identifiable

Visibility is a core component of the FCI family of algorithms.

---

### **(B) Directness**

This describes whether the directed edge is guaranteed to be **direct** (parent → child)
in all MAGs represented by the PAG.

- **Thick arrow**: *Definitely direct*
    - Must be a direct parent in every compatible MAG

- **Thin arrow**: *Possibly indirect*
    - Some MAGs may contain intermediate variables along the causal chain

Directness is independent of visibility.

---

### 3.2 The Four Directed-Edge Types

Because visibility and directness are orthogonal, a PAG directed edge may appear in
one of four stylized forms:

| Visibility | Directness | Appearance | Meaning |
|-----------|------------|------------|---------|
| **Solid** | **Thick** | solid + thick | Visible **and** definitely direct |
| **Solid** | Thin | solid + thin | Visible but possibly indirect |
| **Dashed** | Thick | dashed + thick | Possibly confounded but definitely direct |
| **Dashed** | Thin | dashed + thin | Possibly confounded **and** possibly indirect |

This visualization does **not** change the semantics of the PAG—it only makes explicit
certain implications of the orientation rules.

---

### 3.3 Undirected Edges Represent **Selection Bias**

In a PAG, an undirected edge:

    X — Y    (tail–tail)

represents a **selection effect**, which arises when conditioning on some variable(s)
during data collection or post-processing.

A common conceptual form is:

    X → S ← Y    where S is a (possibly latent) selection variable.

Conditioning on a selection variable induces an association between X and Y
that is **non-causal** and **cannot be removed** by adjusting for measured variables.

In the Tetrad Graph Box, *any* node may be designated as a **selection variable**,
and this affects orientation rules and reachability computations in FCI-style methods.

---

## 4. Saving and Loading Graphs

Tetrad supports several graph interchange mechanisms:

- Plain-text export formats
- JSON-based graph formats (GUI + programmatic)
- Session files containing graphs, data, and parameters
- Programmatic construction from Java, Py-Tetrad, or RPy-Tetrad

### 4.1 Conceptual Plain-Text Format

A minimal conceptual export looks like:

    # Nodes
    X, Y, (Z)

    # Edges
    1. X --> Y
    2. Y o-> Z
    3. X <-> Z

Where:

- Nodes in parentheses, e.g., `(Z)`, are **latent**.
- Edge numbering is optional, used for clarity.
- Commas or semicolons may be used to separate node names.

This is meant to be human-readable and easy to exchange.

---

## 5. Graphs and Data: Name Matching

Graphs refer to variables **by name**, so:

- Node names must match dataset column names exactly.
- Renaming a variable in the data requires renaming the node accordingly.

To avoid issues:

- Avoid spaces
- Avoid unusual punctuation
- Ensure all names are unique

---

## 6. Summary

- **DAG**: Directed, acyclic, no latents.
- **CPDAG**: Equivalence class of DAGs (no circles).
- **MAG**: Allows latent confounding & selection; fully oriented.
- **PAG**: Equivalence class of MAGs; uses tails, circles, and arrowheads.
- **PAG Markup**:
    - Solid/dashed = visible vs. possibly confounded
    - Thick/thin = direct vs. possibly indirect

These concepts provide the foundation needed to interpret and exchange causal graphs
across Tetrad’s GUI and its Python/R/Java interfaces.