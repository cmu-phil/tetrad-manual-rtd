# FLOP

**Command:** `flop`  
**Kind:** Algorithm

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: flop -->

FLOP (Fast Learning of Order and Parents) is a permutation search of the same family as BOSS and GRaSP, due to Wienobst, Henckel, and Weichwald (2026). Like BOSS it searches over topological orders, repeatedly removing each variable from the order and reinserting it at its best-scoring position until no reinsertion improves the total score. It differs from BOSS in three respects.

First, parent sets are chosen by a non-greedy grow-shrink procedure rather than a greedy one: the grow phase adds any variable that improves the local score, not necessarily the best such variable, and the shrink phase removes any parent whose removal improves it. Candidates are visited in random order, so repeated searches from the same order can settle on different DAGs of equal score. Second, when a variable enters or leaves a candidate prefix the parent set is updated by a warm start from the previous parent set, with early exits in the cases where the changed variable cannot affect the result. Third, the search is restarted by iterated local search rather than by independent random restarts: each restart perturbs the best order found so far by about ln(p) random transpositions, rather than drawing a fresh random order.

This implementation is specialized to the linear Gaussian BIC score and takes continuous data or a covariance matrix. It does not accept an arbitrary Score object, and knowledge is not currently supported. For searches needing either of those, use BOSS, which supports the same iterated local search through its useIlsRestarts parameter.

The parameters are as follows:

penaltyDiscount - The multiplier on the ln(N) \* \|parents\| BIC penalty term, written lambda in the paper. The default is 2, following Foygel and Drton (2010).

flopNumRestarts - The number of iterated local search restarts. Note that this differs in meaning from BOSS's numStarts: zero restarts gives one search, from the initial order described below, rather than no search. More restarts can never return a worse-scoring graph, so this parameter trades runtime against score.

seed - The random seed for the perturbations and for the grow-shrink candidate orderings, or -1 for a nondeterministic seed. Because the local search is randomized, results are reproducible only when this is set.

The initial order is constructed by a pivoted Cholesky decomposition of the correlation matrix, which places strongly correlated variables adjacently. The motivation is that grow-shrink parent selection can fail on far-apart ancestor-descendant pairs whose marginal dependence is too weak to detect at finite sample sizes, path graphs being the canonical hard case; an order that puts such pairs close together avoids asking grow-shrink to detect those dependencies. This order is available separately, for use with BOSS or GRaSP, as edu.cmu.tetrad.search.utils.FlopInitialOrder.

Wienobst, M., Henckel, L., & Weichwald, S. (2026). Embracing discrete search: a reasonable approach to causal structure learning.

Foygel, R., & Drton, M. (2010). Extended Bayesian information criteria for Gaussian graphical models. Advances in Neural Information Processing Systems, 23.

<!-- END GENERATED: flop -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
