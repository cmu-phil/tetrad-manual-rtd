# Search Algorithms Full List

This page lists all algorithms whose wrappers implement  
`edu.cmu.tetrad.algcomparison.algorithm.Algorithm` in Tetrad 7.6.9.

Where possible, descriptions are based on the corresponding classes in  
`edu.cmu.tetrad.search`.

Goal: We will make a separate page for each of these, filling in this template:

- [Algorithm Template](algorithm.template.md)

---

## Boss

**Search class:** `edu.cmu.tetrad.search.Boss`  [oai_citation:1‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Best Order Score Search (BOSS)**, a score-based search that optimizes over variable orderings rather than directly over graph structure. Useful as an alternative to FGES with a different bias in how it explores the search space.

---

## BossFci

**Search class:** `edu.cmu.tetrad.search.BossFci`  [oai_citation:2‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Uses **BOSS** as the score-based engine inside a *-FCI template. In other words, it starts from a BOSS-derived CPDAG and then applies an FCI-style latent-variable correction to produce a PAG.

---

## BossPod

**Search class:** `edu.cmu.tetrad.search.BossPod`  [oai_citation:3‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **BOSS-POD**, an IGraphSearch implementation that combines BOSS-style order search with the POD idea (Best Order with downstream tweaks). Used as a specialized variant of BOSS.

---

## Cam

**Search class:** `edu.cmu.tetrad.search.Cam`  [oai_citation:4‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements the **Causal Additive Model (CAM)** algorithm, designed for nonlinear additive models with smooth functions. Targets DAGs in settings where additive noise and smooth regression assumptions are plausible.

---

## Ccd

**Search class:** `edu.cmu.tetrad.search.Ccd`  [oai_citation:5‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Cyclic Causal Discovery (CCD)**, an algorithm (after Richardson) that can learn directed cyclic graphs under certain assumptions. Intended for applications where feedback loops are possible.

---

## Cdnod

**Search class:** `edu.cmu.tetrad.search.Cdnod`  [oai_citation:6‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements the **CDNOD** algorithm for causal discovery under **changing distributions**: it detects edges by exploiting how dependencies change with respect to an explicit change index variable (e.g., time or environment).

---

## Cfci

**Search class:** `edu.cmu.tetrad.search.Cfci`  [oai_citation:7‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

**Status:** Deprecated.  
Earlier FCI-related variant; retained mainly for backward compatibility and experimentation.

---

## Cpc

**Search class:** `edu.cmu.tetrad.search.Cpc` (Conservative PC; see Javadocs under search package index)

Implements **Conservative PC**, a variant of PC that more cautiously orients colliders, aiming to avoid false-positive v-structures at the cost of potentially leaving some triples unoriented.

---

## Cstar

**Search class:** `edu.cmu.tetrad.search.Cstar`  [oai_citation:8‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements the **CStaR** algorithm (Stekhoven et al., 2012). It starts from a CPDAG, then systematically orients undirected edges around a variable to compute **bounds on causal effects**, returning a CPDAG plus effect estimates over orientations.

---

## Dagma

**Search class:** `edu.cmu.tetrad.search.Dagma`  [oai_citation:9‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements the **DAGMA** algorithm, an optimization-based method for learning DAGs using continuous relaxations and acyclicity constraints.

---

## DirectLingam

**Search class:** `edu.cmu.tetrad.search.DirectLingam`  [oai_citation:10‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements the **Direct LiNGAM** algorithm, which assumes linear relationships with non-Gaussian independent noise to identify a unique causal ordering and DAG.

---

## DmFcit

Wrapper for a **“Detect-Mimic + FCIT”** variant: applies a DM-style pre-processing (detect–mimic) and then uses FCIT on transformed or implied variables. Intended for specialized workflows; see Tetrad Javadocs for details.

---

## DmPc

**Search class:** `edu.cmu.tetrad.search.DmPc`  [oai_citation:11‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Detect-Mimic PC (DM-PC)**, a PC-style algorithm preceded by a detect–mimic step, intended to improve orientation or robustness in particular latent or measurement scenarios.

---

## FactorAnalysis

**Search class:** `edu.cmu.tetrad.search.FactorAnalysis`  [oai_citation:12‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements classical **Factor Analysis**, viewed here as a structure-learning procedure for latent variable models with a factor-analytic form.

---

## Fas

**Search class:** `edu.cmu.tetrad.search.Fas`  [oai_citation:13‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Fast Adjacency Search (FAS)**, the adjacency phase of the PC algorithm. It removes edges based on conditional independence tests and returns a (possibly undirected) skeleton.

---

## Fask

**Search class:** `edu.cmu.tetrad.search.Fask`  [oai_citation:14‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **FASK (Fast Adjacency Skewness)**, combining FAS-style adjacencies with skewness-based and non-Gaussian orientation rules to orient edges in linear non-Gaussian models.

---

## FaskConcatenated

Wrapper that applies **FASK** to concatenated or multiple datasets, aggregating results. Used when the FASK idea is applied across multiple runs or partitions.

---

## FaskLofsConcatenated

Variant that combines **FASK** with **LOFS**-style non-Gaussian orientation on concatenated datasets, used for more aggressive orientation leveraging higher-order moments.

---

## FaskPw

Pairwise-oriented **FASK** variant, emphasizing pairwise non-Gaussian orientation rules across edges while retaining a FAS-like skeleton.

---

## FaskVote

Voting-based FASK ensemble: runs multiple FASK instances and aggregates orientations based on some voting or consensus rule, to improve robustness.

---

## FasLofs

A combination of **FAS** for skeleton discovery with **LOFS** (Linear, non-Gaussian Orientation of Fixed Structure) for orientation, providing a pipeline: adjacency search → non-Gaussian orientation.

---

## Fci

**Search class:** `edu.cmu.tetrad.search.Fci`  [oai_citation:16‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Fast Causal Inference (FCI)**, a constraint-based algorithm that learns **PAGs** allowing for latent confounding and selection bias, using conditional independence tests to prune and orient edges.

---

## FciIod

FCI variant that integrates an **IOD (Independence-Of-Distribution)**-style test or diagnostic into the FCI framework. Specialized and mainly of research interest.

---

## Fcit

**Search class:** `edu.cmu.tetrad.search.Fcit`  [oai_citation:18‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **FCI Targeted Testing (FCIT)**, a hybrid algorithm that uses scores (e.g., BOSS) to **prioritize CI tests** in an FCI-style PAG search, reducing spurious independences and improving efficiency when latent variables are present.

---

## Fges

**Search class:** `edu.cmu.tetrad.search.Fges`  [oai_citation:19‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Fast Greedy Equivalence Search (FGES)**, a score-based search over equivalence classes of DAGs, typically using SEM-BIC or similar scores. Scales well to large graphs.

---

## FgesConcatenated

Wrapper that runs **FGES** on concatenated or multiple datasets and aggregates the resulting graphs, providing an ensemble view of the structure.

---

## FgesFci

**Search class:** `edu.cmu.tetrad.search.FgesFci`  [oai_citation:20‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Uses **FGES** as the initial step in a *-FCI template: first learns a CPDAG by FGES, then refines it via FCI-style constraints to obtain a PAG.

---

## FgesMb

**Search class:** `edu.cmu.tetrad.search.FgesMb`  [oai_citation:21‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Applies FGES ideas specifically to **Markov blanket** discovery, returning a CPDAG focusing on neighborhoods of targets.

---

## FirstInflection

Heuristic algorithm that looks for **“first inflection”** behavior in some score or stability path, often in the context of selecting a tuning parameter (e.g., penalty) within stability selection frameworks.

---

## Gfci

**Search class:** `edu.cmu.tetrad.search.Gfci`  [oai_citation:22‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **GFCI / *-FCI**, a hybrid method that starts from a **Markov CPDAG** (often from FGES) and then applies an FCI-like correction to yield a PAG that is correct for models with latent variables.

---

## Gin

**Search class:** `edu.cmu.tetrad.search.Gin`  [oai_citation:23‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements a **Minimal GIN**-style algorithm, typically involving clustering via TSC and then reasoning about generalized independent noise to orient edges or cluster structures.

---

## Glasso

Graphical Lasso–based algorithm that learns a sparse **inverse covariance** (precision) matrix and uses it to define adjacencies in a Gaussian graphical model. Can be used as a baseline or pre-processing skeleton.

---

## Grasp

**Search class:** `edu.cmu.tetrad.search.Grasp`  [oai_citation:24‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **GRaSP (Greedy Relaxations of Sparsest Permutation)**, a permutation-based score search that looks for permutations whose implied CPDAGs are close to the true structure.

---

## GraspFci

**Search class:** `edu.cmu.tetrad.search.GraspFci`  [oai_citation:25‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Uses **GRaSP** as the score-based engine within a *-FCI template, starting from a GRaSP-derived CPDAG and then performing FCI-style latent-variable correction.

---

## IcaLingam

**Search class:** `edu.cmu.tetrad.search.IcaLingam`  [oai_citation:26‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **ICA-LiNGAM**, using independent component analysis in linear non-Gaussian models to recover a unique causal ordering.

---

## IcaLingD

**Search class:** `edu.cmu.tetrad.search.IcaLingD`  [oai_citation:27‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **ICA-LiNG-D** (Lacerda et al., 2012), a stabilized LiNGAM variant; uses ICA with robustness tweaks to estimate a DAG in non-Gaussian settings.

---

## Images, IMaGESBoss

Wrapper for an **image-based causal discovery** pipeline; used when variables are derived from image data or when the algorithm operates over images as inputs. See Tetrad Javadocs for detailed usage.

See the full description here:  
[IMaGES — Independent Multiple-sample Greedy Equivalence Search](algorithms/images.md)

---

## IsFges

**Search class:** `edu.cmu.tetrad.search.IsFges`  [oai_citation:28‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Instance-Specific FGES**, modifying FGES’s scoring step to use an **instance-specific score** (IS-BIC or similar), while reusing the same structural search framework.

---

## IsGfci

**Search class:** `edu.cmu.tetrad.search.IsGFci`  [oai_citation:29‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **instance-specific FGES-FCI (IS-GFCI)**, as introduced by Fattaneh Jabbari. Uses instance-specific scoring within a GFCI-like hybrid.

---

## MimbuildBollen

**Search class:** `edu.cmu.tetrad.search.MimbuildBollen`  [oai_citation:30‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements a **MIM-building** algorithm in the style of Bollen, using a BlockSpec representation to construct measurement models with latent variables.

---

## MimbuildPca

**Search class:** `edu.cmu.tetrad.search.MimbuildPca`  [oai_citation:31‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Constructs MIMs by taking **first principal components** of pure clusters (again guided by BlockSpec), then building a latent measurement model.

---

## PagSampleRfci

Wrapper that uses **RFCI** over **resampled or simulated PAGs**, e.g., for sampling from a distribution of PAGs or performing repeated RFCI runs.

---

## Pc

**Search class:** `edu.cmu.tetrad.search.Pc`  [oai_citation:32‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements unified “**Classic PC**”: a constraint-based algorithm that learns a CPDAG using conditional independence tests, with options for collider orientation style and bidirected edge handling.

See the full description here:  
[PC — Peter/Clark](algorithms/pc.md)

See also PC-Max.

--

## Pc-Max

**Search class:** `edu.cmu.tetrad.search.Pc`  [oai_citation:32‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html) This uses the same search class as PC but uses a collider orientation style of **Max P**.

Implements the **PC-Max** optimization of PC, which improves orientation accuracy, as an option inside the PC algorithm.

See the full description here:  
[PC-Max — Peter/Clark Max](algorithms/pc-max.md)

---

## Pcd

**Search class:** `edu.cmu.tetrad.search.Pcd`  [oai_citation:33‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Variant of PC adapted for **deterministic** relationships. It refuses to remove edges based on CI tests that appear to be deterministic, preserving adjacencies that would otherwise be dropped.

---

## PcMb

**Search class:** `edu.cmu.tetrad.search.PcMb`  [oai_citation:34‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Searches for a CPDAG capturing **Markov blankets** for a given target T, consistent with independence information. PC-style adjacency search but focused on neighborhood structure.

---

## Pcmci

**Search class:** `edu.cmu.tetrad.search.Pcmci`  [oai_citation:35‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **PCMCI** (Runge et al.), a time-series method that learns lagged causal structure (τ ≥ 1) using conditional independence tests over time-lagged variables.

---

## R1, R2, R3

A trio of **research or experimental variants** (often rule- or rank-based) within the Tetrad comparison framework. These are not standard named algorithms; they should be treated as experimental and used with care, consulting the Javadocs for exact behavior.

---

## RestrictedBoss

Variant of **BOSS** that imposes **restrictions** (e.g., max parent set size, tier constraints, or other domain-specific rules) during order search, making the search more constrained and potentially faster or more interpretable.

---

## Rfci

**Search class:** `edu.cmu.tetrad.search.Rfci`  [oai_citation:36‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **Really Fast Causal Inference (RFCI)**, a more computationally efficient variant of FCI that still returns a PAG and handles latent confounding, using pruned CI testing.

---

## RfciBsc

RFCI variant designed to work with a **bootstrap / stability context (BSC)**, e.g., repeated RFCI runs on resampled data, possibly for stability selection or summarization.

---

## Rskew

Robust skewness-based orientation algorithm: a variant of FASK/LOFS-style approaches that uses skew statistics in a more robust or modified manner. Experimental.

---

## RskewE

Extension or experimental version of **Rskew**, possibly with enhanced robustness or alternative estimation; refer to Javadocs for the precise definition.

---

## SingleGraphAlg

Meta-wrapper that represents a **single graph–producing algorithm** in the comparison framework, used when a specific graph is fixed or imported rather than learned from data.

---

## Skew

Base **skewness-based orientation** algorithm that uses skew (non-Gaussian) statistics to orient edges in a fixed skeleton or initial graph, assuming linear non-Gaussian models.

---

## SkewE

Experimental extension of **Skew**, often testing alternative skew measures or orientation rules; primarily of research interest.

---

## Sp

**Search class:** `edu.cmu.tetrad.search.Sp`  [oai_citation:37‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Implements **SP (Sparsest Permutation)**, which searches over variable permutations and selects those whose implied DAGs are especially sparse (fewest edges).

---

## SpFci

**Search class:** `edu.cmu.tetrad.search.SpFci`  [oai_citation:38‡Carnegie Mellon University Philanthropy](https://www.phil.cmu.edu/tetrad-javadocs/7.6.9/edu/cmu/tetrad/search/package-summary.html)

Uses **SP** in place of FGES for the initial step of a *-FCI algorithm, then applies FCI-style corrections to return a PAG.

---

## StabilitySelection

Implements **stability selection** wrappers: repeatedly run a base algorithm (e.g., FGES, BOSS) under resampling or varying penalties, and summarize which edges appear stably across runs.

---

## StARS

Implements **StARS (Stability Approach to Regularization Selection)**: uses stability of edge selections under subsampling to choose a regularization strength (e.g., λ in Glasso or lasso-like procedures).

---

## Tanh

Orientation / scoring algorithm that uses **tanh-based transformations** as part of a non-Gaussian orientation rule set (similar in spirit to LOFS or skew-based methods).

---