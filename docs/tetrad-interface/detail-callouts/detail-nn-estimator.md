# Detail: NN Estimator

The **NN Estimator** fits a nonparametric model to a DAG. For each variable it trains a small
neural network to model that variable given its parents, then runs the DAG forward in causal order
to generate synthetic rows, and compares those rows with the data. Nothing assumes a parametric
family: there is no linearity assumption, no Gaussian assumption and no conditional probability
table. Mixed continuous and discrete data is fine.

It is the answer to a question the other estimators cannot address: **does this DAG, fitted as
flexibly as the data allow, reproduce the joint distribution I actually have?** A DAG that cannot
be made to reproduce the data under a flexible mechanism is in trouble in a way that no choice of
linear coefficients will rescue.

## How it differs from the other estimators in this box

The Estimator box otherwise fits a **Parametric Model** and reports a parameter table. The NN
Estimator is different in both respects:

- Its inputs are a **Data** box and a **Graph** box. There is no Parametric Model in between, and
  you do not specify a functional form.
- Its output is a fitted mechanism plus a set of **diagnostics** — resimulated data, held-out fit
  per node, and per-edge strength — rather than coefficients you would report.

Root variables are not modelled at all; they are resampled from their observed values.

## The tabs

Select **NN Estimator** in an Estimator box with a Data and a Graph parent. The editor has six
tabs.

- **Observed vs. Resimulated** — the one to look at first. Your data on the left, a resimulation
  from the fitted model on the right, drawn identically, as a matrix of histograms and scatter
  plots over whichever variables you choose. If the model has captured the joint distribution the
  two sides should look alike. A pair clearly curved on the left and straight on the right means
  the mechanism under-fit that relationship; structure on the left and a cloud on the right means
  the DAG does not connect those variables closely enough to reproduce their dependence.
- **Cross-Validation** — honest out-of-sample fit. Rows are split into blocks, each held out in
  turn against a model trained on the rest. Continuous variables report held-out R², discrete ones
  the improvement in held-out cross-entropy over predicting the marginal frequencies; zero means
  the parents added nothing, and negative means they hurt. Root variables are omitted. A line above
  the table reports how well the whole factorization generalizes.
- **Edge Strength** — for one edge at a time, how much the child's mechanism actually uses that
  parent. The interventional measures replace the parent's input with an independent draw from its
  own distribution, everything else held fixed, and compare the two sets of draws; this is the
  arrow-strength idea of Janzing and colleagues as DoWhy implements it. Partial strength is a
  different question — how much held-out fit the parent adds — measured on the same folds as the
  Cross-Validation tab.
- **Graph** — the working DAG with its edges shaded by a statistic you pick from a dropdown:
  interventional MMD², partial strength, signed standardized marginal effect, or the
  cross-validation fit of the child. The last is a property of the child rather than of the edge,
  so it is shown on the edges coming into each node.
- **Prune** — **Propose Pruning** suggests edges to drop at a threshold you set, **Apply &
  Re-estimate** removes them and refits, and **Revert Prune** puts them back.
- **Explanation** — the full treatment of everything above, shipped with the version you are
  running. Read it before you rely on any of these numbers; it is more detailed than this page and
  always matches your build.

## Reading the numbers honestly

Five things are easy to get wrong, and all five are the difference between a diagnostic and a
decoration.

**Training fit is optimistic.** Until you run cross-validation, the footer's count of nodes that
beat their marginal baseline is measured on the training rows. Once cross-validation has run, the
held-out summary replaces it. Trust the held-out number.

**Watch the extrapolation fraction.** The footer reports the fraction of resimulated rows in which
some mechanism was asked to extrapolate — a simulated parent value far outside the range its
network was trained on. When that is more than a few percent, expect tails on the resimulated side
that your data never had. The network has no idea what to do out there, so a right-hand marginal
that is wider than the left, or reaches values the data never takes, usually means extrapolation
rather than a finding.

**Edge strengths have a noise floor.** The tab reports a null band: the child's mechanism is
retrained under new seeds and the same comparison made between the original and each refit, which
is how much the fitted conditional moves from training randomness alone. An edge that does not
clear that band is shown in **gray italics**. Those edges have not been shown to be weak — they
have not been shown to be anything. Also note that MMD² is the noisier of the measures, so when it
and the variance-based measure disagree about ranking, prefer the variance-based one.

**Folds are contiguous by default.** Cross-validation cuts blocks of rows in file order, which is
what you want for serially dependent data. But if your rows happen to be sorted by some variable,
each held-out block is a biased slice and the numbers come out pessimistic. Turn on the
shuffle-before-folding option in that case; the permutation is seeded, so it stays reproducible.

**Fitting is seeded, which cuts both ways.** By default the seed is fixed, so resimulating gives
the same answer and two NN Estimator boxes on the same data and DAG agree — which is what you want
when comparing DAGs. The cost is that repeated runs tell you nothing about how much a number moves
under a different fit. If a number matters, change the seed, or randomize it, and refit at least
once to see how far it travels.

## Settings

The network size, training length, learning rate, weight decay, seed, fold count, resimulation
size, and the number of parent configurations and repeats used by the edge-strength measures are
all set in the node's parameter dialog. Their defaults and ranges are listed on the
[Parameters](../../parameter.definitions.md) page along with every other Tetrad parameter.

The networks are deliberately small. They are meant to be flexible enough to reproduce the joint
distribution implied by the DAG, not to win a prediction contest.

## Related pages

- [Estimator Box](../box-by-box/estimator-box.md) — the box this estimator lives in.
- [Data Audit](../data-preparation/data-audit.md) — worth running first; extrapolation and
  near-determinism findings both bear on how to read these diagnostics.
