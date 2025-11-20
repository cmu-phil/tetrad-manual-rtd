(estimator-box)=

# Estimator Box

The **Estimator Box** takes as input a data box (or simulation box) together with an appropriate **parametric model** and produces an **instantiated model** whose parameters have been fitted to the data. In other words, it turns a structural or graphical model plus data into a fully specified statistical model.

The instantiated model can then be:

- used for **simulation**,
- passed to an **updater**,
- inspected via tables and implied matrices,
- or compared to other models using scores.

Although there are several different estimators, they all share the same basic idea:  
given a parametric family, choose parameter values that make the observed data “as likely as possible” (often in the sense of maximum likelihood or penalized likelihood).

---

## Possible Parent Boxes of the Estimator Box

The Estimator Box typically has the following possible **parent boxes**:

- A **parametric model box** (specifying the structure and family)
- A **data box** (or simulation box) providing the sample
- Optionally, a **knowledge box** that constrains parameters or structure

Some estimator types may require specific combinations (for example, SEM estimators need a SEM parametric model).

---

## Possible Child Boxes of the Estimator Box

The Estimator Box can feed into:

- A **graph box** (to view the structure together with estimated parameters)
- A **simulation box** (to simulate new data from the estimated model)
- An **updater box** (to do inference given evidence)
- An **instantiated model box** (to inspect parameters, implied matrices, statistics)
- A **compare box** (to compare alternative models via scores)

---

## ML Bayes Estimations

For **Bayes net models** (categorical/discrete):

- The model is parameterized by **conditional probability tables (CPTs)**.
- The **ML Bayes estimator** computes maximum likelihood estimates of each CPT from the data.
- The likelihood of the full model is the product of the corresponding conditional probabilities over all cases in the sample.

Main properties:

- Works on **Bayes parametric models** with no latent variables.
- Requires that the input data set has **no missing values**.
- Produces a Bayes instantiated model that can be inspected and updated.

A sample ML Bayes estimate looks like this:

![](/_static/images/estimator_box_1.png)

In the resulting instantiated model:

- The **Model** tab shows conditional probability tables for each variable given its parents.
- The **Model Statistics** tab displays the log-likelihood and a **BIC** score of the form  
  \[
  \text{BIC} = 2L - k \ln N,
  \]
  where \(L\) is the log-likelihood, \(k\) the number of free parameters, and \(N\) the sample size.  
  (In Tetrad’s convention, **larger BIC is better**.)

---

## Dirichlet Estimations

The **Dirichlet estimator** is a Bayesian estimator for Bayes nets:

- Each row of a CPT is given a **Dirichlet prior**.
- Posterior means are used as CPT entries, effectively performing **smoothing** of frequencies.

Conceptually:

- It is like adding **pseudo-counts** to each cell before normalizing.
- This avoids zero probabilities in rarely observed or unobserved parent–child configurations.

The resulting Dirichlet instantiated model:

- Has CPT entries that reflect both the data and the prior.
- Is again a Bayes IM and can be used in simulation or updating.

Limitations:

- The Dirichlet estimator in Tetrad does **not** currently handle data sets with **missing values**.

---

## EM Bayes Estimations

The **EM Bayes estimator** extends ML Bayes estimation to handle:

- Data sets with **missing values**,
- Models with **latent variables**.

It uses the **Expectation–Maximization (EM)** algorithm:

1. **E-step**: given current parameters, compute expected sufficient statistics under the current model.
2. **M-step**: update parameters to maximize the expected complete-data log-likelihood.

Key properties:

- Produces Bayes instantiated models (with CPTs) as output.
- Is applicable when:
    - the graph contains latent variables, and/or
    - the data matrix has missing entries.
- Converges to a local maximum of the likelihood function.

As with the ML Bayes estimator, the output model can be:

- Viewed via the **Model** tab,
- Used for simulation,
- Passed to an updater or compare box.

---

## SEM Estimates

For **structural equation models (SEMs)**:

- Variables are typically continuous.
- Relationships are linear with **Gaussian errors**.
- Parameters include regression coefficients, variances, and sometimes covariances of error terms.

A SEM estimator:

- Takes a **SEM parametric model** and a data box.
- Estimates parameters via maximum likelihood (or related methods).
- Produces a **SEM instantiated model**.

A sample SEM estimation output looks like this:

![](/_static/images/estimator_box_2.png)

Features of the SEM estimator:

- The **Model** tab shows the parameterized equations and estimated values.
- The **Implied Matrices** tab shows implied covariance and correlation matrices.
- The **Tabular Editor** shows parameter estimates, standard errors, test statistics, and p values.
- The **Model Statistics** tab shows:
    - Degrees of freedom
    - Chi-square and p value
    - Fit indices such as CFI, RMSEA, RMR (if supported)
    - A BIC value (again of the form \(2L - k \ln N\), with **higher values preferred** in Tetrad’s sign convention).

Tetrad provides several **parameter optimizers** (e.g., RICF, quasi-Newton methods) and different estimators (e.g., FML, FGLS). These can be chosen from menus at the bottom of the estimator window.

Limitations:

- SEM estimation typically assumes **no missing values** in the data set.
- SEM estimators do not work for **cyclic** models.

---

## Scores and Optimizers

Estimation often interacts with **scores**:

- **BIC**: \(2L - k \ln N\), larger is better in Tetrad’s convention.
- Other scores (such as AIC or custom criteria) may be available depending on the model type.

For SEM estimators:

- You can choose among multiple **optimization methods**.
- The optimization process:
    - Starts from an initial parameter guess.
    - Iteratively improves the parameters until convergence.
    - Reports the final parameter set and fit statistics.

For Bayes net estimators:

- EM and Dirichlet variants differ in how they handle missing data and priors.
- Scores like BIC can still be computed to compare competing structures.

---

## Summary

The **Estimator Box** is the bridge from:

> **Data + Model** → **Fully specified, instantiated model**

It supports:

- **ML Bayes estimation**
- **Dirichlet estimation**
- **EM Bayes estimation**
- **SEM estimation**

and provides all of the fitted parameters and diagnostic statistics you need to inspect or use the model downstream in simulation, updating, comparison, or further search.