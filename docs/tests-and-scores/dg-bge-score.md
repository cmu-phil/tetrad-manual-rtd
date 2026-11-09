# DG-BGe (Degenerate Gaussian BGe Score)

**Command:** `dg-bge-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: dg-bge-score -->

DG-BGe is the BGe score (see) applied to the degenerate Gaussian embedding of the DG-BIC score: continuous variables are kept as they are and each discrete variable is replaced by one 0/1 indicator column per category but the last, and the resulting columns are scored with the Normal-Wishart marginal likelihood, taking the family score to be log p(D\_\{A,B\}) - log p(D\_B) over the embedded column sets of the child and its parents. On purely continuous data this is exactly the BGe score; on purely discrete data it is the marginal-likelihood counterpart of DG-BIC in the way that BDeu is the counterpart of the discrete BIC score, though, like DG-BIC, it models only additive (main-effect) dependence of a child's indicators on the parents' indicators, not interactions among parents. It is BF-BGe with truncation limit 1 and no rescaling; see that entry for the hyperparameters and for discreteInteractionOrder, which adds interaction columns among discrete parents (saturating the parent design at high enough order) at the cost of score equivalence. Decomposable, and score-equivalent at interaction order 1; "higher is better." Mixed data. Experimental.

<!-- END GENERATED: dg-bge-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
