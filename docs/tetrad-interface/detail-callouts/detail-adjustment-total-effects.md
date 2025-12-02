# Adjustment & Total Effects

The **Adjustment & Total Effects** tool provides a one-stop interface for:

- finding (generalized) adjustment sets using recursive adjustment, and
- computing **total effects** via linear regression for each adjustment set.

It supports both:

- **single-pair total effects** for all combinations of treatments and outcomes, and
- **joint interventions** with multiple treatments and multiple outcomes.

```{figure} ../../_static/images/tetrad-interface/box-by-box/adjustment-total-effects.png
:name: tetrad-adjustment-total-effects-screenshot
:alt: Adjustment Total Effect Explorer in the Regression box

Explorer for listing adjustment sets and total effects.
```

---

## Where to find it

The **Adjustment & Total Effects** tool is available under the **Regression** box:

1. Add a **Regression** box to the workspace.
2. Connect a **Data** box and a **Graph** box to the Regression box.
3. In the Regression box editor, choose **Adjustment & Total Effects** as the regression method.

The tool requires:

- a **graph** encoding the assumed causal structure, and
- a corresponding **dataset** containing those variables (continuous, for linear regression).

---

## Basic idea

Given:

- a set of treatments \(X\),
- a set of outcomes \(Y\),
- and an estimated causal graph,

the tool:

1. **Finds adjustment sets** \(Z\) using recursive adjustment:
    - either for each **individual pair** \((x, y)\), or
    - for the **joint intervention** on \(X\) with respect to all \(Y\).
2. For each adjustment set \(Z\), runs a **linear regression** and reports the **total effect(s)** as regression coefficients:
    - in the simplest case, this is the coefficient of a single treatment \(x\) on a single outcome \(y\), given \(Z\).

---

## Mode selection

At the top of the editor you choose a **mode**:

- **Total effects for all X–Y pairs** (**PAIRWISE** mode)
- **Joint intervention: p(Y | do(X))** (**JOINT** mode)

### PAIRWISE mode

You specify sets \(X\) and \(Y\), but they are treated **pairwise**:

- For each \(x \in X\) and \(y \in Y\):
    - Tetrad runs **Recursive Adjustment** for the single pair \((x, y)\).
    - For each adjustment set \(Z\) it finds, it runs a linear regression of \(y\) on \(\{x\} \cup Z\).

Each row in the results table corresponds to a triple \((x, y, Z)\) and reports the total effect of \(x\) on \(y\) given \(Z\).

This mode essentially automates “classic” recursive adjustment for many \((x, y)\) pairs at once.

### JOINT mode

Here \(X\) and \(Y\) are treated as **joint sets**:

- Tetrad runs **RecursiveAdjustmentMultiple(X, Y)** to find adjustment sets that are valid for the joint intervention \(p(Y \mid do(X))\).
- For each adjustment set \(Z\) and each \(y \in Y\), it runs a linear regression of \(y\) on \(X \cup Z\).

Each row in the results table corresponds to:

- the **X-set** (possibly multiple treatments),
- one outcome \(y\), and
- one adjustment set \(Z\).

The row stores the full vector of regression coefficients for all \(X\); the summary table shows a single “primary” effect (see below), and the full vector can be inspected via the regression dialog.

---

## Specifying treatments and outcomes

Treatments and outcomes are entered in the **Treatments (X)** and **Outcomes (Y)** text fields.

You can enter:

- **exact variable names**, separated by commas or whitespace, e.g.  
  `X1, X2, X3`
- **wildcard patterns** using `*` and `?`, e.g.
    - `X*` &nbsp;matches all variables whose names start with `X`,
    - `Z?` &nbsp;matches `Z1`, `Za`, etc.

Examples:

- `X1` – just the variable `X1`
- `X1, X2, X3` – three specific treatments
- `X*, Z?` – all variables starting with `X`, plus all two-character variables beginning with `Z`

If a wildcard pattern does not match any variables, the tool shows an error.

---

## Recursive adjustment parameters

Click **Edit parameters…** to configure the recursive adjustment search.

The dialog includes:

- **Max number of adjustment sets**  
  Upper bound on how many adjustment sets to enumerate.

- **Max radius** (`-1` for no limit)  
  Optional distance limit from the chosen endpoint side. Nodes beyond this radius are excluded from candidate adjustment sets.

- **Near which endpoint (0 = X, 1 = Y, other = either)**  
  Determines which side is treated as “closer” when ordering candidate variables:
    - `0` – prefer variables near the treatments,
    - `1` – prefer variables near the outcomes,
    - other – use the minimum of the distances to X and Y.

- **Max path length** (`-1` for no limit)  
  Limits the length of witness paths considered when searching for backdoor paths.

- **Avoid amenable backbone (Perković GAC mode)**  
  If checked, the algorithm will **not** adjust on nodes on the “amenable backbone” (the causal backbone between X and Y), following the generalized adjustment criterion of Perković et al.

These parameters apply both to **PAIRWISE** recursive adjustment and **JOINT** recursive adjustment for multiple treatments.

---

## Results table

After clicking **Compute adjustment sets and effects**, the results appear in a table with the following columns:

1. **#** – row index.
2. **X set** – the treatment set used in the regression for this row.
3. **Y** – the outcome variable for this row (always a singleton).
4. **Adjustment set Z** – the adjustment set used in this regression.
5. **Total effect** – the reported total effect for the primary treatment:
    - In **PAIRWISE** mode, this is the regression coefficient of the single treatment \(x\) on \(y\) given \(Z\).
    - In **JOINT** mode with multiple treatments, each row stores a vector of coefficients for all treatments in \(X\); the table shows the coefficient for the first treatment in the X set (in its displayed order). The full vector is available in the regression dialog.
6. **Abs total effect** – the absolute value of the “Total effect” column, useful for sorting on effect size.

### Sorting and copying

- You can click any column header to **sort** by that column (e.g., by total effect or absolute total effect).
- You can select **multiple rows** (or all rows) and copy them into Excel or another tool.  
  Column headers are not included in the clipboard; they can be added manually if needed.

---

## Viewing full regression results

To see the full regression output for a particular row:

1. Select exactly one row in the table.
2. Click **View regression…**.

A dialog appears showing, for that row:

- the full list of regressors (treatments \(X\) plus \(Z\)),
- the estimated regression coefficients (betas),
- standard errors,
- and, when available, t statistics and p values.

This lets you inspect:

- the full vector of treatment coefficients in **JOINT** mode, and
- other regression diagnostics beyond the “Total effect” summary in the main table.

If multiple rows are selected when you click **View regression…**, the tool will ask you to select exactly one row.

---

## Interpretation and limitations

- The tool uses **linear regression** (ordinary least squares) under the usual assumptions.
- The reported “total effect” is the regression coefficient of a treatment (or treatments) on an outcome **conditional on an adjustment set** \(Z\) that is valid according to recursive adjustment on the supplied graph.
- As always, correctness of the causal interpretation depends on:
    - the appropriateness of the graph (e.g., no major missing confounders, correct orientations), and
    - suitability of a linear model for the variables in question.

This tool is intended to provide a convenient interface for:

- exploring candidate adjustment sets, and
- comparing the associated total effects,

both in the classic **single-pair (x, y)** setting and for **joint interventions** on multiple treatments.  
Additional options (such as O-sets) may be added in future versions.