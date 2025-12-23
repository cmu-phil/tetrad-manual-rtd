# Data Exploration: Understanding Your Data Before Causal Discovery

Exploring a dataset before running causal discovery algorithms is often an important first step.  
Data exploration helps clarify which modeling assumptions are plausible and which methods are likely to be appropriate for the data at hand.

This page describes ways to inspect data using Tetrad’s **Data Box**, and how those observations commonly inform later choices when using Grid Search.

---

## 1. Load and Inspect Your Data

After loading a dataset into a **Data Box**, it can be useful to note a few high-level characteristics:

- Are the variables **continuous**, **discrete**, or **mixed**?
- Are there **missing values**?
- How many variables are there relative to the sample size?

These properties often influence which algorithms, tests, and scores are suitable in later stages of analysis.

> At this point, the goal is not to settle every modeling decision, but to get a sense of which assumptions seem reasonable.

---

## 2. Review Variable Types with *List Attributes*

In the **Data Box**, **List Attributes** provides a summary of:

- Variable names
- Data types (continuous vs. discrete)
- Number of categories (for discrete variables)

This information is relevant because different methods make different assumptions:

- **Continuous data** supports tests such as Fisher-Z and related approaches.
- **Discrete data** requires discrete tests and scores.
- **Mixed data** may call for hybrid or specialized methods.

Later, Grid Search will automatically restrict available tests and scores based on these data types.

---

## 3. Examine Marginal Distributions with Histograms

Histograms in the **Data Box** allow you to inspect individual variables:

- Are distributions roughly symmetric or strongly skewed?
- Are there heavy tails or extreme outliers?
- Do discrete variables have sparse or unbalanced categories?

These features can matter for:

- The behavior of linear-Gaussian tests
- Sensitivity to outliers
- Whether transformations or robust alternatives might be worth considering

At this stage, it is usually sufficient to note potential issues rather than committing to a specific test.

---

## 4. Explore Pairwise Relationships with the Plot Matrix

The **Plot Matrix** provides a visual overview of pairwise relationships:

- Scatterplots for continuous variables
- Apparent linear or nonlinear trends
- Clustering or gaps that may suggest latent structure or selection effects

Visual inspection often reveals structure that is difficult to summarize with a single statistic.  
Patterns such as strong curvature or stratification can indicate that purely linear assumptions may be restrictive.

---

## 5. Consider Linearity and Gaussianity (Informally)

Many commonly used independence tests rely on assumptions such as linearity and Gaussian noise.

When examining the data, it can be helpful to consider:

- Whether relationships appear approximately linear
- Whether distributions are roughly Gaussian
- Whether there are clear departures (e.g., strong curvature or multimodality)

These observations can guide whether linear-Gaussian methods are likely to be adequate or whether nonparametric alternatives should be included in Grid Search.

---

## 6. Reflect on Causal Sufficiency and Latent Variables

Based on domain knowledge and observed patterns, you may wish to consider questions such as:

- Are important common causes likely to be **unmeasured**?
- Do some associations appear potentially spurious?
- Is selection bias or conditioning likely to play a role?

These considerations often inform whether the analysis targets:

- A **DAG or CPDAG**, assuming causal sufficiency, or
- A **PAG**, allowing for latent confounders and selection effects

Perfect certainty is rarely possible; the goal is simply to adopt a defensible starting point.

---

## 7. Clarify Your Modeling Goals

Before running searches, it can help to clarify what kinds of conclusions are of interest:

- **Adjacencies** (which variables are connected)
- **Partial orientations** (arrowheads where identifiable)
- **Fully oriented models** under stronger assumptions

Different goals naturally call for different levels of modeling complexity and diagnostic checking.

---

## 8. Moving Forward

Once you have:

- Identified variable types,
- Noted distributional and relational features,
- Reflected on causal sufficiency,

you are well positioned to move on to method selection and systematic exploration using **Grid Search**.

Careful data exploration often makes later results easier to interpret and evaluate.

---

## Practical Notes

- Even brief exploration can reveal features that affect method choice.
- Visual tools often complement numerical summaries.
- Let observations inform modeling decisions where possible.
- Recording early observations can be helpful when interpreting results later.