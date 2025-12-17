# Data Exploration: Understanding Your Data Before Causal Discovery

Before running any causal search algorithm, it’s essential to explore your dataset. Examining your data helps you form reasonable assumptions about the types of relationships present and which methods are appropriate. This page walks you through the key steps to inspect your data using Tetrad’s Data Box.

---

## 1. Load Your Data

After opening Tetrad and loading your dataset into the **Data Box**, take a moment to look at the overall structure:

- Are the variables continuous, discrete, or a mix?
- Are there missing values?
- How many variables are there relative to the sample size?

These high-level characteristics shape which algorithms and tests are sensible.

---

## 2. List Attribute Characteristics

In the **Data Box**, use **List Attributes** to view:

- Variable names
- Data types (continuous vs discrete)
- Number of categories (for discrete variables)

This helps you decide which statistical tests and scores are appropriate. For example:

- Continuous variables can use tests like Fisher-Z or nonparametric alternatives.
- Discrete variables typically require discrete tests/scores.
- Mixed data may require specialized handling.

---

## 3. Examine Distributions with Histograms

Still in the **Data Box**, view histograms of individual variables:

- Does the distribution appear approximately Gaussian?
- Is it skewed, multimodal, or heavy-tailed?
- Are there outliers that might affect independence tests?

Understanding distribution shapes helps you choose tests/scores and anticipate potential nonlinear relationships.

---

## 4. Explore Pairwise Relationships with Plot Matrix

Open **Plot Matrix** from the **Data Box** to see:

- Scatterplots for pairs of continuous variables
- Patterns that suggest linear or nonlinear dependence
- Clusters or subgroups that may indicate latent structure

Visual inspection often reveals patterns that cannot be captured by automated linearity tests. Use the plot matrix to decide whether linear methods are reasonable, or if you should consider nonparametric techniques.

---

## 5. Note Potential Nonlinearity and Non-Gaussianity

Many conditional independence tests rely on linearity or Gaussian assumptions:

- Strong curvature or clusters in scatterplots suggests nonlinearity.
- Non-Gaussian distributions may reduce the effectiveness of Fisher-Z based tests.

Use your visual findings to guide whether you rely on linear methods or explore nonparametric tests/scores instead.

---

## 6. Think About Causal Sufficiency

Based on your domain knowledge and the patterns you see:

- Do you believe all relevant common causes are measured?
- Are there reasons to suspect latent confounders?
- Could there be selection bias or hidden structure?

These considerations help you decide whether to search for a DAG/CPDAG (assuming causal sufficiency) or a PAG (allowing latent confounders).

---

## 7. Decide on Preliminary Modeling Goals

Before running a search, clarify what output you’re comfortable interpreting:

- **Adjacency structure only** (which variables are connected)
- **Partial orientation** (arrowheads where identifiable)
- **Full causal orientation** under stronger assumptions

Your data exploration should inform what you aim to learn from causal discovery.

---

## 8. What’s Next?

Once you’ve explored your data and formed initial assumptions about:

- variable types,
- linear vs nonlinear relationships,
- causal sufficiency,

you are ready to proceed to the **Algorithm Selection and First Search** step of the workflow.

This preparation will make your search results easier to interpret and more aligned with the structure present in your data.

---

## Tips for Effective Data Exploration

- Don’t rush into causal search without inspecting data patterns.
- Use domain expertise along with visual inspection.
- Document your findings; they guide both methods choice and interpretation.