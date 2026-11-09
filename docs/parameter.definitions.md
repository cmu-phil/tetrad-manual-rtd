# Parameters

<!-- GENERATED FILE - DO NOT EDIT BY HAND.
     Produced by tools/gen_parameter_definitions.py from Tetrad's
     parameter.definitions.html, which is the file Tetrad itself reads at runtime.
     Regenerate with `make params`, then commit the result. -->

Every search parameter Tetrad documents, taken from the release this page was generated from. There are 529 of them. Parameter names are the names used in scripts and in the `Parameters` object, so they are also what you pass from py-tetrad.

**Jump to:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

## A

### acceptanceProportion

- **Short description:** Acceptance Proportion
- **Long description:** An edge occurring in this proportion of individual FASK graphs will appear in the final graph.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### adaptiveBasisSelection

- **Short description:** Yes if uninformative higher-order basis functions should be dropped by a BIC screen
- **Long description:** If Yes, each continuous variable's higher-order basis columns are screened once, on the full sample, and a column is kept only if its correlation with some other variable's embedded block crosses the single-regressor BIC threshold (with a multiplicity adjustment for the number of columns scanned). The linear term is always kept. With this screen, the effective truncation is chosen by the data, so raising the truncation limit past the data-supported order does not degrade the basis function score or test; results converge instead. The screen is marginal (pairwise), so basis directions relevant only conditionally may be dropped.
- **Value type:** Boolean
- **Default value:** true

### addOriginalDataset

- **Short description:** Yes, if adding the original dataset as another bootstrapping
- **Long description:** Select “Yes” here to include an extra run using the original dataset for improved accuracy.
- **Value type:** Boolean
- **Default value:** false

### adjustOrientations

- **Short description:** Yes, if the orientation adjustment step should be included
- **Long description:** Yes, if the orientation adjustment step should be included
- **Value type:** Boolean
- **Default value:** false

### allowBidirected

- **Short description:** Allow bidirected edges to show collider conflicts
- **Long description:** Allow bidirected edges to show collider conflicts
- **Value type:** Boolean
- **Default value:** false

### allowInternalRandomness

- **Short description:** Allow randomness inside algorithm
- **Long description:** This allows variables orders to be shuffled in certain sports to avoid local optima
- **Value type:** Boolean
- **Default value:** true

### alpha

- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** The cutoff, beyond which test results are judged as dependent, for a statistical test of independence. Default 0.01.
- **Value type:** Double
- **Default value:** 0.01
- **Minimum:** 0.0
- **Maximum:** 1.0

### alphaDefault0.05

- **Short description:** Cutoff for p values (alphaDefault0.05) (min = 0.0)
- **Long description:** The cutoff, beyond which test results are judged as dependent, for a statistical test of independence. Default 0.05.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### amBetaAlpha

- **Short description:** The 'alpha' shape parameter for the Beta noise terms.
- **Long description:** The 'alpha' shape parameter for the Beta noise terms.
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** Infinity

### amBetaBeta

- **Short description:** The 'beta' shape parameter for the Beta noise terms.
- **Long description:** The 'beta' shape parameter for the Beta noise terms.
- **Value type:** Double
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** Infinity

### amCoefHigh

- **Short description:** High end of coefficient range (min = 0.0)
- **Long description:** Value m2 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### amCoefLow

- **Short description:** Low end of coefficient range (min = 0.0)
- **Long description:** The parameter m1 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** Infinity

### amCoefSymmetric

- **Short description:** Yes if negative coefficient values should be considered
- **Long description:** Yes if coefficients should be drawn from +/-(a, b); No if from +(a, b).
- **Value type:** Boolean
- **Default value:** true

### amDerivativeMax

- **Short description:** 'Max' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Long description:** 'Max' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Value type:** Double
- **Default value:** 1
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amDerivativeMin

- **Short description:** 'Min' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Long description:** 'Min' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Value type:** Double
- **Default value:** -1
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amDistortionType

- **Short description:** Add distortion: 1 = Before noise (additive) or 2 = After noise (post-nonlinear)
- **Long description:** Add distortion: 1 = Before noise (additive) or 2 = After noise (post-nonlinear)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### amEnsureInvertibility

- **Short description:** Ensure that functions are invertible
- **Long description:** Ensure that functions are invertible
- **Value type:** Boolean
- **Default value:** false

### amFirstDerivMax

- **Short description:** 'Max' for the U(min, max) range for f'(0) for the causal function
- **Long description:** 'Max' for the U(min, max) range for f'(0) for the causal function
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amFirstDerivMin

- **Short description:** 'Min' for the U(min, max) range for f'(0) for the causal function
- **Long description:** 'Min' for the U(min, max) range for f'(0) for the causal function
- **Value type:** Double
- **Default value:** -1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amNumPostNonlinearFunctions

- **Short description:** The number of random post-nonlinear functions to choose from
- **Long description:** The number of random post-nonlinear functions to choose from
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

### amRescaleMax

- **Short description:** Variables will be rescaled to \[min, max\] for this max; if min = max no rescaling will be done
- **Long description:** Variables will be rescaled to \[min, max\] for this max; if min = max no rescaling will be done
- **Value type:** Double
- **Default value:** 1
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amRescaleMin

- **Short description:** Variables will be rescaled to \[min, max\] for this min; if min = max no rescaling will be done
- **Long description:** Variables will be rescaled to \[min, max\] for this min; if min = max no rescaling will be done
- **Value type:** Double
- **Default value:** 1
- **Minimum:** -Infinity
- **Maximum:** Infinity

### amTaylorSeriesDegree

- **Short description:** The maximum exponent for a Taylor series to use as a random post-nonlinear function
- **Long description:** The maximum exponent for a Taylor series to use as a random post-nonlinear function. The f(0) term is set to 0.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### anmNoiseKind

- **Short description:** Noise distribution family: 1 = Beta (skewed), 2 = Gaussian, 3 = Student-t (heavy-tailed)
- **Long description:** Selects the distribution of exogenous noise for the ANM simulator Options: 1 = Beta (skewed), 2 = Gaussian, 3 = Student-t (heavy-tailed).
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### anmNoiseStrength

- **Short description:** Controls variance/strength of noise in GAM simulator
- **Long description:** A slider in \[0,1\] that scales the standard deviation of the chosen noise distribution. Low values yield weak noise, high values yield stronger noise. For Student-t, this also interacts with degrees of freedom (heavier tails at higher strength).
- **Value type:** Double
- **Default value:** 0.4
- **Minimum:** 0.0
- **Maximum:** 10.0

### anmNonlinearity

- **Short description:** Controls strength of nonlinearity in GAM simulator
- **Long description:** A slider in \[0,1\] that simultaneously controls the number of basis units per edge and their amplitude. Low values produce nearly linear functions, high values produce strongly nonlinear functions.
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0.0
- **Maximum:** 10.0

### anmPreset

- **Short description:** Preset function family: 1 = Smooth RBF, 2 = Wavy RBF, 3 = Tanh, 4 = Polynomial
- **Long description:** Selects the base family of nonlinear functions used on each edge for the ANM simulator. Options: 1 = Smooth RBF (gentle), 2 = Wavy RBF (richer), 3 = Tanh (sigmoidal), 4 = Polynomial (low-degree).
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 4

### applyR1

- **Short description:** Yes if the orient away from arrow rule should be applied
- **Long description:** Set this parameter to “No” if a chain of directed edges pointing in the same direction when only the first few such orientations are justified based on the data.
- **Value type:** Boolean
- **Default value:** false

### avgDegree

- **Short description:** Average degree of graph (min = 0)
- **Long description:** The average degree of a graph is equal to 2E / V, where E is the number of edges in the graph and V the number of variables (vertices) in the graph, since each edge has two endpoints.
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 2147483647

## B

### basisRankTransform

- **Short description:** Rank-transform continuous variables to \[-1, 1\] before the basis-function embedding
- **Long description:** If true, each continuous variable is replaced by its mid-ranks mapped to a uniform grid on \[-1, 1\] before the Legendre expansion, so the basis is exactly orthogonal under the empirical measure and every row has the same leverage. The default min-max scaling concentrates the higher-order basis columns on the few most extreme rows; the resulting likelihood-ratio statistic has a power-law null tail, so a handful of high-leverage rows can produce a spurious nonlinear edge at any penalty discount. With the rank transform the null is chi-square on its nominal degrees of freedom, a chi-square calibration of the penalty discount (Data Editor, Tools, Alpha/Penalty Discount Calculator) is exact, and the score is invariant to monotone transformations of the marginals. The cost is that the score models the copula rather than the joint distribution with its marginals (about 6 percent of the likelihood-ratio statistic on Gaussian data, with a gain on skewed data).
- **Value type:** Boolean
- **Default value:** false

### basisScale

- **Short description:** Variables are scaled to \[-b, b\] for this b (0 = standardized)
- **Long description:** Variables are scaled to \[-b, b\] for this b (0 = standardized)
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 500000

### basisType

- **Short description:** Basis type (0 = Polynomial, 1 = Legendre, 2 = Hermite, 3=Chebyshev)
- **Long description:** Basis type (0 = Polynomial, 1 = Legendre, 2 = Hermite, 3=Chebyshev)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 3

### betaHigh

- **Short description:** Upper end of the range for the sine coefficient
- **Long description:** Upper end of the uniform range from which the coefficient on the sine term of each structural equation is drawn in the Linear Sine simulation. See betaLow.
- **Value type:** Double
- **Default value:** 3.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### betaLow

- **Short description:** Lower end of the range for the sine coefficient
- **Long description:** Lower end of the uniform range from which the coefficient on the sine term of each structural equation is drawn in the Linear Sine simulation. Together with betaHigh this fixes the amplitude of the nonlinear component.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### bgeAlphaMu

