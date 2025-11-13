# Reference

The **Reference** section collects all of Tetrad’s low-level, technical specifications  
used throughout the software: parameter definitions, core naming conventions, and
machine-readable configuration assets.

At present, the primary reference resource is the **Parameter Definitions**.

---

## 🔧 Parameter Definitions

Tetrad exposes a large number of configurable parameters used by:

- search algorithms
- scoring functions
- conditional independence tests
- simulation tools

These parameters control every part of Tetrad’s behavior — from maximum depth in PC/FCI,  
to BIC penalties in FGES, to threading, to nonlinear tolerance thresholds.

To support both **machines** and **humans**, the definitions exist in two synchronized forms:

---

### 📄 Machine-Readable Specification (used by the GUI)

👉 [`parameter.definitions.txt`](./_static/manual/parameter.definitions.txt)

This file is parsed directly by:

- the Tetrad GUI
- the Java backend
- Py-Tetrad and RPy-Tetrad wrappers
- algorithm comparison and scripting tools

It contains the authoritative definitions exactly as consumed by the interface.

---

### 📘 Human-Readable Markdown

👉 [`parameter.definitions.md`](./parameter.definitions.md)

This Markdown version provides a clean, readable table of all parameters, including:

- **parameter name**
- **short description**
- **long description**
- **value type** (Boolean / Integer / Double / Enum / String)
- **default value**
- **minimum and maximum values** (for numeric types)

This file is **auto-generated** from the machine-readable source to ensure consistency.

---

## 🔄 Keeping Definitions in Sync

The Markdown file is regenerated whenever the machine-readable file changes, ensuring:

- no drift between documentation and code
- predictable parameter behavior across UI, Java API, Py-Tetrad, and RPy-Tetrad
- reproducible algorithm settings

---

## 📌 Coming Soon

As the documentation evolves, the **Reference** section will eventually include:

- Naming conventions for graphs, edges, and orientations
- CI test and score references
- Simulation model specifications
- Tetrad file formats (`.tetrad`, `.ses`, `.json`, etc.)

For now, the parameter definitions form the core of the structured reference.

If there’s a reference table or glossary you’d like to add, just ask!