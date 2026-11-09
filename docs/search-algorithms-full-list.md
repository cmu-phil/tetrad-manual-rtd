# Search Algorithms — By Type

This page lists all algorithms whose wrappers implement  
`edu.cmu.tetrad.algcomparison.algorithm.Algorithm` in **Tetrad 7.6.9**.

Descriptions are based on the corresponding classes in  
`edu.cmu.tetrad.search`.

This catalog provides a comprehensive overview of all structure-learning
algorithms available in Tetrad, with links to full per-algorithm documentation.

If you are new to Tetrad or want a curated subset of recommended methods, start with  
👉 **[Search Algorithms — Short List](search-algorithms-short-list.md)**

*Note:* Many per-algorithm pages are still being added as part of an ongoing documentation update.

---

## Legend — Algorithm Categories

| Badge | Category | Description |
|-------|-----------|-------------|
| 🔍 | Constraint-based | Uses conditional independence (CI) tests |
| 📏 | Score-based | Optimizes a score such as BIC, BDeu, GIC |
| 🌀 | Hybrid | Combines score-based and CI-test stages |

### Extra Structural Badges

| Badge | Meaning | Description |
|-------|----------|-------------|
| 🧩 | *Latent-capable* | Can output PAGs; handles latent confounding and selection bias |
| 🔁 | *Time-series / lagged* | Supports lagged variables (PCMCI, time-lag FGES/PC) |
| 🎨 | *Non-Gaussian / ICA* | Uses ICA, skewness, or higher-order moments |
| 🧠 | *Multi-dataset* | For multi-sample or cross-subject analyses |
| 📦 | *Resampling / stability* | Ensemble, bootstrap, or stability methods |
| 🧪 | *Experimental* | Research / nonstandard algorithms |
| 🔧 | *Orientation-only* | Orient edges from a fixed skeleton |

---

## 🔍 Constraint-Based Algorithms (CPDAG / PAG)

*Use conditional independence tests to prune adjacencies and orient edges.*

| Algorithm                                            | Description |
|------------------------------------------------------|-------------|
| **Pc** — [PC](algorithms/pc.md) 🔍                   | Classic constraint-based CPDAG search (CI-test–driven). |
| **Pc-Max** — [PC-Max](algorithms/pc.md) 🔍           | PC variant maximizing p-value for collider orientation. |
| **CPC** — [CPC](algorithms/cpc.md) 🔍                | Conservative collider rule reducing false orientations. |
| **PcMb** [PC-MB](algorithms/pcmb.md) 🔍              | Local Markov blanket discovery via PC-style logic. |
| **Fas** — [FAS](algorithms/fas.md) 🔍                | Fast Adjacency Search (the adjacency phase of PC). |
| **Fci** — [FCI](algorithms/fci.md) 🔍🧩              | Full PAG search with latent confounding & selection bias. |
| **Rfci** — [RFCI](algorithms/rfci.md) 🔍🧩           | Fast approximation to FCI (reduced complexity). |
| **FciIod** — [FCI-IOD](algorithms/fci-iod.md) 🔍🧩🧠 | FCI variant for multi-dataset / partially overlapping variable sets. |
| **Pcmci** — [PCMCI](algorithms/pcmci.md) 🔍🔁        | CI-based causal discovery for time-series data. |
| **Ccd** — [CCD](algorithms/ccd.md) 🔍                | Cyclic Causal Discovery (allows feedback loops). |
---

## 📏 Score-Based Algorithms (CPDAG)

*Optimize a score (BIC, GIC, BDeu, IS-BIC, etc.) over DAGs or equivalence classes.*

| Algorithm                                                                | Description                                                       |
|--------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Fges** — [FGES](algorithms/fges.md) 📏                                 | Fast greedy equivalence search; highly scalable.                  |
| **FgesMb** — [FGES-MB](algorithms/fges-mb.md) 📏                         | FGES variant specialized for Markov blankets.                     |
| **Boss** — [BOSS](algorithms/boss.md) 📏                                 | Best Order Score Search over variable orderings.                  |
| **RestrictedBoss** — [Restricted BOSS](algorithms/restricted-boss.md) 📏 | BOSS with parent/tier restrictions for speed.                     |
| **Grasp** — [GRaSP](algorithms/grasp.md) 📏                              | Greedy Relaxations of Sparsest Permutation.                       |
| **LV-Heuristic** — [LV-Heuristic](algorithms/lv-heuristic.md) 🪶         | Heuristic PAG from BOSS DAG; lightweight alternative to FCI/FCIT. |
| **Sp** — [SP](algorithms/sp.md) 📏                                       | Sparsest Permutation; exact but only for very small models.       |
| **Images** 🧩🧠📏 — [IMaGES](algorithms/images.md)                       | Multi-sample FGES with cross-sample consistency.                  |
| **IMaGESBoss** 🧩🧠📏 — [IMaGES](algorithms/images.md)                   | Multi-sample BOSS with cross-sample consistency.                  |

---

## 🌀 Hybrid Algorithms (Score + FCI)

*Start with a CPDAG from a score-based method, then apply FCI-style pruning/orientation to obtain a PAG.*

