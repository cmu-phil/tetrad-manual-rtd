# Python and R Bindings

Tetrad includes an extensive Java implementation of causal discovery algorithms, scores, tests, data structures, and utilities.  
To make this functionality easier to use from other programming environments, we provide **official Python and R bindings** that directly interface with the Java core.

These bindings allow researchers to access the *full power of the Java Tetrad engine* while working in Python or R.

---

## py-tetrad (Python Binding)

**Repository:**  
👉 [https://github.com/cmu-phil/py-tetrad](https://github.com/cmu-phil/py-tetrad)

`py-tetrad` is the **official Python interface** to the Tetrad Java codebase. It exposes:

- Full access to Tetrad causal discovery algorithms (PC, FCI, GFCI, BOSS, GRaSP, etc.)
- Scores, independence tests, and utilities
- Graph objects and graph manipulation APIs
- Dense and sparse matrix tools
- Simulation modules
- Seamless conversion between Python data structures (NumPy arrays, pandas DataFrames) and Tetrad `DataSet`s

`py-tetrad` is ideal when you want to:

- Use **Tetrad’s Java algorithms from Python**
- Access algorithms **not included** in native-Python packages
- Ensure **feature parity** with Tetrad GUI / Java library
- Run algorithms at **Java-level performance**, especially for large datasets

---

## rpy-tetrad (R Binding)

**Repository:**  
👉 [https://github.com/cmu-phil/py-tetrad/tree/main/pytetrad/R](https://github.com/cmu-phil/py-tetrad/tree/main/pytetrad/R)

`rpy-tetrad` provides an R interface built on the py-tetrad infrastructure. It lets R users:

- Call Tetrad Java search algorithms directly from R
- Pass R data frames into the Java Tetrad backend
- Retrieve graphs, adjustment sets, statistics, and scores into R
- Script large-scale analyses using familiar R workflows

`rpy-tetrad` is recommended if you:

- Work primarily in R but want **direct access to Tetrad’s Java engine**
- Need methods not implemented in R packages such as `pcalg`, `dagitty`, or `bnlearn`
- Want consistent results across GUI, Java, Python, and R contexts

---

## When to Use These Bindings

Use **py-tetrad** or **rpy-tetrad** when:

- You need **exact behavior** from Tetrad’s Java implementation  
  (e.g., FGES, FCI variants, BOSS, GRaSP, FCIT, BF-BIC, BF-LRT, O-sets, RA, etc.)
- You want algorithms or features **not implemented natively in Python or R**
- You want to call Tetrad from another language but retain:
    - Same parameters
    - Same scoring behavior
    - Same PAG/CPDAG semantics
    - Same orientation rules
    - Same simulation procedures

In short:  
**If your work depends on the Tetrad Java engine, these bindings are the intended way to access it.**

---

## Related Python Ecosystem Tools

The Python ecosystem also includes the **causal-learn** project, which implements several graph-based causal discovery algorithms natively in Python:

👉 [https://causal-learn.readthedocs.io/en/latest/](https://causal-learn.readthedocs.io/en/latest/)

### Relationship to Tetrad

- **causal-learn** provides well-maintained Python-native implementations of several Tetrad algorithms, plus additional methods and utilities not included in Tetrad.
- **py-tetrad** provides a bridge to **Tetrad’s full Java engine**, including many algorithms and features not currently implemented anywhere else in Python.

### Recommendation

- If you need **pure-Python** implementations with good ecosystem integration, causal-learn is a great choice.
- If you need **the complete Tetrad functionality** (including the newest research algorithms), use py-tetrad or rpy-tetrad.

These projects complement each other well, and many users employ both.

---