# Causal Analysis Workflows

This section of the Tetrad Manual walks you through **practical workflows** for causal discovery and causal modeling.  
Instead of treating causal discovery as a single “run this algorithm and print the answer” operation, these pages guide you through a **reasoned, iterative process** that combines data exploration, assumption setting, systematic search, and model evaluation.

Causal analysis is a *scientific workflow*, not a black box — and this section helps you work like a scientist.

---

## 🧭 What You’ll Learn

This section introduces you to:

1. **Exploring your data** to form sensible assumptions about relationships.
2. **Choosing causal discovery methods** based on what the data suggest.
3. **Using Tetrad’s search tools** (including Grid Search) in a systematic way.
4. **Evaluating candidate models** using diagnostics like the Markov Checker.
5. **Iterating and refining** your assumptions, searches, and conclusions.
6. **Interpreting results responsibly** — including when only partial conclusions are warranted.

---

## 📌 Why Workflows Matter

Causal discovery is underdetermined — many models can fit the same data.  
Rather than hiding this complexity, Tetrad helps you:

- **Look first at your data**, so assumptions are grounded in evidence.
- **Articulate assumptions explicitly** (e.g., latent confounders, functional form).
- **Use tools to eliminate bad models** rather than just produce one.
- **Compare and validate** models across choices of method, parameters, and constraints.
- **Report results with clarity**, distinguishing robust features from tentative ones.

This workflow approach helps you produce results that are easier to defend and interpret.

---

## 🗺️ Navigate the Workflow

The causal analysis workflow is organized into the following pages:

- **[Data Exploration](data-exploration.md)** — how to examine your dataset and form initial assumptions.
- **[Algorithm Selection and Assumptions](choose-an-algorithm.md)** — a decision guide for choosing methods based on data and goals.
- **[Running Searches and Grid Search Tips](grid-search.md)** — how to explore algorithms and parameterizations systematically.
- **[Model Evaluation and Markov Checking](markov-checking.md)** — how to assess whether candidate graphs are consistent with data.
- **[Interpreting Results](interpretation.md)** — how to read and report causal outputs responsibly.
- **Case Studies** — worked examples that walk through the full process from data to interpretation.

> Each page builds on the previous ones, but this is not strictly linear — workflows often involve revisiting earlier steps as you refine assumptions and explore alternatives.

---

## 🧠 Tips Before You Begin

- Treat assumptions as *hypotheses to be tested*.
- Use visual inspection as a first step, not just automated tests.
- Aim for *minimal models that pass diagnostics*, not just “the first output you get.”
- Document your exploration and decisions — it helps both interpretation and reproducibility.

---

## 🙌 Next Step

Start with **[Data Exploration](data-exploration.md)** to ground your assumptions in your dataset before choosing methods.