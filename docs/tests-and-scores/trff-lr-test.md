# TRFF-LR-Test

**Command:** `trff-lr-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: trff-lr-test -->

A likelihood-ratio conditional independence test built on the TRFF BIC score's local model: each variable is regressed on its conditioning set using ridge regression over random Fourier features of the continuous conditioners plus indicator columns for discrete conditioners, with a Student-t error model for continuous targets and a multinomial logistic model for discrete targets. To test X \_\|\|\_ Y \| Z, a reduced model (Y given Z) and a full model (Y given Z plus X) are fit on a single shared design matrix in which the reduced model's columns are a prefix of the full model's columns - the full design appends a linear X column and a fresh block of random Fourier features over (Z, X), or the indicator columns of X when X is discrete - so the two models are nested by construction and the likelihood-ratio statistic is nonnegative. Explicit linear columns for the continuous conditioners are included in both designs so that linear conditional means are represented exactly and the random features carry only the nonlinear remainder.

The degrees of freedom are approximated by the difference in ridge effective degrees of freedom. For a discrete target the deviance is referred to a chi-square with those degrees of freedom. For a continuous target the error scale is profiled per model, and the chi-square reference fails when the added block is not small relative to n; the statistic is therefore converted to the classical F form and referred to an F distribution, which agrees with the chi-square when the added block is small and remains calibrated when it is not. The test is symmetrized: both directions (target Y, adding X; and target X, adding Y) are computed and the more conservative p-value is reported, so results do not depend on argument order. The reference distributions are approximations rather than exact permutation or Wilks results, and the test should be considered experimental; with the default number of random features it is also computationally heavy inside a search. Mixed data.

<!-- END GENERATED: trff-lr-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
