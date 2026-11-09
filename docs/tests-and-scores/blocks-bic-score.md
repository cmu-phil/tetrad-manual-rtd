# Blocks-BIC

**Command:** `blocks-bic-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: blocks-bic-score -->

Blocks-BIC is a block-structured score for searches over latent variables that are each measured by a cluster of indicators, taking its blocks from a connected clustering result. For a candidate family Y \| Pa(Y), let the X block be the concatenation of the indicator columns of the parent blocks and the Y block the indicator columns of the target; the score evaluates reduced-rank models between these two blocks by regularized canonical correlation analysis. For canonical rank r, score(r) = fit(r) - c k(r) ln N - (m c) ln N (r - r\*)^2, where fit(r) is -N times the sum of log(1 - rho\_i^2) over the top r canonical correlations, k(r) = r(p + q - r) is the parameter count, r\* is the trek-implied rank (the sum of the ranks of the parent blocks), and m weights a soft regularizer encouraging agreement with that rank. The score of the family is the maximum over r. Supports an effective sample size.

This score is only offered when the search box is connected to a clustering result. Its companion test is Blocks-Test-TS. Mixed data.

<!-- END GENERATED: blocks-bic-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
