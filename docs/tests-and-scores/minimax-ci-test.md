# Minimax Conditional Independence Test

**Command:** `minimax-ci-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: minimax-ci-test -->

A stratified permutation test of X \_\|\|\_ Y \| Z. The conditioning set is discretized: each continuous Z variable is binned, and each combination of Z bins (and discrete Z values) forms a stratum. Within each stratum, X is permuted relative to Y to build a permutation null for a within-stratum association statistic (a correlation-based statistic for continuous pairs; a G-type statistic when X or Y is discrete), and the per-stratum permutation p-values are combined across strata by a conservative quantile ("soft minimax") aggregation. Because the permutation is carried out within strata, the test makes no distributional or functional-form assumptions about the dependence of X and Y on Z.

The permutation null is exact for X \_\|\|\_ Y \| bin(Z), not X \_\|\|\_ Y \| Z: residual variation of Z within a bin is a bin-geometry bias that does not shrink as n grows, so with a fixed number of bins the test's size degrades as n increases. By default the number of bins per continuous Z dimension therefore grows adaptively at the n^(2/5) rate of Neykov, Balakrishnan, and Wasserman (2021), capped so that expected stratum sizes stay workable (useAdaptiveZBins; set it false to control binsPerContZ manually). Intended scope: conditioning sets with at most about two continuous variables and n of roughly 1000 or more; residual size inflation of a few percentage points above nominal remains at smaller n, and power falls as strata multiply. Best used for spot checks of individual facts rather than as the test inside a search. Mixed data. See Neykov, M., Balakrishnan, S., & Wasserman, L. (2021). Minimax optimal conditional independence testing. The Annals of Statistics, 49(4), 2151-2177.

<!-- END GENERATED: minimax-ci-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
