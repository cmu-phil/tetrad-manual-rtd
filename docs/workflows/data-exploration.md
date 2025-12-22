# Data Exploration: Understanding Your Data Before Causal Discovery

Before running any causal discovery algorithm, it is essential to explore your dataset.  
Data exploration helps you form **reasonable modeling assumptions** and avoid applying methods that are poorly matched to the data.

This page walks you through how to inspect your data using Tetrad’s **Data Box**, and how those observations guide later choices in Grid Search.

---

## 1. Load and Inspect Your Data

After loading your dataset into a **Data Box**, begin by noting a few high-level characteristics:

- Are the variables **continuous**, **discrete**, or **mixed**?
- Are there **missing values**?
- How many variables are there relative to the sample size?

These properties strongly influence which algorithms, tests, and scores are appropriate later on.

> You do *not* need to answer every modeling question now — the goal is simply to understand what kinds of assumptions are plausible.

---

## 2. Review Variable Types with *List Attributes*

In the **Data Box**, use **List Attributes** to view:

- Variable names
- Data types (continuous vs. discrete)
- Number of categories (for discrete variables)

This information directly affects which methods can be used:

- **Continuous data** supports tests like Fisher-Z and nonparametric alternatives.
- **Discrete data** requires discrete tests and scores.
- **Mixed data** may require specialized or hybrid methods.

Grid Search will later restrict available tests and scores based on these data types.

---

## 3. Examine Marginal Distributions with Histograms

Use **Histograms** in the **Data Box** to inspect individual variables:

- Are distributions roughly symmetric or strongly skewed?
- Are there heavy tails or extreme outliers?
- Do discrete variables have very sparse categories?

These features can influence:

- The reliability of linear-Gaussian tests
- Sensitivity to outliers
- Whether transformations or robust methods are worth considering

At this stage, you are *not* deciding on a specific test — just noting potential issues.

---

## 4. Explore Pairwise Relationships with the Plot Matrix

Open the **Plot Matrix** to visually examine relationships between pairs of variables:

- Scatterplots for continuous variables
- Evidence of linear or nonlinear dependence
- Clusters or gaps suggesting latent structure or selection effects

Visual inspection often reveals patterns that no single test can summarize.  
Strong curvature, stratification, or clustering can suggest that purely linear assumptions may be inadequate.

---

## 5. Consider Linearity and Gaussianity (Informally)

Many commonly used independence tests assume linearity and/or Gaussian noise.

Ask yourself:

- Do relationships appear approximately linear?
- Are distributions reasonably close to Gaussian?
- Are there obvious violations (e.g., strong curvature, multimodality)?

These observations help guide whether linear-Gaussian methods are reasonable or whether nonparametric alternatives should be explored in Grid Search.

---

## 6. Reflect on Causal Sufficiency and Latent Variables

Using both domain knowledge and data patterns, consider:

- Are important common causes likely to be **unmeasured**?
- Do some variables appear spuriously associated?
- Is selection bias or conditioning likely to be present?

This helps determine whether you should aim to learn:

- A **DAG or CPDAG** (assuming causal sufficiency), or
- A **PAG** (allowing latent confounders and selection effects)

You do not need certainty — just a defensible starting assumption.

---

## 7. Clarify Your Modeling Goals

Before running any search, decide what kind of conclusions you are aiming for:

- **Adjacencies only** (which variables are connected)
- **Partial orientations** (arrowheads where identifiable)
- **Fully oriented models** under stronger assumptions

Different goals justify different levels of modeling complexity and diagnostic scrutiny.

---

## 8. Ready to Move On

Once you have:

- Identified variable types,
- Noted distributional and relational patterns,
- Reflected on causal sufficiency,

you are ready to proceed to the next step: choosing methods and running systematic searches using **Grid Search**.

Good data exploration makes later results easier to interpret — and easier to trust.

---

## Practical Tips

- Do not skip data exploration — even brief inspection can prevent major mistakes.
- Use visual tools alongside statistical summaries.
- Let observations guide your modeling choices, not the other way around.
- Write down what you notice; it will help when interpreting results later.