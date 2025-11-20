(parametric-model-box)=

# Parametric Model Box

The **Parametric Model Box** is where you choose the probability model used to interpret the structure of your graph.  
This choice affects how likelihoods, scores, regression parameters, and simulations are calculated.

This page organizes the original long block of text into smaller, clearer sections.

---

## Overview

A **parametric model** specifies:

- The distributional family of each variable
- How variables relate to one another via parents
- How parameters of those relationships are estimated
- What assumptions are made (e.g., linear, Gaussian, logistic, multinomial)

Different choices may be appropriate depending on your data type and goals.

---

## Available Parametric Models

### 1. **Linear Gaussian Model**

Assumptions:

- All variables are continuous.
- Relationships are linear.
- Noise terms are independent and Gaussian.

This is the standard model for SEM estimation and for many score-based algorithms.  
Tetrad uses ordinary least squares or maximum likelihood to estimate regression coefficients.

Used when:

- Data is continuous
- Linear relationships are reasonable approximations
- You want to use BIC, AIC, FGES, GES, SEM estimation, etc.

---

### 2. **Logistic Regression Model**

Assumptions:

- Target variable is binary.
- Predictors may be binary, categorical, or continuous.
- Probability of the outcome is modeled via **logit(p)**.

Used for:

- Binary classification
- Binary structural equations
- Hybrid systems mixing discrete and continuous variables

---

### 3. **Multinomial Logistic Model**

Assumptions:

- Target variable has more than two categories
- Categories are unordered (nominal)
- Probabilities are modeled via generalized logits

Used when:

- The child variable is categorical with 3+ values
- Parent set may be mixed-type

---

### 4. **Conditional Gaussian Hybrid Model**

Assumptions:

- Discrete variables may have continuous and/or discrete children
- Continuous children have linear-Gaussian relationships **conditional on** each discrete parent configuration

Features:

- Handles mixed discrete/continuous systems
- Each joint discrete parent state gets its own linear regression parameters
- Fits “mixtures of Gaussians” determined by discrete configuration

---

### 5. **Nonparametric or Semiparametric Models**
*(If available in your build; depends on modules included)*

Examples may include:

- Kernel regression
- Local likelihood estimation
- Spline-based approximations

Used when:

- Linear assumptions fail
- Distributions are skewed or multimodal
- You want flexible estimation without specifying full parametric forms

---

## Parameter Estimation Methods

Depending on the chosen model, Tetrad may estimate:

- **Regression coefficients**  
  via OLS, logistic regression, or multinomial logistic regression

- **Covariance matrices**  
  via empirical or model-implied computations

- **Conditional Gaussian parameters**  
  (means, variances, regression weights) for each discrete context

- **Likelihoods and scores**  
  including BIC, AIC, NML, MDL, and user-defined scores

Estimation happens automatically when you:

- Fit a model
- Compute a score
- Simulate from a graph
- Run regression-based inference

---

## Choosing the Right Model

Choose your parametric model based on:

### Data type
- Continuous → Linear Gaussian
- Binary → Logistic
- Multiclass categorical → Multinomial Logistic
- Mixed discrete/continuous → Conditional Gaussian

### Goal
- Causal discovery with FGES/PC → Usually Linear Gaussian or Conditional Gaussian
- SEM estimation → Linear Gaussian
- Classification → Logistic or Multinomial

### Assumptions
- If linearity fails → consider nonparametric models
- If you need high-speed scoring for large N → Linear Gaussian is the fastest

---

## Limitations and Caveats

- Conditional Gaussian models may require large sample sizes when discrete parent sets are large.
- Logistic/multinomial models may fail to converge if separation is present.
- Nonparametric methods may not scale well to high-dimensional settings.
- Using an inappropriate model (e.g., Linear Gaussian for non-Gaussian data) may degrade orientation accuracy or estimation precision.

---

## Summary

The Parametric Model Box defines the statistical assumptions used throughout Tetrad:

- How data are modeled
- How likelihoods and scores are computed
- How parameters for regressions and conditional distributions are obtained

Choose a model that matches the type of data you have and the assumptions you are willing to make.