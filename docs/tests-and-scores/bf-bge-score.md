# BF-BGe (Basis Function BGe)

**Command:** `bf-bge-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: bf-bge-score -->

BF-BGe is the BGe score applied to the same embedding BF-BIC uses: each continuous variable is expanded into its Legendre basis columns up to truncationLimit and each discrete variable into one indicator column per category but the last. Where BF-BIC scores the expanded family with a BIC-penalized Gaussian likelihood, BF-BGe scores it with the exact Normal-Wishart marginal likelihood of the BGe score (see), taking the family score to be log p(D\_\{A,B\}) - log p(D\_B) over the embedded column sets A of the child and B of its parents. This replaces the BIC penalty on the whole expanded block (the source of BF-BIC's conservatism on weak linear edges) with the Bayesian Occam factor, in the same way that BDeu replaces the discrete BIC penalty. The score is decomposable and score-equivalent, and because the prior scale is added to the scatter matrix, no singularity lambda is needed. "Higher is better."

The prior conventions and hyperparameters are those of the BGe score; alpha\_mu acts only through the prior scale, so smaller values make edges more expensive (bgeAlphaMu = 0.1 tracks SEM BIC at penalty discount 2 in null false-positive rate; the default 1 sits between penalty discounts 1 and 2). Embedded columns with zero variance (unobserved categories) are dropped. Mixed data. Experimental.

With discreteInteractionOrder above 1, a family's parent block is augmented with products of indicator columns from up to that many distinct discrete parents, so that a discrete child can depend on its discrete parents through interactions and not only main effects; an order at least the number of discrete parents gives the saturated design, the same span as BDeu's conditional table, with empty-cell columns dropped. This is not score-equivalent (Markov-equivalent DAGs may score differently), so use it with BOSS or GRaSP; the default order 1 is the score-equivalent additive design.

<!-- END GENERATED: bf-bge-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
