# Graph Types and Formats

Tetrad works with several types of causal graphs and provides multiple ways to
save and load them. This page explains:

- what the main graph types mean (DAG, CPDAG, MAG, PAG), and
- how Tetrad represents and exports them.

The goal is to clarify **what a graph is telling you** and **how it is serialized**
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

Each type encodes different assumptions about hidden variables and selection.

---

### 1.1 DAG — Directed Acyclic Graph

A **DAG** is a graph with only directed edges and **no directed cycles**.

- Edge `X → Y` means “X is a (possibly indirect) cause of Y” in the model.
- No bidirected edges, no undirected edges, no circles on endpoints.
- Represents **one specific causal model**, not an equivalence class.

In Tetrad:

- Many algorithms (e.g., FGES, BOSS, some simulation tools) operate over DAGs.
- You may also draw DAGs manually in the GUI and simulate data from them.

---

### 1.2 CPDAG — Completed Partially Directed Acyclic Graph

A **CPDAG** encodes a **Markov equivalence class** of DAGs.

- Some edges are directed (`X → Y`).
- Some edges are undirected (`X — Y`).
- All DAGs in the class share the same adjacencies and unshielded colliders.

Interpretation:

- `X → Y` – the arrowhead is **invariant** across all DAGs in the class  
  (Y is always a non-ancestor of X).
- `X — Y` – the orientation is **ambiguous**; some DAGs have `X → Y`, others `X ← Y`.

In Tetrad:

- Algorithms like **PC**, **PC-Max**, and **FGES** typically output CPDAGs.
- The CPDAG captures what the data supports **up to Markov equivalence**.

---

### 1.3 MAG — Maximal Ancestral Graph

A **MAG** represents causal structure in the presence of **latent confounders** and
possibly **selection bias**, but with fully specified endpoint marks.

Edges may include:

- `X → Y` – directed edge (X is a cause of Y, no arrowhead at X).
- `X ↔ Y` – bidirected edge (arrowheads at both ends), often indicating
  **latent confounding** between X and Y.
- `X — Y` – undirected edge, often associated with **selection effects**.

Key properties:

- No directed cycles.
- No “almost directed” cycles (paths that are directed except for one bidirected edge).
- “Maximal”: every independence encoded in the graph corresponds to a missing edge.

In Tetrad:

- MAGs are mostly **conceptual targets** for algorithms that output PAGs.
- Certain internal transformations and theory refer to MAG structure explicitly.

---

### 1.4 PAG — Partial Ancestral Graph

A **PAG** encodes an **equivalence class of MAGs**.

- PAGs use three endpoint marks:

    - **Tail**: `-`
    - **Arrowhead**: `>`
    - **Circle**: `o`

- Edges can combine these marks:

    - `X — Y` (tail–tail)
    - `X → Y` (tail–arrowhead)
    - `X o→ Y` (circle–arrowhead)
    - `X ↔ Y` (arrowhead–arrowhead)
    - `X o–o Y` (circle–circle)

Each combination expresses what is **definitely known** versus **still ambiguous**
across all MAGs in the equivalence class.

Typical interpretations:

- `X → Y` – Y is **not** an ancestor of X in any MAG in the class.
- `X ↔ Y` – there is a **latent confounder** between X and Y in all MAGs.
- `X — Y` – selection-related constraints (e.g., conditioning on colliders/selection variables).
- `X o→ Y`, `X o–o Y` – **some endpoints are not yet oriented**; the circle marks
  mean “this endpoint could be a tail or an arrowhead in some MAGs.”

In Tetrad:

- Algorithms like **FCI**, **RFCI**, **GFCI**, **BOSS-FCI**, and **FCIT** output PAGs.
- PAGs are central when there may be **unmeasured confounding** or **selection bias**.
- The GUI draws circle marks explicitly on endpoints to distinguish `o→`, `o–o`, etc.

---

## 2. Edge Endpoint Notation in Tetrad

Tetrad uses a consistent set of symbols at edge endpoints:

- **Tail (`-`)**
- **Arrowhead (`>`)**
- **Circle (`o`)**

