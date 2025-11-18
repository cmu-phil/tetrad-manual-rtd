# Parameter Definitions

## acceptanceProportion
- **Short description:** Acceptance Proportion
- **Long description:** An edge occurring in this proportion of individual FASK graphs will appear in the final graph.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

## addOriginalDataset
- **Short description:** Yes, if adding the original dataset as another bootstrapping
- **Long description:** Select “Yes” here to include asn extra run using the original dataset for improved accuracy.
- **Value type:** Boolean
- **Default value:** false

## adjustOrientations
- **Short description:** Yes, if the orientation adjustment step should be included
- **Long description:** Yes, if the orientation adjustment step should be included
- **Value type:** Boolean
- **Default value:** false

## allowBidirected
- **Short description:** Allow bidirected edges to show collider conflicts
- **Long description:** Allow bidirected edges to show collider conflicts
- **Value type:** Boolean
- **Default value:** false

## allowInternalRandomness
- **Short description:** Allow randomness inside algorithm
- **Long description:** This allows variables orders to be shuffled in certain sports to avoid local optima
- **Value type:** Boolean
- **Default value:** true

## alpha
- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** The cutoff, beyond which test results are judged as dependent, for a statistical test of independence. Default 0.05. Higher alpha yields a sparser graph.
- **Value type:** Double
- **Default value:** 0.01
- **Minimum:** 0.0
- **Maximum:** 1.0

## amBetaAlpha
- **Short description:** The 'alpha' shape parameter for the Beta noise terms.
- **Long description:** The 'alpha' shape parameter for the Beta noise terms.
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** Infinity

## amBetaBeta
- **Short description:** The 'beta' shape parameter for the Beta noise terms.
- **Long description:** The 'beta' shape parameter for the Beta noise terms.
- **Value type:** Double
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** Infinity

## amCoefHigh
- **Short description:** High end of coefficient range (min = 0.0)
- **Long description:** Value m2 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## amCoefLow
- **Short description:** Low end of coefficient range (min = 0.0)
- **Long description:** The parameter m1 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** Infinity

## amCoefSymmetric
- **Short description:** Yes if negative coefficient values should be considered
- **Long description:** Yes if coefficients should be drawn from +/-(a, b); No if from +(a, b).
- **Value type:** Boolean
- **Default value:** true

## amDerivativeMax
- **Short description:** 'Max' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Long description:** 'Max' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Value type:** Double
- **Default value:** 1
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amDerivativeMin
- **Short description:** 'Min' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Long description:** 'Min' for the U(min, max) range for random derivative values (with f(0) = 0)
- **Value type:** Double
- **Default value:** -1
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amDistortionType
- **Short description:** Add distortion: 1 = Before noise (additive) or 2 = After noise (post-nonlinear)
- **Long description:** Add distortion: 1 = Before noise (additive) or 2 = After noise (post-nonlinear)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## amEnsureInvertibility
- **Short description:** Ensure that functions are invertible
- **Long description:** id="amEnsureInvertibility_short_desc"> Ensure that functions are invertible
- **Value type:** Boolean
- **Default value:** false

## amFirstDerivMax
- **Short description:** 'Max' for the U(min, max) range for f'(0) for the causal function
- **Long description:** 'Max' for the U(min, max) range for f'(0) for the causal function
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amFirstDerivMin
- **Short description:** 'Min' for the U(min, max) range for f'(0) for the causal function
- **Long description:** 'Min' for the U(min, max) range for f'(0) for the causal function
- **Value type:** Double
- **Default value:** -1.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amNumPostNonlinearFunctions
- **Short description:** The number of random post-nonlinear functions to choose from
- **Long description:** The number of random post-nonlinear functions to choose from
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

## amRescaleMax
- **Short description:** Variables will be rescaled to [min, max] for this max; if min = max no rescaling will be done
- **Long description:** Variables will be rescaled to [min, max] for this max; if min = max no rescaling will be done
- **Value type:** Double
- **Default value:** 1
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amRescaleMin
- **Short description:** Variables will be rescaled to [min, max] for this min; if min = max no rescaling will be done
- **Long description:** Variables will be rescaled to [min, max] for this min; if min = max no rescaling will be done
- **Value type:** Double
- **Default value:** -1
- **Minimum:** -Infinity
- **Maximum:** Infinity

## amTaylorSeriesDegree
- **Short description:** The maximum exponent for a Taylor series to use as a random post-nonlinear function
- **Long description:** The maximum exponent for a Taylor series to use as a random post-nonlinear function. The f(0) term is set to 0.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## anmNoiseKind
- **Short description:** Noise distribution family: 1 = Beta (skewed), 2 = Gaussian, 3 = Student-t (heavy-tailed)
- **Long description:** Selects the distribution of exogenous noise for the ANM simulator Options: 1 = Beta (skewed), 2 = Gaussian, 3 = Student-t (heavy-tailed).
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## anmNoiseStrength
- **Short description:** Controls variance/strength of noise in ANM simulator
- **Long description:** A slider in [0,1] that scales the standard deviation of the chosen noise distribution. Low values yield weak noise, high values yield stronger noise. For Student-t, this also interacts with degrees of freedom (heavier tails at higher strength).
- **Value type:** Double
- **Default value:** 0.4
- **Minimum:** 0.0
- **Maximum:** 10.0

## anmNonlinearity
- **Short description:** Controls strength of nonlinearity in ANM simulator
- **Long description:** A slider in [0,1] that simultaneously controls the number of basis units per edge and their amplitude. Low values produce nearly linear functions, high values produce strongly nonlinear functions.
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0.0
- **Maximum:** 10.0

## anmPreset
- **Short description:** Preset function family: 1 = Smooth RBF, 2 = Wavy RBF, 3 = Tanh, 4 = Polynomial
- **Long description:** Selects the base family of nonlinear functions used on each edge for the ANM simulator. Options: 1 = Smooth RBF (gentle), 2 = Wavy RBF (richer), 3 = Tanh (sigmoidal), 4 = Polynomial (low-degree).
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 4

## applyR1
- **Short description:** Yes if the orient away from arrow rule should be applied
- **Long description:** Set this parameter to “No” if a chain of directed edges pointing in the same direction when only the first few such orientations are justified based on the data.
- **Value type:** Boolean
- **Default value:** true

## avgDegree
- **Short description:** Average degree of graph (min = 0)
- **Long description:** The average degree of a graph is equal to 2E / V, where E is the number of edges in the graph and V the number of variables (vertices) in the graph, since each edge has two endpoints.
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 2147483647

## basisScale
- **Short description:** Variables are scaled to [-b, b] for this b (0 = standardized)
- **Long description:** id="basisScale_short_desc"> Variables are scaled to [-b, b] for this b (0 = standardized)
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 
- **Maximum:** 500000

## basisType
- **Short description:** Basis type (0 = Polynomial, 1 = Legendre, 2 = Hermite, 3=Chebyshev)
- **Long description:** id="basisType_short_desc"> Basis type (0 = Polynomial, 1 = Legendre, 2 = Hermite, 3=Chebyshev)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 3

## bootstrappingNumThreads
- **Short description:** The number of threads (>= 1) to use for the bootstrapping
- **Long description:** This is the number of threads for the bootstrapping itself. The number of threads that each algorithm uses is set by the individual algorithm.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

## bossAlg
- **Short description:** Picks the BOSS algorithm type, BOSS1 or BOSS2
- **Long description:** 1 = BOSS1, 2 = BOSS2, 3 = BOSS3
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## cacheScores
- **Short description:** Yes score results should be cached, no if not
- **Long description:** Caching scores can use a lot of memory.
- **Value type:** Boolean
- **Default value:** true

## calculateEuclidean
- **Short description:** Yes if the Euclidean norm squared should be calculated (slow), No if not
- **Long description:** The generalized information criterion is defined with an information term that take a Euclidean norm squares; there can be calculated directly.
- **Value type:** Boolean
- **Default value:** false

## cciScoreAlpha
- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.01
- **Minimum:** 0.0
- **Maximum:** 1.0

## cellTableType
- **Short description:** The type of cell table to use (optimization), 1 = AD Tree, 2 = Count Sample
- **Long description:** This is just whether table counts are to be calculated using one method or another, for optimization. The AD tree option uses AD trees to do the calculation; the Count Samples option simply counts the samples for each independence question and builds a table that way.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## cgExact
- **Short description:** Yes if the exact algorithm should be used for continuous parents and discrete children
- **Long description:** For the conditional Gaussian likelihood, if the exact algorithm is desired for discrete children and continuous parents, set this parameter to “Yes”.
- **Value type:** Boolean
- **Default value:** false

## checkAdjacencySepsets
- **Short description:** Yes if adjacency sepsets should be checked after all recursive sepsets check (default=No)
- **Long description:** Yes if adjacency sepsets should be checked after all recursive sepsets check (default=No). This is needed for FCIT to pass an Oracle test but may reduce accuracy.
- **Value type:** Boolean
- **Default value:** false

## checkType
- **Short description:** Model significance check type: 1 = Significance, 2 = Clique, 3 = None
- **Long description:** Model significance check type: 1 = Significance, 2 = Clique, 3 = None
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## clusterSizes
- **Short description:** Cluster sizes to check (comma separated, each >= 2, default = "2")
- **Long description:** Cluster sizes to check (comma separated, each >= 2, default = "2")
- **Value type:** String
- **Default value:** 
- **Minimum:** 
- **Maximum:** 

