# Data Preparation

Most Tetrad workflows begin with a dataset in a **Data** box and end with a
graph or a fitted model. In between those steps, there is often a quiet but
important stage: **checking and preparing the data** so that the assumptions
of the chosen algorithms are at least approximately reasonable.

This section of the manual explains how to:

- Inspect a dataset in the **Data** box:
    - Check variable types and ranges,
    - Look at histograms and scatterplots,
    - Run quick diagnostics for (non-)Gaussianity and outliers.
- Use **Data → Data** tools to transform datasets:
    - Recode or drop variables,
    - Standardize or rescale,
    - Discretize continuous variables,
    - Create derived variables,
    - Subset or resample rows.
- Make **algorithm-aware choices** about preparation:
    - What matters for linear–Gaussian methods versus discrete methods,
    - When discretization is helpful or harmful,
    - When it is worth transforming variables (e.g. logs) versus switching
      to a more flexible search method.

The goal is not to prescribe a single “correct” pre-processing pipeline, but
to make Tetrad’s existing tools visible and to give practical guidance on
when and why to use them.

---

## Where data preparation happens in Tetrad

In the box-based interface, data inspection and preparation are spread across
a few places:

- The **Data** box:
    - Lets you view the dataset, inspect variable names and types,
    - Offers basic plots (histograms, scatterplots, etc.),
    - Provides some quick diagnostics for distributional shape and
      non-Gaussianity.
- **Data → Data** nodes:
    - Take an incoming dataset and produce a **new** dataset node,
      without modifying the original.
    - Each node performs one specific transformation (such as standardizing,
      discretizing, subsetting, or creating new variables).
- **Simulation** and **Compare** boxes (optional):
    - In simulation studies, you may prepare several versions of the same
      dataset (e.g. raw, standardized, discretized) and then compare how
      different algorithms behave on each version.

Throughout this section, we will assume you already know how to create Data
nodes and connect them to other boxes. If not, see the **Tetrad Interface →
Working with Data** pages first.

---

## Typical data preparation workflow

A common pattern in Tetrad looks like this:

1. **Load data** into a Data box.  
   Make sure variable names and types (continuous vs discrete) match what you
   expect.

2. **Inspect the variables**:
    - Use the Data box tools to look at histograms, scatterplots, and simple
      summaries of each variable.
    - Pay particular attention to:
        - Extreme outliers,
        - Very skewed distributions,
        - Obvious coding problems (e.g. -999 or 9999 used as “missing”).

3. **Decide whether a transformation is needed**:
    - For some algorithms, strong skewness or heavy tails are a problem
      (e.g. linear–Gaussian methods using Pearson correlations).
    - For others, they matter less (e.g. some nonparametric or rank-based
      approaches).
    - If you decide to transform, create a **Data → Data** node so the
      original dataset remains available.

4. **Apply Data → Data transformations**:
    - Standardize or center variables if your planned algorithm expects
      roughly comparable scales.
    - Discretize variables if you plan to use a discrete algorithm, or if you
      want to explore whether a coarse-grained representation is informative.
    - Drop or recode clearly problematic variables, or create new variables
      (e.g. sums, differences) that better capture your domain knowledge.

5. **Feed the transformed data into search and estimation**:
    - Connect the transformed Data node to Search, Regression, Estimator, or
      other boxes.
    - Optionally keep several transformed versions in parallel (e.g. raw vs.
      log-transformed) to compare results.

---

## What the rest of this section covers

The remaining pages in this **Data Preparation** section go into more
detail:

- **Inspecting data in the Data box**  
  How to use the plotting and diagnostic tools to understand variable
  distributions, non-Gaussianity, and simple dependence structure.

- **Data → Data transformations**  
  A catalog of transformations, grouped by purpose (basic cleaning, scaling,
  discretization, derived variables, resampling), with short guidance on
  when to use each one.

- **Missing data and simple handling strategies**  
  A brief overview of how Tetrad treats missing values by default and how
  simple Data → Data transformations can be used to drop, flag, or
  crudely impute missingness.

- **Algorithm-aware preparation tips**  
  Short “recipes” for preparing data for common families of algorithms
  (linear–Gaussian, discrete, mixed, and some nonlinear methods).

These pages are intended to be practical. They do not replace full
statistical texts on data cleaning, but they should help you make better
use of the tools already built into Tetrad.