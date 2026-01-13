# Detail: Nonlinearity Checks

## Purpose

The **Nonlinearity Checks** tool provides a systematic way to assess whether the conditional expectation E(Y | X) appears to be linear, nonlinear but additive, or genuinely non-additive, using several complementary statistical tests.

This tool is intended to help users:
- diagnose whether linear modeling assumptions are reasonable,
- decide whether nonlinear causal discovery methods (e.g., RFF-BIC, KCV-BIC, BF-based methods) are warranted,
- understand *why* certain algorithms succeed or fail on a given dataset.

The tool is **descriptive and diagnostic**, not a causal discovery algorithm by itself.

---

## Conceptual Background

Many classical causal discovery methods rely (explicitly or implicitly) on **linear conditional expectations**:

E(Y | X) = β₀ + βᵀX

However, real data often violate this assumption. Common alternatives include:

- **Additive nonlinear mechanisms** (generalized additive models, GAMs):
  Y = f₁(X₁) + ··· + fₖ(Xₖ) + e

- **Non-additive nonlinear mechanisms**:
  Y = f(X₁, …, Xₖ) + e

- **Fully general mechanisms**:
  Y = f(X₁, …, Xₖ, e)

The Nonlinearity Checks tool helps distinguish among these possibilities by combining fast screening tests with more computationally intensive diagnostics.

---

## Modes of Operation

### 1. Pairwise Mode

Each treatment X is tested individually against each outcome Y.

### 2. Conditional Mode

Each outcome Y is tested conditional on **all specified treatments X₁,…,Xₖ**.

---

## Fast Tests (Always Run)

### 1. Ramsey RESET Test

Detects misspecification by adding powers of fitted values to a linear model.

Reference: Ramsey (1969).

### 2. Conditional Moment Test

Checks whether nonlinear features of X explain linear-model residuals.

---

## Slow Tests (Optional)

Enabled via **Include slow tests**.

### 3. CV Linear vs Nonlinear

Linear ridge vs RFF-based nonlinear regression.

### 4. Additivity Check

Additive hinge-basis GAM vs non-additive RFF regression.

---

## Summary

This tool helps distinguish linear, nonlinear-additive, and nonlinear-nonadditive mechanisms and guides appropriate causal modeling choices.
