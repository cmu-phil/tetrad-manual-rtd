# IDA Check (Regression box)

The **IDA Check** panel in the **Regression box** is designed for
*evaluating* IDA-based total effect estimates in simulation studies, where
the **true total effects are known** from the generating DAG.  
It computes Maathuis-style IDA intervals, optionally Optimal IDA intervals,
and compares them to the true total effects variable–pair by variable–pair.

```{figure} ../../_static/images/tetrad-interface/box-by-box/ida-check.png
:name: tetrad-ida-check-screenshot
:alt: IDA Check

IDA Check
```

---

## Layout and controls

The IDA Check window contains:

- **Table / Help buttons (top)**
  - **Table** – shows the main IDA summary table (default view).
  - **Help** – displays a short explanation of the panel.

- **Show Optimal IDA** (checkbox)  
  - **Unchecked**: uses **standard IDA** (Maathuis et al.).  
  - **Checked**: uses **Optimal IDA** (Witte et al.), which tightens or
    refines the IDA interval when possible.

- **Regexes (semicolon separated):** (text field)  
  A filter for the **Pair** column. You can enter one or more Java-style
  regular expressions separated by semicolons (`;`); only rows whose pair
  name matches at least one regex will be shown.

  Examples:
  - `^X1 <- X` – show only effects where the outcome is `X1`.
  - `X3;X4` – show all pairs whose name contains `X3` or `X4`.

- **IDA summary table** (central area)  
  One row per ordered pair “**Y <- X**”, interpreted as the **total effect
  of treatment X on outcome Y**.

- **Summary statistics** (bottom text area)  
  Aggregate measures of how well the IDA intervals match the true total
  effects across all displayed pairs.

- **Done** (button)  
  Closes the IDA Check window.

---

## Table columns

Each row in the table corresponds to one ordered pair (X, Y).

- **Pair**  
  Displayed as `Y <- X`, meaning:
  - **Treatment** = `X`  
  - **Outcome**  = `Y`  

- **Min TE**  
  The **minimum total effect** of X on Y over all DAGs and parent
  sets consistent with the current graph (standard or Optimal IDA,
  depending on the checkbox). This is the left endpoint of the IDA
  interval.

- **Max TE**  
  The **maximum total effect** of X on Y over all compatible DAGs /
  parent sets, i.e., the right endpoint of the IDA interval.

- **IDA Min Effect**  
  The **IDA point estimate** used in the evaluation. In many settings this
  is the effect corresponding to the **minimum absolute value** in the IDA
  interval, but the exact definition follows the implementation used in
  Tetrad’s IDA code.

- **True TE**  
  The **true total effect** of X on Y, computed from the generating
  DAG (available only in simulation).

- **Sq Dist**  
  The **squared distance** between the true total effect and the IDA
  interval, defined as:
  - 0 if `True TE` TE lies inside the interval between Min TE and Max TE (including endpoints)
  - otherwise, the square of the distance from `True TE` to the **nearest
    endpoint** of that interval.

  In other words, `Sq Dist` is a per-pair measure of **how far the IDA
  interval misses the truth, if at all**.

---

## Summary statistics (bottom)

The text area at the bottom reports aggregate measures across all rows in
the table, for example:

- **Average Squared Distance:**  
  The mean of `Sq Dist` over all displayed pairs. This is a single-number
  summary of how well the IDA intervals capture the true total effects.

- **Average Min Squared Difference Est True:**  
  The average squared difference between the **left endpoint** (`Min TE`)
  and the true effect.

- **Average Max Squared Difference Est True:**  
  The average squared difference between the **right endpoint** (`Max TE`)
  and the true effect.

These quantities are useful for **comparing algorithms**: you can run
different search procedures (FCI, GFCI, FCIT, LV-based methods, etc.),
open the IDA Check panel for each resulting graph, and compare the summary
statistics to see which graphs yield better IDA intervals relative to the
known truth.

---

## Typical usage

1. **Run a search algorithm** on simulated data where the true DAG (and
   hence true total effects) are known.

2. Open the **Regression** box and select the **IDA Check** component.

3. Optionally:
   - Use **Regexes** to focus on a subset of pairs,
   - Toggle **Show Optimal IDA** to switch between standard and Optimal
     IDA.

4. Inspect:
   - The table for particular pairs of interest (`Pair`, `Min TE`,
     `Max TE`, `True TE`, `Sq Dist`),
   - And the **summary statistics** to assess overall IDA performance for
     this graph.

5. Repeat with graphs from different algorithms to compare how well they
   support IDA-based total effect estimation.

---

## Notes

- For real data, where the True TE column is not available, all columns 
  and summary statistics that require knowledge of the true total effect are 
  omitted. In this mode, the panel simply reports the IDA (or Optimal IDA) intervals 
  themselves, which can be interpreted as empirical bounds on the unknown total effects.
- The quality of IDA intervals depends on the estimated graph.
  A poor graph may yield intervals that systematically miss the true
  effects, even if the IDA machinery itself is correct.