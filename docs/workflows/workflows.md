# Causal Analysis Workflows

This section of the Tetrad Manual introduces **practical workflows** for causal discovery and causal modeling.

Rather than treating causal discovery as a single “run an algorithm and read off an answer” step, these pages describe a **deliberate, iterative process** that combines data exploration, explicit assumptions, systematic search, and model evaluation.

In Tetrad, causal analysis is a *scientific workflow*, not a black box. This section is intended to support careful reasoning while remaining flexible to different goals and levels of experience.

---

## 🧭 What You’ll Learn

This section outlines how causal analysis is commonly carried out in Tetrad, including how to:

1. **Explore your data** to form sensible, defensible modeling assumptions.
2. **Decide which classes of causal models are appropriate** for the data at hand.
3. **Use Grid Search as a systematic exploration tool** for algorithms, tests, scores, and parameters.
4. **Compare candidate models** rather than committing to a single run.
5. **Evaluate models using diagnostics**, including Markov checking.
6. **Iterate and refine** assumptions and searches as evidence accumulates.
7. **Interpret results carefully**, including cases where conclusions remain limited or partial.

---

## 📌 Why a Workflow Matters

Causal discovery is inherently underdetermined: many different causal models may be compatible with the same data.

Rather than hiding this uncertainty, Tetrad is designed to help you **work with it explicitly**. A workflow-oriented approach allows you to:

- **Begin with the data**, grounding assumptions in observable structure.
- **State assumptions clearly**, such as causal sufficiency or functional form.
- **Compare alternatives systematically**, instead of relying on a single algorithm run.
- **Rule out implausible models** using diagnostics rather than preference.
- **Identify robust features** that persist across reasonable modeling choices.

This approach tends to produce results that are more interpretable, defensible, and reproducible.

---

## 🗺️ How the Workflow Is Organized

The causal analysis workflow in Tetrad is organized around the following pages:

- **[Data Exploration](data-exploration.md)**  
  Inspect datasets and identify features that inform modeling assumptions.

- **[Choosing Assumptions and Methods](choose-an-algorithm.md)**  
  See how data properties (e.g., variable types, potential latent variables) guide methodological choices.

- **[Grid Search: Systematic Causal Discovery](grid-search.md)**  
  Learn how Grid Search supports controlled, comparable exploration of algorithms and parameters.

- **[Model Evaluation and Markov Checking](markov-checking.md)**  
  Use diagnostic tools to assess whether candidate graphs are consistent with the data.

- **[Interpreting Results](interpretation.md)**  
  Learn how to read causal outputs carefully and communicate conclusions with appropriate caution.

- **Case Studies**  
  Worked examples demonstrating the full workflow, from data exploration through interpretation.

> Although these pages are presented in a logical order, causal analysis is rarely linear. Revisiting earlier steps as new insights emerge is both normal and expected.

---

## 🧠 Practical Advice Before You Begin

- Treat assumptions as **working hypotheses**, not fixed truths.
- Use visual and exploratory tools early.
- Prefer **systematic comparison** over one-off runs.
- Focus on **features that persist across models**, not just the highest-scoring output.
- Keep notes on decisions and revisions; this improves interpretation and reproducibility.

---

## 🙌 Where to Start

Begin with **[Data Exploration](data-exploration.md)** to understand your dataset and form initial assumptions before moving on to systematic search using Grid Search.