## coefHigh
- **Short description:** High end of coefficient range (min = 0.0)
- **Long description:** Value m2 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## coefLow
- **Short description:** Low end of coefficient range (min = 0.0)
- **Long description:** The parameter m1 for coefficients drawn from U(-m2, -m1) U U(m1, m2).
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## coefSymmetric
- **Short description:** Yes if negative coefficient values should be considered
- **Long description:** Yes if coefficients should be drawn from +/-(a, b); No if from +(a, b).
- **Value type:** Boolean
- **Default value:** true

## colliderDiscoveryRule
- **Short description:** Collider discovery: 1 = Lookup from adjacency sepsets, 2 = Conservative (CPC), 3 = Max-P
- **Long description:** One may look them up from sepsets, as in the original PC, or estimate them conservatively, as from the Conservative PC algorithm, or by choosing the sepsets with the maximum p-value, as in PC-Max.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## colliderOrientationStyle
- **Short description:** Collider Orientation Style: 1 = Sepsets 2 = Conservative 3 = Max-P
- **Long description:** Collider Orientation Style: 1 = Sepsets 2 = Conservative 3 = Max-P
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 3

## completeRuleSetUsed
- **Short description:** Yes if the complete FCI rule set should be used
- **Long description:** No if the (simpler) final orientation rules set due to P. Spirtes, guaranteeing arrow completeness, should be used; yes if the (fuller) set due to J. Zhang, should be used guaranteeing additional tail completeness.
- **Value type:** Boolean
- **Default value:** true

## concurrentFAS
- **Short description:** Yes if a concurrent FAS should be done
- **Long description:** Yes if the version of the PC adjacency search that uses concurrent processing should be used, no if not.
- **Value type:** Boolean
- **Default value:** false

## conditioningThreshold
- **Short description:** Matrix conditioning values above which Eigenvalue whitening is used. Default 1e-10.
- **Long description:** Matrix conditioning values above which Eigenvalue whitening is used. For smaller tresholds, the faster Cholesky whitening is used. Default 1e-10, < 0 forces Eigenvalue whitening.
- **Value type:** Double
- **Default value:** 1e-10
- **Minimum:** -Infinity
- **Maximum:** Infinity

## conflictRule
- **Short description:** Collider conflicts: 1 = Prioritize existing colliders, 2 = Orient bidirected, 3 = Overwrite existing colliders
- **Long description:** 1 if the “overwrite” rule as introduced in the PCALG R package, 2 if all collider conflicts using bidirected edges, or 3 if existing colliders should be prioritized, ignoring subsequent conflicting information.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## connected
- **Short description:** Yes if graph should be connected
- **Long description:** Yes if a random graph should be generated in which paths exists from every node to every other, no if not.
- **Value type:** Boolean
- **Default value:** false

## correlationThreshold
- **Short description:** Correlation Threshold
- **Long description:** The algorithm will complain if correlations are found that are greater than this in absolute value.
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 1

## covHigh
- **Short description:** High end of covariance range (min = 0.0)
- **Long description:** The parameter c2 for range +/-U(c1, c2) for covariance values, c1 >= 0.0
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## covLow
- **Short description:** Low end of covariance range (min = 0.0)
- **Long description:** The parameter c1 for range +/-U(c1, c2) for covariance values, c2 >= c1
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## covSymmetric
- **Short description:** Yes if negative covariance values should be considered
- **Long description:** Usually covariance values are chosen from +/-U(a, b) for some a, b, no if from +U(a, b).
- **Value type:** Boolean
- **Default value:** true

## cpdag
- **Short description:** True if a CPDAG should be returned, false if a DAG
- **Long description:** The algorithm returns a DAG; if this is set to True, this DAG is converted to a CPDAG
- **Value type:** Boolean
- **Default value:** true

## cstarCpdagAlgorithm
- **Short description:** Algorithm: 1 = PC Stable, 2 = FGES, 3 = BOSS, 4 = Restricted BOSS
- **Long description:** The CPDAG algorithm to use: 1 = PC Stable, 2 = FGES, 3 = BOSS, 4 = Restricted BOSS
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 1
- **Maximum:** 4

## cutoffConstrainSearch
- **Short description:** Constraint-independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

## cutoffDataSearch
- **Short description:** Independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

## cutoffIndTest
- **Short description:** Independence cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.0

## cyclicCoefHigh
- **Short description:** Cyclic: High end of coefficient range for coefficients in cycles
- **Long description:** Cyclic: Higb end of coefficient range for coefficients in cycles
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## cyclicCoefLow
- **Short description:** Cyclic: Low end of coefficient range for coefficients in cycles
- **Long description:** Cyclic: Low end of coefficient range for coefficients in cycles
- **Value type:** Double
- **Default value:** 0.2
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## cyclicCoefStyle
- **Short description:** Cyclic: 0 = Auto 1 = Fix Radius 2 = Cap Products, 3 = None,
- **Long description:** Cyclic: 0 = Choose for Me 1 = Scale SCCs to cyclic radius 2 = Cap cyclic products in SCCs, 3 = Regular SEM initialization
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 3

## cyclicMaxProd
- **Short description:** Cyclic: Upper bound on product of coefficients around feedback loops.
- **Long description:** Cyclic: Upper bound on product of coefficients around feedback loops.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## cyclicRadius
- **Short description:** Cyclic: Target spectral radius used to stabilize cyclic feedback.
- **Long description:** Cyclic: Target spectral radius used to stabilize cyclic feedback.
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0
- **Maximum:** 1

## dataType
- **Short description:** "continuous" or "discrete"
- **Long description:** For a mixed data type simulation, if this is set to “continuous” or “discrete”, all variables are taken to be of that sort. This is used as a double-check to make sure the percent discrete is set appropriately.
- **Value type:** String
- **Default value:** categorical
- **Minimum:** 
- **Maximum:** 

## depth
- **Short description:** Maximum size of conditioning set ('depth', unlimited =-1)
- **Long description:** The depth of search for algorithms like the PC adjacency search, which is the maximum size of any conditioning set considered. In order to express that no limit should be imposed, use the value -1.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

## determinismThreshold
- **Short description:** Threshold for judging a regression of a variable onto its parents to be deterministic (min = 0.0)
- **Long description:** When regressing a child variable onto a set of parent variables, one way to test for determinism is to test how close to singular the data is; this gives a threshold for this. The default value is 0.1.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

## differentGraphs
- **Short description:** Yes if a different graph should be used for each run
- **Long description:** If ‘Yes’ a new random graph is chosen for each run; if ‘No’, the same graph is always used.
- **Value type:** Boolean
- **Default value:** false

## discretize
- **Short description:** Yes if continuous variables should be discretized when child is discrete
- **Long description:** Yes if for the conditional Gaussian likelihood, when scoring X->D where X is continuous and D discrete, one should to simply discretize X for just those cases. If no, the integration will be exact.
- **Value type:** Boolean
- **Default value:** true

## doColliderOrientation
- **Short description:** Yes if unshielded collider orientation should be done
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

## doFgesFirst
- **Short description:** Yes if FGES should be done as an initial step
- **Long description:** For BOSS, for some cases, doing FGES as an initial step can reduce the maximum permutation size needed to solve a problem.
- **Value type:** Boolean
- **Default value:** false

## doOneEquationOnly
- **Short description:** True if only one equation should be used when expanding the basis
- **Long description:** True if only one equation should be used when expanding the basis
- **Value type:** Boolean
- **Default value:** false

## doPossibleDsep
- **Short description:** Yes if the possible d-sep search should be done
- **Long description:** This algorithm has a possible d-sep path search, which can be time-consuming. See Spirtes, Glymour, and Scheines (2000) for details.
- **Value type:** Boolean
- **Default value:** true

## ebicGamma
- **Short description:** EBIC Gamma (0-1)
- **Long description:** The gamma parameter for Extended BIC (Chen and Chen). In [0, 1].
- **Value type:** Double
- **Default value:** 0.8
- **Minimum:** 0.0
- **Maximum:** 1.0

## effectiveSampleSize
- **Short description:** The effective sample size, or -1 if the true sample size is to be used.
- **Long description:** The effective sample size, or -1 is the true sample size is to be used.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

## errorsNormal
- **Short description:** Yes if errors should be Normal; No if they should be abs(Normal) (i.e., non-Gaussian)
- **Long description:** A “quick and dirty” way to generate linear, non-Gaussian data is to set this parameter to “No”; then the errors will be sampled from a Beta distribution.
- **Value type:** Boolean
- **Default value:** true

## errorThreshold
- **Short description:** Error Threshold
- **Long description:** Adjusts the threshold for judging conditional dependence.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1

## ess
- **Short description:** Yes if the equivalent sample size should be used in place of N
- **Long description:** We calculate the equivalent sample size by assuming that all record are equally correlated
- **Value type:** Boolean
- **Default value:** false

## excludeSelectionBias
- **Short description:** Yes if the possibility of selection bias should be excluded
- **Long description:** If set to “true,” the algorithm assumes that no selection bias is present and disables selection-related orientation rules (including the final rules of Zhang 2008) and disallows tail–tail (`---`) edges. If set to “false” (the default), selection bias is permitted, and the full FCI orientation rule set is applied.
- **Value type:** Boolean
- **Default value:** false

## extraEdgeRemovalStep
- **Short description:** The extra edge removal step to use: 1 = LV_LITE, 2 = Greedy, 3 = Max P, 4 = Min P
- **Long description:** The extra edge removal step to use: 1 = LV_LITE, 2 = Greedy, 3 = Max P, 4 = Min P
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

