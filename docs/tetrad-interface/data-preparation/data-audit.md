# Data Audit

```{figure} ../../_static/images/tetrad-interface/box-by-box/data-audit.png
:name: tetrad-data-audit-screenshot
:alt: Data Audit window for the Auto MPG data.

The Data Audit for the Auto MPG data used in the worked example.
```

The **Data Audit** reports properties of a dataset that bear on the choice and the reliability of a
causal search. It is the first thing worth running on a dataset you have not analyzed before,
because most of what it finds is invisible in a spreadsheet view and fatal to a search if ignored.

Open it from the Data box: **Tools → Data Audit...**. It is also available in the Simulation box,
on simulated data.

## What the audit will and will not tell you

The audit is **findings-only**. It reports what is true of the data and takes no position on what
you should do about it. That is deliberate: what to do depends on which method you intend to use
and on where the data came from, neither of which the audit knows. The interpretation lives here,
in this page, not in the program.

Each finding carries one of two severities:

- **INFO** — a property worth knowing that is not necessarily a defect.
- **WARNING** — a property that typically degrades or invalidates common analyses if ignored.

A warning is not an error. Several of the checks are heuristics on the shape of a distribution, and
a few of them will flag a perfectly good variable. Read the finding, look at the variable, and
decide.

Equally, **the absence of a finding is not a clean bill of health.** Specific blind spots are noted
under each check below, and the general ones are collected at the end of this page.

## The panel

For a **dataset**, the audit has three tabs:

- **Findings** — one row per finding, with its severity, the variables involved, and a message
  carrying the relevant numbers.
- **Variables** — a per-variable summary.
- **Missingness** — the missing-data report, including pattern information and Little's MCAR test.

For a **covariance matrix**, there are two tabs, **Findings** and **Report**, and the checks are
the ones that can be computed from a matrix rather than from rows.

Alongside the tables:

- **A grouping-variable selector**, offered when the dataset has at least one discrete variable.
  Choosing a variable recomputes row autocorrelations *within* its groups rather than over the file
  as a whole. Use it whenever the file stacks blocks — subjects, sites, regions, semesters — since
  otherwise block-level mean shifts and the jumps at block boundaries contaminate the pooled
  estimate and the audit reports serial dependence that is really block structure.
- **Notes...** — the audit's cross-references to other diagnostics that bear on the findings.
- **Copy to Clipboard**, and **Select All Cells** / **Copy Cells** from the right-click menu, for
  getting a report out.

### Actions the audit can take for you

Four of the findings come with a way to act on them in place. Each previews what it will do and
asks for confirmation, and each recomputes the audit afterwards so you can see what changed.

- **Recode Selected Sentinel Values to Missing...** — turns the flagged codes in the selected rows
  into missing values.
- **Recode a Value to Missing in All Variables...** — the same for one value across every variable,
  which is what you want when a single code such as `-99` was used file-wide.
- **Remove Variables by Missingness...** — preview and apply a missingness-rate cutoff, dropping
  the variables above it.
- **Remove Variables Creating Determinism...** — proposes which variable to drop from each
  determinism finding so that the finding is resolved, and reports the fitted equation for each
  removed variable, fitted before removal. Which member of a deterministic relation to drop is not
  decidable from the data, so the choice is yours; prefer dropping the *derived* variable, the one
  computed from the others.
- **Plot Matrix for Selected Row(s)...** — opens a plot matrix for the variables a finding names,
  which is usually the fastest way to see whether a flag is real.

## The findings

### Columns that carry no information

**CONSTANT_COLUMN** — the column has at most one distinct value among its non-missing entries.
Constancy is determined exactly, not by a variance threshold. Every test and score involving the
variable is degenerate, and including it makes the covariance matrix of the continuous variables
singular. Drop the column.

**NEAR_CONSTANT** — the variable varies but barely: negligible nonzero variance, or a discrete
variable with almost all its mass on one category. Exactly constant columns are reported as
`CONSTANT_COLUMN` instead and never both. Treat it as very low information; dropping it is usually
right, and keeping it will cost you numerical stability.

**DUPLICATE_COLUMNS** — two columns are exact affine functions of one another on the rows where
both are observed: identical columns, complementary indicators such as `y = 1 - x`, or rescaled
copies. One of the pair carries nothing the other does not. Drop one.

### Variable type and granularity

**CONTINUOUS_FEW_VALUES** — a variable declared continuous takes few distinct values. Either it
should be declared discrete, or it was mechanically converted from a discrete source. Decide which,
and redeclare it if so; a few-valued "continuous" variable makes linear machinery behave oddly.

**DISCRETE_MANY_LEVELS** — a discrete variable has many levels. Conditioning on it, or crossing it
with other discrete variables, produces many small cells. If the levels are ordered, treating it as
continuous is an alternative; otherwise consider collapsing categories.

**SMALL_MARGINAL_CELL** — a discrete variable has categories with very small counts. Tests
involving those categories are unreliable. Collapse or drop the sparse categories.

