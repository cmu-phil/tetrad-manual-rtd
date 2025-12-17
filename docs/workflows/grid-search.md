# Running Searches and Grid Search Tips

Once you have explored your data and chosen a starting set of assumptions and methods (see *Algorithm Selection and Assumptions*), the next step is to **systematically run causal searches** and explore key parameters. This page introduces how to perform searches in Tetrad, basic grid search patterns, and recommended practices for evaluating models across parameter settings.

Unlike one-shot causal discovery, **systematic search exploration** helps you understand how sensitive your results are to assumptions, test/score choices, and tuning parameters. It also creates a natural path toward evaluating models via diagnostics like the Markov Checker.

---

## When to Use Grid Search

Tetrad’s **Grid Search** tool is especially helpful when:

- You want to explore **multiple parameter settings** for a given algorithm.
- You want to compare **different algorithms** under similar settings.
- You want to see how sensitive structures are to test/score choice or tuning.
- You’re aiming to find **minimal Markov-consistent models** — those that pass diagnostics with minimal complexity.

Grid Search is a flexible exploration tool — and for beginners, the challenge is knowing *which parameters to vary first* and *how to interpret the results*.

---

## Running a Basic Search

In the Tetrad UI:

1. **Open the Search dialog**
    - Choose your preferred causal discovery method (e.g., PC, FCI, GES).
2. **Select tests or scores**
    - Pick a conditional independence test or score that matches data type and assumptions.
3. **Configure parameters**
    - For test-based methods: significance level (α)
    - For score-based methods: penalty/discount
4. **Run the search**
    - Review the output graph in the **Graph** pane

After the first run, before interpreting results, ask:

- Does the output pass basic sanity checks?
- Do adjacencies make sense given known relationships?
- Are there unexpected orientations?

If not, consider running a grid search over key parameters rather than focusing on this single run.

---

## What to Sweep in Grid Search

When you start exploring with Grid Search, vary *one or two knobs at a time* to keep the analysis interpretable. Some common choices:

### 1. **Significance Level (α) — For Test-Based Methods**
- Typical values: 0.01, 0.05, 0.10
- Lower α → sparser graph
- Higher α → denser graph

Sweep across 3–5 α values to see how sparsity and conditional independence support change.

---

### 2. **Penalty / Discount — For Score-Based Methods**
- Higher penalties → favor simpler models
- Lower penalties → allow more edges

Try a range of penalties to see where the balance between fit and complexity lies.

---

### 3. **Algorithm Family**
- Run both constraint-based and score-based methods
- If you’re allowing latent variables, compare FCI variants vs score–search hybrids

This provides practical insight into how robust findings are across families of methods.

---

### 4. **Tests / Scores**
- On the test side: Fisher-Z vs rank-based vs nonparametric tests
- On the score side: BIC vs alternative scoring functions

Different tests/scores respond to data characteristics differently; sweeping them helps diagnose sensitivity.

---

## Interpreting Grid Search Results

Once your grid search runs complete, you’ll typically have a collection of models varying in sparsity and structure.

### Two Key Quantities to Focus On

1. **Markov Consistency Statistic**
    - How well does each graph’s implied conditional independences match the data?
    - Use the Markov Checker (see *Model Evaluation and Markov Checking*) to compare candidates.

2. **Model Complexity**
    - Number of edges (and degrees of freedom, when available)
    - Simpler models that still pass Markov diagnostics are often preferable.

Plotting these against each other (e.g., complexity vs Markov goodness) can reveal *trade-offs* and help you identify minimal models.

---

## A Practical Starter Pattern

For non-experts, here’s a simple pattern to begin with:

1. **Select one algorithm family** (e.g., PC or FCI)
2. **Sweep α / penalty** across a small range
3. **Evaluate each result** with:
    - Markov Checker
    - Visual inspection for glaring inconsistencies
4. **Identify minimal models** that pass diagnostics with the fewest edges
5. **Optionally compare** with a second algorithm family

Repeat with revised assumptions or background knowledge as needed.

---

## How to Read Grid Search Output

In the Grid Search results:

- Each row corresponds to a different parameter setting (or algorithm).
- You will see:
    - The estimated graph
    - Key statistics (number of edges, Markov statistics, etc.)
- Click on a result to inspect the graph.

As you compare results:

- Look for **stable adjacencies/orientations** that appear across settings.
- Treat **fragile edges** (those that appear only under specific settings) with caution.

The goal is not to find a single “best” graph in isolation but to understand which features are robust across reasonable choices.

---

## Tips to Avoid Common Pitfalls

### 🔹 Don’t Sweep Everything at Once
Exploding the search over too many parameters makes interpretation hard. Start with one or two meaningful dimensions.

---

### 🔹 Keep Background Knowledge Fixed Initially
Before adding tiers, forbidden edges, or directional constraints, explore search space with minimal knowledge to see what the data alone suggests.

---

### 🔹 Use Visual Diagnostics
Look at graphs generated under extreme parameters (very sparse and very dense) to ensure your choices bracket the most plausible structures.

---

### 🔹 Document Your Choices
Keep track of the parameters you use and the resulting models. This transparency helps later when interpreting or reporting results.

---

## Where This Fits in the Workflow

Grid Search bridges:
- **Algorithm selection** (choosing methods and assumptions), and
- **Model evaluation** (using Markov Checking and other diagnostics).

It helps turn what could be a single guess at a graph into a *systematic exploration* with interpretable outputs.

---

## 🧭 Next Step

After running searches and collecting candidate models:

→ Continue with **Model Evaluation and Markov Checking** to assess whether those models are consistent with your data.