## faithfulnessAssumed
- **Short description:** Yes if (one edge) faithfulness should be assumed
- **Long description:** Assumes that if X _||_ Y, by an independence test, then X _||_ Y | Z for nonempty Z.
- **Value type:** Boolean
- **Default value:** false

## faskAdjacencyMethod
- **Short description:** Non-skewness Adjacencies: 1 = FAS Stable, 2 = FGES, 3 = External Graph, 4 = None
- **Long description:** This is the method FASK will use to find non-skewness adjacencies. For External graph, an external graph must be supplied.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

## faskAssumeLinearity
- **Short description:** Linearity assumed
- **Long description:** True if a linear, non-Gaussian, additive model is assume; false if a nonlinear, non-Gaussian, additive model is assumed.
- **Value type:** Boolean
- **Default value:** true

## faskDelta
- **Short description:** For FASK v1, the bias for orienting with negative coefficients ('0' means no bias.)
- **Long description:** The bias procedure for v1 is given in the published description.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

## faskLeftRightRule
- **Short description:** The left right rule: 1 = FASK v1, 2 = FASK v2, 3 = RSkew, 4 = Skew, 5 = Tanh
- **Long description:** The FASK left right rule v2 is default, but two other (related) left-right rules are given for relation to the literature, and the v1 FASK rule is included for backward compatibility.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 5

## faskNonempirical
- **Short description:** Variables should be assumed to have positive skewness
- **Long description:** If false (default), each variable is multiplied by the sign of its skewness in the left-right rule.
- **Value type:** Boolean
- **Default value:** false

