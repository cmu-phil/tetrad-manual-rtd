# Causal Analysis Workflows

This section of the Tetrad Manual walks you through **practical workflows** for causal discovery and causal modeling.

Rather than treating causal discovery as a single “run this algorithm and print the answer” operation, these pages guide you through a **reasoned, iterative process** that combines data exploration, explicit assumptions, systematic search, and model evaluation.

In Tetrad, causal analysis is a *scientific workflow*, not a black box — and this section is designed to help you work like a scientist.

---

## 🧭 What You’ll Learn

This section introduces you to how causal analysis is typically carried out in Tetrad, including how to:

1. **Explore your data** to form sensible assumptions about relationships.
2. **Decide what kinds of causal models are appropriate** for your data.
3. **Use Grid Search as a systematic search tool** to explore algorithms, tests, scores, and parameters.
4. **Compare candidate models** rather than committing prematurely to a single result.
5. **Evaluate models using diagnostics**, including Markov checking.
6. **Iterate and refine** assumptions, searches, and conclusions as evidence accumulates.
7. **Interpret results responsibly**, including cases where conclusions are necessarily partial.

---

## 📌 Why a Workflow Matters

Causal discovery is fundamentally underdetermined: many different causal models may be compatible with the same data.

Rather than hiding this complexity, Tetrad is designed to help you **manage it explicitly**. A workflow-oriented approach allows you to:

- **Start from the data**, grounding assumptions in observable structure.
- **State assumptions clearly**, such as the presence of latent variables or functional form.
- **Systematically compare alternatives**, instead of relying on a single algorithm run.
- **Eliminate implausible models** using diagnostics rather than selecting a favorite.
- **Distinguish robust features** of a result from features that depend on modeling choices.

This approach produces results that are more interpretable, defensible, and reproducible.

---

## 🗺️ How the Workflow Is Organized

The causal analysis workflow in Tetrad is organized around the following pages:

- **[Data Exploration](data-exploration.md)**  
  Learn how to examine your dataset and identify features that inform modeling assumptions.

- **[Choosing Assumptions and Methods](choose-an-algorithm.md)**  
  Understand how properties of the data (e.g., discrete vs. continuous, presence of latent variables) guide methodological choices.

- **[Grid Search: Systematic Causal Discovery](grid-search.md)**  
  Learn how to use Grid Search as the *default* way to explore algorithms, tests, scores, and parameter settings in a controlled, comparable way.

- **[Model Evaluation and Markov Checking](markov-checking.md)**  
  Use diagnostic tools to assess whether candidate graphs are consistent with the data and modeling assumptions.

- **[Interpreting Results](interpretation.md)**  
  Learn how to read causal outputs carefully and report conclusions with appropriate caution.

- **Case Studies**  
  Worked examples that demonstrate the full workflow, from data exploration through interpretation.

> Although these pages are presented in a logical order, causal analysis is rarely linear. It is normal — and expected — to revisit earlier steps as new insights emerge.

---

## 🧠 Practical Advice Before You Begin

- Treat assumptions as **hypotheses to be explored**, not facts.
- Use visual and exploratory tools before running searches.
- Prefer **systematic comparison** over one-off algorithm runs.
- Look for **features that persist across models**, not just the highest-scoring output.
- Keep notes on your decisions — this improves both interpretation and reproducibility.

---

## 🙌 Where to Start

Begin with **[Data Exploration](data-exploration.md)** to understand your dataset and form initial assumptions before moving on to systematic search using Grid Search.