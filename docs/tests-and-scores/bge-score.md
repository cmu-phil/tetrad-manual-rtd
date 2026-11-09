# BGe Score

**Command:** `bge-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: bge-score -->

BGe (Bayesian Gaussian equivalent) is the Gaussian analog of the BDeu score: the local score of a family Y \| Pa is the exact log marginal likelihood of the data for that family under a Normal-Wishart prior on the mean and precision of the linear Gaussian model, so no asymptotic penalty term is involved. It is score-equivalent and decomposable, and "higher is better." See Geiger, D., and Heckerman, D. (2002), Parameter priors for directed acyclic graphical models and the characterization of several probability distributions, Annals of Statistics 30(5), 1412-1440, and the corrected formula in Kuipers, J., Moffa, G., and Heckerman, D. (2014), Addendum on the scoring of Gaussian directed acyclic graphical models, Annals of Statistics 42(4), 1689-1691.

The prior has two hyperparameters: bgeAlphaMu, the prior precision on the mean (alpha\_mu), and bgeAlphaWOffset, the Wishart degrees of freedom above the number of variables p (alpha\_w = p + bgeAlphaWOffset). The prior mean is the sample mean and the prior scale matrix is T = t diag(s\_j^2), with t = alpha\_mu (alpha\_w - p - 1) / (alpha\_mu + 1) and s\_j^2 the sample variance of variable j; for unit-variance data this is the bnlearn/Kuipers default T = t I, and scaling to the sample variances makes the DAG ranking invariant to the units of measurement. The defaults alpha\_mu = 1, alpha\_w = p + 2 follow Kuipers et al. and bnlearn. As with BDeu's prior equivalent sample size, larger alpha\_mu tends to favor denser graphs. Supports an effective sample size. Continuous data or a covariance matrix.

<!-- END GENERATED: bge-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
