# Tetrad Manual

Welcome to the official documentation for **Tetrad**, the open-source platform for causal discovery, causal inference, simulation, and graph-based statistical reasoning developed at Carnegie Mellon University.

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
graph.formats
data.formats
search-algorithms-short-list
search-algorithms-full-list
parameter.definitions
about
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
- Multinomial, SEM, and general function-based generators
- Nonlinear and non-Gaussian options
- Resampling and bootstrapping tools

### 2. **Specify prior knowledge (optional)**
- Required or forbidden edges
- Tiered/temporal background knowledge
- Selection variables

### 3. **Run a causal search algorithm**
Choose among:
- **Constraint-based** (PC (with Map-P option), FCI, RFCI…)
- **Score-based** (FGES, BOSS, GRaSP…)
- **Hybrid** (GFCI, BOSS-FCI, FCIT…)
- **Specialized** (LiNGAM, CAM, NOTEARS, ANM models…)
- **Latent Structure Search** (Causal clustering, PC over clusters, Gin…)

### 4. **Inspect and modify the resulting graph**
- Orient edges
- Add/remove adjacencies
- Run legality checks
- Get graph comparisons statistics

### 5. **Estimate causal effects**
- Adjustment sets
- IDA-style estimation, Optimal IDA
- Path calculations and comparison tools

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
  ➡️ [Open algorithms page](search-algorithms-short-list)

### **Parameter Reference**
Parameter definitions for all search, score, test, and simulation components.  
➡️ [Open reference](reference)

### **Changelog**
A history of changes across Tetrad versions and UI updates.  
➡️ [Open changelog](changelog)

---

## 🔧 Using Tetrad Programmatically

Tetrad can also be used outside the GUI through its programmatic interfaces (Java, Python, and R). Rather than duplicating links here, we refer you to the **official Tetrad website**, which always contains up-to-date links to:

- Java Javadocs
- Py-Tetrad (Python interface)
- RPy-Tetrad (R interface)
- Tutorials and example scripts
- Download pages

See:  
👉 [https://www.cmu.edu/dietrich/philosophy/tetrad/index.html](https://www.cmu.edu/dietrich/philosophy/tetrad/index.html)

### Related Python Ecosystem Tools

The Python ecosystem also includes **causal-learn**, a well-supported project that implements several Tetrad-style algorithms natively in Python, together with additional methods and utilities tailored to the Python community:

👉 [https://causal-learn.readthedocs.io/en/latest/](https://causal-learn.readthedocs.io/en/latest/)

Tetrad and causal-learn share common theoretical foundations and can be used side-by-side depending on your workflow, programming environment, and performance needs.

---

## 🙋 Need help?

The Tetrad GitHub repository hosts issue tracking, discussions, and development notes:

👉 [https://github.com/cmu-phil/tetrad](https://github.com/cmu-phil/tetrad)