**SMALL_PAIRWISE_CELLS** — a pair of discrete variables has small expected cell counts under
independence, so conditional independence tests involving the pair, or conditioning sets containing
them, will be unreliable. The same remedy, or restrict the conditioning depth.

### Coded and censored values

These two are the most consequential findings on real data and the easiest to miss, because
arithmetic cannot distinguish a code from a measurement.

**SENTINEL_VALUE** — a continuous variable has a repeated point mass at one extreme of its range,
separated from the rest of the distribution by a gap far larger than the typical spacing between
adjacent values. That is the signature of a code such as `0`, `-1`, `-99` or `999` written in to
mark a measurement that was not taken. The damage is not confined to the flagged variable: a shared
code creates spurious association between any two variables carrying it on the same rows, and
attenuates the association between a coded variable and an uncoded one, so correlations move in
both directions and can change sign. The point mass also costs tests their power, and a graph can
pass a Markov check because nothing rejects rather than because the graph is right. Use **Recode
Selected Sentinel Values to Missing...**, then decide how to handle the missingness.

The check cannot read your codebook. A genuine boundary value that repeats and sits far from its
neighbors will be flagged, and a code that falls inside the observed range or coincides with
plausible measurements will not be. Whether the flagged value is a code is a question about the
data's provenance.

**BOUNDARY_ATOM** — a large share of a variable's values sit at the top or bottom of its range with
*no* gap separating them from the rest: a grade of 100, a detector at its maximum, a scale that ran
out. This is a real measurement but a censored one — a cell at the ceiling says "at least this
much". Treating the atom as an exact value flattens that end of the distribution and attenuates
every correlation the variable takes part in, by an amount that differs from variable to variable
with the size of the atom. Because it does not cancel across a block, rank-based and
correlation-based structure tests read the attenuation as structure. Rank correlation does not
rescue it: the ordering inside the tied mass does not exist to be recovered. Treating the atom as
missing is wrong in the other direction, since it discards the information that the value was large
and is missing-not-at-random besides.

The remedy is to treat the bound as a bound: a censored covariance estimate — for RLCD, the
censor-ceiling option — or a test for discrete or mixed data after dichotomizing at the bound.

`SENTINEL_VALUE` and `BOUNDARY_ATOM` share the mass condition and are separated by the gap: a
repeated extreme value with a gap is a candidate code, one without is a candidate bound. Only
continuous variables are checked.

### Determinism and near-determinism

Functional determinism among the variables violates faithfulness, and it destabilizes conditional
independence judgments in a specific and damaging way: conditioning sets containing the determining
variables render the determined variable pseudo-independent of everything, separating sets become
pathological, and constraint-based orientation can produce arrowheads no mechanism supports — a
computed column "causing" its own inputs. This is why the audit works so hard at detecting it, and
why **Remove Variables Creating Determinism...** exists.

In every determinism finding, **the determined variable is listed first** and the determining set
follows.

**EXACT_LINEAR_DEPENDENCE** — the correlation matrix of the continuous variables is rank-deficient:
some variable is an exact linear function of the others on the analyzed rows. This finding cannot
localize the dependence; localizable exact dependencies are reported as `DUPLICATE_COLUMNS`.

**NEAR_DETERMINISM_LINEAR** — a continuous variable is nearly a linear function of the others
(multiple R² above threshold). When a small subset accounts for most of the dependence, that subset
is named; when the dependence is diffuse, only the determined variable is listed.

**NEAR_DETERMINISM_NONLINEAR** — a continuous variable is nearly a smooth, generally nonlinear
function of a small set of others, judged by leave-one-out cross-validated R² of a spline
regression, and reported only where the linear check did not fire. Computed columns with nonlinear
defining formulas are caught here. Cross-validation is the overfitting guard, so a high value
cannot come from basis flexibility alone. Two limits are worth knowing: subsets are grown greedily
and reported at the first size reaching the threshold, so with correlated predictors the subset is
not unique; and the spline basis is linear beyond its boundary knots, so dependence carried mostly
in the extreme tails can be understated.

**NEAR_DETERMINISM_DISCRETE_CONTINUOUS** — a continuous variable is nearly determined by a discrete
one (eta-squared above threshold); the discrete variable is close to a deterministic coarsening of
the continuous one.

**DETERMINISTIC_RELATION** — a variable is constant, within tolerance, inside every multi-row cell
of the joint values of a small set of other few-valued variables. This check is nonparametric and
joint, so it catches nonlinear functions of *combinations* of variables that the linear and
single-discrete checks miss. Only minimal determining sets are reported. The search is bounded — a
maximum determining-set size, a maximum distinct-value count for determiners, and a fixed work
budget — so its absence does not rule out determinism beyond those bounds.

**HIGH_CORRELATION** — a pair of continuous variables is very highly correlated in absolute value.
Short of determinism, but the same instability in milder form.

### Sample size and conditioning

**LOW_SAMPLE_RATIO** — few rows per variable, which limits the conditioning depth you can trust.
Reduce the depth, or use a method that conditions less aggressively.

