# Tetrad Manual

Welcome to the official documentation for **Tetrad**, the open-source platform for causal discovery, causal inference, simulation, and graph-based statistical reasoning developed at Carnegie Mellon University.

---

### 📘 RTD Documentation In Progress

This **Read the Docs** version of the Tetrad manual is currently **under active development**.  
Many sections are newly rewritten, while others temporarily link to the classic HTML manual.  
Content will continue to be migrated, expanded, and reorganized.

If you encounter issues or would like to request a section, please file an issue:

👉 https://github.com/cmu-phil/tetrad/issues

---

Tetrad provides:

- A **graphical user interface (GUI)** for interactive causal modeling
- A comprehensive **Java library** with search algorithms, scores, and independence tests
- **Python and R bindings** (Py-Tetrad and RPy-Tetrad)
- A flexible architecture for extending algorithms, adding custom tests, and integrating new workflows

This site is the **Read the Docs** version of the Tetrad manual, reorganized into small, navigable sections for ease of use.

```{toctree}
:maxdepth: 2
:hidden:

quickstart
user-guide
search-algorithms
reference
changelog
```

---

## 🚀 What is Tetrad?

Tetrad is a suite of tools for:

- Discovering causal structure from observational or experimental data
- Estimating causal effects
- Simulating data from DAGs, MAGs, and SEMs
- Working with DAGs, CPDAGs, MAGs, PAGs, and other causal graph types
- Performing score-based, constraint-based, and hybrid causal search

The system has been under active development for nearly 30 years and includes many of the most widely used and theoretically grounded causal discovery methods.

---

## 🧭 Start Here — Core User Workflows

Most users interact with Tetrad through a simple pipeline:

### 1. **Load or simulate data**
- Continuous, discrete, or mixed datasets
- SEM-based generators
- Nonlinear and non-Gaussian options
- Resampling and bootstrapping tools

### 2. **Specify prior knowledge (optional)**
- Required or forbidden edges
- Tier/background knowledge
- Selection variables

### 3. **Run a causal search algorithm**
Choose among:
- **Constraint-based** (PC, FCI, PC-Max, RFCI…)
- **Score-based** (FGES, BOSS, GRaSP…)
- **Hybrid** (GFCI, BOSS-FCI, FCIT…)
- **Specialized** (LiNGAM, CAM, NOTEARS, LASSO variants, ANM models)

### 4. **Inspect and modify the resulting graph**
- Orient edges
- Add/remove adjacencies
- Run legality checks
- Compare graphs side-by-side

### 5. **Estimate causal effects**
- Adjustment sets
- IDA-style estimation (including PAG IDA)
- Efficiency-oriented and path-specific tools

Each of these steps is documented in the sections linked below.

---

## 📚 Manual Sections

### **Quickstart**
A short “get going in 5 minutes” guide showing how to load data, run your first search, and interpret results.  
➡️ [Open quickstart](quickstart)

### **User Guide**
A structured walkthrough of the Tetrad interface:
- Data box
- Knowledge box
- Search box
- Graph box
- Simulation tools
- Effect estimation  
  ➡️ [Open user guide](user-guide)

### **Algorithms**
Detailed descriptions of every algorithm shipped with Tetrad, including:
- When to use it
- What assumptions it makes
- What types of graphs it returns  
  ➡️ [Open algorithms page](search-algorithms)

### **Parameter Reference**
Machine-readable and human-readable parameter definitions for all search, score, test, and simulation components.  
➡️ [Open reference](reference)

### **Changelog**
A history of changes across Tetrad versions and UI updates.  
➡️ [Open changelog](changelog)

---

## 🔧 Using Tetrad from Python or R

Tetrad can be used outside the GUI via:

- **Py-Tetrad** (Python): `pip install py-tetrad`
- **RPy-Tetrad** (R): R interface via `reticulate`

Links to language-specific docs will be added in future revisions.

---

## 🙋 Need help?

The Tetrad GitHub repository hosts issue tracking, discussions, and development notes:

👉 https://github.com/cmu-phil/tetrad