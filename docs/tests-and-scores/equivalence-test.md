# Equivalence (TOST)

**Command:** `equivalence-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: equivalence-test -->

Judges independence only on positive evidence that the partial correlation is negligible, by a two-one-sided-test (TOST) equivalence test on the Fisher z scale. An ordinary test answers "can I reject rho = 0?", and a constraint-based adjacency search deletes an edge when it cannot, which treats absence of evidence as evidence of absence. This test answers the question edge removal actually needs, "can I show \|rho\| is below a margin?", reporting independence just in case the (1 - 2\*alpha) confidence interval for the Fisher z of the partial correlation lies entirely inside (-z0, +z0), where z0 = atanh(equivalenceMargin).

The practical difference is which way the burden of proof falls, and it matters most for weak associations. An ordinary test's removal region, \|z\| \< c\*se, shrinks as the sample grows, so a weak but real edge is deleted most eagerly at the sample sizes where deleting it is least justified; and because a search tries many conditioning subsets per pair and removes the edge if any one of them fails to reject, each extra subset is another chance to delete a real adjacency. This test's removal region instead grows with the sample size toward \|rho\| \< margin, so nothing is deleted until the data can show it is negligible. On bivariate normal data at margin 0.10 and alpha 0.05, a true correlation of 0.05 was called independent 81% of the time by Fisher Z at n = 500 against 23% here, while at a true correlation of 0.10, the boundary of this test's null hypothesis, the rate stayed at alpha for every sample size tried.

Two cautions. The margin must exceed roughly 1.645/sqrt(n) at alpha = 0.05 or no pair is ever removable and the search returns a complete graph, which is why equivalenceMargin defaults to 0, meaning that the margin is scaled to the sample size; and asymptotically every pair whose partial correlation falls below the margin is removed, so the margin must sit below the weakest association worth keeping. Note also that this test's notion of independence is weaker than an ordinary test's notion of dependence, so an algorithm whose orientation rules ask whether two variables are dependent may be degraded by it; for CCD, prefer the algorithm's useEquivalenceRemoval parameter, which applies the equivalence rule to the adjacency phase alone and leaves orientation on the selected test. Continuous data or a covariance matrix.

<!-- END GENERATED: equivalence-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