| Algorithm | Description |
|----------|-------------|
| **Gfci** — [GFCI](algorithms/gfci.md) 🌀🧩 | FGES → FCI refinement yielding a PAG. |
| **GraspFci** — [GRaSP-FCI](algorithms/grasp-fci.md) 🌀🧩 | GRaSP → FCI refinement. |
| **BossFci** — [BOSS-FCI](algorithms/boss-fci.md) 🌀🧩 | BOSS → FCI refinement. |
| **SpFci** — [SP-FCI](algorithms/sp-fci.md) 🌀🧩 | Sparsest Permutation → FCI refinement. |
| **Fcit** — [FCIT](algorithms/fcit.md) 🌀🧩 | Score-guided selective testing; efficient, legal-PAG output. |

---

## 🎨 Non-Gaussian, Moment-Based, and Orientation Algorithms

*Use ICA, skewness, or higher-order moments to orient edges or to supplement a skeleton.*

| Algorithm                                                          | Description                                           |
|--------------------------------------------------------------------|-------------------------------------------------------|
| **DirectLingam** — [Direct LiNGAM](algorithms/direct-lingam.md) 🎨 | Direct LiNGAM for linear non-Gaussian models.         |
| **IcaLingam** — [ICA LiNGAM](algorithms/ica-lingam.md) 🎨          | ICA-based LiNGAM (classic).                           |
| **IcaLingD** — [ICA LiNG-D](algorithms/ica-lingd.md) 🎨            | Cyclic LiNGAM (Lacerda et al.).                       |
| **Fask** — [FASK](algorithms/fask.md) 🎨                           | FAS skeleton + skewness-based orientation.            |
| **FaskVote** — [FASK-Vote](algorithms/fask-vote.md) 🎨📦           | Voting ensemble of FASK.                              |
| **Pairwise** — [Pairwise](algorithms/pairwise.md) 🎨               | Pairwise-skewness orientation.                        |

---

## Nonlinear & Distribution-Shift Algorithms

*Handle nonlinear functions, distribution shifts, or cyclic behavior.*

| Algorithm                                   | Description |
|---------------------------------------------|-------------|
| **Cam** — [CAM](algorithms/cam.md)          | Causal Additive Model (nonlinear additive noise SEMs). |
| **Dagma** — [DAGMA](algorithms/dagma.md) 📏 | Continuous DAG optimization with smooth acyclicity constraint. |
| **Cdnod** — [CD-NOD](algorithms/cdnod.md)   | Causal discovery under distributional changes. |

---

## 📦 Stability / Resampling / Ensemble Wrappers

*Run algorithms repeatedly under resampling or varying penalties.*

| Algorithm                                                                            | Description |
|--------------------------------------------------------------------------------------|-------------|
| **StabilitySelection** — [Stability Selection](algorithms/stability-selection.md) 📦 | Stability selection for edges across resampling. |
| **StARS** — [StARS](algorithms/stars.md) 📦                                          | Stability Approach to Regularization Selection. |
| **PagSamplingRfci** — [PAG Sampling RFCI](algorithms/pag-sampling-rfci.md) 🔍🧩📦    | RFCI on resampled/generated PAGs. |
| **RfciBsc** — [RFCI-BSC](algorithms/rfci-bsc.md) 🔍🧩📦                              | RFCI with bootstrap/stability selection. |

---

## 🧪 Specialized / Utility Algorithms

*Special-purpose, experimental, or workflow-specific methods.*

| Algorithm                                                                | Description |
|--------------------------------------------------------------------------|-------------|
| **DM** [DM](algorithms/dm.md) 🧪                                         | Detect–Mimic (intermediate-latent preprocessing). |
| **Cstar** [CStaR](algorithms/cstar.md) 🧪                                | Bounds on causal effects via edge-orientation patterns. |
| **SingleGraphAlg** [Single Graph Alg](algorithms/single-graph-alg.md) 🧪 | Wrapper for running Tetrad on a fixed imported graph. |

---

## Latent Clustering (Measurement Block Discovery)

These algorithms discover measurement clusters—groups of indicators that behave as if they share a single latent parent.  
See **[Latent Clusters](algorithms/latent-cluster.md)** for details.

| Algorithm | Description |
|----------|-------------|
| **TSC** | Trek Separation Clusters using rank constraints. |
| **FOFC** | First-Order Factor Clustering via pure tetrads. |
| **FTFC** | Fast Tetrad-Factor Clustering using sextads. |
| **GFFC** | Generalized Factor Finding Clustering (2×2 → 3×3 → …). |
| **BPC** | Build Pure Clusters (global purification & merging). |

Once clusters are obtained, they can be treated as **measurement blocks**. These blocks may be supplied to algorithms that support:

- **Blocks-Test-TS** — a trek-separation conditional independence test over blocks;
- **Blocks-BIC** — a block-aware score.

In this mode, *any* algorithm that accepts a test and/or a score (PC, FGES, BOSS, GFCI, etc.) can be run on the **latent layer**: each cluster becomes a latent node, and Blocks-Test-TS / Blocks-BIC handle independence and scoring among the latent variables.

---

## Latent Structure / Measurement-Model Construction

Building on cluster discovery and block-based search, these algorithms explicitly construct latent variables or full measurement models before running structural search on the latent layer.

| Algorithm                                               | Description                                              |
|---------------------------------------------------------|----------------------------------------------------------|
| **[Factor Analysis](algorithms/factor-analysis.md)** 🧩 | Classical SEM-style factor analysis (measurement model). |
| **[Mimbuild Bollen](algorithms/mimbuild-bollen.md)** 🧩 | MIM builder using Bollen-style BlockSpec constraints.    |
| **[Mimbuild PCA](algorithms/mimbuild-pca.md)** 🧩       | PCA-based measurement model from pure clusters.          |