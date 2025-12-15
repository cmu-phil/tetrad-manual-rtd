# Regression box

The **Regression box** is used to estimate numerical relationships
between variables *after* a causal model (or adjustment strategy) has
been selected. Unlike search or graph-editing boxes, the Regression box
does **not** modify the graph. Instead, it provides regression-based
summaries that help interpret causal effects implied by the current
model.

The tools in this box are primarily used to:

-   estimate regression coefficients for selected variables,
-   compute total causal effects using valid adjustment sets,
-   sanity-check effect estimates under different graph orientations.

The Regression box currently provides four main tools:

-   Multiple Linear Regression\
-   Logistic Regression\
-   Adjustment Total Effects\
-   IDA Check

Each is described below.

------------------------------------------------------------------------

## Multiple Linear Regression

**Purpose**\
Estimate linear relationships between a continuous outcome variable and
one or more predictor variables.

**Model** For outcome Y and predictors X₁,...,Xₖ, the fitted model is: Y
= β₀ + β₁X₁ + ... + βₖXₖ + ε,

where ε is an error term.

**Typical use** - Exploratory analysis of associations. - Baseline
comparison for causal effect estimates. - Regression-based effect
summaries after choosing a graph.

**Output** - Estimated coefficients (β values). - Standard errors and
test statistics. - Model fit diagnostics (when available).

**Notes** - This tool estimates *associational* regressions unless the
predictors and covariates are chosen using a valid adjustment set. -
Interpretation as a causal effect requires appropriate adjustment for
confounding.

------------------------------------------------------------------------

## Logistic Regression

**Purpose**\
Estimate the effect of predictors on a binary outcome variable.

**Model** For a binary outcome Y ∈ {0,1}, the model is: logit(P(Y=1)) =
β₀ + β₁X₁ + ... + βₖXₖ.

**Typical use** - Modeling binary outcomes (e.g., success/failure). -
Estimating log-odds effects under adjustment.

**Output** - Regression coefficients on the log-odds scale. - Standard
errors and test statistics.

**Notes** - As with linear regression, causal interpretation requires
appropriate covariate adjustment. - Coefficients represent changes in
log-odds, not probabilities.

------------------------------------------------------------------------

## Adjustment Total Effects

**Purpose**\
Estimate **total causal effects** of one or more treatment variables on
an outcome variable using valid adjustment sets derived from the graph.

**Conceptual approach** 1. A valid adjustment set is identified using
the graph. 2. A regression model is fit with the treatment(s) and
adjustment variables as predictors. 3. The coefficient(s) corresponding
to the treatment variable(s) are reported as total effect estimates.

**Typical use** - Estimating causal effects implied by a DAG or PAG. -
Comparing effect sizes across different adjustment sets. - Handling
single or multiple treatments.

**Notes** - This tool relies on standard regression models (linear or
logistic, depending on the outcome). - The validity of the effect
estimates depends on the correctness of the adjustment set.

*(See the Adjustment Total Effects detail page for full definitions and
examples.)*

------------------------------------------------------------------------

## IDA Check

**Purpose**\
Evaluate the stability of effect estimates across Markov-equivalent
graphs using the IDA (Intervention Calculus when the DAG is Absent)
framework.

**Conceptual approach** - For each DAG consistent with the estimated
equivalence class: - Compute a valid adjustment set. - Estimate the
causal effect using regression. - Compare the resulting effect estimates
across DAGs.

**Typical use** - Assess sensitivity of effect estimates to graph
uncertainty. - Identify effects that are robust across equivalence
classes.

**Output** - A range or set of effect estimates rather than a single
number.

**Notes** - IDA Check does not assert that any single estimate is
correct. - Instead, it highlights how much conclusions may vary given
graph ambiguity.

*(See the IDA Check detail page for definitions and interpretation.)*

------------------------------------------------------------------------

## Interpretation and workflow notes

-   The Regression box is typically used **after** graph estimation or
    adjustment set selection.
-   Results should be interpreted in light of the assumptions encoded in
    the graph.
-   Regression estimates are only causal when the chosen covariates
    block all backdoor paths.

------------------------------------------------------------------------

## Summary

The Regression box provides regression-based tools for translating
causal structure into numerical effect estimates. It bridges the gap
between graphical causal models and quantitative interpretation, while
making explicit the assumptions required for causal claims.
