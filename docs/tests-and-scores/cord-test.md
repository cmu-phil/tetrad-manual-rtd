# CORD

**Command:** `cord-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: cord-test -->

CORD is an omnibus, nonparametric conditional independence test built on orthogonal rank scores of the full conditional distribution. Where covariance- and mean-based tests (Fisher Z, GCM) see only dependence in location, CORD keeps power against dependence in variance, tails, and co-volatility. The implementation is cross-fitted: the sample is partitioned into three folds, the three cyclic role-rotations of the partition are run, and the per-observation scores are pooled into a single studentized statistic, so the p-value is continuous and does not pile up at 1, which lets it be thresholded in a constraint-based search. Because CORD models the conditional distribution of one variable it is directional; by default both orientations are run and their p-values combined by the Cauchy (ACAT) rule of Liu and Xie (2020), which is order-invariant and valid under arbitrary dependence.

Requires the raw continuous sample rather than a covariance matrix; rows with missing values are dropped listwise. It is considerably slower than Fisher Z. Continuous data.

<!-- END GENERATED: cord-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