- **Short description:** BGe prior precision on the mean (alpha\_mu)
- **Long description:** The prior precision on the mean in the Normal-Wishart prior of the BGe score (bnlearn's iss.mu). Acts like a prior equivalent sample size for the mean; larger values tend to favor denser graphs. Default 1.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 1.0E-4
- **Maximum:** 1.7976931348623157E308

### bgeAlphaWOffset

- **Short description:** BGe Wishart degrees of freedom above the number of variables (alpha\_w = p + offset)
- **Long description:** The degrees of freedom of the Wishart prior in the BGe score, given as an offset above the number of variables p, so alpha\_w = p + bgeAlphaWOffset. Must exceed 1 so that the prior scale t = alpha\_mu (alpha\_w - p - 1) / (alpha\_mu + 1) is positive. The default 2 gives alpha\_w = p + alpha\_mu + 1 for the default alpha\_mu = 1, as recommended by Kuipers et al. (2014) and used by bnlearn.
- **Value type:** Double
- **Default value:** 2.0
- **Minimum:** 1.01
- **Maximum:** 1.7976931348623157E308

### binsPerContXY

- **Short description:** Bins per continuous X/Y variable
- **Long description:** Number of quantile bins used to discretize continuous X and Y variables within each conditioning stratum. Larger values increase sensitivity to nonlinear dependence but require more data per stratum.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 20

### binsPerContZ

- **Short description:** Bins per continuous Z variable (fixed mode)
- **Long description:** Number of quantile bins used to discretize continuous conditioning (Z) variables when forming strata. Used only when adaptive Z binning (useAdaptiveZBins) is disabled. Note that with a fixed bin count the level of a stratified permutation test degrades as the sample size grows: within-bin residual dependence under the conditional-independence null is a fixed bias determined by the bin width, while the permutation reference tightens with n. The bin count must therefore grow with n (roughly n^(2/5)); prefer adaptive binning except in controlled experiments.
- **Value type:** Integer
- **Default value:** 16
- **Minimum:** 2
- **Maximum:** 200

### bootstrappingNumThreads

- **Short description:** The number of threads (\>= 1) to use for the bootstrapping
- **Long description:** This is the number of threads for the bootstrapping itself. The number of threads that each algorithm uses is set by the individual algorithm.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

### bossAlg

- **Short description:** Picks the BOSS algorithm type, BOSS1 or BOSS2
- **Long description:** 1 = BOSS1, 2 = BOSS2, 3 = BOSS3
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### bwMaxRows

- **Short description:** Max rows used to estimate median bandwidth (subsample for speed).
- **Long description:** Max rows used to estimate median bandwidth (subsample for speed).
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 1
- **Maximum:** 2000000

## C

### cacheScores

- **Short description:** Yes score results should be cached, no if not
- **Long description:** Caching scores can use a lot of memory.
- **Value type:** Boolean
- **Default value:** true

### calculateEuclidean

- **Short description:** Yes if the Euclidean norm squared should be calculated (slow), No if not
- **Long description:** The generalized information criterion is defined with an information term that take a Euclidean norm squares; there can be calculated directly.
- **Value type:** Boolean
- **Default value:** false

### catRho

- **Short description:** Categorical kernel similarity (rho, range 0-1)
- **Long description:** 0 = categories fully distinct; values closer to 1 make categories more similar
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0
- **Maximum:** 1

### cciScoreAlpha

- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.01
- **Minimum:** 0.0
- **Maximum:** 1.0

### cdnodColliderStyle

- **Short description:** Collider orientation rule: 1 = sepsets, 2 = conservative, 3 = max-p
- **Long description:** Selects how colliders are oriented in CD-NOD. 1 uses the sepset found during adjacency search, which is fastest but inherits any error in that sepset. 2 (conservative) orients a collider only when every sepset for the pair agrees, marking the triple ambiguous otherwise, so it trades orientations for reliability. 3 (max-p) picks the sepset with the largest p-value for the conditional independence, which is usually more accurate than 1 and less timid than 2. Any other value falls back to 1.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### cdnodContextMargin

- **Short description:** Score margin a context variable must clear to be retained as a parent
- **Long description:** The improvement in score that adding a context variable as a parent must exceed before that context variable is kept. Larger values make the algorithm more conservative about attributing a variable's behavior to the context (regime, environment, or dataset index) rather than to the system variables.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

### cdnodExcludeContextsFromS

- **Short description:** Bar context variables from appearing in separating sets
- **Long description:** If true, context variables are never included in the separating sets used for collider orientation. This is appropriate when the context variable is understood as an exogenous regime indicator that should explain differences in mechanism rather than screen off system variables from one another. If false, context variables compete for inclusion in sepsets on the same footing as system variables.
- **Value type:** Boolean
- **Default value:** false

### cdnodGreedyContexts

- **Short description:** Add context parents greedily rather than exhaustively
- **Long description:** If true, context variables are added as parents one at a time in order of score improvement, stopping when no remaining context variable clears the margin. If false, context subsets are considered together, which is more thorough but combinatorially more expensive.
- **Value type:** Boolean
- **Default value:** true

### cdnodMaxContextsPerNode

- **Short description:** Maximum number of context variables attached to any one node
- **Long description:** A cap on how many context variables may be retained as parents of a single node. Keeping this at 1 reflects the common assumption that a node's mechanism changes with at most one regime indicator; raising it allows a node to depend on several context variables at once, at the cost of more parameters and a greater risk of spurious context attachments.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

### cdnodMaxPMargin

- **Short description:** Margin by which the best sepset must win under the max-p rule
- **Long description:** Under the max-p collider rule, the p-value of the winning sepset must exceed that of the best competing sepset by at least this margin before the collider is oriented. The default of 0.0 orients whenever there is any advantage at all. Raising it suppresses orientations that rest on a near-tie between competing sepsets, which is a common source of unstable orientations near the significance boundary. Has no effect unless cdnodColliderStyle is 3.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### cdnodScoreContexts

- **Short description:** Score context variables as candidate parents
- **Long description:** If true, context variables participate in scoring as candidate parents of system variables, which is what allows CD-NOD to detect that a mechanism differs across regimes. If false, context variables are carried along but never scored, and the search reduces to the corresponding non-context algorithm.
- **Value type:** Boolean
- **Default value:** true

### cellTableType

- **Short description:** The type of cell table to use (optimization), 1 = AD Tree, 2 = Count Sample
- **Long description:** This is just whether table counts are to be calculated using one method or another, for optimization. The AD tree option uses AD trees to do the calculation; the Count Samples option simply counts the samples for each independence question and builds a table that way.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### cgExact

- **Short description:** Yes if the exact algorithm should be used for continuous parents and discrete children
- **Long description:** For the conditional Gaussian likelihood, if the exact algorithm is desired for discrete children and continuous parents, set this parameter to “Yes”.
- **Value type:** Boolean
- **Default value:** false

### checkAdjacencySepsets

- **Short description:** Yes if adjacency sepsets should be checked after all recursive sepsets check (default=No)
- **Long description:** Yes if adjacency sepsets should be checked after all recursive sepsets check (default=No). This is needed for FCIT to pass an Oracle test but may reduce accuracy.
- **Value type:** Boolean
- **Default value:** false

### checkType

- **Short description:** Model significance check type: 1 = Significance, 2 = Clique, 3 = None
- **Long description:** Model significance check type: 1 = Significance, 2 = Clique, 3 = None
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### clusterSizes

- **Short description:** Cluster sizes to check (comma separated, each \>= 2, default = "2")
- **Long description:** Cluster sizes to check (comma separated, each \>= 2, default = "2")
- **Value type:** String

### coefHigh

- **Short description:** High end of coefficient range (min = 0.0)
- **Long description:** Value m2 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### coefLow

- **Short description:** Low end of coefficient range (min = 0.0)
- **Long description:** The parameter m1 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### coefSymmetric

- **Short description:** Yes if negative coefficient values should be considered
- **Long description:** Yes if coefficients should be drawn from +/-(a, b); No if from +(a, b).
- **Value type:** Boolean
- **Default value:** true

### colliderDiscoveryRule

- **Short description:** Collider discovery: 1 = Lookup from adjacency sepsets, 2 = Conservative (CPC), 3 = Max-P
- **Long description:** One may look them up from sepsets, as in the original PC, or estimate them conservatively, as from the Conservative PC algorithm, or by choosing the sepsets with the maximum p-value, as in PC-Max.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### colliderOrientationStyle

- **Short description:** Collider Orientation Style: 1 = Sepsets 2 = Conservative 3 = Max-P
- **Long description:** Collider Orientation Style: 1 = Sepsets 2 = Conservative 3 = Max-P
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### completeRuleSetUsed

- **Short description:** Yes if the complete FCI rule set should be used
- **Long description:** No if the (simpler) final orientation rules set due to P. Spirtes, guaranteeing arrow completeness, should be used; yes if the (fuller) set due to J. Zhang, should be used guaranteeing additional tail completeness.
- **Value type:** Boolean
- **Default value:** true

### concurrentFAS

- **Short description:** Yes if a concurrent FAS should be done
- **Long description:** Yes if the version of the PC adjacency search that uses concurrent processing should be used, no if not.
- **Value type:** Boolean
- **Default value:** false

### conditioningThreshold

- **Short description:** Matrix conditioning values above which Eigenvalue whitening is used. Default 1e-10.
- **Long description:** Matrix conditioning values above which Eigenvalue whitening is used. For smaller tresholds, the faster Cholesky whitening is used. Default 1e-10, \< 0 forces Eigenvalue whitening.
- **Value type:** Double
- **Default value:** 1e-10
- **Minimum:** -Infinity
- **Maximum:** Infinity

### conflictRule

- **Short description:** Collider conflicts: 1 = Prioritize existing colliders, 2 = Orient bidirected, 3 = Overwrite existing colliders
- **Long description:** 1 if the “overwrite” rule as introduced in the PCALG R package, 2 if all collider conflicts using bidirected edges, or 3 if existing colliders should be prioritized, ignoring subsequent conflicting information.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### connected

- **Short description:** Yes if graph should be connected
- **Long description:** Yes if a random graph should be generated in which paths exists from every node to every other, no if not.
- **Value type:** Boolean
- **Default value:** false

### convergenceThreshold

- **Short description:** Convergence tolerance for the factor analysis iteration
- **Long description:** The factor extraction iterates until successive estimates of a loading differ by less than this amount. Smaller values give a more precisely converged solution at the cost of more iterations. Note that this is a convergence tolerance, not a loading cutoff; the cutoff used for drawing edges is fa\_threshold.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** Infinity

### cordEngine

- **Short description:** Cord Engine: 1, 2, 3,...
- **Long description:** Cord Engine: 1, 2, 3...
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 10

### cordLearningRate

- **Short description:** Shrinkage (learning rate) applied to each gradient-boosting round
- **Long description:** The step-size shrinkage multiplying each boosting round's contribution to the conditional-CDF regression. Smaller values regularize more strongly and usually need more rounds (see number of estimators); typical values lie in (0, 1\].
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.0

### cordMaxLeafNodes

- **Short description:** Maximum number of leaf nodes per boosted tree
- **Long description:** Controls the complexity (effective interaction depth) of each tree in the boosting ensemble. Larger values permit more flexible conditional-distribution fits at higher risk of overfitting and greater cost.
- **Value type:** Integer
- **Default value:** 31
- **Minimum:** 2
- **Maximum:** 2147483647

### cordNumEstimators

- **Short description:** Number of gradient-boosting rounds (trees) per conditional-CDF regression
- **Long description:** Each threshold-indicator regression is fit by a histogram gradient-boosted tree ensemble with this many boosting rounds. More rounds sharpen the conditional-distribution estimate up to a point, at higher runtime; smaller learning rates generally require more rounds.
- **Value type:** Integer
- **Default value:** 300
- **Minimum:** 1
- **Maximum:** 2147483647

### cordNumThresholds

- **Short description:** Number of response quantile thresholds K used to estimate the conditional CDF
- **Long description:** The conditional distribution P(Y ≤ t \| X) is estimated at K threshold levels placed at quantiles of the response, and the omnibus statistic aggregates the resulting rank scores across those levels. Larger K resolves finer distributional (higher-moment and tail) structure at proportionally greater computational cost.
- **Value type:** Integer
- **Default value:** 9
- **Minimum:** 2
- **Maximum:** 2147483647

### cordSeed

- **Short description:** Base seed for the test's deterministic pseudorandom draws (-1 = random)
- **Long description:** CORD mixes this base seed with a canonical encoding of the (x, y, Z) fact so that repeated and orientation-swapped calls agree; changing it reshuffles the cross-fitting and boosting randomness. Determinism is always in effect (there is no "off" value).
- **Value type:** Long
- **Default value:** 50
- **Minimum:** 0
- **Maximum:** 9223372036854775807

### cordSymmetric

- **Short description:** Yes, if both orientations of Y \_\|\|\_ Z \| X are tested and combined; No for a single orientation
- **Long description:** CORD is asymmetric: testing Y \_\|\|\_ Z \| X is not identical to testing Z \_\|\|\_ Y \| X. When Yes, both orientations are evaluated and combined by Bonferroni as p = min(1, 2 \* min(p\_xy, p\_yx)); when No, the exact single-orientation statistic is reported. Symmetric mode roughly doubles the cost.
- **Value type:** Boolean
- **Default value:** false

### correlationThreshold

- **Short description:** Correlation Threshold
- **Long description:** The algorithm will complain if correlations are found that are greater than this in absolute value.
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 1

### covHigh

- **Short description:** High end of covariance range (min = 0.0)
- **Long description:** The parameter c2 for range +/-U(c1, c2) for covariance values, c1 \>= 0.0
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### covLow

- **Short description:** Low end of covariance range (min = 0.0)
- **Long description:** The parameter c1 for range +/-U(c1, c2) for covariance values, c2 \>= c1
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### covSymmetric

- **Short description:** Yes if negative covariance values should be considered
- **Long description:** Usually covariance values are chosen from +/-U(a, b) for some a, b, no if from +U(a, b).
- **Value type:** Boolean
- **Default value:** true

### cpdag

- **Short description:** True if a CPDAG should be returned, false if a DAG
- **Long description:** The algorithm returns a DAG; if this is set to True, this DAG is converted to a CPDAG
- **Value type:** Boolean
- **Default value:** true

### cstarCpdagAlgorithm

- **Short description:** Algorithm: 1 = PC Stable, 2 = FGES, 3 = BOSS, 4 = Restricted BOSS
- **Long description:** The CPDAG algorithm to use: 1 = PC Stable, 2 = FGES, 3 = BOSS, 4 = Restricted BOSS
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 1
- **Maximum:** 4

### customNoiseExpression

- **Short description:** Exogenous noise distribution, e.g. Exp(1), Gumbel(0, 1), U(0, 1)
- **Long description:** The distribution expression each exogenous noise term is drawn from, independently per variable and record, when custom (non-Gaussian) noise is in effect. In the Linear Non-Gaussian SEM simulation this expression is always used; the noise scale comes from the expression itself, so the Gaussian error variance bounds do not apply, and correlated errors are ignored.
- **Value type:** String
- **Default value:** Exp(1)

### customNoiseOption

- **Short description:** Exogenous Noises: 1 = Use standard Linear Gaussian noises, 2 = Use custom noise distribution
- **Long description:** If 2, the custom exogenous noise distribution expression will be used. The Linear Gaussian SEM and Linear Non-Gaussian SEM simulations set this themselves and do not list it.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### cutoffConstrainSearch

- **Short description:** Constraint-independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### cutoffDataSearch

- **Short description:** Independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### cutoffIndTest

- **Short description:** Independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### cyclicCoefHigh

- **Short description:** Cyclic: High end of coefficient range for coefficients in cycles
- **Long description:** Cyclic: Higb end of coefficient range for coefficients in cycles
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### cyclicCoefLow

- **Short description:** Cyclic: Low end of coefficient range for coefficients in cycles
- **Long description:** Cyclic: Low end of coefficient range for coefficients in cycles
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### cyclicCoefStyle

- **Short description:** Cyclic: 0 = Auto 1 = Fix Radius 2 = Cap Products, 3 = None,
- **Long description:** Cyclic: 0 = Choose for Me 1 = Scale SCCs to cyclic radius 2 = Cap cyclic products in SCCs, 3 = Regular SEM initialization
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 3

### cyclicMaxProd

- **Short description:** Cyclic: Upper bound on product of coefficients around feedback loops.
- **Long description:** Cyclic: Upper bound on product of coefficients around feedback loops.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### cyclicRadius

- **Short description:** Cyclic: Target spectral radius used to stabilize cyclic feedback.
- **Long description:** Cyclic: Target spectral radius used to stabilize cyclic feedback.
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0
- **Maximum:** 1

## D

### daoErrorDistribution

- **Short description:** Error distribution: 1 = Gaussian, 2 = Exponential, 3 = Gumbel, 4 = Laplace, 5 = Uniform
- **Long description:** The distribution family the exogenous errors are drawn from, following the reference DaO implementation. Each family is scaled so that the error variance equals the variance the DaO method calibrated for that variable, so the standardized correlation structure of the data is preserved whichever family is chosen. As in the reference implementation, the Exponential and Gumbel errors are not centered, so variable means shift under those choices; the Gaussian, Laplace, and Uniform errors have mean zero.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

### daoRandomizeOrder

- **Short description:** Yes, if randomly permuting the variable order after graph generation
- **Long description:** Select "Yes" to randomly shuffle the node ordering of the DAG after generation and any scale-free rewiring. This ensures that the topological order of variables is not reflected in their column order in the output dataset, preventing algorithms from exploiting ordering artifacts.
- **Value type:** Boolean
- **Default value:** true

### daoSfIn

- **Short description:** Yes, if rewiring the DAG to have a scale-free in-degree distribution
- **Long description:** Select "Yes" to rewire the generated DAG using preferential attachment so that the in-degree distribution follows a power law, as described in Andrews & Kummerfeld (2024). This produces hub-like sink nodes with many parents.
- **Value type:** Boolean
- **Default value:** false

### daoSfOut

- **Short description:** Yes, if rewiring the DAG to have a scale-free out-degree distribution
- **Long description:** Select "Yes" to rewire the generated DAG using preferential attachment so that the out-degree distribution follows a power law, as described in Andrews & Kummerfeld (2024). This produces hub-like source nodes with many children.
- **Value type:** Boolean
- **Default value:** false

### dataType

- **Short description:** "continuous" or "discrete"
- **Long description:** For a mixed data type simulation, if this is set to “continuous” or “discrete”, all variables are taken to be of that sort. This is used as a double-check to make sure the percent discrete is set appropriately.
- **Value type:** String
- **Default value:** categorical

### deCoupling

- **Short description:** Probability that a factor is protocol-coupled to an earlier factor (min = 0.0, max = 1.0)
- **Long description:** With this probability, a design factor's value range is scaled by a randomly chosen earlier uncoupled factor (a non-factorial design, as when larger chord lengths are tested only at smaller attack angles). Coupling produces strong protocol-induced dependence among the inputs and appears as a directed edge in the true graph.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### deDerivedNoise

- **Short description:** Noise standard deviation for derived variables (min = 0.0)
- **Long description:** The standard deviation of the noise added to each derived variable's unit-variance systematic part. Small values make derived variables near-deterministic functions of their parents, the classic hard case for score-based orientation.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### dedupByCpdag

- **Short description:** Yes if models are de-duplicated by CPDAG rather than by permutation
- **Long description:** When Yes, permutations in the same Markov equivalence class (same CPDAG, same score) are counted once.
- **Value type:** Boolean
- **Default value:** true

### deEmitConfigColumn

- **Short description:** Append a discrete CONFIG column naming each row's configuration block (requires deSortByConfiguration)
- **Long description:** If set together with deSortByConfiguration, a discrete bookkeeping column named CONFIG is appended to the dataset, giving each row's configuration block - the analogue of the TOWN column in the corrected Boston Housing data. Its purpose is to let the block structure be named in grouped analyses; in particular, selecting it as the data audit's serial grouping variable recomputes the serial dependence check with per-block centering, which separates block structure from genuine time-series structure. The column is bookkeeping, not a variable of the system: it should be excluded from causal searches, and since it has one category per block it will trip the many-discrete-levels audit finding if treated as an ordinary variable. Has no effect when deSortByConfiguration is off.
- **Value type:** Boolean
- **Default value:** false

### deInteraction

- **Short description:** Pairwise-interaction mixing weight for derived and response functions (min = 0.0, max = 1.0)
- **Long description:** The weight of the pairwise-interaction part (products of the mapped parents) relative to the additive part in derived and response functions. High values mimic interaction-heavy physics such as Strouhal scaling, which violates the additivity assumed by per-parent basis expansions.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### deMaxLevels

- **Short description:** Maximum number of levels per design factor (min = 2)
- **Long description:** Each design factor's number of grid levels is drawn uniformly between deMinLevels and deMaxLevels.
- **Value type:** Integer
- **Default value:** 12
- **Minimum:** 2
- **Maximum:** 2147483647

### deMinLevels

- **Short description:** Minimum number of levels per design factor (min = 2)
- **Long description:** Each design factor's number of grid levels is drawn uniformly between deMinLevels and deMaxLevels.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 2147483647

### deNumDerived

- **Short description:** Number of near-deterministic derived intermediates (min = 0)
- **Long description:** The number of derived variables (D1, ...), each a near-deterministic smooth function of a random subset of the design factors (like a computed boundary-layer parameter), with noise standard deviation deDerivedNoise.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

### deNumFactors

- **Short description:** Number of grid-valued design factors (min = 2)
- **Long description:** In the Designed Experiment simulation, the number of exogenous design factors (F1, F2, ...). These take a small number of evenly spaced levels, sampled uniformly, mimicking factors SET by an experimenter rather than sampled from a distribution.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 2147483647

### deNumResponses

- **Short description:** Number of measured responses (min = 1)
- **Long description:** The number of response variables (R1, ...). Each is a function of all factors and derived variables, mixing additive and pairwise-interaction parts by weight deInteraction, plus noise with standard deviation deResponseNoise. Responses are the only genuinely 'measured' random variables in the design.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

### depth

- **Short description:** Depth (Maximum size of conditioning set, unlimited =-1)
- **Long description:** The depth of search for algorithms like the PC adjacency search, which is the maximum size of any conditioning set considered. In order to express that no limit should be imposed, use the value -1.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### deResponseNoise

- **Short description:** Noise standard deviation for response variables (min = 0.0)
- **Long description:** The standard deviation of the noise added to each response's unit-variance systematic part. The default 0.4 gives R-squared of about 0.85 given the inputs.
- **Value type:** Double
- **Default value:** 0.4
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### deSelection

- **Short description:** Fraction of rows dropped by selection on measurability (min = 0.0, max \< 1.0)
- **Long description:** If greater than 0, the lowest deSelection fraction of rows by (first response plus noise) is dropped before the dataset is returned, as when rows exist only where the response was above a noise floor. Selection induces dependence among the inputs in the observed sample that is NOT in the true (pre-selection) graph; extra input-input edges found by searches on selected data are expected and are part of what this simulation studies.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### deSortByConfiguration

- **Short description:** Emit rows grouped into configuration blocks, sweeping the first factor within each block
- **Long description:** If set, rows are emitted grouped into configuration blocks: the first factor is swept through its full level grid in ascending order within each block (like the frequency sweep in the Airfoil data), and the remaining factors are drawn once per block and held constant across the block. The data-generating structure is unchanged; only the row order and the repeated-measures grouping differ. The emitted file then shows strong serial dependence in file order that is BLOCK structure (repeated measures), not time-series structure: block-constant factors read as near-1 lag-1 autocorrelation, and the dependence collapses when autocorrelations are computed within groups (for example, via the data audit's serial grouping variable). These two readings of a serial dependence finding call for different remedies: clustering or configuration-level aggregation and blocks-by-configuration resampling here, versus lag modeling for genuine time series. Combined with deSelection, block lengths vary naturally, as the measurable frequency bands per configuration vary in Airfoil.
- **Value type:** Boolean
- **Default value:** false

### determinismThreshold

- **Short description:** Threshold for judging a regression of a variable onto its parents to be deterministic (min = 0.0)
- **Long description:** When regressing a child variable onto a set of parent variables, one way to test for determinism is to test how close to singular the data is; this gives a threshold for this. The default value is 0.1.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

### differentGraphs

- **Short description:** Yes if a different graph should be used for each run
- **Long description:** If ‘Yes’ a new random graph is chosen for each run; if ‘No’, the same graph is always used.
- **Value type:** Boolean
- **Default value:** false

### discreteInteractionOrder

- **Short description:** Interaction order among discrete parents in the BGe embedding scores (1 = additive)
- **Long description:** For the BF-BGe and DG-BGe scores: the maximum number of distinct discrete parents whose indicator columns are multiplied to form interaction columns in a family's parent block. 1 (the default) is the additive design of DG-BIC and BF-BIC, in which a discrete child depends on its discrete parents only through main effects. 2 adds pairwise interactions; an order at least the number of discrete parents gives the saturated design, the same span as BDeu's conditional table. Empty-cell product columns are dropped. Orders above 1 are not score-equivalent (Markov-equivalent DAGs may score differently), so they are intended for permutation searches such as BOSS and GRaSP.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 20

### discretize

- **Short description:** Yes if continuous variables should be discretized when child is discrete
- **Long description:** Yes if for the conditional Gaussian likelihood, when scoring X-\>D where X is continuous and D discrete, one should to simply discretize X for just those cases. If no, the integration will be exact.
- **Value type:** Boolean
- **Default value:** true

### dmMergeThreshold

- **Short description:** Jaccard similarity threshold for merging input clusters
- **Long description:** Minimum Jaccard similarity required between the representative input sets of two clusters for them to be merged into a single latent variable in DM-Merge. The Jaccard similarity is the size of the intersection of the two input sets divided by the size of their union, ranging from 0 (no overlap) to 1 (identical sets). Higher values require greater overlap before merging, producing more latent variables with more distinct input sets. Lower values allow more aggressive merging, producing fewer latents that each capture a broader range of inputs. A value of 1.0 merges only clusters with identical input sets; the default of 0.78 allows moderate tolerance for noisy or partial overlap.
- **Value type:** Double
- **Default value:** 0.78
- **Minimum:** 0.0
- **Maximum:** 1.0

### doColliderOrientation

- **Short description:** Yes if unshielded collider orientation should be done
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

### doFgesFirst

- **Short description:** Yes if FGES should be done as an initial step
- **Long description:** For BOSS, for some cases, doing FGES as an initial step can reduce the maximum permutation size needed to solve a problem.
- **Value type:** Boolean
- **Default value:** false

### doHigherRankExpansion

- **Short description:** Allow higher-rank expansion for shared parents
- **Long description:** If enabled, Trek-MIMIC will attempt to identify shared measured parents of latents by expanding the search to higher-rank configurations beyond the default rank-1 case. This can recover more complex shared-cause structure but increases runtime and the risk of false positives. Disable for faster, more conservative searches.
- **Value type:** Boolean
- **Default value:** true
- **Minimum:** false
- **Maximum:** true

### doLegalityGating

- **Short description:** Yes to do legality gating, no to map the resulting graph to nearest PAG
- **Long description:** Yes to do legality gating, no to map the resulting graph to nearest PAG
- **Value type:** Boolean
- **Default value:** true

### domainColumn

- **Short description:** Domain column name
- **Long description:** The name of the column holding the domain index (batch, site, cohort, country) for tests that stratify by domain, such as the Stratified Rank test. The column should be discrete, or a continuous column whose values are all whole numbers; it is removed from the variable list and used only to split the rows into domains, within which the test statistics are computed and then pooled. If no column of this name exists but the data set has exactly one discrete column, that column is used and a note is logged.
- **Value type:** String
- **Default value:** domain

### doOneEquationOnly

- **Short description:** True if only one equation should be used when expanding the basis
- **Long description:** True if only one equation should be used when expanding the basis
- **Value type:** Boolean
- **Default value:** false

### doPossibleDsep

- **Short description:** Yes if the possible d-sep search should be done
- **Long description:** This algorithm has a possible d-sep path search, which can be time-consuming. See Spirtes, Glymour, and Scheines (2000) for details.
- **Value type:** Boolean
- **Default value:** true

## E

### ebicGamma

- **Short description:** EBIC Gamma (0-1)
- **Long description:** The gamma parameter for Extended BIC (Chen and Chen). In \[0, 1\].
- **Value type:** Double
- **Default value:** 0.8
- **Minimum:** 0.0
- **Maximum:** 1.0

### effectiveSampleSize

- **Short description:** The effective sample size, or -1 if the true sample size is to be used.
- **Long description:** The effective sample size, or -1 is the true sample size is to be used.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### equivalenceMargin

- **Short description:** Largest \|partial correlation\| counted as negligible, or 0 to scale it to the sample size.
- **Long description:** The equivalence (TOST) test reports independence only when it can show the partial correlation is smaller in magnitude than this margin, rather than merely failing to reject zero. The margin is squeezed from both sides: it must exceed about 1.645/sqrt(n) at alpha = 0.05 or nothing is ever removable and the adjacency search returns a complete graph, and it must stay below the weakest association worth keeping, since asymptotically every pair below the margin is removed. Because the usable range depends on the sample size, leaving this at 0 is recommended: the margin is then set automatically to equivalenceMarginMultiplier times the smallest margin the sample size could certify.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 0.999

### equivalenceMarginMultiplier

- **Short description:** Equivalence margin as a multiple of the smallest one the sample size can certify (min \> 1).
- **Long description:** Used when equivalenceMargin is 0. The margin is set to this multiple of tanh(c/sqrt(n-3)), the smallest margin the sample size could certify at all, which turns a sample-size-dependent choice into one dimensionless knob. The multiplier trades adjacency precision for the retention of weak real edges: on random cyclic linear-Gaussian graphs, 2.0 improved recall of Richardson virtual edges and of dotted-underline triples at every sample size tested for about 0.015 of adjacency precision, 1.6 moved further in that direction at a real cost in endpoint accuracy at large samples, and values above about 2.5 began deleting the virtual edges and degraded everything. Values at or below 1 are not allowed, since the margin would then certify nothing.
- **Value type:** Double
- **Default value:** 2.0
- **Minimum:** 1.01
- **Maximum:** 100.0

### errorsNormal

- **Short description:** Yes if errors should be Normal; No if they should be abs(Normal) (i.e., non-Gaussian)
- **Long description:** A “quick and dirty” way to generate linear, non-Gaussian data is to set this parameter to “No”; then the errors will be sampled from a Beta distribution.
- **Value type:** Boolean
- **Default value:** true

### ess

- **Short description:** Yes if the equivalent sample size should be used in place of N
- **Long description:** We calculate the equivalent sample size by assuming that all record are equally correlated
- **Value type:** Boolean
- **Default value:** false

### excludeSelectionBias

- **Short description:** Yes if the possibility of selection bias should be excluded
- **Long description:** If true ("Yes"), the algorithm assumes no selection bias and disables selection-related orientation rules (including certain final rules in Zhang 2008). If false ("No") the algorithm allows for selection bias and uses the full rule set.
- **Value type:** Boolean
- **Default value:** true

### extraEdgeRemovalStep

- **Short description:** The extra edge removal step to use: 1 = LV\_LITE, 2 = Greedy, 3 = Max P, 4 = Min P
- **Long description:** The extra edge removal step to use: 1 = LV\_LITE, 2 = Greedy, 3 = Max P, 4 = Min P
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

## F

### fa_threshold

- **Short description:** Minimum absolute loading for an edge from a factor to a variable
- **Long description:** After factors are extracted, an edge is drawn from a factor to a measured variable when the absolute value of the corresponding loading exceeds this threshold. Raising it yields a sparser, more interpretable measurement model and drops weakly loading variables; lowering it retains more edges, including ones attributable to noise. This is a loading cutoff and is distinct from convergenceThreshold, which controls when the iteration stops.
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** Infinity

### faithfulnessAssumed

- **Short description:** Yes if (one edge) faithfulness should be assumed
- **Long description:** Assumes that if X \_\|\|\_ Y, by an independence test, then X \_\|\|\_ Y \| Z for nonempty Z.
- **Value type:** Boolean
- **Default value:** false

### faskAdjacencyMethod

- **Short description:** Non-skewness Adjacencies: 1 = FAS Stable, 2 = FGES, 3 = External Graph, 4 = None
- **Long description:** This is the method FASK will use to find non-skewness adjacencies. For External graph, an external graph must be supplied.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

### faskAssumeLinearity

- **Short description:** Linearity assumed
- **Long description:** True if a linear, non-Gaussian, additive model is assume; false if a nonlinear, non-Gaussian, additive model is assumed.
- **Value type:** Boolean
- **Default value:** true

### faskDelta

- **Short description:** For FASK v1, the bias for orienting with negative coefficients ('0' means no bias.)
- **Long description:** The bias procedure for v1 is given in the published description.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### faskLeftRightRule

- **Short description:** The left right rule: 1 = FASK v1, 2 = FASK v2, 3 = RSkew, 4 = Skew, 5 = Tanh
- **Long description:** The FASK left right rule v2 is default, but two other (related) left-right rules are given for relation to the literature, and the v1 FASK rule is included for backward compatibility.
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 5

### faskNonempirical

- **Short description:** Variables should be assumed to have positive skewness
- **Long description:** If false (default), each variable is multiplied by the sign of its skewness in the left-right rule.
- **Value type:** Boolean
- **Default value:** false

### faskOverrideBlockLength

- **Short description:** Block length for the FASK override bootstrap (1 = i.i.d. resampling)
- **Long description:** Only used by single-dataset FASK when faskOverrideBootstraps is positive. One (the default) resamples rows independently, which is correct when the rows are independent. A larger value resamples contiguous blocks of that length (a moving-block bootstrap), which is what autocorrelated rows require -- time series such as LFP recordings. Resampling autocorrelated rows independently makes the resamples far more alike than independent samples would be, so the sign consensus becomes much too easy to achieve and false reversals follow; a common choice is about the square root of the number of rows.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 100000

### faskOverrideBootstraps

- **Short description:** Bootstrap resamples gating an override of a compelled external orientation in single-dataset FASK
- **Long description:** Only used by single-dataset FASK, and only when an external graph is supplied with faskPoolExternalOrientations true. Zero (the default) means no gate: the left-right statistic overturns a compelled orientation whenever it opposes it, which on compelled edges is simply plain FASK, so the external orientations then have no effect. A positive value requires every resample's left-right statistic to oppose the compelled direction before the override is taken (strict sign consensus). With one dataset there is no cross-dataset consensus to appeal to, so this is what makes the override a test rather than a relabeling. Cost is linear in this value times the number of adjacencies.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 100000

### faskPoolAdjacency

- **Short description:** FASK-Pool adjacency search: 1 = IMaGES, 2 = pooled FAS, 3 = MG-FAS, 4 = MG-LiNG, 5 = MG-FAS & MG-LiNG intersection, 6 = IMaGES restricted to MG-FAS
- **Long description:** Selects how the common adjacency structure is estimated across the datasets before FASK orientation (used by both FASK-Pool and FASK-Vote). 1: IMaGES (BOSS on the score averaged across datasets). 2: pooled FAS (FAS-Stable with per-dataset Fisher Z p-values combined by Fisher's method). 3: MG-FAS: the pooled moral graph (full-order partial correlations, Fisher-combined across datasets) pruned by FAS-style sepset tests restricted to moral neighborhoods; cycle-safe, recommended when errors may be Gaussian. 4: MG-LiNG: the pooled moral graph filtered by per-dataset ICA (LiNG) estimates of B, pooled by median; requires non-Gaussian errors. 5: the intersection of 3 and 4; in simulations with skewed errors this gave the best adjacency precision at full recall, and skewed errors are the FASK setting. Options 3-5 target the skeleton of a possibly cyclic linear model; note that no method based only on conditional independence can remove Richardson-style virtual adjacencies around cycles. 6: IMaGES restricted to the MG-FAS skeleton: MG-FAS is run first and its adjacencies are imposed on the IMaGES (BOSS) search as a superstructure, by forbidding both directions of every pair outside it, so the score search can only remove adjacencies from that skeleton and never add them. This addresses the fact that on cyclic data a DAG-based score search adds adjacencies to compensate for cycles it cannot represent, many of them moralized (married) pairs, which MG-FAS prunes by sepset tests. Because its output is a subset of the MG-FAS adjacencies, its recall cannot exceed MG-FAS's.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 6

### faskPoolAdjacencyOrientations

- **Short description:** Use the IMaGES CPDAG's compelled orientations as defaults
- **Long description:** Only consulted when FASK-Pool runs its own adjacency search (no external graph) and only the IMaGES option produces orientations; the other adjacency options return undirected graphs. If true (default), the compelled edges of the IMaGES CPDAG -- BOSS over the score averaged across the datasets, so already a combination of all of them -- become default orientations, and the pooled left-right statistic can overturn a default only when it opposes it, every dataset's statistic individually opposes it (strict cross-dataset sign consensus), and, when the orientation alpha is above zero, the pooled statistic is significant at that level. Reversible (undirected) edges of the CPDAG carry no orientation information and are oriented from the pooled statistic as usual. If false, only the adjacencies of the IMaGES graph are used and every edge is oriented from the pooled statistic. Note that with a single dataset the sign consensus is vacuous, so a positive orientation alpha should be used to gate the override.
- **Value type:** Boolean
- **Default value:** true

### faskPoolExternalAdjacencyFraction

- **Short description:** Fraction of the external graphs a pair must be adjacent in
- **Long description:** Only consulted when more than one external graph is given to FASK-Pool (one per dataset). A pair enters the composite skeleton when the number of graphs in which it is adjacent exceeds this fraction of the number of graphs. Zero takes the union of the skeletons, 0.5 (the default) a strict majority, and 1.0 the intersection.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### faskPoolExternalOrientations

- **Short description:** Use the external graphs' compelled orientations as defaults (FASK, FASK-Vote and FASK-Pool)
- **Long description:** Only consulted when external graphs are given to FASK-Pool. The external-graph algorithm is run separately on each dataset (unless it is itself a multi-dataset algorithm, which pools internally and is run once), and the resulting graphs are combined. If true (default), the compelled orientations of those graphs are tallied per pair and the majority direction, if there is one, becomes the default orientation; a tie leaves the pair to the pooled statistic. The pooled left-right statistic can overturn a default only when it opposes it and, when the orientation alpha is above zero, is significant at that level; if the evidence is unanimous (no graph compels the other direction), every dataset's statistic must individually oppose it as well (strict cross-dataset sign consensus). Reversible (undirected) edges are oriented from the pooled statistic as usual; a supplied DAG is converted to its CPDAG first so reversible edges do not act as compelled. If false, the external graphs contribute adjacencies only. Note that a fixed source graph supplied in the interface is the same graph for every dataset and so carries no cross-dataset evidence; with one graph, or one dataset, the sign consensus is vacuous, so a positive orientation alpha should be used to gate the override. FASK-Vote and single-dataset FASK read this parameter too, each with the counter-signal its own structure supports: FASK-Vote tallies the same way and overturns a default only when the vote opposes it, requiring a unanimous vote (every dataset voted, every one against) when the evidence is unanimous and an ordinary majority when the evidence is divided; single-dataset FASK, where there are no other datasets to appeal to, requires every bootstrap resample's statistic to oppose the default (see faskOverrideBootstraps, which is the only real gate there -- left at zero, the override is unconditional and the external orientations have no effect).
- **Value type:** Boolean
- **Default value:** true

### fasRule

- **Short description:** Adjacency search: 1 = PC, 2 = PC-Stable, 3 =f Concurrent PC-Stable
- **Long description:** For variants of PC, one may select either to use the usual PC adjacency search, or the procedure from the PC-Stable algorithm (Diego and Maathuis), or the latter using a concurrent algorithm.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### fastIcaA

- **Short description:** Fast ICA 'a' parameter.
- **Long description:** This is the 'a' parameter of Fast ICA. (See Hyvarinen, A. (2001); it ranges between 1 and 2; we use a default of 1.1.
- **Value type:** Double
- **Default value:** 1.1
- **Minimum:** 1.0
- **Maximum:** 2.0

### fastIcaMaxIter

- **Short description:** The maximum number of optimization iterations.
- **Long description:** This is the maximum number if iterations of the optimization procedure of ICA. (See Hyvarinen, A. (2001). It's an integer greater than 0; we use a default of 2000.
- **Value type:** Double
- **Default value:** 2000
- **Minimum:** 1
- **Maximum:** 500000

### fastIcaTolerance

- **Short description:** Fast ICA tolerance parameter.
- **Long description:** This is the tolerance parameter of Fast ICA. (See Hyvarinen, A. (2001); we use a default of 1e-6.
- **Value type:** Double
- **Default value:** 1e-6
- **Minimum:** 0.0
- **Maximum:** 1000.0

### fcitCorrectness

- **Short description:** Warrant for the result: 1 = Guarantee I-map, 2 = Score step, 3 = Saturating step
- **Long description:** The warrant the search relies on for the final graph, a three-way choice shared by FCIT, FCIT-ZM, and the \*-FCI family (BFCI, GFCI, SP-FCI, GRaSP-FCI). 1 = Guarantee I-map: every candidate the legality gate accepts must additionally be an I-map of the independence test, that is, every nonadjacent pair of its implied MAG must have a test-confirmed separator at imapAlpha; the saturating step is off. 2 = Score step: every accepted candidate's Zhang MAG is scored by RICF BIC against the committed state's; the saturating step is off, and a SEM BIC score built on a covariance matrix with zero structure prior is required, so this option is available only for continuous data. The acceptance rule, shared by all of them since November 2026 and following the BFCI-Bryan score step, requires a strict improvement for each removal; the \*-FCI family alone accepts a tie when re-selecting a separating set for an already nonadjacent pair, where no edge is removed. 3 = Saturating step: no extra per-commit gate; when no single removal commits, all pairs with test-confirmed separating sets are removed jointly, which is the step the oracle correctness argument needs. The saturating step is not a separate switch: it runs exactly when neither gate is on. Option 1 is the default; its no-stall property rests on a conjecture, while option 3 is the configuration proved correct in the oracle under the GFCI assumptions.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### fcitSlAllowClassEscape

- **Short description:** Yes the MAG iteration in permitted to escape the Markov equivalence class
- **Long description:** The Step Lemma for FCIT-SL requires iteration of MAGs only within the Markov equivalent class of the initial MAG; this allows escape.
- **Value type:** Boolean
- **Default value:** false

### fcitStartsWith

- **Short description:** Initial Markov PAG: 1 = BOSS, 2 = GRaSP, 3 = SP, 4 = Complete PAG
- **Long description:** Initial Markov PAG: 1 = BOSS, 2 = GRaSP, 3 = SP, 4 = Complete PAG
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

### fDegree

- **Short description:** Degree of the polynomial basis in the MVP likelihood, or -1 to choose automatically
- **Long description:** The degree of the polynomial expansion used in the mixed variable polynomial likelihood for the MVP score and the MVP likelihood ratio test. A value of -1 lets the implementation choose the degree from the data. Higher degrees allow more flexible conditional mean functions but consume degrees of freedom quickly and can destabilize the test at small sample sizes.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### fdrQ

- **Short description:** FDR q value, often 0.01 - 0.1, or 0 if FDR should not be done.
- **Long description:** FDR q value, often 0.01 - 0.1, or 0 if FDR should not be done.
- **Value type:** Double
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 1

### ffmlFfFeatures

- **Short description:** Number of Fourier features used for nonlinear continuous effects
- **Long description:** Number of random Fourier (or orthogonal random) features used to approximate the continuous kernel in FFML score. Increasing this value improves the accuracy of the kernel approximation and allows more flexible nonlinear modeling of continuous parents, but increases runtime and memory usage. Smaller values are faster but provide a coarser approximation of nonlinear effects.
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 1000000

### ffmlInteractionLambda

- **Short description:** FFML discrete-continuous interaction weight (0 = additive)
- **Long description:** Weight of the product-kernel interaction term for discrete parents. At 0 (the default), discrete parents enter as additive one-hot main effects (BF/DG-style) and catRho is inert; positive values add per-level response functions with catRho pooling.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0
- **Maximum:** 1.7976931348623157E308

### ffmlRidge

- **Short description:** Ridge / noise-variance (σ²) term for FFML Gaussian-process marginal likelihood
- **Long description:** Positive ridge (jitter) term added to the GP covariance when computing the FFML (Feature-Function Marginal Likelihood) score. In the FFML implementation this parameter is used as the observation noise variance σ² in the marginal likelihood (i.e., K + σ²I in the n×n path, and G + σ²I in the feature-space path). Larger values enforce smoother, more heavily regularized fits; smaller values allow tighter fits but can be less numerically stable.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0e12

### fileOutPath

- **Short description:** Results output path
- **Long description:** Path to a directory in which results can be stored
- **Value type:** String
- **Default value:** cstar-out

### fisherEpsilon

- **Short description:** Epsilon where \|xi.t - xi.t-1\| \< epsilon, criterion for convergence
- **Long description:** This is a parameter for the linear Fisher option. The idea of Fisher model (for the linear case) is to shock the system every so often and let it converge by applying the rules of transformation (that is, the linear model) repeatedly until convergence.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 4.9E-324
- **Maximum:** 1.7976931348623157E308

### flopNumRestarts

- **Short description:** The number of iterated local search (ILS) restarts for FLOP (default 20)
- **Long description:** The number of iterated local search restarts. Zero gives a single local search from the principled initial order. Each restart perturbs the best-found order with about ln(p) random transpositions and reruns the local search, keeping the best-scoring result; more restarts can never yield a worse-scoring graph, at the expense of run-time.
- **Value type:** Integer
- **Default value:** 20
- **Minimum:** 0
- **Maximum:** 2147483647

### fofcAlpha

- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.0

## G

### gammaHigh

- **Short description:** Upper end of the range for the sine frequency
- **Long description:** Upper end of the uniform range from which the frequency multiplier inside the sine term is drawn in the Linear Sine simulation. See gammaLow.
- **Value type:** Double
- **Default value:** 1.5
- **Minimum:** -Infinity
- **Maximum:** Infinity

### gammaLow

- **Short description:** Lower end of the range for the sine frequency
- **Long description:** Lower end of the uniform range from which the frequency multiplier inside the sine term is drawn in the Linear Sine simulation. Higher frequencies produce more oscillation over the range of the parent and so a more strongly nonlinear dependence.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** -Infinity
- **Maximum:** Infinity

### gcmControlFunction

- **Short description:** Yes if the BE-GCM regressions should be augmented with a control function in the fitted mean
- **Long description:** The BE-GCM regression basis is additive over the conditioning variables' basis columns and cannot represent interactions among them; yet even under purely additive data-generating functions, the conditional means of the higher-order tested grid cells contain interaction terms (powers of sums), so the test over-rejects true conditional independencies when conditioning on two or more variables -- typically visible as an excess of implied conditional independencies judged dependent in the Markov Checker, at any Z-truncation. If Yes, each side's regression design is augmented with a univariate basis in that side's first-stage fitted mean (a control function): under additive-noise mechanisms the conditional means of all grid cells are functions of the fitted mean alone, so this captures the missing interaction and composition terms. Power is essentially unaffected. The fitted mean is a generated regressor, so exact finite-sample arguments no longer apply; calibration with this option has been checked empirically on additive nonlinear systems.
- **Value type:** Boolean
- **Default value:** false

### gcmMultiplierSamples

- **Short description:** Number of multiplier bootstrap samples for the BE-GCM max statistic (0 = Sidak bound)
- **Long description:** The p-value of the basis-expanded GCM test is computed by a Rademacher multiplier bootstrap of the maximum studentized residual cross-covariance over the basis-pair grid, which accounts for the dependence among the grid cells. This parameter sets the number of bootstrap samples; the p-value granularity is 1 / (samples + 1). Setting it to 0 uses a Sidak bound over the grid with the normal tail instead, which is faster but conservative. The bootstrap is seeded deterministically from the tested independence fact, so results are reproducible.
- **Value type:** Integer
- **Default value:** 500
- **Minimum:** 0
- **Maximum:** 1000000

### gcmRegressorType

- **Short description:** 1 = Linear Ridge, 2 = RFF Ridge
- **Long description:** Selects the regression model used by the GCM conditional independence test. The regressor type determines how the conditional mean of each variable is modeled given the conditioning set, ranging from linear to nonlinear (RFF-based) regressors.
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2

### gcmRffFeatures

- **Short description:** Number of random Fourier features
- **Long description:** Number of random Fourier features (RFF) used to represent nonlinear relationships in the GCM regression models. Larger values increase expressiveness and runtime cost.
- **Value type:** Integer
- **Default value:** 200
- **Minimum:** 0
- **Maximum:** 1000000

### gcmRffSigma

- **Short description:** RFF kernel bandwidth (sigma)
- **Long description:** Bandwidth parameter (sigma) for the random Fourier feature construction used in the GCM test. Smaller values produce higher-frequency features; larger values produce smoother features.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 1e-6
- **Maximum:** 1.0e6

### gcmRidge

- **Short description:** Ridge regularization strength
- **Long description:** Ridge (L2) regularization strength used when fitting regression models within the GCM test. Larger values increase shrinkage and numerical stability; smaller values allow more flexible fits.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0e12

### gcmZTruncationLimit

- **Short description:** Truncation limit for the BE-GCM regression (Z-side) basis; 0 = twice the grid truncation
- **Long description:** The BE-GCM test residualizes the tested basis grid of X and Y on a basis expansion of Z. The GCM guarantee requires this regression sieve to approximate the conditional means of the tested grid functions, which under nonlinear relations are compositions of higher degree than the grid itself; if the regression basis is too small, the test over-rejects true conditional independence. This parameter sets the truncation of the Z-side regression basis separately from the tested grid. The default 0 selects twice the grid truncation limit, which covers quadratic relations exactly; raise it for more strongly nonlinear systems. Values below the grid truncation are raised to it. The Z-side basis is never pruned by adaptive basis selection.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 1000

### generalSemErrorTemplate

- **Short description:** General function for error terms
- **Long description:** This template specifies how distributions for error terms are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** Beta(2, 5)

### generalSemFunctionTemplateLatent

- **Short description:** General function template for latent variables
- **Long description:** This template specifies how equations for latent variables are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** TSUM(NEW(B)\*$)/\>

### generalSemFunctionTemplateMeasured

- **Short description:** General function template for measured variables
- **Long description:** This template specifies how equations for measured variables are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** TSUM(NEW(B)\*$\>

### generalSemParameterTemplate

- **Short description:** General function for parameters
- **Long description:** This template specifies how distributions for parameter terms are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** Split(-1.0, -0.5, 0.5, 1.0)

### ginBackend

- **Short description:** Backend test: 1 = dcor 2 = pearson.
- **Long description:** Choose unconditional test for residual independence: “dcor” detects nonlinear relations, “pearson” is fast but linear only.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### ginPermutations

- **Short description:** Number of permutations for dCor.
- **Long description:** Number of random shuffles used to compute p-values for dCor; higher values give more reliable p-values but increase runtime; ignored if backend is pearson.
- **Value type:** Integer
- **Default value:** 200
- **Minimum:** 0
- **Maximum:** 100000

### ginRidge

- **Short description:** Ridge penalty for OLS regression
- **Long description:** Small positive value added to regression diagonals for numerical stability when fitting residual models; larger values regularize more but bias residuals.
- **Value type:** Double
- **Default value:** 1e-8
- **Minimum:** 0
- **Maximum:** 100000

### gmasAllowAdditions

- **Short description:** Allow GMAS to add edges, not only delete and re-type them
- **Long description:** GMAS improves a BOSS-seeded MAG by greedy search under the MAG BIC. With this set to Yes, the move set includes ADDING a directed or bidirected edge between a non-adjacent pair, which is what lets the search restore an adjacency the BOSS seed missed. With it set to No the search may only delete edges, reverse them, or change their type, which is the comparison that isolates what additions contribute. Additions cost one model fit per non-adjacent ordered pair per sweep, so turning them off is also much faster.
- **Value type:** Boolean
- **Default value:** true

### gmasLookaheadDepth

- **Short description:** How many moves deep GMAS looks when its sweep stalls (1 or 2)
- **Long description:** With 1, GMAS is plain steepest ascent and stops at the first graph no single move improves. With 2, a stall triggers a search over PAIRS of moves that share a node, which reaches corrections whose two halves are individually non-improving -- deleting a spurious edge and re-typing a neighbouring directed edge to bidirected, for instance, where neither step improves the score alone. Depth 2 recovers such cases and is markedly slower; the pair search is capped internally.
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2

### gmasTriangleEscapeOnly

- **Short description:** Restrict GMAS's two-move escape to triangle pairs (faster, slightly less thorough)
- **Long description:** With this set to Yes, the two-move escape considers only pairs of moves whose touched edges share a node and whose far endpoints are adjacent in the pre-move MAG -- the GFCI situation, where a score-induced extra edge shields a collider and the deletion and its accompanying re-orientation lie in a common triangle. This captures nearly all of the repairs the full escape finds and is typically two to four times faster, mostly because declaring a local optimum requires exhausting the escape neighbourhood and the triangle neighbourhood is far smaller. With it set to No (the default), the escape searches all pairs sharing a node, which is exact but slower.
- **Value type:** Boolean
- **Default value:** false

### graspAlg

- **Short description:** 1 = GRaSP1, 2 = GRaSP2, 3 = esp, 4 = GRaSP4, 5 = GRaSP4
- **Long description:** Which version of GRaSP (temp parameter)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

### graspBreakAfterImprovement

- **Short description:** Yes if depth first search returns after first improvement, No for depth first traversal.
- **Long description:** Exploring the full list in every DFS call is equivalent to what we've been calling the Random Carnival Game procedure (RCG).
- **Value type:** Boolean
- **Default value:** true

### graspCheckCovering

- **Short description:** Yes if covering of edges should be checked (GASP), no if not (GRASP)
- **Long description:** An edge X is covered if Parents(X) = Parents(Y) \\ \{X\}. Not checking covering expands the search space.
- **Value type:** Boolean
- **Default value:** false

### graspDepth

- **Short description:** Recursion depth (for GRaSP)
- **Long description:** This is the depth of recursion for the depth first search.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 2147483647

### graspForwardTuckOnly

- **Short description:** Yes if only forward tucks should be checked, no if also reverse tucks should be checked.
- **Long description:** A forward tuck for X-\>Y moves Y to the before position of X in the permutation. A reverse tuck moves Y to after the position of X in the permutation. Including reverse tucks expands the search space.
- **Value type:** Boolean
- **Default value:** false

### graspNonSingularDepth

- **Short description:** Recursion depth for nonsingular tucks
- **Long description:** This is the depth of recursion at which multiple tucks may be considered per score improvement
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

### graspOrderedAlg

- **Short description:** Yes if earlier GRaSP stages should be performed before later stages
- **Long description:** GRaSP has three stages; these can be performed separately or in order; by default Yes.
- **Value type:** Boolean
- **Default value:** true

### graspSingularDepth

- **Short description:** Recursion depth for singular tucks
- **Long description:** This is the depth of recursion for the singular tucks.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

### graspToleranceDepth

- **Short description:** Recursion depth for tolerance tucks
- **Long description:** This is the maximum number of non-greedy tucks in depth first order --that is, tucks where the score is allowed to decrease rather than increase.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### graspUseRaskuttiUhler

- **Short description:** Yes to use Raskutti and Uhler's DAG-building method (test), No to use Grow-Shrink (score).
- **Long description:** Raskutti and Uhler's method adds and edge X-\>Y if Y \~\_\|\|\_ X \| Prefix(Y, pi) \\ \{X\}. Grow-Shrink adds an edge X-\>Y if X is in the Markov blanket of Y where the variable set is restricted to Prefix(Y, pi).
- **Value type:** Boolean
- **Default value:** false

### graspUseScore

- **Short description:** Yes if the score should be used for MB calculations, no if the test should be used instead.
- **Long description:** In either case, compositional graphoid axioms are assumed by the Grow-Shrink algorithm.
- **Value type:** Boolean
- **Default value:** true

### graspUseVpScoring

- **Short description:** No sure
- **Long description:** Not sure
- **Value type:** Boolean
- **Default value:** false

### guaranteeAcyclic

- **Short description:** True if the output should be guaranteed to be acyclic
- **Long description:** The estimated B matrix is further thresholded by setting small coefficients to zero until an acyclic model is produced.
- **Value type:** Boolean
- **Default value:** true

### guaranteeCpdag

- **Short description:** Guarantee that the output is a legal CPDAG
- **Long description:** It is possible due to unfaithfulness for the Meek rules to output a non-CPDAG; this parameter guarantees a CPDAG if set to 'Yes'.
- **Value type:** Boolean
- **Default value:** true

### guaranteeIid

- **Short description:** Recursive simulation is used for acyclic models; if not should i.i.d. be assumed?
- **Long description:** For cyclic models, the Fisher simulation model is used, which is a time series. Selecting 'Yes' here guarantees that a new data point starts from a new shock without influence from the previous time step.
- **Value type:** Boolean
- **Default value:** true

### guaranteePag

- **Short description:** Ensure the output is a legal PAG (where feasible)
- **Long description:** Repairs errors in PAGs due to almost cyclic paths or non-maximalities. This comes with a certain risk; errors in PAGs indicate that the PAG assumptions were not met; the user may wish to consider why before selecting this
- **Value type:** Boolean
- **Default value:** false

## H

### henckelPruning

- **Short description:** Whether to do Henckel et al. (2020) Algorithm 1 pruning.
- **Long description:** Whether to do Henckel et al. (2020) Algorithm 1 pruning.
- **Value type:** Boolean
- **Default value:** False

### hiddenDimension

- **Short description:** For Nonlinear Additive Model, the number of nodes per edge
- **Long description:** For a shallow multilayer perception (MLP), the number of nodes in the hidden layer
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 500000

### hiddenDimensions

- **Short description:** For perceptrons, the number of nodes in hidden layers (comma separated)
- **Long description:** For perceptrons, the number of nodes in hidden layers (comma separated)
- **Value type:** String
- **Default value:** 200,200,200,200,200,200

## I

### ia

- **Short description:** IA parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** true

### imagesMetaAlg

- **Short description:** IMaGES "meta" algorithm. 1 = FGES, 2 = BOSS-Tuck
- **Long description:** Sets the meta algorithm to be optimized using the IMaGES (average BIC) score.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

### imapAlpha

- **Short description:** Significance level for the I-map gate's tests (default 0.001)
- **Long description:** The I-map gate vetoes a candidate when a separator it asserts tests dependent at this level. Kept separate from, and smaller than, the removal alpha so that a veto requires a strong dependence; this reduces false vetoes from test noise. Applied to the test's p-value when it is a probability; otherwise the test's own verdict is used.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.0

### include_structure_model

- **Short description:** Yes if the (MimBuild) structure model should be included in the output graph
- **Long description:** FOFC proper yields a measurement model--that is, a set of pure children for each of the discovered latents. One can estimate the structure over the latents (the structure model) using Mimbuild. This structure model is included in the output if this parameter is set to Yes.
- **Value type:** Boolean
- **Default value:** false

### includeAllNodes

- **Short description:** True if all nodes should be included in the output
- **Long description:** True if all nodes should be included in the output.
- **Value type:** Boolean
- **Default value:** false

### includeNegativeCoefs

- **Short description:** Yes if negative coefficients should be included in the model
- **Long description:** One may include positive coefficients, negative coefficients, or both, in the model. To include negative coefficients, set this parameter to “Yes”.
- **Value type:** Boolean
- **Default value:** true

### includeNegativeSkewsForBeta

- **Short description:** Yes if negative skew values should be included in the model, if Beta errors are chosen
- **Long description:** Yes if negative skew values should be included in the model, if Beta errors are chosen.
- **Value type:** Boolean
- **Default value:** true

### includePositiveCoefs

- **Short description:** Yes if positive coefficients should be included in the model
- **Long description:** Yes if We may include positive coefficients, should be included in the model, no if not.
- **Value type:** Boolean
- **Default value:** true

### includePositiveSkewsForBeta

- **Short description:** Yes if positive skew values should be included in the model, if Beta errors are chosen
- **Long description:** Yes if positive skew values should be included in the model, if Beta errors are chosen.
- **Value type:** Boolean
- **Default value:** true

### inputScale

- **Short description:** For a shallow multilayer perception (MLP), the input scale (affects bumpiness)
- **Long description:** Input scale for the network--inputs into each node are scaled by this
- **Value type:** Double
- **Default value:** 5.0
- **Minimum:** 0.0
- **Maximum:** Infinity

### instanceRow

- **Short description:** Indicates a particular row in the testing dataset (one-indexed)
- **Long description:** If the algorithm uses a testing dataset, this row index points to a specific row in the data to be used as input to the algorithm. This is one-indexed.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

### instanceSpecificAlpha

- **Short description:** Weight for instance-specific component to the score
- **Long description:** Weight for instance-specific component to the score.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0
- **Maximum:** Infinity

### interceptHigh

- **Short description:** Upper end of the range for the equation intercept
- **Long description:** Upper end of the uniform range from which the intercept of each structural equation is drawn in the Linear Sine simulation. See interceptLow.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### interceptLow

- **Short description:** Lower end of the range for the equation intercept
- **Long description:** Lower end of the uniform range from which the intercept of each structural equation is drawn in the Linear Sine simulation.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### intervalBetweenRecordings

- **Short description:** Interval between data recordings for the linear Fisher model (min = 1)
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### intervalBetweenShocks

- **Short description:** Interval between shocks (R. A. Fisher simulation model) (min = 1)
- **Long description:** This is a parameter for the linear Fisher option. This sets the number of step between shocks.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### ionAdjacencySearch

- **Short description:** Yes if ION should iterate over separation facts one at a time
- **Long description:** If Yes, the ION branch and prune step iterates over the recorded separation facts one at a time, blocking the possibly connecting paths for each fact in turn. If No, all facts are handled together in a single pass. Iterating one fact at a time can reduce the number of candidate graphs held in memory at once.
- **Value type:** Boolean
- **Default value:** false

### ionPathLengthSearch

- **Short description:** Yes if ION should block possibly connecting paths shortest first
- **Long description:** If Yes, the ION branch and prune step considers possibly connecting paths in order of increasing length, blocking shorter paths before longer ones. This prunes the search space earlier and usually reduces run time and memory use. If No, paths of all lengths are considered together.
- **Value type:** Boolean
- **Default value:** true

### ipen

- **Short description:** IPEN parameter (GLASSO)
- **Long description:** This sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

### is

- **Short description:** IS parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

### itr

- **Short description:** ITR parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

## K

### kciAlpha

- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### kciCutoff

- **Short description:** Cutoff
- **Long description:** Cutoff for p-values.
- **Value type:** Integer
- **Default value:** 6
- **Minimum:** 1
- **Maximum:** 2147483647

### kciEpsilon

- **Short description:** Epsilon, a small positive number
- **Long description:** See Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012). Kernel-based conditional independence test and application in causal discovery.. This parameter is the epsilon for Proposition 5, a small positive number.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** Infinity

### kciNumBootstraps

- **Short description:** Number of bootstraps
- **Long description:** This parameter is the number of bootstraps for Theorems 4 from Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012) and Proposition 5, a positive integer.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### kciUseApproximation

- **Short description:** Use the Gamma approximation algorithm
- **Long description:** Referring to Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012), if this parameter is set to ‘Yes’, the Gamma approximation algorithm is used; if no, the exact procedure is used.
- **Value type:** Boolean
- **Default value:** true

### kernelRegressionSampleSize

- **Short description:** Minimum sample size to use per conditioning for kernel regression
- **Long description:** The smallest set of nearest data points on which to allow a judgment to be based for a nonlinear regression.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### kernelType

- **Short description:** Kernel type (1 = Gaussian, 2 = Linear, 3 = Polynomial)
- **Long description:** Determines which kernel type will be used (1 = Gaussian, 2 = Linear, 3 = Polynomial).
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### kernelWidth

- **Short description:** Kernel width
- **Long description:** A larger kernel width means that more information will be taken into account but possibly less focused information.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 4.9E-324
- **Maximum:** Infinity

### kmlBandwidthMultiplier

- **Short description:** Bandwidth multiplier on the median heuristic, default = 1
- **Long description:** Bandwidth multiplier on the median heuristic, default = 1.
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 1e-50
- **Maximum:** Infinity

### kmlFeatureType

- **Short description:** Type of features: 1 = Random FFs, 2 = Orthogonal Random FFs
- **Long description:** Type type of random features: 1 = Random FFs or 2 = Orthogonal Random FFs
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2

### kmlJitter

- **Short description:** Jitter escalation base for Cholesky stabilization. Must be \> 0.
- **Long description:** Jitter escalation base for Cholesky stabilization. Must be \> 0.
- **Value type:** Double
- **Default value:** 1e-10
- **Minimum:** 1e-50
- **Maximum:** Infinity

### kmlLambda

- **Short description:** Ridge lambda, default = 1
- **Long description:** Ridge lambda, default = 1
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** Infinity

### kmlNumFeatures

- **Short description:** The number of random features used for kernel approximations
- **Long description:** The number of random features used for kernel approximations
- **Value type:** Integer
- **Default value:** 200
- **Minimum:** 1
- **Maximum:** 2147483647

## L

### lambda1

- **Short description:** lambda1
- **Long description:** Tuning parameter for DAGMA
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0
- **Maximum:** Infinity

### linearHigh

- **Short description:** Upper end of the range for the linear coefficient
- **Long description:** Upper end of the uniform range from which the coefficient on the linear term of each structural equation is drawn in the Linear Sine simulation. See linearLow.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### linearLow

- **Short description:** Lower end of the range for the linear coefficient
- **Long description:** Lower end of the uniform range from which the coefficient on the linear term of each structural equation is drawn in the Linear Sine simulation. Together with linearHigh this fixes the strength of the linear component relative to the sine component.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** -Infinity
- **Maximum:** Infinity

### lingamPruneAlpha

- **Short description:** Alpha for the t-test in LiNGAM's regression pruning step
- **Long description:** Significance level for the per-coefficient two-sided t-test in LiNGAM's regression refit-and-prune step (see lingamRefitAndPrune). A coefficient is kept when its p-value falls below this alpha. Smaller values prune more aggressively; 0.001 worked well at sample sizes of 1000 to 5000 in simulation.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.0

### lingamRefitAndPrune

- **Short description:** Yes to refit LiNGAM coefficients by regression and prune by t-test
- **Long description:** Yes to follow LiNGAM's acyclicity trimming with the pruning step of Shimizu et al. (2006), step 5: the trimmed model fixes the causal order, each variable is regressed on all its predecessors in that order, and coefficients are kept when significant by a t-test at lingamPruneAlpha. This replaces the noisier ICA-derived coefficients with regression estimates and prunes in a scale-free way, where the Threshold B cut alone depends on the units of the data. The Threshold B parameter still governs the trimming stage that fixes the order. No to return the ICA-derived trimmed coefficients as before.
- **Value type:** Boolean
- **Default value:** true

### logFinalOrientations

- **Short description:** Yes to log the rule-by-rule output of the final FCI orientation
- **Long description:** Yes to log the rule-by-rule output of the final FCI orientation (R1-R4 firings, discriminating path stamps, BK orientation). Separate from the verbose flag, which gives the search-level narrative (removals tried and committed, sepsets, saturating step) without this voluminous orientation output.
- **Value type:** Boolean
- **Default value:** false

### lowerBound

- **Short description:** Lower bound cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.3
- **Minimum:** 0.0
- **Maximum:** 1.0

### lvHeuristicOnly

- **Short description:** Yes if the LV-Heuristic result only should be returned; no if further tests are to be done.
- **Long description:** Yes if the Lv-Heuristic result only should be returned; no if further tests are to be done.
- **Value type:** Boolean
- **Default value:** false

## M

### manualLambda

- **Short description:** Lambda (manually set)
- **Long description:** The manually set lambda for GIC--the default is 10, though this should be set by the user to a good value.
- **Value type:** Double
- **Default value:** 10.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### maxBlockingPathLength

- **Short description:** Maximum path length for paths for searching for path blocking sets (-1 = no limit)
- **Long description:** The maximum length of paths to search for path blocking sets.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### maxCategories

- **Short description:** Maximum number of categories (min = 2)
- **Long description:** The maximum number of categories to be used for randomly generated discrete variables. The default is 2. This needs to be greater or equal to than the minimum number of categories.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

### maxCellsPerStratum

- **Short description:** Maximum contingency cells per stratum
- **Long description:** Upper bound on the number of cells allowed in a contingency table for a single stratum. Strata producing larger tables are skipped to avoid sparse or unstable likelihood-ratio statistics.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 4
- **Maximum:** 1000

### maxCorrelation

- **Short description:** Maximum absolute correlation considered
- **Long description:** For the Nandy rule, the absolute max correlation r. For the standard BIC or high-dimensional rule, the maximum absolute residual correlation.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### maxDegree

- **Short description:** The maximum degree of the graph (min = -1)
- **Long description:** An upper bound on the maximum degree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### maxDiscriminatingPathLength

- **Short description:** The maximum length for any discriminating path. -1 if unlimited (min = -1)
- **Long description:** See Spirtes, Glymour, and Scheines (2000) for the definition of discrimination path. Finding discriminating paths can be expensive. This sets the maximum length of such paths that the algorithm tries to find.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### maxDistinctValuesDiscrete

- **Short description:** The maximum number of distinct values in a column for discrete variables (min = 0)
- **Long description:** Discrete variables will be simulated using any number of categories from 2 up to this maximum. If set to 0 or 1, discrete variables will not be generated.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### maxIndegree

- **Short description:** Maximum indegree of graph (min = 1)
- **Long description:** An upper bound on the maximum indegree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### maxit

- **Short description:** MAXIT parameter (GLASSO) (min = 1)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Integer
- **Default value:** 10000
- **Minimum:** 1
- **Maximum:** 2147483647

### maxIterations

- **Short description:** The maximum number of iterations the algorithm should go through orienting edges
- **Long description:** In orienting, this algorithm may go through a number of iterations, conditioning on more and more variables until orientations are set. This sets that number.
- **Value type:** Integer
- **Default value:** 15
- **Minimum:** 0
- **Maximum:** 2147483647

### maxLatentSubsetSize

- **Short description:** Max cluster subset size for latent-latent edge removal
- **Long description:** Maximum size of cluster subsets tested when attempting to remove spurious latent-latent edges via conditional rank. In Trek-MIMIC, a latent-latent edge between two clusters is a candidate for removal if some subset of one cluster, of size up to this bound, yields a conditional rank of zero against the other cluster. Larger values allow more thorough pruning at the expense of combinatorial runtime cost; smaller values are faster but may retain spurious edges. A value of 1 restricts testing to individual cluster members only.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 20

### maxObservedLevelsPerVar

- **Short description:** Maximum observed levels per variable
- **Long description:** Maximum number of distinct observed levels retained for a discrete variable within a stratum. Variables with more levels are compressed to the most frequent levels to control table size.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 2
- **Maximum:** 1000

### maxOutdegree

- **Short description:** Maximum outdegree of graph (min = 1)
- **Long description:** An upper bound on the maximum outdegree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### maxPaxPOrientationHeuristicMaxLength

- **Short description:** The maximum path length to use for the max p heuristic version.
- **Long description:** The maximum path length to use for the max p heuristic version.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** 100000

### maxPOrientationMaxPathLength

- **Short description:** Maximum path length for the unshielded collider heuristic for max P (min = 0)
- **Long description:** For the Max P “heuristic” to work, it must be the case that X and Z are only weakly associated—that is, that paths between them are not too short. This bounds the length of paths for this purpose.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 2147483647

### maxPossibleSepPathLength

- **Short description:** The maximum length for searching for possible d-sep sets. -1 if unlimited (min = -1)
- **Long description:** The maximum length for searching for possible d-sep sets. -1 if unlimited (min = -1)
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### maxRank

- **Short description:** The algorithm looks for clusters from rank 1 up through this rank
- **Long description:** The algorithm looks for clusters from rank 1 up through this rank
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 1000

### maxRuns

- **Short description:** Cap on the total number of hill-climb runs (initial plus deferred)
- **Long description:** A hard cap on the number of hill-climb runs, ensuring the search terminates regardless of the split threshold.
- **Value type:** Integer
- **Default value:** 10000
- **Minimum:** 1
- **Maximum:** 1000000

### maxScoreDrop

- **Short description:** Maximum score drop for the process triples step
- **Long description:** In orienting unshielded colliders by examining triples of nodes, the score is permitted to drop by this much.
- **Value type:** Double
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** Infinity

### maxSepsetSize

- **Short description:** For testing steps in FCIT, the maximum conditioning set size
- **Long description:** In the extra edge removal step, we build conditioning sets based on the current PAG to attempt to remove adjacencies from the graph, by blocking paths from x to y of up to this length. This is the maximum size these sets are allowed to grow to.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 0
- **Maximum:** 2147483647

### mb

- **Short description:** Find Markov blanket(s)
- **Long description:** Looks for the graph over the Markov blanket(s) and target(s) if true
- **Value type:** Boolean
- **Default value:** false

### mcAlpha

- **Short description:** Markov Checker Alpha Level (0 to 1)
- **Long description:** Markov Checker Alpha Level (0 to 1)
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### meanHigh

- **Short description:** High end of mean range (min = 0.0)
- **Long description:** The default is for there to be no shift in mean, but shifts from a minimum value to a maximum value may be specified. The minimum must be less than or equal to this maximum.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### meanLow

- **Short description:** Low end of mean range (min = 0.0)
- **Long description:** The default is for there to be no shift in mean, but shifts from a minimum value to a maximum value may be specified. The minimum must be greater than or equal to this minimum.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### measurementVariance

- **Short description:** Additive measurement noise variance (min = 0.0)
- **Long description:** If the value is greater than zero, independent Gaussian noise will be added with mean zero and the given variance to each variable in the simulated output.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### mgmParam1

- **Short description:** MGM tuning parameter #1 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### mgmParam2

- **Short description:** MGM tuning parameter #2 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### mgmParam3

- **Short description:** MGM tuning parameter #3 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### mimbuildType

- **Short description:** Mimbuild type: 1 = PCA, 2 = Bollen
- **Long description:** Mimbuild type: 1 = PCA, 2 = Bollen
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### mimicGroupSpecs

- **Short description:** MIMIC: List of count:children:parents, comma separated; e.g. 5:6:3,2:8:3:
- **Long description:** List of count:children:parents, comma separated; e.g. 5:6:3,2:8:3
- **Value type:** String
- **Default value:** 5:6:3

### mimicNumSharedParents

- **Short description:** Number of measured parents shared between latent groups
- **Long description:** The number of measured variables that serve as a parent to more than one latent in the generated MIMIC structure. Shared parents are the impurity that makes the measurement model harder to recover, so setting this above zero is the way to test how a clustering algorithm degrades when purity fails.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### mimLatentGroupSpecs

- **Short description:** MIM: List of count:children:(rank), comma separated; e.g. 5:6(1),2:8(2):
- **Long description:** List of count:children:(rank), comma separated; e.g. 5:6(1),2:8(2)
- **Value type:** String
- **Default value:** 5:6(1)

### mimLatentMeasuredImpureParents

- **Short description:** MIM: Number of Latent --\> Measured impure edges
- **Long description:** It is possible for structural nodes to have as children measured variables that are children of other structural nodes. These edges in the graph will be considered impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimMeasuredMeasuredImpureAssociations

- **Short description:** MIM: Number of Measured \<-\> Measured impure edges
- **Long description:** It is possible for measures from two different structural nodes to be confounded. These confounding (bidirected) edges will be considered to be impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimMeasuredMeasuredImpureParents

- **Short description:** MIM: Number of Measured --\> Measured impure edges
- **Long description:** It is possible for measures from two different structural nodes to have directed edges between them. These edges will be considered to be impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimMetaEdgeConnectionType

- **Short description:** 1 = Cartesian Product 2 = Corresponding, 3 = Patchy Connections
- **Long description:** 1 = Cartesian Product 2 = Corresponding, 3 = Patchy Connections
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1

### mimMimNumStructuralNodes

- **Short description:** Number of measurements per Latent
- **Long description:** Each structural node in the MIM will be created to have this many measured children.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimNumChildrenPerGroup

- **Short description:** MIM: Number of children for each group latents
- **Long description:** Each group of latents shares a common set of children of this size.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimNumStructuralEdges

- **Short description:** MIM: Number of structural edges
- **Long description:** This is a parameter for generating random multiple indicator models (MIMs). A structural edge is an edge connecting two structural nodes.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### mimNumStructuralNodes

- **Short description:** Number of structural nodes
- **Long description:** This is a parameter for generating random multiple indicator models (MIMs). A structural node is one of the latent variables in the model; each structural node has a number of child measured variables.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### minCategories

- **Short description:** Minimum number of categories (min = 2)
- **Long description:** The minimum number of categories to be used for randomly generated discrete variables. The default is 2.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

### minCountPerCell

- **Short description:** The minimum count per cell in a chi square table.
- **Long description:** Increasing this can improve accuracy of chi square estimates.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

### minimaxFfFeatures

- **Short description:** Number of Fourier features (FF)
- **Long description:** Number of Fourier features used to represent nonlinear effects of continuous parents in the Minimax score. Larger values increase flexibility and runtime/memory cost; smaller values are faster but less expressive.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 0
- **Maximum:** 1000000

### minimaxFfSigma

- **Short description:** FF length scale (σ) — larger = smoother; smaller = more flexible.
- **Long description:** Bandwidth parameter (sigma) for the random Fourier feature construction used on continuous parents. Smaller sigma yields higher-frequency features (more local variation); larger sigma yields smoother features. This interacts with data scaling, so it is typically tuned relative to standardized inputs.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 1e-6
- **Maximum:** 1.0e6

### minimaxIrlsIters

- **Short description:** Maximum IRLS iterations
- **Long description:** Maximum number of IRLS (iteratively reweighted least squares) iterations used to fit Minimax local models. Increasing this may improve convergence for difficult problems but increases runtime.
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 10000

### minimaxMaxNu

- **Short description:** Maximum Student-t degrees of freedom (nu)
- **Long description:** Upper bound on the Student-t degrees of freedom parameter used by the Minimax-t model for continuous children. Smaller nu yields heavier tails (more robust to outliers); larger nu approaches a Gaussian. This parameter caps nu to prevent the fit from drifting to effectively Gaussian behavior.
- **Value type:** Double
- **Default value:** 30
- **Minimum:** 2
- **Maximum:** 1000

### minimaxPermutations

- **Short description:** Number of permutations
- **Long description:** Specifies the number of random permutations used to approximate the null distribution in the Minimax permutation procedure. This parameter applies both to the Minimax conditional independence test and to Minimax-based scores. Larger values yield more stable and accurate p-value or score estimates, especially for small significance levels, at the cost of increased computation time. Smaller values improve speed but may introduce Monte Carlo variability. Internally, a small minimum number of permutations may be enforced to ensure numerical stability of the resulting p-values.
- **Value type:** Integer
- **Default value:** 500
- **Minimum:** 1
- **Maximum:** 100000

### minimaxRidge

- **Short description:** Ridge penalty (L2) for Minimax regression/IRLS
- **Long description:** Ridge (L2) regularization strength used when fitting Minimax local conditional models. Larger values shrink coefficients more aggressively (more conservative, more stable, smaller edf); smaller values fit more closely to the data but may overfit and be numerically less stable.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0e12

### minimaxScale

- **Short description:** Scale for Fourier features (FF)
- **Long description:** Sets the scale used for constructing Fourier Features (FF) for continuous parents in the Minimax score. Larger values produce smoother features (longer length-scale); smaller values allow more rapid variation. This controls the effective complexity of the nonlinear parent representation.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 1e-6
- **Maximum:** 1.0e6

### minParamSampleSize

- **Short description:** The minimum sample size per parameter
- **Long description:** The minimum sample size per parameter
- **Value type:** Integer
- **Default value:** 20
- **Minimum:** 1
- **Maximum:** 100000000

### minSampleSizePerCell

- **Short description:** For conditional Gaussian, the minimum sample size per cell
- **Long description:** For conditional Gaussian, the minimum sample size per cell
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 100000000

### minStratumSize

- **Short description:** Minimum stratum size
- **Long description:** Minimum number of samples required for a conditioning stratum to be included in the test. Smaller strata are discarded to ensure stable estimation of contingency-table statistics.
- **Value type:** Integer
- **Default value:** 6
- **Minimum:** 1
- **Maximum:** 1000

### missingDataPolicy

- **Short description:** Missing-data policy: "default", "fail", "listwise", "testwise", "em", "pairwise", or "mi"
- **Long description:** How missing values in the dataset are handled by scores and independence tests. "default" preserves each component's historical behavior (typically test-wise deletion, with a logged warning). "fail" refuses data containing missing values. "listwise" deletes every row with at least one missing value up front. "testwise" uses, for each local calculation, only the rows complete on the variables involved; unbiased only if values are missing completely at random (MCAR). "em" estimates the covariance matrix once by expectation-maximization under a saturated Gaussian model and proceeds as complete data; valid under the weaker missing-at-random (MAR) assumption for approximately multivariate normal continuous data. "pairwise" also estimates one covariance matrix and proceeds as complete data, but by pairwise deletion: each correlation from the rows complete on its pair, rescaled by each variable's standard deviation over all its observed rows, and shrunk toward the identity just enough to be positive definite. It needs no model of the data and is accepted wherever "em" is, but is unbiased only under MCAR; choose a pairwise effective sample size mode with it. "mi" performs multiple imputation and is handled by a search wrapper over imputed datasets, not by a single score or test. Values are case-insensitive.
- **Value type:** String
- **Default value:** default

### missingEmMaxIterations

- **Short description:** Maximum EM iterations (default 1000; min 1)
- **Long description:** The maximum number of iterations for the EM covariance estimator. If the tolerance is not met within this many iterations, the estimate at the final iteration is used and the run is reported as not converged. Used only when missingDataPolicy is "em".
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### missingEmRidge

- **Short description:** Ridge for the EM covariance estimator (default 0.0; min 0.0)
- **Long description:** A nonnegative value added to the diagonal of the covariance matrix in the M-step of the EM covariance estimator, for numerical stability when the estimated matrix is near-singular. Used only when missingDataPolicy is "em".
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### missingEmTolerance

- **Short description:** Convergence tolerance for the EM covariance estimator (default 1.0E-6)
- **Long description:** The convergence tolerance for the observed-data log likelihood in the EM covariance estimator; iteration stops when the improvement falls below this value. Must be positive. Used only when missingDataPolicy is "em".
- **Value type:** Double
- **Default value:** 1.0E-6
- **Minimum:** 4.9E-324
- **Maximum:** 1.7976931348623157E308

### missingEssMode

- **Short description:** Effective sample size mode under the EM and test-wise policies: "fullN", "minPairwise", or "meanPairwise"
- **Long description:** How the effective sample size used by penalized scores (the n in BIC) is determined when the analysis runs on a covariance matrix estimated from incomplete data. "fullN" uses the nominal number of rows (anti-conservative when much data is missing). "minPairwise" uses the minimum, over variable pairs, of the number of rows on which both variables are observed (most conservative). "meanPairwise" uses the mean of those pairwise counts. Values are case-insensitive. Used when missingDataPolicy is "em" or, for the embedded scores (degenerate Gaussian and basis-function BIC), "testwise". Under test-wise deletion the BIC penalty already scales with each family's own row count, but the likelihood term is multiplied by the effective sample size; leaving that at "fullN" credits the fit with every row while charging the penalty for the family's actual rows, which biases the search toward denser graphs. For the embedded scores the mode is computed on the raw variables rather than the embedded columns, so that "meanPairwise" does not weight a variable by the width of its embedding block.
- **Value type:** String
- **Default value:** fullN

### missingNumImputations

- **Short description:** Number of imputed datasets for multiple imputation (default 10; min 1)
- **Long description:** The number of completed datasets, m, generated under multiple imputation. The search is run on each imputed dataset and the resulting graphs are pooled by edge frequency. Larger values give more stable pooled results at proportionally greater cost. With 1 there is nothing to pool: the result is the graph from one completed dataset, with no indication of how much it depends on the imputed values. Used only when missingDataPolicy is "mi".
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### missingTestwiseCommonRows

- **Short description:** Experimental: under the "testwise" policy, compute each local score comparison on the rows its two sides share
- **Long description:** Under test-wise deletion, the two sides of a local score comparison are by default fit on different row sets, so their difference is not a likelihood ratio of anything well defined, and searches tend to add too many edges. With this option, each comparison is instead computed on the rows complete on all of the variables it involves, making it a nested-model likelihood ratio on one sample, with the BIC penalty at that sample's own row count. This is honored only by searches that decide through local score differences (e.g., FGES) on scores that implement it (currently SEM BIC); searches that optimize a sum of local scores (BOSS, GRaSP) are unaffected by it, since their objective has no per-comparison row set. Precision is typically bought at a cost in recall, as fewer rows support each decision. Used only when missingDataPolicy is "testwise".
- **Value type:** Boolean
- **Default value:** false

### mnarNumExtraInfluences

- **Short description:** MNAR: The number of extra influences on missing value selection.
- **Long description:** MNAR: The number of extra influences on missing value selection.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### mnarNumVariablesWithMissing

- **Short description:** MNAR: The number of variables with missing values.
- **Long description:** MNAR: The number of variables with missing values.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** 2147483647

### mnarThreshold

- **Short description:** MNAR: Remove this fraction upper tail values for columns with missing values
- **Long description:** MNAR: Remove this fraction upper tail values for columns with missing values
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.0

## N

### noiseExpression

- **Short description:** Expression specifying how noise values are generated
- **Long description:** An expression in the Tetrad expression language specifying how noise values should be sampled for the error term in the model. The expression is evaluated independently for each sample to produce a noise value. The expression may use any supported random generators and arithmetic operations defined in the expression language.
- **Value type:** String
- **Default value:** N(0, Uniform(1, 3))

### noRandomlyDeterminedIndependence

- **Short description:** Yes, if using the cutoff threshold for the independence test.
- **Long description:** null
- **Value type:** Boolean
- **Default value:** false

### numBasisFunctions

- **Short description:** Number of functions to use in (truncated) basis
- **Long description:** This parameter specifies how many of the most significant basis functions to use as a basis.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

### numberOfExpansions

- **Short description:** Number of expansions of the algorithm away from the target
- **Long description:** Each expansion iterates to concentrically more variables
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 1000

### numberResampling

- **Short description:** The number of bootstraps/resampling iterations (min = 0)
- **Long description:** For bootstrapping, the number of bootstrap iterations that should be done by the algorithm, with results summarized.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### numBscBootstrapSamples

- **Short description:** The number of bootstrappings drawing from posterior dist. (min = 1)
- **Long description:** The number of bootstrappings drawing from posterior dist. (min = 1)
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 2147483647

### numCategories

- **Short description:** Number of categories for discrete variables (min = 2)
- **Long description:** The number of categories to be used for randomly generated discrete variables. The default is 4; the minimum is 2.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 2147483647

### numCategoriesToDiscretize

- **Short description:** The number of categories used to discretize continuous variables, if necessary (min = 2)
- **Long description:** In case the exact algorithm is not used for discrete children and continuous parents is not used, this parameter gives the number of categories to use for this second (discretize) backup copy of the continuous variables.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

### numFactors

- **Short description:** Number of factors to extract
- **Long description:** The number of latent factors the factor analysis extracts. This is fixed in advance rather than estimated, so it should be set from theory or from a scree plot on the same data.
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2147483647

### numFfFeatures

- **Short description:** Number of Fourier features used for nonlinear continuous effects
- **Long description:** Number of random Fourier (or orthogonal random) features used to approximate the continuous kernel in feature-function (FF)–based scores. Increasing this value improves the accuracy of the kernel approximation and allows more flexible nonlinear modeling of continuous parents, but increases runtime and memory usage. Smaller values are faster but provide a coarser approximation of nonlinear effects.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 1
- **Maximum:** 1000000

### numLags

- **Short description:** The number of lags in the time lag model
- **Long description:** A time lag model may take variables from previous time steps into account. This determines how many steps back these relevant variables might go.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### numLatents

- **Short description:** Number of additional latent variables (min = 0)
- **Long description:** The number of additional latent variables to include in the datasets
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### numMeasures

- **Short description:** Number of measured variables (min = 1)
- **Long description:** The number of measured (recorded in data) variables to include in the dataset.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### numRandomizedSearchModels

- **Short description:** The number of search probabilistic model (min = 1)
- **Long description:** The number of search probabilistic model (min = 1)
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### numRuns

- **Short description:** Number of runs (min = 1)
- **Long description:** An analysis(randomly pick graph, randomly simulate a dataset, run an algorithm on it, look at the result) may be run over and over again this many times.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

### numStarts

- **Short description:** The number of restarts of the search (default 1)
- **Long description:** The number of times the algorithm should be started and run to completion, with the best-scoring result kept. By default, restarts after the first begin from fresh random orders. Some algorithms offer an alternative restart style; for example, BOSS with the useIlsRestarts option perturbs the best order found so far (iterated local search) instead of starting from a fresh random order.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

### numSub-samples

- **Short description:** Number of sub-samples
- **Long description:** Number of sub-samples
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 500000

### numSubsamples

- **Short description:** The number of subsamples to generate.
- **Long description:** CStaR works by generating subsamples and summarizing across them; this specified the number of subsamples to generate. Must be \>= 1. effects in the CStaR table
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 100000

### numThreads

- **Short description:** The number of threads (\>= 1) to use for the search
- **Long description:** The number of threads to use for the search.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

## O

### optimalAcrossBranches

- **Short description:** Yes to consider every ordering visited across all branches, not just each branch's optimum
- **Long description:** When Yes, orderings that are suboptimal within their own branch are also eligible for the top-k list.
- **Value type:** Boolean
- **Default value:** false

### orientAndPrune

- **Short description:** Orient latent-latent edges and prune transitive inputs
- **Long description:** If enabled, Trek-MIMIC will attempt to orient the latent-latent edges in the output graph and prune away transitive measured inputs that are not identifiable given the latent structure. Orienting latent-latent edges recovers causal direction among the latents where possible; pruning transitive inputs removes measured cause nodes whose influence is fully mediated by other latents and therefore cannot be distinguished from direct effects. Disable to retain the unoriented skeleton and all measured inputs as found.
- **Value type:** Boolean
- **Default value:** true
- **Minimum:** false
- **Maximum:** true

### orientationAlpha

- **Short description:** Alpha threshold used for orientation (where necessary). ('0' turns this off.)
- **Long description:** Used for orienting 2-cycles and testing for zero edges.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### orientTowardMConnections

- **Short description:** Yes if Richardson's step C (orient toward d-connection) should be used
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

### orientVisibleFeedbackLoops

- **Short description:** Yes if visible feedback loops should be oriented
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

### osDegradeCensorProp

- **Short description:** Fraction of continuous system and outcome variables censored at a detection limit (min = 0.0, max = 1.0)
- **Long description:** That fraction of the continuous, non-ordinalized system and outcome variables is censored at a detection limit: values beyond the limit are recorded AT the limit, with the side (right or left) chosen at random and the limit placed at the osDegradeCensorQuantile quantile. Rows are kept; this is measurement, not selection, and the true graph is unchanged. (The row-removal analogue, truncation, is selection; see the Designed Experiment simulation's deSelection.)
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### osDegradeCensorQuantile

- **Short description:** Quantile at which the censoring limit is placed (min = 0.5, max = 1.0)
- **Long description:** For right-censoring the limit is at this quantile of the column; for left-censoring, at one minus this quantile. E.g., 0.9 censors the top (or bottom) 10 percent of values to the limit.
- **Value type:** Double
- **Default value:** 0.9
- **Minimum:** 0.5
- **Maximum:** 1.0

### osDegradeMissingMechanism

- **Short description:** Missingness mechanism: none, mcar, mar, or mnar
- **Long description:** If not none, cells of system, index, and outcome variables are marked missing at an exact per-column rate of osDegradeMissingProp (context variables are always fully observed). mcar is independent of everything. mar is driven by the first observed context variable, which is fully observed, so missingness is at random given context. mnar is driven by the underlying value of the cell itself. In each case the missing cells are those with the highest driver-plus-noise scores, so the mechanism is probabilistic but the rate is exact.
- **Value type:** String
- **Default value:** none

### osDegradeMissingProp

- **Short description:** Fraction of cells marked missing per eligible column (min = 0.0, max = 1.0)
- **Long description:** The exact per-column missingness rate applied to system, index, and outcome variables when osDegradeMissingMechanism is not none.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.0

### osDegradeOrdinalizeProp

- **Short description:** Fraction of system variables recorded as ordered categories (min = 0.0, max = 1.0)
- **Long description:** That fraction of system variables is generated continuous but RECORDED as ordered categories at random cutpoints (osTypeNumCategories levels) -- measurement coarsening. This reproduces the ordinal nominal-coding pathology: the true graph is the graph of the underlying continuous system, and the coarsening is measurement.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### osFormIndexNoise

- **Short description:** Noise standard deviation for index variables (min = 0.0)
- **Long description:** The noise standard deviation of index variables; small values make indices near-deterministic functions of their parents.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### osFormInteraction

- **Short description:** Pairwise-interaction weight for index and outcome functions (min = 0.0, max = 1.0)
- **Long description:** The weight of pairwise products of continuous parents in index and outcome functions, relative to the additive part.
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** 1.0

### osFormNonlinearity

- **Short description:** Monotone transmission nonlinearity weight (min = 0.0, max = 1.0)
- **Long description:** The mixing weight of a random strictly monotone map (sinh, asinh, signed power, or exponential) applied to each continuous parent's value before it enters a child. 0 gives linear transmission.
- **Value type:** Double
- **Default value:** 0.3
- **Minimum:** 0.0
- **Maximum:** 1.0

### osGraphAvgSystemDegree

- **Short description:** Average degree of the system DAG (min = 0.0)
- **Long description:** The average degree of the DAG among the system variables.
- **Value type:** Double
- **Default value:** 2.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### osGraphEdgeDensity

- **Short description:** Multiplier on all cross-role edge probabilities (min = 0.0, max = 1.0)
- **Long description:** Scales all cross-role edge inclusion probabilities in the Observational Study simulation: context to system (base 0.4), system to index (0.5), index to index (0.4), context to index (0.2), and the parent probabilities of outcomes (system 0.5, index 0.7, context 0.3). 1.0 gives the base densities; smaller values give sparser graphs. The density of the DAG among the system variables is controlled separately by osGraphAvgSystemDegree. Minimum-parent floors (indices get at least two system parents, outcomes at least two parents) are kept regardless.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### osGraphNumContext

- **Short description:** Number of observed context variables (min = 0)
- **Long description:** In the Observational Study simulation, the number of exogenous context variables (C1, ...): weather, season, region, demographics. A fraction osTypePropContextDiscrete are discrete; the rest continuous. In serial mode continuous context is AR(1) and discrete context is a sticky Markov chain.
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 2147483647

### osGraphNumHiddenContext

- **Short description:** Number of hidden context variables (min = 0)
- **Long description:** Context variables that influence the system but are OMITTED from the dataset -- latent confounders. They appear in the true graph as latent nodes, so FCI-style evaluation is possible.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### osGraphNumIndices

- **Short description:** Number of index variables (min = 0)
- **Long description:** Near-deterministic functions (noise osFormIndexNoise) of system variables and earlier index variables (chains, like the FWI system's ISI/BUI -\> FWI). In serial mode each index is a recursive accumulator with memory drawn from \[osSerialIndexMemoryLow, osSerialIndexMemoryHigh\].
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 2147483647

### osGraphNumOutcomes

- **Short description:** Number of outcome variables (min = 0)
- **Long description:** Outcome variables (Y1, ...) depending on system, index, and context variables with pairwise interactions (weight osFormInteraction). Discrete via softmax if osTypeDiscreteOutcome.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

### osGraphNumSystem

- **Short description:** Number of system variables (min = 1)
- **Long description:** The number of variables in the causal system proper (S1, ...), forming a DAG among themselves with average degree osGraphAvgSystemDegree, with context parents.
- **Value type:** Integer
- **Default value:** 6
- **Minimum:** 1
- **Maximum:** 2147483647

### osPanelEmitSubjectColumn

- **Short description:** Append a discrete SUBJECT column naming each row's subject in the stacked dataset (requires osPanelNumSubjects \> 1)
- **Long description:** If set with osPanelNumSubjects greater than 1, a discrete bookkeeping column named SUBJECT is appended to the stacked dataset, giving each row's subject - the analogue of deEmitConfigColumn in the designed-experiment simulation and of the TOWN column in the corrected Boston Housing data. Its purpose is to let the panel structure be named: as the data audit's serial grouping variable (per-block centering), as the block column for within-block centering, or as a tier-0 fixed-effects variable in a knowledge-constrained search. The column is bookkeeping, not a variable of the system, and is not in the true graph; unless used as a grouping or tier variable it should be excluded from search. With one category per subject it will trip the many-discrete-levels audit finding if treated as an ordinary variable. Ignored when osPanelEmitSubjectsAsDataSets is on, where the column would be constant.
- **Value type:** Boolean
- **Default value:** false

### osPanelEmitSubjectsAsDataSets

- **Short description:** Emit each subject as its own data model instead of stacking them (requires osPanelNumSubjects \> 1)
- **Long description:** If set with osPanelNumSubjects greater than 1, each subject is emitted as a separate data model sharing the run's true graph, so the number of data models is numRuns times osPanelNumSubjects and getSubjectStarts returns \{0\} for each. This is the convention consumed by multi-data-set algorithms such as IMaGES, and by score pooling generally: in a comparison these algorithms are handed the simulation's data models and sum their scores across them, so each subject is scored from its own covariance and per-subject intercepts and slopes are absorbed. Note that a comparison draws its pooled selection from all data models, so with numRuns greater than 1 and differentGraphs on, subjects from different runs, with different graphs, would be pooled; use numRuns = 1, or turn differentGraphs off, in this mode. When off, the subjects are concatenated into one dataset per run.
- **Value type:** Boolean
- **Default value:** false

### osPanelNumSubjects

- **Short description:** Number of independent subjects (min = 1)
- **Long description:** The sample is divided into this many independent subjects: replicates of the same system, sampleSize / osPanelNumSubjects rows each. Each subject has a random intercept on the system variables, which is a subject-level latent confounder in the pooled data. By default the subjects are concatenated into one dataset per run with the structure undeclared, as panel data usually arrive; subject start rows are then available from getSubjectStarts, and in serial mode lagging must not cross subject boundaries. See osPanelEmitSubjectColumn to name the structure in the stacked dataset, and osPanelEmitSubjectsAsDataSets to emit one data model per subject instead.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

### osPanelSubjectShiftSd

- **Short description:** Standard deviation of each subject's random intercept on the system variables (min = 0.0)
- **Long description:** With osPanelNumSubjects greater than 1, each subject draws an independent random intercept for each system variable from a normal distribution with this standard deviation (for a discrete system variable, one such draw per category on its logits). System variables are on roughly unit scale before pooled standardization, so 0.5 displaces subjects by about half a standard deviation. The intercept is a pure offset on the variable that owns it, and within-subject centering removes it there exactly. It becomes a confounder that centering cannot remove only where it reaches a child through a nonlinear transmission map: the subject then sits on a different part of the curve, and the within-subject relationship differs in shape, not just in level. Larger values move subjects further along the map; larger osFormNonlinearity bends the map more. Either makes the panel structure harder to correct for. Set to 0 for subjects that are exact replicates. Ignored when osPanelNumSubjects is 1.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### osSerialArCoef

- **Short description:** AR(1) coefficient for continuous context in serial mode (min = 0.0, max \< 1.0)
- **Long description:** The autoregression coefficient of continuous context variables in serial mode; the process is stationary with unit variance.
- **Value type:** Double
- **Default value:** 0.7
- **Minimum:** 0.0
- **Maximum:** 1.0

### osSerialIndexMemoryHigh

- **Short description:** High end of the index accumulator memory range (min = 0.0, max \< 1.0)
- **Long description:** See osSerialIndexMemoryLow.
- **Value type:** Double
- **Default value:** 0.9
- **Minimum:** 0.0
- **Maximum:** 1.0

### osSerialIndexMemoryLow

- **Short description:** Low end of the index accumulator memory range (min = 0.0, max \< 1.0)
- **Long description:** In serial mode, each index variable's accumulator memory delta (I\{t\} = delta I\{t-1\} + g(parents) + noise) is drawn uniformly from \[osSerialIndexMemoryLow, osSerialIndexMemoryHigh\] -- heterogeneous memory, from FFMC-like short memory to DC-like drought memory.
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** 1.0

### osSerialMaxLag

- **Short description:** Maximum lag of the time series; 0 turns serial dependence off (min = 0)
- **Long description:** If greater than 0, one time series per subject is generated, and the true graph is a time lag graph with this maximum lag, following the time-series conventions. Self-lags, AR(1) context, and index accumulators act at lag 1; each cross-lag edge acts at a lag drawn uniformly from 1 to osSerialMaxLag. If 0, rows are i.i.d. and the true graph is an ordinary DAG.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### osSerialPropCrossLag

- **Short description:** Probability of a cross-lag edge per ordered system pair (min = 0.0, max = 1.0)
- **Long description:** In serial mode, for each ordered pair of distinct system variables (X, Y), the edge X\{t-1\} -\> Y\{t\} is included with this probability. Reciprocal cross-lags represent feedback honestly.
- **Value type:** Double
- **Default value:** 0.15
- **Minimum:** 0.0
- **Maximum:** 1.0

### osTypeDiscreteOutcome

- **Short description:** Yes if outcomes are discrete via softmax
- **Long description:** If yes, outcome variables are discrete, sampled from softmax logits that are linear in the (soft-clipped) parent values -- continuous-parents-to-discrete-child, logistic style.
- **Value type:** Boolean
- **Default value:** false

### osTypeNumCategories

- **Short description:** Number of categories for discrete variables (min = 2)
- **Long description:** The number of levels for discrete context variables, discrete outcomes, and ordinalized system variables.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

### osTypePropContextDiscrete

- **Short description:** Fraction of observed context variables that are discrete (min = 0.0, max = 1.0)
- **Long description:** A fixed count, round(osTypePropContextDiscrete times osGraphNumContext), of the observed context variables is made discrete, chosen at random (osTypeNumCategories levels, uniform, or a sticky Markov chain in serial mode); the rest are continuous. Discrete parents act through level-specific shifts (conditional Gaussian style). No random draws are made when the count is zero, so existing seeds are unaffected by a setting of 0.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### osTypePropSystemDiscrete

- **Short description:** Fraction of system variables that are discrete (min = 0.0, max = 1.0)
- **Long description:** A fixed count, round(osTypePropSystemDiscrete times osGraphNumSystem), of the system variables is made discrete with osTypeNumCategories levels, chosen at random. Unlike ordinalization, these are genuinely discrete causes: each is generated from its parents through softmax logits, as discrete outcomes are, and enters its children through per-category shifts, as discrete context does, so a discrete variable can sit inside the causal system with both parents and children. That is the case in which conditional-Gaussian and degenerate-Gaussian treatments of mixed data differ most, and the one that discrete context and outcomes alone cannot produce. Discrete system variables are never ordinalized or censored. In serial mode each has a sticky self-lag, keeping its previous value with probability equal to its self-lag coefficient and otherwise being redrawn from its parents, and takes part in no cross-lag edges. In panel mode the subject effect is a per-category shift on its logits. No random draws are made when the count is zero, so existing seeds are unaffected by the default.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### otherPermMethod

- **Short description:** 1 = RCG, 2 = GSP, 3 = ESP, 4 = SP
- **Long description:** RCG (Random Carnival Game); GSP ("Greedy SP") GSP using tucking ESP ("Edge SP") is from Solus et al. SP ("Sparsest Permutation") Raskutti and Uhler
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

### outputCpdag

- **Short description:** Yes if CPDAG should be output, no if a DAG.
- **Long description:** BOSS can output a DAG or the CPDAG of the DAG. Additional knowledge will be taken into account.
- **Value type:** Boolean
- **Default value:** true

### outputRBD

- **Short description:** Constraint Scoring: Yes: Dependent Scoring, No: Independent Scoring.
- **Long description:** Constraint Scoring: Yes: Dependent Scoring, No: Independent Scoring.
- **Value type:** Boolean
- **Default value:** true

## P

### parallelized

- **Short description:** Yes if the search should be parallelized
- **Long description:** This search is capable of being parallelized; select yes if the search should be parallelized, not if it should be run in a single thread
- **Value type:** Boolean
- **Default value:** true

### pathsMaxDistanceFromEndpoint

- **Short description:** The maximum distance of an allowable node from the endpoint of a path for adjustment
- **Long description:** In order to give guidance to which adjustment sets to report, this parameter lets one give a maximum distance from the endpoint of a path for a node to be included in an adjustment set.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 100000

### pathsMaxLength

- **Short description:** The maximum length of a path to report
- **Long description:** Since paths may be long, especially for large graphs, this parameter allows one to limit the length of a path to report. It must be at least 2.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 2
- **Maximum:** 100000

### pathsMaxLengthAdjustment

- **Short description:** The maximum length of a backdoor path to consider for adjustment.
- **Long description:** The maximum length of a backdoor path to consider for finding an adjustment set. Amenable paths of any length are considered.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 2
- **Maximum:** 100000

### pathsMaxNumSets

- **Short description:** The maximum number of adjustment sets to output
- **Long description:** There may be too many legal adjustments to sets to output; this places a bound on how many to output. These will be listed in order of increasing size.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 0
- **Maximum:** 100000

### pathsNearWhichEndpoint

- **Short description:** 1 = near source, 2 = near target, 3 = near either
- **Long description:** Adjustment sets may be found near the source, near the target, or near either.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### pcHeuristic

- **Short description:** Heuristics to stabilize skeleton: 0 = None, 1 = Heuristic 1, 2 = Heuristic 2, 3 = Heuristic 3
- **Long description:** NONE = no heuristic, PC-1 = sort nodes alphabetically; PC-1 = sort edges by p-value; PC-3 = additionally sort edges in reverse order using p-values of associated independence facts. See CPS.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 3

### pcOrderRefinement

- **Short description:** Yes if PC's result should be refined by a permutation search using the same independence test
- **Long description:** If Yes, a causal order is read off the PC result and used as the starting permutation for GRaSP, run with the same independence test and no score; the CPDAG of the refined permutation is returned. Each adjacency is then decided by a test given the candidate parents of the later variable instead of by any accepting subset of neighbors, which recovers edges PC removes by conditioning on descendants. The result need not contain or be contained in the PC result. Not applied to time-lag (replicating) searches.
- **Value type:** Boolean
- **Default value:** false

### pcRefinementAlpha

- **Short description:** Cutoff for p values in PC's order refinement step (0 = use alpha)
- **Long description:** The alpha used by the independence test during PC's order refinement step. In that step each retained edge rests on a single test, so a stricter cutoff than PC's own alpha is usually appropriate. A value of 0 uses the test's alpha unchanged. Ignored unless pcOrderRefinement is Yes.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.0

### penaltyDiscount

- **Short description:** Penalty discount (default = 2.0; min = 0.0)
- **Long description:** The parameter c in a modified BIC-style score of the form 2L – c k ln N, where L is the log-likelihood, k is the effective number of degrees of freedom, and N is the sample size.
- **Value type:** Double
- **Default value:** 2.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### penaltyDiscountDefault1

- **Short description:** Penalty discount (min = 0.0, default = 1.0)
- **Long description:** The parameter c added to a modified BIC score of the form 2L – c k ln N, where L is the likelihood, k the number of degrees of freedom, and N the sample size. Higher c yields sparser graphs. A value of 1.0 corresponds to the classical BIC penalty scaling.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### penaltyDiscountZs

- **Short description:** Penalty discount (min = 0.0)
- **Long description:** The parameter c added to a modified BIC score of the form 2L – c k lambda, where L is the likelihood, k the number of degrees of freedom, and lambda the choice of GIC lambda. Higher c yield sparser graphs.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### percentDiscrete

- **Short description:** Percentage of discrete variables (0 - 100) for mixed data
- **Long description:** For a mixed data type simulation, specifies the percentage of variables that should be simulated (randomly) as discrete. The rest will be taken to be continuous. The default is 0—i.e. no discrete variables.
- **Value type:** Double
- **Default value:** 50.0
- **Minimum:** 0.0
- **Maximum:** 100.0

### percentResampleSize

- **Short description:** The percentage of resample size (min = 10%)
- **Long description:** This parameter specifies the percentage of records in the bootstrap (as a percentage of the total original sample size of the data being bootstrapped).
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 10
- **Maximum:** 100

### percentStability

- **Short description:** Proportion of subsample graphs in which an edge must appear to be retained
- **Long description:** In stability selection, the wrapped algorithm is run on many subsamples and an edge is placed in the output graph when it appears, with the same orientation, in more than this proportion of the subsample graphs. Higher values yield sparser and more conservative graphs. Note that because orientation must also agree, edges whose direction is unstable are dropped even when adjacency is stable.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### percentSubsampleSize

- **Short description:** Size of each subsample as a proportion of the full sample
- **Long description:** The proportion of rows drawn for each subsample in stability selection and in StARS. The customary choice is one half, which keeps subsamples large enough to be informative while making them differ enough from one another for instability to be measurable.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

### piThr

- **Short description:** A fixed threshold for calculating E\[V\] and PCER
- **Long description:** A fixed threshold, default 0.5
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0
- **Maximum:** 1

### poissonLambda

- **Short description:** Lambda parameter for the Poisson distribution (\> 0)
- **Long description:** Lambda parameter for the Poisson distribution
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 1e-10
- **Maximum:** Infinity

### polynomialConstant

- **Short description:** For polynomial kernel: The constant
- **Long description:** The constant of the polynomial kernel, if used, which determine tradeoff between higher and lower order terms
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 5000

### polynomialDegree

- **Short description:** For polynomial kernel: The degree
- **Long description:** The degree of the polynomial kernel, if used
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 5000000

### poolDataSets

- **Short description:** Yes if the data sets should be pooled into one search (IMaGES-style) rather than searched separately
- **Long description:** When several data sets with the same variables are given (for example, several subjects, sessions, or regions), Yes runs the algorithm ONCE with its score replaced by the sum of that score over the data sets (the IMaGES score) and/or its independence test replaced by the Fisher combination of the per-data-set p-values. So BOSS with any score pooled is IMaGES with that score, and PC with any test pooled is a pooled PC. No (the default) runs the algorithm separately on each data set and returns one graph per data set. Time lags are applied to each data set separately before pooling, and bootstrapping resamples rows within each data set. Pooling assumes the data sets share one causal structure and are independent of one another.
- **Value type:** Boolean
- **Default value:** false

### pooledTestMethod

- **Short description:** How per-data-set p-values are combined when data sets are pooled: fisher or tippett
- **Long description:** When several data sets are pooled (poolDataSets = Yes) for a test-based search, each independence fact is tested in every data set and the resulting p-values are combined into one. "fisher" (the default) uses Fisher's method, -2 times the sum of the log p-values referred to a chi-square distribution; it is the most powerful choice when the dependence, if present, is present in all data sets, and its power grows with the number of data sets. "tippett" uses the smallest p-value with a Sidak adjustment for the number of data sets; it is more powerful when a dependence is present in only some of the data sets, at a small cost in power when it is present in all of them, and is somewhat more sensitive to a single outlying data set. Both assume the data sets are independent of one another.
- **Value type:** String
- **Default value:** fisher

### poolImputations

- **Short description:** Yes if several imputations of one data set should be searched as one, pooling each test over them (default no)
- **Long description:** When the data are several imputations of one data set with missing values (for example, from the Impute Missing Values box with more than one imputation), Yes runs the algorithm ONCE. Each statistical test is computed on every imputation and the results are combined by the rule of Li, Meng, Raghunathan, and Rubin (1991) for chi-square statistics from multiply imputed data, so that disagreement among the imputations counts against rejecting; any score-based stage uses the average of the imputations' covariance matrices. No (the default) runs the algorithm separately on each imputation and returns one graph per imputation, which can differ a great deal. This is not the poolDataSets option: imputations share their observed values and are not independent data sets. The combining rule is an approximation that assumes values missing at random and improves with more imputations; ten or more is a reasonable number. It has no effect with a single data set. In the Latent Clusters box, where the clustering algorithms make all of their decisions from a covariance matrix, Yes runs the chosen algorithm on the average of the imputations' covariance matrices at the full sample size. That average is the multiple-imputation point estimate of the covariance; the disagreement among the imputations is not carried into it, so running the tests at the full sample size would treat the data as complete. When the effectiveSampleSize parameter is left at -1, the pooled run therefore estimates an effective sample size from the disagreement among the imputations (Rubin's rules applied to the Fisher-z correlations, taking the least well determined pair) and runs the tests at that size, reporting it in the log; setting effectiveSampleSize overrides the estimate.
- **Value type:** Boolean
- **Default value:** false

### precomputeCovariances

- **Short description:** True if covariance matrix should be precomputed for tabular continuous data
- **Long description:** For more than 5000 variables or so, set this to false in order to calculate covariances on the fly from data.
- **Value type:** Boolean
- **Default value:** true

### preserveMarkov

- **Short description:** Preserve the Markov property (checking MBs) if initial graph is Markov
- **Long description:** The Markov property checking MBs says that if msep(x, y \| MB(x)) then x \_\|\|\_ y \| MB(x). Checking true for this property will tell the algorithm to ensure this property if the scoring step produces a Markov graph. Not applicable when running the algorithm from Oracle.
- **Value type:** Boolean
- **Default value:** false

### priorEquivalentSampleSize

- **Short description:** Prior equivalent sample size (min = 1.0)
- **Long description:** This sets the prior equivalent sample size. This number is added to the sample size for each conditional probability table in the model and is divided equally among the cells in the table.
- **Value type:** Double
- **Default value:** 10.0
- **Minimum:** 1.0
- **Maximum:** 1.7976931348623157E308

### probabilityOfEdge

- **Short description:** Probability of an adjacency being included in the graph
- **Long description:** Every possible adjacency in the graph is included it the graph with this probability.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### probCycle

- **Short description:** The probability of adding a cycle to the graph
- **Long description:** Sets the probability that any particular set of 3, 4, or 5 of nodes will be used to form a cycle in the graph.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### probRemoveColumn

- **Short description:** Probability of randomly removing a column from a dataset
- **Long description:** For testing algorithms with overlapping variables, columns may be removed from datasets with this probability.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### probTwoCycle

- **Short description:** The probability of creating a 2-cycles in the graph (0 - 1)
- **Long description:** Any edge X\*-\*Y may be replaced with a 2-cycle (feedback loop) between X and Y with this probability.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### pythonCiServer

- **Short description:** Path to Python CI server script
- **Long description:** Absolute path to the Python CI server script (e.g., kci\_server.py) used for Python-based CI tests. If left blank, Tetrad will use the bundled server script shipped inside the Tetrad JAR and extract it to a local cache directory at runtime.
- **Value type:** String
- **Default value:** Use bundled script
- **Minimum:** N/A
- **Maximum:** N/A

### pythonExe

- **Short description:** Path to Python executable for Python-based CI tests
- **Long description:** Absolute path to the Python interpreter used to run the external CI server process. This should typically point to the Python executable inside a dedicated virtual environment that has the required packages installed (e.g., causal-learn and its dependencies).
- **Value type:** String
- **Default value:** /Users/josephramsey/venvs/kci/bin/python
- **Minimum:** N/A
- **Maximum:** N/A

## R

### randomizeColumns

- **Short description:** Yes if the order of the columns in each dataset should be randomized
- **Long description:** In the real world where unfaithfulness is an issue the order of variables in the data may for some algorithms affect the output. For testing purposes, if Yes, the data columns are randomly re-ordered.
- **Value type:** Boolean
- **Default value:** true

### randomSelectionSize

- **Short description:** The number of datasets that should be taken in each random sample
- **Long description:** The number of dataset that should be taken in each random sample of datasets.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### raRadius

- **Short description:** Radius of search for Recursive Adjustment (-1 = no limit)
- **Long description:** The maximum distance from and endpoint to look for conditioning nodes, for Recursive Adjustment
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### rbRadius

- **Short description:** Radius of search for Recursive Blocking (-1 = no limit)
- **Long description:** The maximum distance from and endpoint to look for conditioning nodes, for Recursive Blocking
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### rcit.approx

- **Short description:** Null approximation method: 1 = Gamma, 2 = Saddlepoint, 3 = Davies-Imhof, 4 = Permutation
- **Long description:** 1 = Gamma / Satterthwaite Approximation 2 = Saddlepoint / Lugannani–Rice Approximation 3 = Davies / Imhof (Exact) Inversion Methods 4 = Permutation test
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

### rcit.centerFeatures

- **Short description:** Center feature matrices
- **Long description:** If true, center random-feature matrices before regression and test-statistic computation. Recommended for numerical stability and alignment with kernelized formulations.
- **Value type:** Boolean
- **Default value:** true

### rcit.lambda

- **Short description:** Ridge regularization (λ)
- **Long description:** Ridge penalty used when residualizing feature maps of X and Y against Z. Prevents ill-conditioning when Z features are collinear.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### rcit.numFeaturesXY

- **Short description:** Random Fourier features for X and Y
- **Long description:** Number of random Fourier features for the tested variables X and Y. Small values (e.g., 3–10) often suffice; increasing improves power but adds cost.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### rcit.numFeaturesZ

- **Short description:** Random Fourier features for Z
- **Long description:** Number of random Fourier features used to represent the conditioning set Z. Larger values are more accurate but slower; values in the 50–300 range are typical.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 1
- **Maximum:** 2147483647

### rcit.permutations

- **Short description:** Permutations for "perm" approx
- **Long description:** Number of permutations used when rcit.approx = "perm". Ignored for analytic approximations (lpd4, hbe, gamma, chi2).
- **Value type:** Integer
- **Default value:** 500
- **Minimum:** 1
- **Maximum:** 2147483647

### rcit.rcitMode

- **Short description:** Use RCIT (true) or RCoT (false)
- **Long description:** Chooses between the two randomized kernel tests: RCIT augments Y with Z features (tests X ⟂ Y,Z \| Z), while RCoT uses only X and Y features with residualization against Z. In the original RCIT code base this switch is exposed as rcit=True/False.
- **Value type:** Boolean
- **Default value:** true

### rcitNumF

- **Short description:** Number of random Fourier features for the conditioning set
- **Long description:** The number of random Fourier features used to approximate the kernel over the conditioning set in the external RCIT test. More features give a closer approximation to the exact kernel test and more power, at a roughly linear cost in time and memory.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 1
- **Maximum:** 2147483647

### rcitNumF2

- **Short description:** Number of random Fourier features for the two variables being tested
- **Long description:** The number of random Fourier features used for the pair of variables whose independence is being tested in the external RCIT test. This is normally much smaller than rcitNumF, since only two variables are involved rather than the whole conditioning set.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 1
- **Maximum:** 2147483647

### rcitNumFeatures

- **Short description:** The number of random features to use
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

### recoveryOddsThreshold

- **Short description:** Posterior-odds threshold at or above which a clash triggers edge recovery rather than a mark
- **Long description:** The posterior-odds threshold (base rate times likelihood ratio, PcAR Sec. 14) at or above which a tier-1 clash is recovered (edge reinstated) rather than merely marked as contested. Only has an effect when rescueAction=2 (RECOVER) and a RecoveryOddsEstimator has been wired. Default 1.0 is the paper's own non-conservative endpoint: recover exactly when posterior odds favor a present edge over no edge (posterior probability \>= 0.5), rather than an arbitrary large number chosen to suppress recovery. With the base-rate-only estimator wired in the algcomparison wrapper (PcAR#paperCancellationBaseRateOdds), this threshold will rarely be met at realistic sample sizes, since that estimator omits the likelihood-ratio term -- this reflects the paper's own finding that base-rate evidence alone is seldom sufficient, not a miscalibration of the threshold.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** Infinity

### recursive

- **Short description:** Yes if the algorithm should proceed recursively, no if not
- **Long description:** Where recursive or nonrecursive variants of an algorithm are available, this selects which one to use.
- **Value type:** Boolean
- **Default value:** false

### recursiveDepth

- **Short description:** Depth of recursive operations (-1 = no limit)
- **Long description:** Depth of recursive operations (-1 = no limit)
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### regularizationLambda

- **Short description:** Small number \>= 0 Add lambda to the the diagonal of correlation/covariance matrices. Default 1e-8.
- **Long description:** Small number \>= 0 Add lambda to the the diagonal of correlation/covariance matricers. Default 1e-8.
- **Value type:** Double
- **Default value:** 1e-8
- **Minimum:** 0
- **Maximum:** Infinity

### reharvestSepsets

- **Short description:** Experimental: keep the sepset map faithful to the current PAG (re-harvest after each commit)
- **Long description:** In BFCI-Bryan, after each accepted removal, replace every recorded separating set that no longer m-separates its pair in the committed graph by a separator that does. A total map of separators of the current PAG projects back to that PAG, so the carried graph is unchanged; what changes is that later removals are projected from separators of the current graph rather than of earlier ones. With this on, the generalized Meek conjecture implies that the I-map-gated search never stalls. On data, re-harvested entries are graph-derived rather than test-confirmed.
- **Value type:** Boolean
- **Default value:** false

### removeAlmostCycles

- **Short description:** Yes if almost-cycles should be removed from the PAG.
- **Long description:** When x \<-\> y, x \~\~\> y, removes any unshielded triples into x and rebuilds the PAG.
- **Value type:** Boolean
- **Default value:** false

### removeEffectNodes

- **Short description:** True if effect nodes should bre removed from possible causes
- **Long description:** True if effect nodes should be removed from possible causes
- **Value type:** Boolean
- **Default value:** true

### requireImapStates

- **Short description:** Require each state the legality gate accepts to be an I-map of the test (the saturating step runs only when this is off)
- **Long description:** In BFCI-Bryan, additionally require every candidate accepted by the legality gate (single-edge passes and saturating step) to be an I-map of the independence test: for each nonadjacent pair of the candidate's MAG, a separator in that MAG must be judged independent at imapAlpha. A pair passes without a test when a known test-confirmed separator still m-separates it; otherwise one recursive-blocking separator is tested. Pairs whose seeded sepset the test refuted are exempt. Spends tests, so on data a false dependence becomes a veto. The saturating (joint-removal) step is not a separate choice: it runs if and only if this option is off. In FCIT this gate is option 1 of fcitCorrectness.
- **Value type:** Boolean
- **Default value:** true

### resamplingEnsemble

- **Short description:** Ensemble method: Preserved (1), Highest (2), Majority (3), Median (4)
- **Long description:** Preserved = keep the highest frequency edges; Highest = keep the highest frequency edges but ignore the no edge case if maximal; Majority = keep edges only if their frequency is greater than 0.5; Median = instead of assembling a composite of edges from different bootstrap graphs (which in general is not a legal member of the algorithm's output class), display the single bootstrap graph closest to the ensemble edge frequencies. The displayed graph is one the algorithm actually produced, so it is legal for its class (e.g., a legal CPDAG or PAG), and its edges are annotated with the ensemble frequencies. As of 2026-8-13 the Median graph is always the initial display for bootstrap searches; the other ensemble views can be selected afterwards from the Ensemble Display menu (right-click the graph).
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 1
- **Maximum:** 4

### resamplingWithReplacement

- **Short description:** Yes, if sampling with replacement (bootstrapping)
- **Long description:** Yes if resampling is to be done with replacement, No if without replacement. If with replacement, it is possible to have more than one copy of some of the records in the original dataset being included in the bootstrap.
- **Value type:** Boolean
- **Default value:** true

### rescueAction

- **Short description:** What to do with a detected adjacency-faithfulness clash: 0=off, 1=mark, 2=recover, 3=recover corroborated only
- **Long description:** Controls the action taken on a tier-1 orientation-clash detection (PcAR, Sec. 14 of the unfaithful-triangles analysis). 0 (OFF) runs no detection. 1 (MARK, the default) records the deletion as contested but leaves the skeleton exactly as FAS produced it. 2 (RECOVER) reinstates a flagged edge when the posterior odds -- base rate times a likelihood ratio from a discriminating re-test of the pair, computed by the wired odds estimator -- meet the recovery-odds threshold; note that the discriminating re-test is only reliable when the clash's collider claim about the pivot is genuine, so RECOVER can reinstate false edges where the pivot is in truth a mediator or common cause of the pair. 3 (RECOVER\_CORROBORATED) reinstates only pairs independently flagged by both the tier-1 clash pass and the tier-2 Markov audit, ignoring the odds threshold; with no Markov auditor wired it behaves identically to MARK. Recovery modes (2 and 3) modify the skeleton and can introduce false edges; MARK is free of skeleton risk.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 3

### resolveAlmostCyclicPaths

- **Short description:** True just in case almost cyclic paths should be resolved in the direction of the cycle.
- **Long description:** If true we resolved \<-\> edges as --\> if there is a directed path x\~\~\>y.
- **Value type:** Boolean
- **Default value:** false

### rlcdAllowNonLeafX

- **Short description:** RLCD: allow observed variables to act as non-sinks (parents) (default true)
- **Long description:** If true, RLCD may condition on observed variables when testing rank constraints, so that an observed variable can be found to be a parent of a latent or of other observed variables. If false, observed variables are treated as pure indicators.
- **Value type:** Boolean
- **Default value:** true

### rlcdCeilingValue

- **Short description:** RLCD: the ceiling at and above which values are censored when rlcdCensorCeiling is on (default 100)
- **Long description:** The common ceiling used by rlcdCensorCeiling. A value equal to or above it is read as censored. 100 is right for percentage grades; use the top of the scale for other bounded measures.
- **Value type:** Double
- **Default value:** 100
- **Minimum:** -Infinity
- **Maximum:** Infinity

### rlcdCensorCeiling

- **Short description:** RLCD: treat values at the ceiling (rlcdCeilingValue) as censored, not as exact (default false)
- **Long description:** If true, a value equal to or above rlcdCeilingValue in any variable is read as censored: known only to be at least the ceiling. This is what a grade of 100 means when many students score 100: the scale ran out, not the ability. Treated as exact values, ceiling scores flatten the top of each distribution and attenuate every correlation the variable takes part in, which weakens or hides rank constraints; treated as missing, they are missing because of their own size, which the EM policy's missing-at-random assumption does not cover. With this on, RLCD estimates one covariance matrix for both stages by stochastic EM under a multivariate normal model in which each censored value is drawn from its conditional distribution truncated above the ceiling, and runs every rank test on that matrix with a per-query sample size from the pairwise counts of uncensored values. Ordinary missing values (NaN) are handled in the same pass as missing at random. Under Gaussian errors the estimate is close to exact; under skewed errors the correction is partial but large. Uses the same ceiling for every variable; variables with no values at the ceiling are unaffected. When on, this takes the place of missingDataPolicy for RLCD, and the rank tests use the mean pairwise sample-size rule whatever missingEssMode shows, since the full-N rule overstates the information in a censored estimate. The estimate is deterministic (truncated-normal moments, iterated to a fixed point), so the same data and settings give the same answer.
- **Value type:** Boolean
- **Default value:** false

### rlcdCheckV

- **Short description:** RLCD: discard a rank-deficient set when a proper subset is already deficient (default true)
- **Long description:** If true, a set of covers found rank deficient at rank k is discarded when one of its proper subsets is already rank deficient at the correspondingly lower rank, since the deficiency is then explained by the subset rather than by a shared latent over the whole set.
- **Value type:** Boolean
- **Default value:** true

### rlcdKnowledgeInStage1

- **Short description:** RLCD: give background knowledge to stage 1 as well as stage 2 (default true)
- **Long description:** Stage 2 always honours background knowledge: tier precedence in placing clusters, forbidden parents, and the orientation of whatever the tiers order. This decides whether stage 1, the search for the observed skeleton that defines the partitions, sees it too. Under tier constraints the stage-1 search returns a denser skeleton, the clique merge then puts more variables into one partition, and the rank tests over a larger set of weakly correlated variables are more likely to fail to reject rank one across all of it, giving one latent over many variables. Measured in simulation, knowledge in stage 2 alone recovered latent structure slightly better than no knowledge, while knowledge in stage 1 recovered it worse; stage-1 knowledge did remove false observed adjacencies at partition boundaries. Leave true where the observed edges and their directions are the point; set false where the latent structure is the point and the knowledge is extensive.
- **Value type:** Boolean
- **Default value:** true

### rlcdLatentGate

- **Short description:** RLCD: look for latents in a group of variables only if its rank constraints call for one (default true)
- **Long description:** Before RLCD searches a group of observed variables for latent clusters, it checks whether the group has the kind of rank deficiency that only a latent variable can produce: two sets of variables, all adjacent to one another in the stage-1 graph, whose cross-covariance (possibly after conditioning on a neighbor) has lower rank than their size. This is the condition of Theorems 5 and 9 of Dong et al. (2024). If no such deficiency is found, no latent is introduced in that group and its stage-1 edges are kept. Without the check, a dense group of observed variables with no latent behind them is sometimes given a latent that stands in for structure among the observed variables. The check is an approximation (it uses the stage-1 graph and a limited set of conditioning variables) and errs toward allowing the search. Set to false to search every group, as the causal-learn implementation does.
- **Value type:** Boolean
- **Default value:** true

### rlcdMaxK

- **Short description:** RLCD: maximum cluster cardinality to search (default 3; min 1)
- **Long description:** The largest rank k for which RLCD searches for rank-deficient sets of covers. A rank-k cluster is placed under k latent variables. Larger values allow more latents per cluster but increase the number of tests.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

### rlcdObservedExplanationAlpha

- **Short description:** RLCD: alpha of the observed-explanation test (default 0.05)
- **Long description:** The significance level of the rank test used by rlcdObservedExplanationCheck to decide whether a set of observed variables explains a rank deficiency. It is separate from, and by default larger than, the cluster alpha: a larger alpha rejects more readily, so an underpowered explanation test is less likely to explain a true cluster away by accident. Lower it to remove more candidate latents, raise it to protect more of them.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### rlcdObservedExplanationCheck

- **Short description:** RLCD: make a cluster only if no equally small set of observed variables explains its rank deficiency (default false)
- **Long description:** If true, a set of variables found rank deficient, at a rank that would introduce t new latents, becomes a cluster only if no t observed variables from the same partition explain the deficiency equally well, that is, make the two sides rank-independent when conditioned on. Rank constraints alone cannot tell a latent common cause from an observed separator: the later part of a chain of observed variables (unit scores in course order, say) is rank one against the earlier part because the variable between them separates them, and without this check RLCD reads the chain as a measurement model. The check also removes rank deficiencies that a dense observed causal structure implies in the population, which no test of implied constraints can remove because they are real. In simulation it costs nothing on true measurement models at moderate sample size; at small sample size an underpowered explanation test can explain a true cluster away by accident, which the separate, larger rlcdObservedExplanationAlpha guards against. Candidate explaining sets are tried from one variable up to t, smallest first, up to 20000 sets per deficiency.
- **Value type:** Boolean
- **Default value:** false

### rlcdPartitionCliqueThreshold

- **Short description:** RLCD: minimum stage-1 clique size for partitioning (default 3; min 1)
- **Long description:** In stage 1, maximal cliques of the skeleton of the stage-1 search result with at least this many members are merged when they share two or more variables, and merged groups with at least four variables become the partitions within which the stage-2 rank search runs.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

### rlcdQualifyObservedCauses

- **Short description:** RLCD: keep an observed-to-latent arrow only when an observed parent identifies its direction (default true)
- **Long description:** Rank constraints cannot tell an observed cause of a latent from an indicator of it: an observed variable pointing into a latent, and the same variable as a child of the latent, imply the same covariance over the observed variables. So an arrow between an observed variable O and a latent L in RLCD's output is a placement rather than a finding. What identifies the direction is a directed observed parent P of O that is not itself attached to L. If O causes L, P is dependent on L's indicators marginally and independent of them given O (a chain). If O is an indicator, P is independent of them marginally and dependent given O (a collider at O). With this on, each directed observed-latent edge is checked against every such parent: all chain signatures give O into L, all collider signatures give L into O, and anything else is not identified. An arrow from O into L that is not identified, including one with no directed observed parent, is made undirected; an arrow from L into O that is not identified is left as the measurement-model default, unless the parents actively disagree, in which case it too is made undirected. Latent-to-latent edges are not touched. Set false to see the raw stage-2 placements.
- **Value type:** Boolean
- **Default value:** true

### rlcdResolveTwoIndicatorLatents

- **Short description:** RLCD: try to replace a latent with two indicators by a direct edge, using non-Gaussianity (default false)
- **Long description:** Rank constraints cannot tell a direct edge between two indicators of a latent from a second latent over the pair, and RLCD reports the second latent. If this is true, each latent in the output with exactly two observed children, no observed parent, and exactly one latent neighbor that has at least three pure indicators is tested with third-order cumulants, using that neighbor's indicators as references. If the test shows a direct edge, the two-indicator latent is replaced by the edge, and the two variables are made indicators of the neighbor; otherwise the latent is kept. The test needs positive evidence for the edge (an equivalence test), so it rarely turns a real latent into an edge, but it also leaves many real edges as latents. It needs skewed data: with Gaussian data nothing changes, and ceiling or floor effects, which skew data without independent skewed causes, can mislead it. With several pooled imputations the edge is taken only if every imputation shows it. Not done with a stratified rank test.
- **Value type:** Boolean
- **Default value:** false

### rlcdStabilityRuns

- **Short description:** RLCD: number of bootstrap reruns for a stability summary after the main run (default 0 = none)
- **Long description:** When greater than zero, RLCD first does its normal run, which is the graph returned, and then reruns the same configuration this many times on bootstrap resamples of the rows (the same rows across pooled imputations). The reruns do not change the graph. They produce a report in the log: for each latent of the main graph, its observed children with the fraction of reruns in which each was clustered with the others; the observed pairs clustered together in at least half the reruns but not in the main graph; the observed adjacencies of the main graph with the fraction of reruns in which they appear; and the number of latents found per rerun. One line of this is attached to the graph as the attribute "RLCD stability". Each rerun costs as much as the main run, so ten reruns take ten times as long; see rlcdStabilityTimeLimit. The stop button stops the reruns at the next run boundary and the main graph is still returned, with the summary over the reruns completed. Latent names differ from run to run, so everything in the report is stated in terms of the observed variables.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### rlcdStabilityTimeLimit

- **Short description:** RLCD: wall-clock budget in seconds for the stability reruns (default 300)
- **Long description:** A bound on the total time spent in the reruns requested by rlcdStabilityRuns. It is checked between reruns: another rerun starts only if, at the average pace so far, it would finish within the budget. No rerun is cut off part way, so the actual time can exceed the budget by at most one run. When the budget stops the reruns early, the report says how many of the requested reruns it is based on. The main run is not subject to this limit.
- **Value type:** Double
- **Default value:** 300
- **Minimum:** 0
- **Maximum:** Infinity

### rlcdStage1Fges

- **Short description:** RLCD: use FGES instead of BOSS for the stage-1 search (default false)
- **Long description:** RLCD first runs a score-based search over the observed variables to partition them. By default this is BOSS with the SEM BIC score; if true, FGES is used instead, which is closer to the GES stage of the causal-learn implementation.
- **Value type:** Boolean
- **Default value:** false

### rlcdStage1None

- **Short description:** RLCD: skip the stage-1 search and run the rank search unconstrained (default false)
- **Long description:** If true, no stage-1 search is run: the complete graph over the observed variables is used, so all variables form one partition and the stage-2 rank search runs unconstrained. This matches the reference implementation's "all" setting and overrides the FGES/BOSS choice. It gives up the pruning that makes RLCD tractable as the number of variables grows, so it is recommended only for small variable sets.
- **Value type:** Boolean
- **Default value:** false

### rlcdUnfoldCovers

- **Short description:** RLCD: unfold discovered latent covers into their children for further tests (default true)
- **Long description:** If true, after latent covers are discovered, the search also considers replacing each subset of them by their children when forming candidate sets, which is how relations between a latent and the children of another latent are found. If false, only the covers themselves are used.
- **Value type:** Boolean
- **Default value:** true

## S

### sampleSize

- **Short description:** Sample size (min = 1)
- **Long description:** Determines now many records should be generated for the data. The minimum number of records is 1; the default is set to 1000.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

### sampleStyle

- **Short description:** Sample style: 1 = Subsample 2 = Bootstrap
- **Long description:** Sample style: 1 = Subsample 2 = Bootstrap
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### saveBootstrapGraphs

- **Short description:** Yes if individual bootstrapping graphs should be saved
- **Long description:** Bootstrapping provides a summary over individual search graphs; select Yes here if these individual graphs should be saved
- **Value type:** Boolean
- **Default value:** false

### saveLatentVars

- **Short description:** Save latent variables.
- **Long description:** Yes if one wishes to have values for latent variables saved out with the rest of the data; No if only data for the measured variables should be saved.
- **Value type:** Boolean
- **Default value:** false

### scaleFreeAlpha

- **Short description:** For scale-free graphs, the parameter alpha (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### scaleFreeBeta

- **Short description:** For scale-free graphs, the parameter beta (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Double
- **Default value:** 0.9
- **Minimum:** 0.0
- **Maximum:** 1.0

### scaleFreeDeltaIn

- **Short description:** For scale-free graphs, the parameter delta\_in (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### scaleFreeDeltaOut

- **Short description:** For scale-free graphs, the parameter delta\_out (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

### scalingFactor

- **Short description:** Scaling factor.
- **Long description:** For Gaussian kernel: The scaling factor.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 4.9E-324
- **Maximum:** Infinity

### scoreCheckPenaltyDiscount

- **Short description:** Penalty discount for the RICF-BIC score check (default = 1.0; min \> 0.0)
- **Long description:** The parameter c in the MAG BIC used by the per-removal score check, 2L – c k ln N, where L is the RICF log-likelihood of the Zhang MAG implied by the candidate PAG, k is the number of MAG parameters (error variances plus edges), and N is the sample size. With c = 1 the acceptance rule is the classical BIC test. Larger values make the gate more willing to remove edges; smaller values make it more conservative. Independent of the penalty discount used by the initializer score.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 4.9E-324
- **Maximum:** 1.7976931348623157E308

### scoreTestCalibratedPValues

- **Short description:** Report calibrated p-values instead of raw score differences
- **Long description:** A score used as an independence test normally reports its local score difference, which is negative for independence and is not a probability. With this set to Yes, the test instead reports the p-value of the corresponding likelihood-ratio test, which is asymptotically Uniform(0, 1) under the null, and reports the significance level at which its own sign rule operates. This does NOT change the accept/reject decision or the graph a search returns; it makes the p-value diagnostics of the Markov check (Anderson-Darling, KS, Fisher, binomial) well defined for a score-based test. Ignored when the score cannot supply a calibrated p-value, as when the structure prior is non-zero.
- **Value type:** Boolean
- **Default value:** false

### seed

- **Short description:** Seed for pseudorandom number generator (-1 = off)
- **Long description:** The seed is the initial value of the internal state of the pseudorandom number generator. A value of -1 skips setting a new seed.
- **Value type:** Long
- **Default value:** -1
- **Minimum:** 50
- **Maximum:** 9223372036854775807

### selectionMinEffect

- **Short description:** Minimum effect size for listing effects in the CStaR table
- **Long description:** Minimum effect size for listing effects in the CStaR table
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

### selfLoopCoef

- **Short description:** The coefficient for the self-loop (default 0.0)
- **Long description:** For simulating time series data, each variable depends on itself one time-step back with a linear edge that has this coefficient.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** Infinity

### semBicRule

- **Short description:** Lambda: 1 = Chickering, 2 = Nandy
- **Long description:** The Chickering Rule uses the difference of BIC scores to add or remove edges. The Nandy et al. rule uses a single calculation of a partial correlation in place of the likelihood difference.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### semBicStructurePrior

- **Short description:** Structure Prior for SEM BIC (default 0)
- **Long description:** Structure prior; default is 0 (turned off); may be any positive number otherwise
- **Value type:** Double
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** Infinity

### semGicRule

- **Short description:** Lambda: 1 = ln n, 2 = pn^1/3, 3 = 2 ln pn, 4 = 2(ln pn + ln ln pn), 5 = ln ln n ln pn, 6 = ln n ln pn, 7 = Manual
- **Long description:** The rule used for calculating the lambda term of the score. We follow Kim, Y., Kwon, S., & Choi, H. (2012) and articles referenced therein. For high-dimensional data.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 1
- **Maximum:** 7

### semImSimulationType

- **Short description:** Yes if recursive simulation, No if reduced form simulation
- **Long description:** Determines the type of simulation done. If recursive, the graph must be a DAG in causal order. "Reduced form" means X = (I - B)^-1 e, which requires a possibly large matrix inversion.
- **Value type:** Boolean
- **Default value:** true

### sepsetFinderMethod

- **Short description:** The method to use for finding sepsets, 1 = Greedy, 2 = Min-p, 3 = Max-p (default).
- **Long description:** The method to use for finding sepsets, 1 = Greedy, 2 = Min-p, 3 = Max-p (default).
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 3

### shrinkageMode

- **Short description:** Shrinkage Mode: 1 = None 2 = Ridge 3 = Ledoit-Wolf
- **Long description:** Shrinkage Mode: 1 = None 2 = Ridge 3 = Ledoit-Wolf
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

### significanceChecked

- **Short description:** True if the significance of the cluster should be checked.
- **Long description:** True if the significance of clusters should be checked, false if not.
- **Value type:** Boolean
- **Default value:** false

### simulationErrorType

- **Short description:** 1 = Usual LG SEM, 2 = U(lb, ub), 3 = Exp(lambda), 4 = Gumbel(mu, beta), 5 = Gamma(shape, scale)
- **Long description:** Exogenous error type
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

### simulationParam1

- **Short description:** Indep error parameter #1
- **Long description:** Exogenous error parameter #1
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -1000
- **Maximum:** 1000

### simulationParam2

- **Short description:** Indep error parameter #2, if used
- **Long description:** Exogenous error parameter #2
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -1000
- **Maximum:** 1000

### singularityLambda

- **Short description:** Singularities: Small number \>= 0 Add lambda to the the diagonal, \< 0 Pseudoinverse
- **Long description:** Singularities: Small number \>= 0 Add lambda to the the diagonal, \< 0 Pseudoinverse
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

### skewEdgeThreshold

- **Short description:** Threshold for including additional edges detectable by skewness
- **Long description:** For FASK, this includes an adjacency X—Y in the model if \|corr(X, Y \| X \> 0) – corr(X, Y \| Y \> 0)\| exceeds some threshold. The default for this threshold is 0.3.
- **Value type:** Double
- **Default value:** 0.3
- **Minimum:** 0.0
- **Maximum:** Infinity

### skipNumRecords

- **Short description:** Number of records that should be skipped between recordings (min = 0)
- **Long description:** Data recordings are made every this many steps.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### splitDelta

- **Short description:** Score gap below which near-tied orderings are deferred and explored (0 = off)
- **Long description:** When an improving move beats an alternative placement by less than this amount, the alternative is deferred for separate exploration.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** Infinity

### stableFAS

- **Short description:** Yes if the Colombo et al. 'stable' FAS should be done, to avoid skeleton order dependency
- **Long description:** If Yes, the "stable" version of the PC adjacency search is used, which for k \> 0 fixes the graph for depth k + 1 to that of the previous depth k.
- **Value type:** Boolean
- **Default value:** true

### standardize

- **Short description:** Yes if the data should be standardized
- **Long description:** Yes if each variable in the data should be standardized to have mean zero and variance 1.
- **Value type:** Boolean
- **Default value:** false

### StARS.cutoff

- **Short description:** Instability cutoff beta for StARS
- **Long description:** The StARS instability cutoff. StARS selects the least sparse penalty whose estimated edge instability across subsamples stays strictly below this value. Smaller values demand a more stable graph and therefore yield sparser output. The conventional choice in the StARS literature is 0.05.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

### startFromCompleteGraph

- **Short description:** Yes, if the procedure should start from a complete graph
- **Long description:** Yes, if the procedure should start from a complete graph
- **Value type:** Boolean
- **Default value:** false

### stratifiedPermutations

- **Short description:** Permutations for the stratified rank test (0 = likelihood ratio)
- **Long description:** When positive, the Stratified Rank test computes its p-values by the permutation scheme of Dong et al. (ICML 2026, Theorem 5), which does not assume Gaussianity within domains: within each domain the trailing canonical variates are permuted and the pooled statistic is recomputed this many times. When zero, the default, the Gaussian likelihood-ratio form is used. The permutation form multiplies the cost of every test by roughly this number, which inside a search such as PC or FCI can be very slow; it is meant for checking conclusions on data whose within-domain distributions are badly non-Gaussian, not for routine use.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 100000

### stratifyByDomain

- **Short description:** Stratify by the domain column
- **Long description:** When true, the algorithm runs in stratified (domain-pooled) mode: the rows are split by the column named by the domainColumn parameter, every rank decision pools the within-domain statistics across domains, and for RLCD the first stage is scored on the within-domain covariance. For data gathered in several batches, sites, or cohorts whose causal structure is shared but whose coefficients and means may differ by domain. Note for RLCD in the interface: RLCD accepts continuous data, so code the domain index as an integer-valued continuous column.
- **Value type:** Boolean
- **Default value:** false

### structurePrior

- **Short description:** Structure prior coefficient (min = 0.0)
- **Long description:** The default number of parents for any conditional probability table. Higher weight is accorded to tables with about that number of parents. The prior structure weights are distributed according to a binomial distribution.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### symmetricFirstStep

- **Short description:** Yes if the first step for FGES should do scoring for both X-\>Y and Y-\>X
- **Long description:** If Yes, scores for both X-\>Y and X\<-Y will be calculated and the higher score used.
- **Value type:** Boolean
- **Default value:** false

## T

### takeLogs

- **Short description:** Yes logs should be taken, No if not
- **Long description:** The formula for the score allows a log to be taken optionally in the information term.
- **Value type:** Boolean
- **Default value:** true

### targetName

- **Short description:** Target variable name
- **Long description:** The name of the target variables--for Markov blanket searches, this is the name of the variable for which one wants the Markov blanket or Markov blanket graph.
- **Value type:** String

### targets

- **Short description:** Target names (comma or space separated)
- **Long description:** Target names (comma or space separated).
- **Value type:** String

### testTimeout

- **Short description:** Timeout for tests in milliseconds, or -1 if no timeout.
- **Long description:** Timeout for tests in milliseconds, or -1 if no timeout.
- **Value type:** Long
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 9223372036854775807

### tetrad_test_bpc

- **Short description:** The tetrad test used: 1 = Wishart, 2 = Delta (Bollen-Ting)
- **Long description:** The tetrad test used: 1 = Wishart, 2 = Delta
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2

### tetrad_test_fofc

- **Short description:** The tetrad test used: 1 = CCA, 2 = Bollen-Ting, 3 = Wishart
- **Long description:** The tetrad test used: 1 = CCA, 2 = Bollen-Ting, 3 = Wishart
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

### thr

- **Short description:** THR parameter (GLASSO) (min = 0.0)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Double
- **Default value:** 1.0E-4
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### thresholdAlpha

- **Short description:** Error Threshold
- **Long description:** Adjusts the threshold for judging conditional dependence.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1

### thresholdBHat

- **Short description:** Threshold on the B Hat matrix.
- **Long description:** The estimated B matrix is thresholded by setting small entries less than this threshold to zero.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

### thresholdForNumEigenvalues

- **Short description:** Threshold to determine how many eigenvalues to use--the lower the more (0 to 1)
- **Long description:** Referring to Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012), this parameter is the threshold to determine how many eigenvalues to use--the lower the more (0 to 1).
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** Infinity

### thresholdNoRandomConstrainSearch

- **Short description:** Yes, if using the cutoff threshold for the meta-constraints independence test (stage 2).
- **Long description:** Yes, if using the cutoff threshold for the meta-constraints independence test (stage 2).
- **Value type:** Boolean
- **Default value:** true

### thresholdNoRandomDataSearch

- **Short description:** Yes, if using the cutoff threshold for the constraints independence test (stage 1).
- **Long description:** null
- **Value type:** Boolean
- **Default value:** false

### thresholdW

- **Short description:** Threshold on the W matrix.
- **Long description:** The estimated W matrix is thresholded by setting small entries less than this threshold to zero.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

### timeLag

- **Short description:** For time lag searches,\`a time lag, automatically applied (zero if none)
- **Long description:** Automatically applies the time lag transform to the data, creating additional lagged variables. If zero, no time lag is applied. A positive integer
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

### timeLagReplicatingGraph

- **Short description:** For time lag searches, whether to make the graph replicate edges across time lags, SVAR-style
- **Long description:** For time lag searches, whether to make the graph replicate edges across time lags, SVAR-style
- **Value type:** Boolean
- **Default value:** false

### timeLimit

- **Short description:** Time limit
- **Long description:** T-Separation requires a time limit. Default 1000.
- **Value type:** Double
- **Default value:** 1000.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### timeout

- **Short description:** Timeout (best graph returned, -1 = no timeout)
- **Long description:** The algorithm will time out at approximately this number of seconds from when it started and return the final graph found at that point.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

### topBracket

- **Short description:** Top bracket to look for causes in
- **Long description:** Top bracket, 'q'
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 1
- **Maximum:** 500000

### topK

- **Short description:** The number of top-scoring models to retain
- **Long description:** The maximum number of distinct top-scoring models kept and reported by the search.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 1000000

### trffFfFeatures

- **Short description:** Number of Fourier features (FF)
- **Long description:** Number of Fourier features used to represent nonlinear effects of continuous parents in the Minimax score. Larger values increase flexibility and runtime/memory cost; smaller values are faster but less expressive.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 0
- **Maximum:** 1000000

### trffNu

- **Short description:** Student-t degrees of freedom (nu)
- **Long description:** The Student-t degrees of freedom parameter used by the TRFF model for continuous children. Smaller nu yields heavier tails and greater robustness to outliers. Larger nu reduces tail heaviness and approaches a Gaussian model. In practice, values above roughly 50–100 behave nearly Gaussian.
- **Value type:** Double
- **Default value:** 5
- **Minimum:** 2
- **Maximum:** 1000

### trffRidge

- **Short description:** Ridge (L2) regularization strength for T-RFF local models
- **Long description:** Ridge (L2) regularization parameter used when fitting local conditional models in the T-RFF BIC score.
- **Value type:** Double
- **Default value:** 1e-3
- **Minimum:** 0.0
- **Maximum:** 1.0e12

### trffSymmetrized

- **Short description:** Symmetrize the TRFF LR test over (X, Y)
- **Long description:** If enabled (the default), the TRFF LR test is computed in both directions - regressing Y on Z plus X, and regressing X on Z plus Y - and the larger (more conservative) p-value is reported, so the result does not depend on the order of the pair, as constraint-based algorithms expect. Each direction controls its level, so the maximum does as well. If disabled, only the direction with Y as the regression target is computed, which halves the cost per query but makes the test asymmetric in its arguments.
- **Value type:** Boolean
- **Default value:** true

### trimmingStyle

- **Short description:** Trimming Style: 1 = None, 2 = Adjacencies, 3 = MB DAG, 4 = Possibly directed paths
- **Long description:** 'Adjacencies' trims to the adjacencies the targets, MB DAGs to the Union(MB(targets)) U targets, potentially directed trims to nodes with potentially directed paths to the targets.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 4

### trueErrorVariance

- **Short description:** True error variance
- **Long description:** The true error variance of the model, assuming this is the same for all variables.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### truncationLimit

- **Short description:** Truncation limit for basis functions
- **Long description:** Basis functions 1 though this number will be used.. The Degenerate Gaussian category indicator variables for mixed data are also used.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 1000

### tscClusterRank

- **Short description:** TSC cluster rank (if desired)
- **Long description:** TSC cluster rank (if desired)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 500

### tscClusterSize

- **Short description:** TSC cluster size (if desired)
- **Long description:** TSC cluster size (if desired)
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 500

### tscEnableHierarchy

- **Short description:** Yes, if hierarchical latents should be detected
- **Long description:** Yes, if hierarchical latents should be detected
- **Value type:** Boolean
- **Default value:** true

### tscMinRankDrop

- **Short description:** Min rank drop for detecting hierarchical latents
- **Long description:** Min rank drop for detecting hierarchical latents
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 100

### tscMinRedundancy

- **Short description:** Minimum redundancy for clusters beyond size = rank + 1
- **Long description:** Minimum redundancy: require at least k extra indicators per latent (\|C\| ≥ r+1+k). Higher values suppress trivially sized clusters.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 1000

### tscMode

- **Short description:** TSC mode: 1 = Metaloop, 2 = Specific size/rank
- **Long description:** TSC mode: 1 = Metaloop, 2 = Specific cluster size/rank
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### tscPcUseBoss

- **Short description:** Yes, if the procedure should use BOSS (with the BOSS-specific parameters) and not PC
- **Long description:** Yes, if the procedure should use BOSS (with the BOSS-specific parameters) and not PC
- **Value type:** Boolean
- **Default value:** false

### tscSingletonPolicy

- **Short description:** Singletons: 1 = Exclude 2 = Include
- **Long description:** Singletons: 1 = Exclude 2 = Include
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

### twoCycleAlpha

- **Short description:** Alpha orienting 2-cycles (min = 0.0)
- **Long description:** The alpha level of a T-test used to determine where 2-cycles exist in the graph. A value of zero turns off 2-cycle detection.
- **Value type:** Double
- **Default value:** 0.01
- **Minimum:** 0.0
- **Maximum:** 1.0

### twoCycleScreeningThreshold

- **Short description:** Upper bound for \|left-right\| to count as 2-cycle. (Set to zero to turn off pre-screening.)
- **Long description:** 2-cycles are screened by looking to see if the left-right rule returns a difference smaller than this threshold. To turn off the screening, set this to zero.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** Infinity

## U

### upperBound

- **Short description:** Upper bound cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.7
- **Minimum:** 0.0
- **Maximum:** 1.0

### useAdaptiveZBins

- **Short description:** Adaptive bins for continuous Z
- **Long description:** If enabled (recommended), the number of quantile bins per continuous conditioning (Z) variable grows with the sample size at the rate d \~ n^(2/5) of Neykov, Balakrishnan and Wasserman (2021), capped so that the expected number of samples per stratum remains workable when several continuous Z variables multiply the cell count. This growth is required for the permutation calibration to control the test's level: with a fixed bin count, within-bin residual dependence under the conditional-independence null does not shrink with n, and the test becomes increasingly anticonservative as the sample size grows. If disabled, the fixed binsPerContZ value is used instead.
- **Value type:** Boolean
- **Default value:** true

### useBes

- **Short description:** True if the optional BES step should be used
- **Long description:** This algorithm can use the backward equivalence search from the GES algorithm as one of its steps.
- **Value type:** Boolean
- **Default value:** false

### useBesDefaultTrue

- **Short description:** True if the BES step of BOSS should be used (recommended for hybrid algorithms)
- **Long description:** Hybrid latent-variable algorithms that start from a BOSS CPDAG (BFCI, BFCI-C, BFCI-D, FCIT and relatives, GMAS, LV-heuristic, BOSS-CCD, ION) rely on that CPDAG being an I-map of the data; the backward equivalence search (BES) step of BOSS is what guarantees this under faithfulness. Without it BOSS can stop at a non-I-map local optimum, and the resulting false separations are propagated as false colliders that the later phases of these algorithms cannot undo. For these algorithms the step is therefore on by default; it costs little time relative to the rest of the search. Plain BOSS as a CPDAG search is controlled by the separate useBes parameter.
- **Value type:** Boolean
- **Default value:** true

### useBossAdjacencies

- **Short description:** Yes if BOSS (rather than FAS-Stable) should supply the initial adjacency skeleton
- **Long description:** If set to "Yes", the initial adjacency skeleton for the search is taken from the skeleton of a BOSS CPDAG estimated with the supplied score, instead of running FAS-Stable. A global score-based search typically yields better finite-sample adjacencies than FAS; subsequent orientation steps proceed identically. Ignored if an external graph is supplied.
- **Value type:** Boolean
- **Default value:** false

### useCorrDiffAdjacencies

- **Short description:** Yes if adjacencies from conditional correlation differences should be used
- **Long description:** FASK can use adjacencies X—Y where \|corr(X,Y\|X\>0) – corr(X,Y\|Y\>0)\| \> threshold. This expression will be nonzero only if there is a path between X and Y; heuristically, if the difference is greater than, say, 0.3, we infer an adjacency.
- **Value type:** Boolean
- **Default value:** true

### useDataOrder

- **Short description:** Yes just in case data variable order should be used for the first initial permutation.
- **Long description:** In either case, if multiple starting points are used, taking the best scoring model from among these, subsequent starting points will all be random shuffles.
- **Value type:** Boolean
- **Default value:** true

### useEquivalenceRemoval

- **Short description:** Yes if CCD should remove edges only on positive evidence of independence.
- **Long description:** If Yes, CCD's adjacency phase uses an equivalence (TOST) test governed by equivalenceMargin and equivalenceMarginMultiplier, while the orientation steps keep the independence test selected for the algorithm. The adjacency phase decides whether to delete an edge, which is served by a test demanding positive evidence that the partial correlation is negligible; the orientation steps instead ask whether two variables are dependent, where an equivalence test's weaker "not shown to be negligible" would worsen CCD's tendency to commit to directions the data do not support. This requires the selected test to be Fisher Z, since the equivalence test is defined on the partial correlation. Default No, which leaves CCD's behaviour unchanged.
- **Value type:** Boolean
- **Default value:** false

### useFasAdjacencies

- **Short description:** Yes if adjacencies from the FAS search (correlation) should be used
- **Long description:** Determines whether adjacencies found by conditional correlation should be included in the final model.
- **Value type:** Boolean
- **Default value:** true

### useGap

- **Short description:** Yes if the GAP algorithms should be used. Not if the SAG algorithm should be used
- **Long description:** True if one should first find all possible initial sets, grows these out, and then picks a non-overlapping such largest sets from these. Not if one should grow pure clusters one at a time, excluding variables found in earlier clusters.
- **Value type:** Boolean
- **Default value:** false

### useIlsRestarts

- **Short description:** Yes if restarts should use iterated local search (ILS) rather than fresh random orders (default No)
- **Long description:** If Yes, restarts after the first perturb the best order found so far with about ln(m) random transpositions and rerun the search from there, in the style of the FLOP algorithm (Wienobst, Henckel, and Weichwald, 2026), rather than starting from a fresh random order. ILS restarts typically reconverge much faster than random restarts and escape local optima more effectively per unit of compute. The number of restarts is controlled by numStarts.
- **Value type:** Boolean
- **Default value:** false

### useMaxAcrossStrata

- **Short description:** Use maximum across strata
- **Long description:** If enabled, the overall test statistic is computed as the maximum dependence statistic across all strata (minimax aggregation). If disabled, statistics are aggregated more conservatively across strata.
- **Value type:** Boolean
- **Default value:** true

### useMaxPHeuristic

- **Short description:** Yes if the max P heuristic version should be used to search for sepsets
- **Long description:** Yes if the max P heuristic version should be used to search for sepsets
- **Value type:** Boolean
- **Default value:** false

### useMaxPOrientationHeuristic

- **Short description:** Use the max p heuristic version
- **Long description:** Use the max p heuristic version
- **Value type:** Boolean
- **Default value:** false

### usePass0

- **Short description:** BFCI-Bryan: run Pass 0 (re-select seeded sepsets the test refutes)
- **Long description:** The sepset map is seeded from the initial DAG with parent sets. Pass 0 re-selects, under the legality gate, each seeded entry the independence test refutes. Turn off to keep the DAG's entries regardless of the test, as in the original pseudocode; this isolates the effect of Pass 0, which can change orientations without removing any edge.
- **Value type:** Boolean
- **Default value:** true

### useSaturatingStep

- **Short description:** True if the saturating (joint-removal) step should run after the single-edge passes
- **Long description:** In the gated \*-FCI variants, after the single-edge removal passes, jointly remove the pairs that have a test-confirmed separating set but whose single removals the legality gate rejected, accepting the result if it is a legal PAG. In the oracle a reachable state can have no legal single removal while the joint removal gives the true PAG, so this step is needed for correctness. It does nothing on a run that does not stall.
- **Value type:** Boolean
- **Default value:** true

### useScore

- **Short description:** Yes if the score should be used; no if the test should be used
- **Long description:** BOSS can run either from a score or a test; this lets you choose which.
- **Value type:** Boolean
- **Default value:** true

### useSkewAdjacencies

- **Short description:** Yes if adjacencies based on skewness should be used
- **Long description:** FASK can use adjacencies X—Y where \|corr(X,Y\|X\>0) – corr(X,Y\|Y\>0)\| \> threshold. This expression will be nonzero only if there is a path between X and Y; heuristically, if the difference is greater than, say, 0.3, we infer an adjacency. To see adjacencies included for this reason, set this parameter to “Yes”. Sanchez-Romero, Ramsey et al., (2018) Network Neuroscience.
- **Value type:** Boolean
- **Default value:** true

### useVarimax

- **Short description:** Use the varimax-rotated factor solution
- **Long description:** If true, the graph is built from the varimax-rotated loadings, which concentrate each variable's weight on as few factors as possible and so usually give a more interpretable measurement model. If false, the unrotated successive-residual solution is used instead. Note that rotation changes which edges pass the fa\_threshold cutoff, so the two settings can produce different graphs.
- **Value type:** Boolean
- **Default value:** true

## V

### varHigh

- **Short description:** High end of variance range (min = 0.0)
- **Long description:** The parameter 'b' for drawing independent variance values, from +U(a, b).
- **Value type:** Double
- **Default value:** 3.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### varLow

- **Short description:** Low end of variance range (min = 0.0)
- **Long description:** The parameter 'a' for drawing independent variance values, from +U(a, b).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

### verbose

- **Short description:** Yes if verbose output should be printed or logged
- **Long description:** If this parameter is set to ‘Yes’, extra (“verbose”) output will be printed if available giving some details about the step-by-step operation of the algorithm.
- **Value type:** Boolean
- **Default value:** false

## W

### wThreshold

- **Short description:** wThreshold
- **Long description:** Tuning parameter for DAGMA
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0
- **Maximum:** Infinity

## Z

### zsMaxIndegree

- **Short description:** Maximum indegree of true graph (min = 0)
- **Long description:** This is the maximum number of parents one expects any node to have in the true model.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 0
- **Maximum:** 2147483647

### zSRiskBound

- **Short description:** Risk bound
- **Long description:** This is the probability of getting the true model if a correct model is discovered. Could underfit.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0
- **Maximum:** 1

---

Generated from `parameter.definitions.html`.