**COMPLETE_CASES_FORCE_SINGULARITY** — the number of complete rows minus one is smaller than the
number of continuous variables, so *any* covariance matrix computed on complete cases is singular
by arithmetic, whatever the variables measure. When this fires, joint linear-dependence findings
cannot be attributed to relationships among particular variables: the singularity is forced by the
complete-case count. Fix the missingness or reduce the variable set before reading anything into
those findings.

### Missing values

**MISSING_DATA** — the dataset has missing values; the finding carries summary statistics, and the
**Missingness** tab has the pattern detail and Little's MCAR test.

**PAIRWISE_CORRELATION_NOT_PSD** — the pairwise-complete correlation matrix has a negative
eigenvalue. Because each entry is computed on a different subset of rows, the assembled matrix is
not the correlation matrix of any single sample, so joint quantities derived from it — rank,
variance inflation factors, partial correlations — can be incoherent. Individual pairwise
correlations remain interpretable, each on its own row subset.

### Distributional shape

**NON_GAUSSIAN** — a continuous variable's marginal deviates from Gaussian by the Anderson-Darling
test. Whether this is bad news depends entirely on your method: it is a threat to linear-Gaussian
machinery and an **asset** to methods that exploit non-Gaussianity, such as the LiNGAM family.
Note that when a variable also carries a sentinel code or a boundary atom, a non-Gaussianity
finding on it usually describes the point mass rather than the measured quantity.

### Row structure

**SERIAL_DEPENDENCE** — a continuous variable is autocorrelated across consecutive rows, so the
rows are not exchangeable as given and tests assuming i.i.d. rows may be anticonservative. The
check is one-sided with respect to row order: a flag means the rows are dependent *in the order
given*, but no flag does not rule out dependence under some other ordering, for instance if a time
series was shuffled before it was saved. If the file concatenates blocks, set the grouping variable
and recompute before concluding anything.

**GROUP_CONSTANT_VARIABLE** — a variable is constant within every level of the grouping variable,
as a subject-level attribute would be in a repeated-measures file. Its effective sample size for
correlational purposes is the number of groups, not the number of rows, and with few groups such
variables are often exactly collinear with one another by accident.

### Variable names

**RESERVED_VARIABLE_NAME** — a name collides with a convention Tetrad's own machinery reads. The
cases are: `base:k` with integer `k`, which the time-series machinery reads as `base` lagged `k`
steps, reported as INFO since the data may genuinely be lagged; a name with a colon whose suffix
does not parse as a lag; a name beginning with `E_`, the prefix under which SEM graphs generate
error-term nodes; and a name containing `*` or `,`, which knowledge specifications read as a
wildcard and a list separator. Rename unless you meant the convention.

### Findings specific to a supplied covariance matrix

These are emitted when the audit is run on a covariance matrix rather than on rows.

**COVARIANCE_NOT_SYMMETRIC** — an entry differs from its transpose by more than a small fraction of
the largest entry. A covariance matrix is symmetric by definition, so this indicates a transcription
or assembly error. The remaining checks are run on the symmetrized matrix.

**NONPOSITIVE_VARIANCE** — a diagonal entry is zero or negative. A zero variance is the
covariance-matrix analog of a constant column; a negative one is not a variance at all and marks
the input as invalid. Such variables are excluded from the correlation-derived checks.

**COVARIANCE_NOT_PSD** — the matrix has a negative eigenvalue, so it is not the covariance matrix
of any dataset. This arises from entrywise assembly across different row subsets, from transcription
or rounding, or from procedures that do not guarantee positive semidefiniteness. Likelihoods,
partial correlations and regression coefficients can fail or behave incoherently.

**EXTREME_VARIANCE_SCALE** — the ratio of largest to smallest positive variance is extreme, usually
unstandardized variables in very different units. It degrades the conditioning of decompositions
and inversions even when the implied correlations are unremarkable.

**SAMPLE_SIZE_FORCES_SINGULARITY** — the stated sample size `n` satisfies `n - 1 < p`, so any
ordinary sample covariance matrix from `n` rows is singular by arithmetic. The message states which
case holds: if the supplied matrix's rank is at most `n - 1` it is consistent with that arithmetic,
and joint linear-dependence findings cannot be attributed to particular variables; if its rank
exceeds `n - 1`, it cannot be an ordinary sample covariance matrix at the stated `n`, so either the
sample size is misstated or the matrix was regularized, shrunk, or model-implied.

## General limits

Collecting the caveats above in one place, because they matter:

- Several checks are heuristics on the shape of an observed distribution. They cannot read a
  codebook and take no position on provenance.
- The determinism searches are bounded in set size, in determiner granularity and in work budget.
  Absence of a finding does not rule out determinism outside those bounds.
- The serial-dependence check is one-sided with respect to the row order as given.
- New finding codes may be added in later releases, so a report you automate against should
  tolerate codes it does not know.

## Related pages

- [Data Preparation](index.md) — where the audit fits in the wider preparation stage.
- [Parameters](../../parameter.definitions.md) — the thresholds the audit's checks use are
  parameters like any others.