Conceptually:

| Endpoint | Meaning (informal) |
|---------|---------------------|
| `-`     | “Could be an ancestor; no arrowhead here.” |
| `>`     | “Not an ancestor; arrowhead points *toward* this node.” |
| `o`     | “Endpoint type not fully determined (could be `-` or `>` in some MAGs).” |

Examples:

- **DAG/CPDAG**: often just `→` and `—`
- **MAG/PAG**: combinations like `o→`, `↔`, `—`, `o–o`

---

## 3. How Graphs Are Saved and Loaded

Tetrad interacts with graphs through:

- The **GUI** (Save Graph / Load Graph)
- **Session/project files** (saving everything at once)
- **Programmatic APIs** (Java, Py-Tetrad, RPy-Tetrad)
- **Plain-text graph formats** for exchange

This section focuses on **standalone graph formats** rather than full project/session
files.

> **Note:** The exact set of export/import formats may evolve; this page describes
> the general structure and semantics rather than committing to a specific file
> extension or menu label.

---

### 3.1 Plain Text Graph Format (Conceptual)

A typical Tetrad-style plain text graph export consists of:

- A list of **nodes**
- A list of **edges**, where each edge uses the endpoint symbols described above

A simple conceptual example:

```text
# Nodes
X, Y, Z

# Edges
X --> Y
Y o-> Z
X <-> Z
```

Here:

- `X --> Y` – tail at X, arrowhead at Y
- `Y o-> Z` – circle at Y, arrowhead at Z (PAG-style uncertain endpoint)
- `X <-> Z` – arrowheads at both ends, representing latent confounding

Different tools (GUI, Py-Tetrad, RPy-Tetrad) may provide different wrappers or
file extensions around this same underlying representation.

---

### 3.2 Session Files and Embedded Graphs

Tetrad’s GUI project/session files:

- Store **graphs, datasets, knowledge, and parameters together**
- Include graph structure in an internal format (often JSON or a similar structured form)
- Are intended for **re-opening complete projects**, not just exchanging graphs

For graph-only transfer between tools, tabular datasets + explicit graph exports
are often more convenient.

---

### 3.3 Programmatic Graph Objects

From Java or Py-Tetrad:

- Graphs are represented by classes like `Graph`, `Edge`, and specialized graph types.
- These objects can be:
    - Constructed from text formats,
    - Exported to text or JSON,
    - Converted between graph types (e.g., DAG → CPDAG → PAG).

The exact APIs are documented in the Java/Python-specific documentation; here we
focus on the **conceptual meaning** and **file-level shape** of graphs.

---

## 4. Interpreting Graphs Correctly

When looking at a graph in Tetrad:

1. **Check the graph type** (DAG, CPDAG, MAG, PAG).
    - This determines what the endpoint marks *mean*.

2. **Pay attention to endpoints**:
    - Arrowheads (`>`) indicate non-ancestors.
    - Tails (`-`) allow ancestry at that endpoint.
    - Circles (`o`) mark uncertainty.

3. **Remember the scope of the claim**:
    - DAG: claims about a **single** causal structure.
    - CPDAG: claims about all DAGs in a **Markov equivalence class**.
    - MAG: claims about a **single** latent-variable model.
    - PAG: claims that hold across an **equivalence class of MAGs**.

---

## 5. Graphs and Data: Name Matching

Graphs and datasets are linked via **variable names**:

- The node names in a graph must match the **column names** in the data.
- Renaming variables in the data without renaming nodes in the graph
  will usually break the connection.

Best practice:

- Decide on a naming convention (no spaces, no strange symbols).
- Keep names consistent across data files, graph exports, and prior knowledge.

---

## 6. Summary

- **DAGs**: directed, acyclic; no latent confounding in the representation.
- **CPDAGs**: represent equivalence classes of DAGs; mix of `→` and `—`.
- **MAGs**: allow latent confounders and selection; fully specified endpoints.
- **PAGs**: represent equivalence classes of MAGs; use `-`, `>`, and `o` endpoints.