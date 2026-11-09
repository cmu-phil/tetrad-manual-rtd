# Stratified Rank (Domain-Pooled)

**Command:** `stratified-rank-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: stratified-rank-test -->

A conditional independence test for data gathered in several domains - batches, sites, cohorts, semesters, countries - whose causal structure is shared but whose linear coefficients, means, and noise variances may differ by domain. The hypothesis X \_\|\|\_ Y \| Z is judged by the vanishing of the partial cross-covariance of X and Y given Z within each domain: the Bartlett canonical-correlation statistic is computed inside each domain separately and the statistics and degrees of freedom are summed across domains, which is valid because the domains are disjoint samples. This is the Phase 1 test of LCD-NOD (Dong, Dai, Ng, Spirtes, and Zhang, Identifying Partially Observed Causal Models from Heterogeneous/Nonstationary Data, ICML 2026), whose Theorem 1 shows that the within-domain covariance constraints are exactly those of the homogeneous linear model with the same graph. The covariance of the domains mixed together carries no such guarantee: testing it both invents dependence that is an artifact of the mixing and can mask real dependence whose sign or strength varies by domain, which is why a search run on concatenated multi-site data so often returns a hairball.

To use it: include in the data set one column holding the domain index - a discrete column, or a continuous column whose values are all whole numbers - and load the data as usual. In a Search box, choose a constraint-based algorithm such as PC or FCI, select this test, and set the Domain column name parameter to that column's name; the default is a column named "domain", and if no column of the given name exists but the data set has exactly one discrete column, that column is used and a note is logged. The domain column is removed from the variable list and used only to split the rows, so it does not appear in the output graph; the remaining variables must be continuous. The same test can be selected in the Markov Checker to ask whether a fitted graph satisfies its implied independencies within domains.

Each domain must have enough rows for its own covariance matrix: domains too small for the statistic to discriminate are skipped, along with their degrees of freedom, and if no domain is usable the result is marked invalid. Many very small domains make the chi-square approximation rough even when they are not skipped, so merge small domains into larger ones first. The statistic is the Gaussian likelihood-ratio form and assumes linearity within each domain; with a single domain it reduces to the ordinary Wilks rank test. A tabular data set is required - a covariance matrix cannot be used, since the rows must be split by domain. Continuous data plus one discrete domain column.

<!-- END GENERATED: stratified-rank-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