## fasRule
- **Short description:** Adjacency search: 1 = PC, 2 = PC-Stable, 3 =f Concurrent PC-Stable
- **Long description:** For variants of PC, one may select either to use the usual PC adjacency search, or the procedure from the PC-Stable algorithm (Diego and Maathuis), or the latter using a concurrent algorithm.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## fastIcaA
- **Short description:** Fast ICA 'a' parameter.
- **Long description:** This is the 'a' parameter of Fast ICA. (See Hyvarinen, A. (2001); it ranges between 1 and 2; we use a default of 1.1.
- **Value type:** Double
- **Default value:** 1.1
- **Minimum:** 1.0
- **Maximum:** 2.0

## fastIcaMaxIter
- **Short description:** The maximum number of optimization iterations.
- **Long description:** This is the maximum number if iterations of the optimization procedure of ICA. (See Hyvarinen, A. (2001). It's an integer greater than 0; we use a default of 2000.
- **Value type:** Double
- **Default value:** 2000
- **Minimum:** 1
- **Maximum:** 500000

## fastIcaTolerance
- **Short description:** Fast ICA tolerance parameter.
- **Long description:** This is the tolerance parameter of Fast ICA. (See Hyvarinen, A. (2001); we use a default of 1e-6.
- **Value type:** Double
- **Default value:** 1e-6
- **Minimum:** 0.0
- **Maximum:** 1000.0

## fcitStartsWith
- **Short description:** The algorithm to find the initial CPDAG: 1 = BOSS, 2 = GRaSP, 3 = SP
- **Long description:** The algorithm to find the initial CPDAG: 1 = BOSS, 2 = GRaSP, 3 = SP
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## fdrQ
- **Short description:** FDR q value, often 0.01 - 0.1, or 0 if FDR should not be done.
- **Long description:** FDR q value, often 0.01 - 0.1, or 0 if FDR should not be done.
- **Value type:** Double
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 1

## fileOutPath
- **Short description:** Results output path
- **Long description:** Path to a directory in which results can be stored
- **Value type:** String
- **Default value:** cstar-out
- **Minimum:** 
- **Maximum:** 

## fisherEpsilon
- **Short description:** Epsilon where |xi.t - xi.t-1| < epsilon, criterion for convergence
- **Long description:** This is a parameter for the linear Fisher option. The idea of Fisher model (for the linear case) is to shock the system every so often and let it converge by applying the rules of transformation (that is, the linear model) repeatedly until convergence.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 4.9E-324
- **Maximum:** 1.7976931348623157E308

## fofcAlpha
- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** 1.0

## generalSemErrorTemplate
- **Short description:** General function for error terms
- **Long description:** This template specifies how distributions for error terms are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** Beta(2, 5)
- **Minimum:** 
- **Maximum:** 

## generalSemFunctionTemplateLatent
- **Short description:** General function template for latent variables
- **Long description:** This template specifies how equations for latent variables are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** TSUM(NEW(B)*$)/>
- **Minimum:** 
- **Maximum:** 

## generalSemFunctionTemplateMeasured
- **Short description:** General function template for measured variables
- **Long description:** This template specifies how equations for measured variables are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** TSUM(NEW(B)*$>
- **Minimum:** 
- **Maximum:** 

## generalSemParameterTemplate
- **Short description:** General function for parameters
- **Long description:** This template specifies how distributions for parameter terms are to be generated. For help in constructing such templates, see the Generalized SEM PM model.
- **Value type:** String
- **Default value:** Split(-1.0, -0.5, 0.5, 1.0)
- **Minimum:** 
- **Maximum:** 

## ginBackend
- **Short description:** Backend test: 1 = dcor 2 = pearson.
- **Long description:** Choose unconditional test for residual independence: “dcor” detects nonlinear relations, “pearson” is fast but linear only.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## ginPermutations
- **Short description:** Number of permutations for dCor.
- **Long description:** Number of random shuffles used to compute p-values for dCor; higher values give more reliable p-values but increase runtime; ignored if backend is pearson.
- **Value type:** Integer
- **Default value:** 200
- **Minimum:** 0
- **Maximum:** 100000

## ginRidge
- **Short description:** Ridge penalty for OLS regression
- **Long description:** Small positive value added to regression diagonals for numerical stability when fitting residual models; larger values regularize more but bias residuals.
- **Value type:** Double
- **Default value:** 1e-8
- **Minimum:** 0
- **Maximum:** 100000

## graspAlg
- **Short description:** 1 = GRaSP1, 2 = GRaSP2, 3 = esp, 4 = GRaSP4, 5 = GRaSP4
- **Long description:** Which version of GRaSP (temp parameter)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

## graspBreakAfterImprovement
- **Short description:** Yes if depth first search returns after first improvement, No for depth first traversal.
- **Long description:** Exploring the full list in every DFS call is equivalent to what we've been calling the Random Carnival Game procedure (RCG).
- **Value type:** Boolean
- **Default value:** true

## graspCheckCovering
- **Short description:** Yes if covering of edges should be checked (GASP), no if not (GRASP)
- **Long description:** An edge X is covered if Parents(X) = Parents(Y) \ {X}. Not checking covering expands the search space.
- **Value type:** Boolean
- **Default value:** false

## graspDepth
- **Short description:** Recursion depth (for GRaSP)
- **Long description:** This is the depth of recursion for the depth first search.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 2147483647

## graspForwardTuckOnly
- **Short description:** Yes if only forward tucks should be checked, no if also reverse tucks should be checked.
- **Long description:** A forward tuck for X->Y moves Y to the before position of X in the permutation. A reverse tuck moves Y to after the position of X in the permutation. Including reverse tucks expands the search space.
- **Value type:** Boolean
- **Default value:** false

## graspNonSingularDepth
- **Short description:** Recursion depth for nonsingular tucks
- **Long description:** This is the depth of recursion at which multiple tucks may be considered per score improvement
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

## graspOrderedAlg
- **Short description:** Yes if earlier GRaSP stages should be performed before later stages
- **Long description:** GRaSP has three stages; these can be performed separately or in order; by default Yes.
- **Value type:** Boolean
- **Default value:** true

## graspSingularDepth
- **Short description:** Recursion depth for singular tucks
- **Long description:** This is the depth of recursion for the singular tucks.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 2147483647

## graspToleranceDepth
- **Short description:** Recursion depth for tolerance tucks
- **Long description:** This is the maximum number of non-greedy tucks in depth first order --that is, tucks where the score is allowed to decrease rather than increase.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## graspUseRaskuttiUhler
- **Short description:** Yes to use Raskutti and Uhler's DAG-building method (test), No to use Grow-Shrink (score).
- **Long description:** Raskutti and Uhler's method adds and edge X->Y if Y ~_||_ X | Prefix(Y, pi) \ {X}. Grow-Shrink adds an edge X->Y if X is in the Markov blanket of Y where the variable set is restricted to Prefix(Y, pi).
- **Value type:** Boolean
- **Default value:** false

## graspUseScore
- **Short description:** Yes if the score should be used for MB calculations, no if the test should be used instead.
- **Long description:** In either case, compositional graphoid axioms are assumed by the Grow-Shrink algorithm.
- **Value type:** Boolean
- **Default value:** true

## graspUseVpScoring
- **Short description:** No sure
- **Long description:** Not sure
- **Value type:** Boolean
- **Default value:** false

## guaranteeAcyclic
- **Short description:** True if the output should be guaranteed to be acyclic
- **Long description:** The estimated B matrix is further thresholded by setting small coefficients to zero until an acyclic model is produced.
- **Value type:** Boolean
- **Default value:** true

## guaranteeCpdag
- **Short description:** Guarantee that the output is a legal CPDAG
- **Long description:** It is possible due to unfaithfulness for the Meek rules to output a non-CPDAG; this parameter guarantees a CPDAG if set to 'Yes'.
- **Value type:** Boolean
- **Default value:** true

## guaranteeIid
- **Short description:** Recursive simulation is used for acyclic models; if not should i.i.d. be assumed?
- **Long description:** For cyclic models, the Fisher simulation model is used, which is a time series. Selecting 'Yes' here guarantees that a new data point starts from a new shock without influence from the previous time step.
- **Value type:** Boolean
- **Default value:** true

## guaranteePag
- **Short description:** Ensure the output is a legal PAG (where feasible)
- **Long description:** Repairs errors in PAGs due to almost cyclic paths or non-maximalities. This comes with a certain risk; errors in PAGs indicate that the PAG assumptions were not met; the user may wish to consider why before selecting this
- **Value type:** Boolean
- **Default value:** false

## henckelPruning
- **Short description:** Whether to do Henckel et al. (2020) Algorithm 1 pruning.
- **Long description:** Whether to do Henckel et al. (2020) Algorithm 1 pruning.
- **Value type:** Boolean
- **Default value:** False

## hiddenDimension
- **Short description:** For Nonlinear Additive Model, the number of nodes per edge
- **Long description:** For a shallow multilayer perception (MLP), the number of nodes in the hidden layer
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 500000

## hiddenDimensions
- **Short description:** For perceptrons, the number of nodes in hidden layers (comma separated)
- **Long description:** For perceptrons, the number of nodes in hidden layers (comma separated)
- **Value type:** String
- **Default value:** 50,50,50,50,50
- **Minimum:** 
- **Maximum:** 

## ia
- **Short description:** IA parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** true

## imagesMetaAlg
- **Short description:** IMaGES "meta" algorithm. 1 = FGES, 2 = BOSS-Tuck
- **Long description:** Sets the meta algorithm to be optimized using the IMaGES (average BIC) score.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

## includeAllNodes
- **Short description:** True if all nodes should be included in the output
- **Long description:** True if all nodes should be included in the output.
- **Value type:** Boolean
- **Default value:** false

## includeNegativeCoefs
- **Short description:** Yes if negative coefficients should be included in the model
- **Long description:** One may include positive coefficients, negative coefficients, or both, in the model. To include negative coefficients, set this parameter to “Yes”.
- **Value type:** Boolean
- **Default value:** true

## includeNegativeSkewsForBeta
- **Short description:** Yes if negative skew values should be included in the model, if Beta errors are chosen
- **Long description:** Yes if negative skew values should be included in the model, if Beta errors are chosen.
- **Value type:** Boolean
- **Default value:** true

## includePositiveCoefs
- **Short description:** Yes if positive coefficients should be included in the model
- **Long description:** Yes if We may include positive coefficients, should be included in the model, no if not.
- **Value type:** Boolean
- **Default value:** true

## includePositiveSkewsForBeta
- **Short description:** Yes if positive skew values should be included in the model, if Beta errors are chosen
- **Long description:** Yes if positive skew values should be included in the model, if Beta errors are chosen.
- **Value type:** Boolean
- **Default value:** true

## inputScale
- **Short description:** For a shallow multilayer perception (MLP), the input scale (affects bumpiness)
- **Long description:** For a shallow multilayer perception (MLP), the input scale (affects bumpiness)
- **Value type:** Double
- **Default value:** 5.0
- **Minimum:** 0.0
- **Maximum:** Infinity

## instanceRow
- **Short description:** Indicates a particular row in the testing dataset (one-indexed)
- **Long description:** If the algorithm uses a testing dataset, this row index points to a specific row in the data to be used as input to the algorithm. This is one-indexed.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

## instanceSpecificAlpha
- **Short description:** Weight for instance-specific component to the score
- **Long description:** Weight for instance-specific component to the score.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0
- **Maximum:** Infinity

## intervalBetweenRecordings
- **Short description:** Interval between data recordings for the linear Fisher model (min = 1)
- **Long description:** 
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## intervalBetweenShocks
- **Short description:** Interval between shocks (R. A. Fisher simulation model) (min = 1)
- **Long description:** This is a parameter for the linear Fisher option. This sets the number of step between shocks.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## ipen
- **Short description:** IPEN parameter (GLASSO)
- **Long description:** This sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

## is
- **Short description:** IS parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

## itr
- **Short description:** ITR parameter (GLASSO)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Boolean
- **Default value:** false

## kciAlpha
- **Short description:** Cutoff for p values (alpha) (min = 0.0)
- **Long description:** Alpha level (0 to 1)
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

## kciCutoff
- **Short description:** Cutoff
- **Long description:** Cutoff for p-values.
- **Value type:** Integer
- **Default value:** 6
- **Minimum:** 1
- **Maximum:** 2147483647

## kciEpsilon
- **Short description:** Epsilon, a small positive number
- **Long description:** See Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012). Kernel-based conditional independence test and application in causal discovery.. This parameter is the epsilon for Proposition 5, a small positive number.
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** Infinity

## kciNumBootstraps
- **Short description:** Number of bootstraps
- **Long description:** This parameter is the number of bootstraps for Theorems 4 from Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012) and Proposition 5, a positive integer.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

## kciUseApproximation
- **Short description:** Use the Gamma approximation algorithm
- **Long description:** Referring to Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012), if this parameter is set to ‘Yes’, the Gamma approximation algorithm is used; if no, the exact procedure is used.
- **Value type:** Boolean
- **Default value:** true

## kernelRegressionSampleSize
- **Short description:** Minimum sample size to use per conditioning for kernel regression
- **Long description:** The smallest set of nearest data points on which to allow a judgment to be based for a nonlinear regression.
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## kernelType
- **Short description:** Kernel type (1 = Gaussian, 2 = Linear, 3 = Polynomial)
- **Long description:** Determines which kernel type will be used (1 = Gaussian, 2 = Linear, 3 = Polynomial).
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## kernelWidth
- **Short description:** Kernel width
- **Long description:** A larger kernel width means that more information will be taken into account but possibly less focused information.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 4.9E-324
- **Maximum:** Infinity

## lambda1
- **Short description:** lambda1
- **Long description:** Tuning parameter for DAGMA
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0
- **Maximum:** Infinity

## lowerBound
- **Short description:** Lower bound cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.3
- **Minimum:** 0.0
- **Maximum:** 1.0

## manualLambda
- **Short description:** Lambda (manually set)
- **Long description:** The manually set lambda for GIC--the default is 10, though this should be set by the user to a good value.
- **Value type:** Double
- **Default value:** 10.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## maxBlockingPathLength
- **Short description:** Maximum path length for paths for searching for path blocking sets (-1 = no limit)
- **Long description:** The maximum length of paths to search for path blocking sets.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

## maxCategories
- **Short description:** Maximum number of categories (min = 2)
- **Long description:** The maximum number of categories to be used for randomly generated discrete variables. The default is 2. This needs to be greater or equal to than the minimum number of categories.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

## maxCorrelation
- **Short description:** Maximum absolute correlation considered
- **Long description:** For the Nandy rule, the absolute max correlation r. For the standard BIC or high-dimensional rule, the maximum absolute residual correlation.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## maxDegree
- **Short description:** The maximum degree of the graph (min = -1)
- **Long description:** An upper bound on the maximum degree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

## maxDiscriminatingPathLength
- **Short description:** The maximum length for any discriminating path. -1 if unlimited (min = -1)
- **Long description:** See Spirtes, Glymour, and Scheines (2000) for the definition of discrimination path. Finding discriminating paths can be expensive. This sets the maximum length of such paths that the algorithm tries to find.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

## maxDistinctValuesDiscrete
- **Short description:** The maximum number of distinct values in a column for discrete variables (min = 0)
- **Long description:** Discrete variables will be simulated using any number of categories from 2 up to this maximum. If set to 0 or 1, discrete variables will not be generated.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## maxIndegree
- **Short description:** Maximum indegree of graph (min = 1)
- **Long description:** An upper bound on the maximum indegree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

## maxit
- **Short description:** MAXIT parameter (GLASSO) (min = 1)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Integer
- **Default value:** 10000
- **Minimum:** 1
- **Maximum:** 2147483647

## maxIterations
- **Short description:** The maximum number of iterations the algorithm should go through orienting edges
- **Long description:** In orienting, this algorithm may go through a number of iterations, conditioning on more and more variables until orientations are set. This sets that number.
- **Value type:** Integer
- **Default value:** 15
- **Minimum:** 0
- **Maximum:** 2147483647

## maxOutdegree
- **Short description:** Maximum outdegree of graph (min = 1)
- **Long description:** An upper bound on the maximum outdegree of any node in the graph. If no limit is to be placed on the maximum degree, use the value -1.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

## maxPaxPOrientationHeuristicMaxLength
- **Short description:** The maximum path length to use for the max p heuristic version.
- **Long description:** The maximum path length to use for the max p heuristic version.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** 100000

## maxPOrientationMaxPathLength
- **Short description:** Maximum path length for the unshielded collider heuristic for max P (min = 0)
- **Long description:** For the Max P “heuristic” to work, it must be the case that X and Z are only weakly associated—that is, that paths between them are not too short. This bounds the length of paths for this purpose.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 2147483647

## maxRank
- **Short description:** The algorithm looks for clusters from rank 1 up through this rank
- **Long description:** The algorithm looks for clusters from rank 1 up through this rank
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 1000

## maxScoreDrop
- **Short description:** Maximum score drop for the process triples step
- **Long description:** In orienting unshielded colliders by examining triples of nodes, the score is permitted to drop by this much.
- **Value type:** Double
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** Infinity

## maxSepsetSize
- **Short description:** For testing steps in FCIT, the maximum conditioning set size
- **Long description:** In the extra edge removal step, we build conditioning sets based on the current PAG to attempt to remove adjacencies from the graph, by blocking paths from x to y of up to this length. This is the maximum size these sets are allowed to grow to.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 0
- **Maximum:** 2147483647

## mb
- **Short description:** Find Markov blanket(s)
- **Long description:** Looks for the graph over the Markov blanket(s) and target(s) if true
- **Value type:** Boolean
- **Default value:** false

## mcAlpha
- **Short description:** Markov Checker Alpha Level (0 to 1)
- **Long description:** Markov Checker Alpha Level (0 to 1)
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

## meanHigh
- **Short description:** High end of mean range (min = 0.0)
- **Long description:** The default is for there to be no shift in mean, but shifts from a minimum value to a maximum value may be specified. The minimum must be less than or equal to this maximum.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## meanLow
- **Short description:** Low end of mean range (min = 0.0)
- **Long description:** The default is for there to be no shift in mean, but shifts from a minimum value to a maximum value may be specified. The minimum must be greater than or equal to this minimum.
- **Value type:** Double
- **Default value:** 0.5
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## measurementVariance
- **Short description:** Additive measurement noise variance (min = 0.0)
- **Long description:** If the value is greater than zero, independent Gaussian noise will be added with mean zero and the given variance to each variable in the simulated output.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## mgmParam1
- **Short description:** MGM tuning parameter #1 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## mgmParam2
- **Short description:** MGM tuning parameter #2 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## mgmParam3
- **Short description:** MGM tuning parameter #3 (min = 0.0)
- **Long description:** The MGM algorithm has three internal tuning parameters, of which this is one.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## mimbuildType
- **Short description:** Mimbuild type: 1 = PCA, 2 = Bollen
- **Long description:** Mimbuild type: 1 = PCA, 2 = Bollen
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## mimLatentGroupSpecs
- **Short description:** MIM: List of count:children:(rank), comma separated; e.g. 5:6(1),2:8(2):
- **Long description:** List of count:children:(rank), comma separated; e.g. 5:6(1),2:8(2)
- **Value type:** String
- **Default value:** 5:6(1)
- **Minimum:** 
- **Maximum:** 

## mimLatentMeasuredImpureParents
- **Short description:** MIM: Number of Latent --> Measured impure edges
- **Long description:** It is possible for structural nodes to have as children measured variables that are children of other structural nodes. These edges in the graph will be considered impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimMeasuredMeasuredImpureAssociations
- **Short description:** MIM: Number of Measured <-> Measured impure edges
- **Long description:** It is possible for measures from two different structural nodes to be confounded. These confounding (bidirected) edges will be considered to be impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimMeasuredMeasuredImpureParents
- **Short description:** MIM: Number of Measured --> Measured impure edges
- **Long description:** It is possible for measures from two different structural nodes to have directed edges between them. These edges will be considered to be impure.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimMetaEdgeConnectionType
- **Short description:** 1 = Cartesian Product 2 = Corresponding, 3 = Patchy Connections
- **Long description:** 1 = Cartesian Product 2 = Corresponding, 3 = Patchy Connections
- **Value type:** 
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3 Value Type: Integer

## mimMimNumStructuralNodes
- **Short description:** Number of measurements per Latent
- **Long description:** Each structural node in the MIM will be created to have this many measured children.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimNumChildrenPerGroup
- **Short description:** MIM: Number of children for each group latents
- **Long description:** Each group of latents shares a common set of children of this size.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimNumStructuralEdges
- **Short description:** MIM: Number of structural edges
- **Long description:** This is a parameter for generating random multiple indicator models (MIMs). A structural edge is an edge connecting two structural nodes.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## mimNumStructuralNodes
- **Short description:** Number of structural nodes
- **Long description:** This is a parameter for generating random multiple indicator models (MIMs). A structural node is one of the latent variables in the model; each structural node has a number of child measured variables.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## minCategories
- **Short description:** Minimum number of categories (min = 2)
- **Long description:** The minimum number of categories to be used for randomly generated discrete variables. The default is 2.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

## minCountPerCell
- **Short description:** The minimum count per cell in a chi square table.
- **Long description:** Increasing this can improve accuracy of chi square estimates.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

## minParamSampleSize
- **Short description:** The minimum sample size per parameter
- **Long description:** The minimum sample size per parameter
- **Value type:** Integer
- **Default value:** 20
- **Minimum:** 1
- **Maximum:** 100000000

## minSampleSizePerCell
- **Short description:** For conditional Gaussian, the minimum sample size per cell
- **Long description:** For conditional Gaussian, the minimum sample size per cell
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 100000000

## mnarNumExtraInfluences
- **Short description:** MNAR: The number of extra influences on missing value selection.
- **Long description:** id="mnarNumExtraInfluences_short_desc"> MNAR: The number of extra influences on missing value selection.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## mnarNumVariablesWithMissing
- **Short description:** MNAR: The number of variables with missing values.
- **Long description:** id="mnarNumVariablesWithMissing_short_desc"> MNAR: The number of variables with missing values.
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 0
- **Maximum:** 2147483647

## mnarThreshold
- **Short description:** MNAR: Remove this fraction upper tail values for columns with missing values
- **Long description:** id="mnarThreshold_short_desc"> MNAR: Remove this fraction upper tail values for columns with missing values
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** 1.0

## noRandomlyDeterminedIndependence
- **Short description:** Yes, if using the cutoff threshold for the independence test.
- **Long description:** null
- **Value type:** Boolean
- **Default value:** false

## numBasisFunctions
- **Short description:** Number of functions to use in (truncated) basis
- **Long description:** This parameter specifies how many of the most significant basis functions to use as a basis.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 2147483647

## numberOfExpansions
- **Short description:** Number of expansions of the algorithm away from the target
- **Long description:** Each expansion iterates to concentrically more variables
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 1000

## numberResampling
- **Short description:** The number of bootstraps/resampling iterations (min = 0)
- **Long description:** For bootstrapping, the number of bootstrap iterations that should be done by the algorithm, with results summarized.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## numBscBootstrapSamples
- **Short description:** The number of bootstrappings drawing from posterior dist. (min = 1)
- **Long description:** The number of bootstrappings drawing from posterior dist. (min = 1)
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 2147483647

## numCategories
- **Short description:** Number of categories for discrete variables (min = 2)
- **Long description:** The number of categories to be used for randomly generated discrete variables. The default is 4; the minimum is 2.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 2
- **Maximum:** 2147483647

## numCategoriesToDiscretize
- **Short description:** The number of categories used to discretize continuous variables, if necessary (min = 2)
- **Long description:** In case the exact algorithm is not used for discrete children and continuous parents is not used, this parameter gives the number of categories to use for this second (discretize) backup copy of the continuous variables.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 2
- **Maximum:** 2147483647

## numLags
- **Short description:** The number of lags in the time lag model
- **Long description:** A time lag model may take variables from previous time steps into account. This determines how many steps back these relevant variables might go.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## numLatents
- **Short description:** Number of additional latent variables (min = 0)
- **Long description:** The number of additional latent variables to include in the datasets
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## numMeasures
- **Short description:** Number of measured variables (min = 1)
- **Long description:** The number of measured (recorded in data) variables to include in the dataset.
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## numRandomizedSearchModels
- **Short description:** The number of search probabilistic model (min = 1)
- **Long description:** The number of search probabilistic model (min = 1)
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## numRuns
- **Short description:** Number of runs (min = 1)
- **Long description:** An analysis(randomly pick graph, randomly simulate a dataset, run an algorithm on it, look at the result) may be run over and over again this many times.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2147483647

## numStarts
- **Short description:** Number of sub-samples
- **Long description:** Number of sub-samples
- **Value type:** Integer
- **Default value:** 50
- **Minimum:** 1
- **Maximum:** 500000

## numSubsamples
- **Short description:** The number of subsamples to generate.
- **Long description:** CStaR works by generating subsamples and summarizing across them; this specified the number of subsamples to generate. Must be >= 1. effects in the CStaR table
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 100000

## numThreads
- **Short description:** The number of threads (>= 1) to use for the search
- **Long description:** The number of threads to use for the search.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 1000000

## orientationAlpha
- **Short description:** Alpha threshold used for orientation (where necessary). ('0' turns this off.)
- **Long description:** Used for orienting 2-cycles and testing for zero edges.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## orientTowardMConnections
- **Short description:** Yes if Richardson's step C (orient toward d-connection) should be used
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

## orientVisibleFeedbackLoops
- **Short description:** Yes if visible feedback loops should be oriented
- **Long description:** Please see the description of this algorithm in Thomas Richardson and Peter Spirtes in Chapter 7 of Computation, Causation, & Discovery by Glymour and Cooper eds.
- **Value type:** Boolean
- **Default value:** true

## otherPermMethod
- **Short description:** 1 = RCG, 2 = GSP, 3 = ESP, 4 = SP
- **Long description:** RCG (Random Carnival Game); GSP ("Greedy SP") GSP using tucking ESP ("Edge SP") is from Solus et al. SP ("Sparsest Permutation") Raskutti and Uhler
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

## outputCpdag
- **Short description:** Yes if CPDAG should be output, no if a DAG.
- **Long description:** BOSS can output a DAG or the CPDAG of the DAG.
- **Value type:** Boolean
- **Default value:** true

## outputRBD
- **Short description:** Constraint Scoring: Yes: Dependent Scoring, No: Independent Scoring.
- **Long description:** Constraint Scoring: Yes: Dependent Scoring, No: Independent Scoring.
- **Value type:** Boolean
- **Default value:** true

## parallelized
- **Short description:** Yes if the search should be parallelized
- **Long description:** This search is capable of being parallelized; select yes if the search should be parallelized, not if it should be run in a single thread
- **Value type:** Boolean
- **Default value:** false

## pathsMaxDistanceFromEndpoint
- **Short description:** The maximum distance of an allowable node from the endpoint of a path for adjustment
- **Long description:** In order to give guidance to which adjustment sets to report, this parameter lets one give a maximum distance from the endpoint of a path for a node to be included in an adjustment set.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 0
- **Maximum:** 100000

## pathsMaxLength
- **Short description:** The maximum length of a path to report
- **Long description:** Since paths may be long, especially for large graphs, this parameter allows one to limit the length of a path to report. It must be at least 2.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 2
- **Maximum:** 100000

## pathsMaxLengthAdjustment
- **Short description:** The maximum length of a backdoor path to consider for adjustment.
- **Long description:** The maximum length of a backdoor path to consider for finding an adjustment set. Amenable paths of any length are considered.
- **Value type:** Integer
- **Default value:** 8
- **Minimum:** 2
- **Maximum:** 100000

## pathsMaxNumSets
- **Short description:** The maximum number of adjustment sets to output
- **Long description:** There may be too many legal adjustments to sets to output; this places a bound on how many to output. These will be listed in order of increasing size.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 0
- **Maximum:** 100000

## pathsNearWhichEndpoint
- **Short description:** 1 = near source, 2 = near target, 3 = near either
- **Long description:** Adjustment sets may be found near the source, near the target, or near either.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## pcHeuristic
- **Short description:** Heuristics to stabilize skeleton: 0 = None, 1 = Heuristic 1, 2 = Heuristic 2, 3 = Heuristic 3
- **Long description:** NONE = no heuristic, PC-1 = sort nodes alphabetically; PC-1 = sort edges by p-value; PC-3 = additionally sort edges in reverse order using p-values of associated independence facts. See CPS.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 3

## penaltyDiscount
- **Short description:** Penalty discount (min = 0.0)
- **Long description:** The parameter c added to a modified BIC score of the form 2L – c k ln N, where L is the likelihood, k the number of degrees of freedom, and N the sample size. Higher c yield sparser graphs.
- **Value type:** Double
- **Default value:** 2.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## penaltyDiscountZs
- **Short description:** Penalty discount (min = 0.0)
- **Long description:** The parameter c added to a modified BIC score of the form 2L – c k lambda, where L is the likelihood, k the number of degrees of freedom, and lambda the choice of GIC lambda. Higher c yield sparser graphs.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## percentDiscrete
- **Short description:** Percentage of discrete variables (0 - 100) for mixed data
- **Long description:** For a mixed data type simulation, specifies the percentage of variables that should be simulated (randomly) as discrete. The rest will be taken to be continuous. The default is 0—i.e. no discrete variables.
- **Value type:** Double
- **Default value:** 50.0
- **Minimum:** 0.0
- **Maximum:** 100.0

## percentResampleSize
- **Short description:** The percentage of resample size (min = 10%)
- **Long description:** This parameter specifies the percentage of records in the bootstrap (as a percentage of the total original sample size of the data being bootstrapped).
- **Value type:** Integer
- **Default value:** 100
- **Minimum:** 10
- **Maximum:** 100

## piThr
- **Short description:** A fixed threshold for calculating E[V] and PCER
- **Long description:** A fixed threshold, default 0.5
- **Value type:** Double
- **Default value:** 0.6
- **Minimum:** 0
- **Maximum:** 1

## poissonLambda
- **Short description:** Lambda parameter for the Poisson distribution (> 0)
- **Long description:** Lambda parameter for the Poisson distribution
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 1e-10
- **Maximum:** Infinity

## polynomialConstant
- **Short description:** For polynomial kernel: The constant
- **Long description:** The constant of the polynomial kernel, if used, which determine tradeoff between higher and lower order terms
- **Value type:** Double
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 5000

## polynomialDegree
- **Short description:** For polynomial kernel: The degree
- **Long description:** The degree of the polynomial kernel, if used
- **Value type:** Double
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 5000000

## precomputeCovariances
- **Short description:** True if covariance matrix should be precomputed for tabular continuous data
- **Long description:** For more than 5000 variables or so, set this to false in order to calculate covariances on the fly from data.
- **Value type:** Boolean
- **Default value:** true

## preserveMarkov
- **Short description:** Preserve the Markov property (checking MBs) if initial graph is Markov
- **Long description:** The Markov property checking MBs says that if msep(x, y | MB(x)) then x _||_ y | MB(x). Checking true for this property will tell the algorithm to ensure this property if the scoring step produces a Markov graph. Not applicable when running the algorithm from Oracle.
- **Value type:** Boolean
- **Default value:** false

## priorEquivalentSampleSize
- **Short description:** Prior equivalent sample size (min = 1.0)
- **Long description:** This sets the prior equivalent sample size. This number is added to the sample size for each conditional probability table in the model and is divided equally among the cells in the table.
- **Value type:** Double
- **Default value:** 10.0
- **Minimum:** 1.0
- **Maximum:** 1.7976931348623157E308

## probabilityOfEdge
- **Short description:** Probability of an adjacency being included in the graph
- **Long description:** Every possible adjacency in the graph is included it the graph with this probability.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

## probCycle
- **Short description:** The probability of adding a cycle to the graph
- **Long description:** Sets the probability that any particular set of 3, 4, or 5 of nodes will be used to form a cycle in the graph.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## probRemoveColumn
- **Short description:** Probability of randomly removing a column from a dataset
- **Long description:** For testing algorithms with overlapping variables, columns may be removed from datasets with this probability.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## probTwoCycle
- **Short description:** The probability of creating a 2-cycles in the graph (0 - 1)
- **Long description:** Any edge X*-*Y may be replaced with a 2-cycle (feedback loop) between X and Y with this probability.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## randomizeColumns
- **Short description:** Yes if the order of the columns in each dataset should be randomized
- **Long description:** In the real world where unfaithfulness is an issue the order of variables in the data may for some algorithms affect the output. For testing purposes, if Yes, the data columns are randomly re-ordered.
- **Value type:** Boolean
- **Default value:** true

## randomSelectionSize
- **Short description:** Use RCIT (true) or RCoT (false)
- **Long description:** Chooses between the two randomized kernel tests: RCIT augments Y with Z features (tests X ⟂ Y,Z | Z), while RCoT uses only X and Y features with residualization against Z. In the original RCIT code base this switch is exposed as rcit=True/False.
- **Value type:** Boolean
- **Default value:** true

## rcitNumFeatures
- **Short description:** The number of random features to use
- **Long description:** 
- **Value type:** Integer
- **Default value:** 10
- **Minimum:** 1
- **Maximum:** 2147483647

## recursive
- **Short description:** Yes if the algorithm should proceed recursively, no if not
- **Long description:** Where recursive or nonrecursive variants of an algorithm are available, this selects which one to use.
- **Value type:** Boolean
- **Default value:** false

## regularizationLambda
- **Short description:** Small number >= 0 Add lambda to the the diagonal of correlation/covariance matrices. Default 1e-8.
- **Long description:** Small number >= 0 Add lambda to the the diagonal of correlation/covariance matricers. Default 1e-8.
- **Value type:** Double
- **Default value:** 1e-8
- **Minimum:** 0
- **Maximum:** Infinity

## removeAlmostCycles
- **Short description:** Yes if almost-cycles should be removed from the PAG.
- **Long description:** When x <-> y, x ~~> y, removes any unshielded triples into x and rebuilds the PAG.
- **Value type:** Boolean
- **Default value:** false

## removeEffectNodes
- **Short description:** True if effect nodes should bre removed from possible causes
- **Long description:** True if effect nodes should be removed from possible causes
- **Value type:** Boolean
- **Default value:** true

## resamplingEnsemble
- **Short description:** Ensemble method: Preserved (1), Highest (2), Majority (3)
- **Long description:** Preserved = keep the highest frequency edges; Highest = keep the highest frequency edges but ignore the no edge case if maximal; Majority = keep edges only if their frequency is greater than 0.5.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## resamplingWithReplacement
- **Short description:** Yes, if sampling with replacement (bootstrapping)
- **Long description:** Yes if resampling can be done with replacement, No if not. or without replacement. If with replacement, it is possible to have more than one copy of some of the records in the original dataset being included in the bootstrap.
- **Value type:** Boolean
- **Default value:** true

## resolveAlmostCyclicPaths
- **Short description:** True just in case almost cyclic paths should be resolved in the direction of the cycle.
- **Long description:** If true we resolved <-> edges as --> if there is a directed path x~~>y.
- **Value type:** Boolean
- **Default value:** false

## sampleSize
- **Short description:** Sample size (min = 1)
- **Long description:** Determines now many records should be generated for the data. The minimum number of records is 1; the default is set to 1000.
- **Value type:** Integer
- **Default value:** 1000
- **Minimum:** 1
- **Maximum:** 2147483647

## saveBootstrapGraphs
- **Short description:** Yes if individual bootstrapping graphs should be saved
- **Long description:** Bootstrapping provides a summary over individual search graphs; select Yes here if these individual graphs should be saved
- **Value type:** Boolean
- **Default value:** false

## saveLatentVars
- **Short description:** Save latent variables.
- **Long description:** Yes if one wishes to have values for latent variables saved out with the rest of the data; No if only data for the measured variables should be saved.
- **Value type:** Boolean
- **Default value:** false

## scaleFreeAlpha
- **Short description:** For scale-free graphs, the parameter alpha (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Double
- **Default value:** 0.05
- **Minimum:** 0.0
- **Maximum:** 1.0

## scaleFreeBeta
- **Short description:** For scale-free graphs, the parameter beta (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Double
- **Default value:** 0.9
- **Minimum:** 0.0
- **Maximum:** 1.0

## scaleFreeDeltaIn
- **Short description:** For scale-free graphs, the parameter delta_in (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## scaleFreeDeltaOut
- **Short description:** For scale-free graphs, the parameter delta_out (min = 0.0)
- **Long description:** We use the algorithm for generating scale free graphs described in B. Bollobas,C. Borgs, J. Chayes, and O. Riordan (2003). Please see this article for a description of the parameters.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** -2147483648
- **Maximum:** 2147483647

## scalingFactor
- **Short description:** Scaling factor.
- **Long description:** For Gaussian kernel: The scaling factor.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 4.9E-324
- **Maximum:** Infinity

## seed
- **Short description:** Seed for pseudorandom number generator (-1 = off)
- **Long description:** The seed is the initial value of the internal state of the pseudorandom number generator. A value of -1 skips setting a new seed.
- **Value type:** Long
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 9223372036854775807

## selectionMinEffect
- **Short description:** Minimum effect size for listing effects in the CStaR table
- **Long description:** Minimum effect size for listing effects in the CStaR table
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## selfLoopCoef
- **Short description:** The coefficient for the self-loop (default 0.0)
- **Long description:** For simulating time series data, each variable depends on itself one time-step back with a linear edge that has this coefficient.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** Infinity

## semBicRule
- **Short description:** Lambda: 1 = Chickering, 2 = Nandy
- **Long description:** The Chickering Rule uses the difference of BIC scores to add or remove edges. The Nandy et al. rule uses a single calculation of a partial correlation in place of the likelihood difference.
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## semBicStructurePrior
- **Short description:** Structure Prior for SEM BIC (default 0)
- **Long description:** Structure prior; default is 0 (turned off); may be any positive number otherwise
- **Value type:** Double
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** Infinity

## semGicRule
- **Short description:** Lambda: 1 = ln n, 2 = pn^1/3, 3 = 2 ln pn, 4 = 2(ln pn + ln ln pn), 5 = ln ln n ln pn, 6 = ln n ln pn, 7 = Manual
- **Long description:** The rule used for calculating the lambda term of the score. We follow Kim, Y., Kwon, S., & Choi, H. (2012) and articles referenced therein. For high-dimensional data.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 1
- **Maximum:** 7

## semImSimulationType
- **Short description:** Yes if recursive simulation, No if reduced form simulation
- **Long description:** Determines the type of simulation done. If recursive, the graph must be a DAG in causal order. "Reduced form" means X = (I - B)^-1 e, which requires a possibly large matrix inversion.
- **Value type:** Boolean
- **Default value:** true

## sepsetFinderMethod
- **Short description:** The method to use for finding sepsets, 1 = Greedy, 2 = Min-p, 3 = Max-p (default).
- **Long description:** The method to use for finding sepsets, 1 = Greedy, 2 = Min-p, 3 = Max-p (default).
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 3

## shrinkageMode
- **Short description:** Shrinkage Mode: 1 = None 2 = Ridge 3 = Ledoit-Wolf
- **Long description:** Shrinkage Mode: 1 = None 2 = Ridge 3 = Ledoit-Wolf
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3

## significanceChecked
- **Short description:** True if the significance of the cluster should be checked.
- **Long description:** True if the significance of clusters should be checked, false if not.
- **Value type:** Boolean
- **Default value:** false

## simulationErrorType
- **Short description:** 1 = Usual LG SEM, 2 = U(lb, ub), 3 = Exp(lambda), 4 = Gumbel(mu, beta), 5 = Gamma(shape, scale)
- **Long description:** Exogenous error type
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 5

## simulationParam1
- **Short description:** Indep error parameter #1
- **Long description:** Exogenous error parameter #1
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -1000
- **Maximum:** 1000

## simulationParam2
- **Short description:** Indep error parameter #2, if used
- **Long description:** Exogenous error parameter #2
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** -1000
- **Maximum:** 1000

## singularityLambda
- **Short description:** Singularities: Small number >= 0 Add lambda to the the diagonal, < 0 Pseudoinverse
- **Long description:** Singularities: Small number >= 0 Add lambda to the the diagonal, < 0 Pseudoinverse
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** -Infinity
- **Maximum:** Infinity

## skewEdgeThreshold
- **Short description:** Threshold for including additional edges detectable by skewness
- **Long description:** For FASK, this includes an adjacency X—Y in the model if |corr(X, Y | X > 0) – corr(X, Y | Y > 0)| exceeds some threshold. The default for this threshold is 0.3.
- **Value type:** Double
- **Default value:** 0.3
- **Minimum:** 0.0
- **Maximum:** Infinity

## skipNumRecords
- **Short description:** Number of records that should be skipped between recordings (min = 0)
- **Long description:** Data recordings are made every this many steps.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## stableFAS
- **Short description:** Yes if the Colombo et al. 'stable' FAS should be done, to avoid skeleton order dependency
- **Long description:** If Yes, the "stable" version of the PC adjacency search is used, which for k > 0 fixes the graph for depth k + 1 to that of the previous depth k.
- **Value type:** Boolean
- **Default value:** true

## standardize
- **Short description:** Yes if the data should be standardized
- **Long description:** Yes if each variable in the data should be standardized to have mean zero and variance 1.
- **Value type:** Boolean
- **Default value:** false

## startFromCompleteGraph
- **Short description:** Yes, if the procedure should start from a complete graph
- **Long description:** Yes, if the procedure should start from a complete graph
- **Value type:** Boolean
- **Default value:** false

## structurePrior
- **Short description:** Structure prior coefficient (min = 0.0)
- **Long description:** The default number of parents for any conditional probability table. Higher weight is accorded to tables with about that number of parents. The prior structure weights are distributed according to a binomial distribution.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## symmetricFirstStep
- **Short description:** Yes if the first step for FGES should do scoring for both X->Y and Y->X
- **Long description:** If Yes, scores for both X->Y and X<-Y will be calculated and the higher score used.
- **Value type:** Boolean
- **Default value:** false

## takeLogs
- **Short description:** Yes logs should be taken, No if not
- **Long description:** The formula for the score allows a log to be taken optionally in the information term.
- **Value type:** Boolean
- **Default value:** true

## targetName
- **Short description:** Target variable name
- **Long description:** The name of the target variables--for Markov blanket searches, this is the name of the variable for which one wants the Markov blanket or Markov blanket graph.
- **Value type:** String
- **Default value:** 
- **Minimum:** 
- **Maximum:** 

## targets
- **Short description:** Target names (comma or space separated)
- **Long description:** Target names (comma or space separated).
- **Value type:** String
- **Default value:** 
- **Minimum:** 
- **Maximum:** 

## testTimeout
- **Short description:** Yes if the algorithm should try moving variables pairwise
- **Long description:** In some cases, two moves are required simultaneously to get an orientation right in the final step. This is not generally needed when optimizing using BIC or for large models.
- **Value type:** Boolean
- **Default value:** true

## tetrad_test_bpc
- **Short description:** The tetrad test used: 1 = Wishart, 2 = Delta (Bollen-Ting)
- **Long description:** The tetrad test used: 1 = Wishart, 2 = Delta
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 1
- **Maximum:** 2

## tetrad_test_fofc
- **Short description:** The tetrad test used: 1 = CCA, 2 = Bollen-Ting, 3 = Wishart
- **Long description:** The tetrad test used: 1 = CCA, 2 = Bollen-Ting, 3 = Wishart
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 4

## thr
- **Short description:** THR parameter (GLASSO) (min = 0.0)
- **Long description:** Sets the maximum number of iterations of the optimization loop.
- **Value type:** Double
- **Default value:** 1.0E-4
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## thresholdBHat
- **Short description:** Threshold on the B Hat matrix.
- **Long description:** The estimated B matrix is thresholded by setting small entries less than this threshold to zero.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

## thresholdForNumEigenvalues
- **Short description:** Threshold to determine how many eigenvalues to use--the lower the more (0 to 1)
- **Long description:** Referring to Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012), this parameter is the threshold to determine how many eigenvalues to use--the lower the more (0 to 1).
- **Value type:** Double
- **Default value:** 0.001
- **Minimum:** 0.0
- **Maximum:** Infinity

## thresholdNoRandomConstrainSearch
- **Short description:** Yes, if using the cutoff threshold for the meta-constraints independence test (stage 2).
- **Long description:** Yes, if using the cutoff threshold for the meta-constraints independence test (stage 2).
- **Value type:** Boolean
- **Default value:** true

## thresholdNoRandomDataSearch
- **Short description:** Yes, if using the cutoff threshold for the constraints independence test (stage 1).
- **Long description:** null
- **Value type:** Boolean
- **Default value:** false

## thresholdW
- **Short description:** Threshold on the W matrix.
- **Long description:** The estimated W matrix is thresholded by setting small entries less than this threshold to zero.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0.0
- **Maximum:** Infinity

## timeLag
- **Short description:** For time lag searches,`a time lag, automatically applied (zero if none)
- **Long description:** Automatically applies the time lag transform to the data, creating additional lagged variables. If zero, no time lag is applied. A positive integer
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 2147483647

## timeLagReplicatingGraph
- **Short description:** For time lag searches, whether to make the graph replicate edges across time lags, SVAR-style
- **Long description:** For time lag searches, whether to make the graph replicate edges across time lags, SVAR-style
- **Value type:** Boolean
- **Default value:** false

## timeLimit
- **Short description:** Time limit
- **Long description:** T-Separation requires a time limit. Default 1000.
- **Value type:** Double
- **Default value:** 1000.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## timeout
- **Short description:** Timeout (best graph returned, -1 = no timeout)
- **Long description:** The algorithm will time out at approximately this number of seconds from when it started and return the final graph found at that point.
- **Value type:** Integer
- **Default value:** -1
- **Minimum:** -1
- **Maximum:** 2147483647

## topBracket
- **Short description:** Top bracket to look for causes in
- **Long description:** Top bracket, 'q'
- **Value type:** Integer
- **Default value:** 5
- **Minimum:** 1
- **Maximum:** 500000

## trimmingStyle
- **Short description:** Trimming Style: 1 = None, 2 = Adjacencies, 3 = MB DAG, 4 = Possibly directed paths
- **Long description:** 'Adjacencies' trims to the adjacencies the targets, MB DAGs to the Union(MB(targets)) U targets, potentially directed trims to nodes with potentially directed paths to the targets.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 4

## trueErrorVariance
- **Short description:** True error variance
- **Long description:** The true error variance of the model, assuming this is the same for all variables.
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## truncationLimit
- **Short description:** Truncation limit for basis functions
- **Long description:** Basis functions 1 though this number will be used.. The Degenerate Gaussian category indicator variables for mixed data are also used.
- **Value type:** Integer
- **Default value:** 3
- **Minimum:** 1
- **Maximum:** 1000

## tscClusterRank
- **Short description:** TSC cluster rank (if desired)
- **Long description:** TSC cluster rank (if desired)
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 0
- **Maximum:** 500

## tscClusterSize
- **Short description:** TSC cluster size (if desired)
- **Long description:** TSC cluster size (if desired)
- **Value type:** Integer
- **Default value:** 2
- **Minimum:** 0
- **Maximum:** 500

## tscEnableHierarchy
- **Short description:** Yes, if hierarchical latents should be detected
- **Long description:** Yes, if hierarchical latents should be detected
- **Value type:** Boolean
- **Default value:** true

## tscMinRankDrop
- **Short description:** Min rank drop for detecting hierarchical latents
- **Long description:** Min rank drop for detecting hierarchical latents
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 100

## tscMinRedundancy
- **Short description:** Minimum redundancy for clusters beyond size = rank + 1
- **Long description:** Minimum redundancy: require at least k extra indicators per latent (|C| ≥ r+1+k). Higher values suppress trivially sized clusters.
- **Value type:** Integer
- **Default value:** 0
- **Minimum:** 0
- **Maximum:** 1000

## tscMode
- **Short description:** TSC mode: 1 = Metaloop, 2 = Specific size/rank
- **Long description:** TSC mode: 1 = Metaloop, 2 = Specific cluster size/rank
- **Value type:** Integer
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 2

## tscPcUseBoss
- **Short description:** Yes, if the procedure should use BOSS (with the BOSS-specific parameters) and not PC
- **Long description:** Yes, if the procedure should use BOSS (with the BOSS-specific parameters) and not PC
- **Value type:** Boolean
- **Default value:** false

## tscSingletonPolicy
- **Short description:** Singletons: 1 = Exclude 2 = Include 3 = Collect as Noise
- **Long description:** Singletons: 1 = Exclude 2 = Include 3 = Collect as Noise
- **Value type:** 
- **Default value:** 1
- **Minimum:** 1
- **Maximum:** 3 Value Type: Integer

## twoCycleAlpha
- **Short description:** Alpha orienting 2-cycles (min = 0.0)
- **Long description:** The alpha level of a T-test used to determine where 2-cycles exist in the graph. A value of zero turns off 2-cycle detection.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** 1.0

## twoCycleScreeningThreshold
- **Short description:** Upper bound for |left-right| to count as 2-cycle. (Set to zero to turn off pre-screening.)
- **Long description:** 2-cycles are screened by looking to see if the left-right rule returns a difference smaller than this threshold. To turn off the screening, set this to zero.
- **Value type:** Double
- **Default value:** 0.0
- **Minimum:** 0.0
- **Maximum:** Infinity

## upperBound
- **Short description:** Upper bound cutoff threshold
- **Long description:** null
- **Value type:** Double
- **Default value:** 0.7
- **Minimum:** 0.0
- **Maximum:** 1.0

## useBes
- **Short description:** True if the optional BES step should be used
- **Long description:** This algorithm can use the backward equivalence search from the GES algorithm as one of its steps.
- **Value type:** Boolean
- **Default value:** false

## useCorrDiffAdjacencies
- **Short description:** Yes if adjacencies from conditional correlation differences should be used
- **Long description:** FASK can use adjacencies X—Y where |corr(X,Y|X>0) – corr(X,Y|Y>0)| > threshold. This expression will be nonzero only if there is a path between X and Y; heuristically, if the difference is greater than, say, 0.3, we infer an adjacency.
- **Value type:** Boolean
- **Default value:** true

## useDataOrder
- **Short description:** Yes just in case data variable order should be used for the first initial permutation.
- **Long description:** In either case, if multiple starting points are used, taking the best scoring model from among these, subsequent starting points will all be random shuffles.
- **Value type:** Boolean
- **Default value:** true

## useFasAdjacencies
- **Short description:** Yes if adjacencies from the FAS search (correlation) should be used
- **Long description:** Determines whether adjacencies found by conditional correlation should be included in the final model.
- **Value type:** Boolean
- **Default value:** true

## useGap
- **Short description:** Yes if the GAP algorithms should be used. Not if the SAG algorithm should be used
- **Long description:** True if one should first find all possible initial sets, grows these out, and then picks a non-overlapping such largest sets from these. Not if one should grow pure clusters one at a time, excluding variables found in earlier clusters.
- **Value type:** Boolean
- **Default value:** false

## useMaxPHeuristic
- **Short description:** Yes if the max P heuristic version should be used to search for sepsets
- **Long description:** Yes if the max P heuristic version should be used to search for sepsets
- **Value type:** Boolean
- **Default value:** false

## useMaxPOrientationHeuristic
- **Short description:** Use the max p heuristic version
- **Long description:** Use the max p heuristic version
- **Value type:** Boolean
- **Default value:** false

## useScore
- **Short description:** Yes if the score should be used; no if the test should be used
- **Long description:** BOSS can run either from a score or a test; this lets you choose which.
- **Value type:** Boolean
- **Default value:** true

## useSkewAdjacencies
- **Short description:** Yes if adjacencies based on skewness should be used
- **Long description:** FASK can use adjacencies X—Y where |corr(X,Y|X>0) – corr(X,Y|Y>0)| > threshold. This expression will be nonzero only if there is a path between X and Y; heuristically, if the difference is greater than, say, 0.3, we infer an adjacency. To see adjacencies included for this reason, set this parameter to “Yes”. Sanchez-Romero, Ramsey et al., (2018) Network Neuroscience.
- **Value type:** Boolean
- **Default value:** true

## varHigh
- **Short description:** High end of variance range (min = 0.0)
- **Long description:** The parameter 'b' for drawing independent variance values, from +U(a, b).
- **Value type:** Double
- **Default value:** 3.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## varLow
- **Short description:** Low end of variance range (min = 0.0)
- **Long description:** The parameter 'a' for drawing independent variance values, from +U(a, b).
- **Value type:** Double
- **Default value:** 1.0
- **Minimum:** 0.0
- **Maximum:** 1.7976931348623157E308

## verbose
- **Short description:** Yes if verbose output should be printed or logged
- **Long description:** If this parameter is set to ‘Yes’, extra (“verbose”) output will be printed if available giving some details about the step-by-step operation of the algorithm.
- **Value type:** Boolean
- **Default value:** false

## verbose
- **Short description:** Yes if the (MimBuild) structure model should be included in the output graph
- **Long description:** FOFC proper yields a measurement model--that is, a set of pure children for each of the discovered latents. One can estimate the structure over the latents (the structure model) using Mimbuild. This structure model is included in the output if this parameter is set to Yes.
- **Value type:** Boolean
- **Default value:** false

## wThreshold
- **Short description:** wThreshold
- **Long description:** Tuning parameter for DAGMA
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0
- **Maximum:** Infinity

## zsMaxIndegree
- **Short description:** Maximum indegree of true graph (min = 0)
- **Long description:** This is the maximum number of parents one expects any node to have in the true model.
- **Value type:** Integer
- **Default value:** 4
- **Minimum:** 0
- **Maximum:** 2147483647

## zSRiskBound
- **Short description:** Risk bound
- **Long description:** This is the probability of getting the true model if a correct model is discovered. Could underfit.
- **Value type:** Double
- **Default value:** 0.1
- **Minimum:** 0
- **Maximum:** 1
