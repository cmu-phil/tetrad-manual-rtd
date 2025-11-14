# Reference

The **Reference** section collects Tetrad’s low-level, technical specifications:
parameter definitions, data formats, core naming conventions, and other machine-
readable assets used throughout the software.

This section is meant for **power users, developers, and anyone needing exact file
formats or algorithm parameters**.

## 🔧 Parameter Definitions

Tetrad exposes a large number of configurable parameters used by:

- search algorithms
- scoring functions
- conditional independence tests
- simulation tools

These parameters control nearly every part of Tetrad’s behavior — from maximum depth
in PC/FCI, to BIC penalties in FGES, to threading, to nonlinear tolerance thresholds.

---

This link gives a listing of all parameters:

👉 [`parameter.definitions.md`](./parameter.definitions.md)

For each parameter, the following information is provided:

- **parameter name**
- **short description**
- **long description**
- **value type** (Boolean / Integer / Double / Enum / String)
- **default value**
- **minimum and maximum values** (for numeric types)

---

## 📂 Data Formats

Tetrad supports data formats for tabular data (continuous, discrete, mixed) and corrleation/covariance matrices.

See this dedicated page for all details, edge cases, and examples:

👉 [`data.formats`](./data.formats)

## 🕸️ Graph Formats

Tetrad supports a variety of graph types for representing causal relationships and latent variables.

Mostly the supported theory resolves around DAGs (Directed Acyclic Graphs), CPDAGs (Completed Partially Directed Acyclic Graphs), MAGs (Mixed Ancestral Graphs), and PAGs (Partial Ancestral Graphs).

See this dedicated page for all details, with examples:

👉 [`graph.formats`](./graph.formats)

---

## 📌 Coming Soon

Future expansions to this section will cover:

- Graph and orientation naming conventions
- CI test and score catalogs
- Simulation model specifications
- All Tetrad file formats (`.tetrad`, `.ses`, `.json`, `.dot`, covariance/correlation formats)
- Legacy and interoperability formats

If there’s a reference table or glossary you’d like to add next, just let me know!