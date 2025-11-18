# Search Algorithms — Full Catalog

This page lists all algorithms whose wrappers implement  
`edu.cmu.tetrad.algcomparison.algorithm.Algorithm` in Tetrad 7.6.9.

Where possible, descriptions are based on the corresponding classes in  
`edu.cmu.tetrad.search`.

This catalog provides a concise overview of all structure-learning algorithms available in Tetrad, with links to full per-algorithm documentation.

If you are new to Tetrad or just want a curated subset of recommended methods, start with the [Search Algorithms — Short List](search-algorithms-short-list.md).

Note: Many algorithm pages are still being worked on as part of an ongoing documentation update. Pages will populate over time.

## Legend — Algorithm Categories

| Badge | Meaning | Description |
|-------|----------|-------------|
| 🔍 **Constraint-based** | Uses conditional independence (CI) tests | PC, CPC, PC-Max, FCI, RFCI, etc. |
| 📏 **Score-based** | Optimizes a score such as BIC, BDeu, or GIC | FGES, BOSS, GRaSP, SP, etc. |
| 🌀 **Hybrid** | Combines score-based and CI-test phases | GFCI, BOSS-FCI, GRaSP-FCI, FCIT, etc. |

### Extra Structural Badges

| Badge | Meaning | Description |
|-------|----------|-------------|
| 🧩 **Latent-capable** | Can output PAGs and handle latent confounding | FCI, RFCI, GFCI, FCIT, BOSS-FCI, etc. |
| 🔁 **Time-series / lagged** | Supports lagged variables / PCMCI-style searches | PCMCI, time-lag settings in PC/FGES |
| 🧪 **Experimental** | Research/unstable algorithms | R1/R2/R3, RSkew, SkewE, etc. |
| 🎨 **Non-Gaussian / ICA** | Uses ICA, skewness, LOFS, or higher-order moments | LiNGAM, FASK, LOFS variants |
| 🧠 **Multi-dataset / subject-level** | Designed for multiple datasets | IMaGES, concatenated FGES/FASK variants |
| 🔧 **Orientation-only** | Works with a fixed skeleton | LOFS, skew-based methods |

---

## 🔍 Constraint-Based Algorithms (CPDAG / PAG)
*Use conditional independence tests to prune adjacencies and orient edges.*

| Algorithm                                         | Description |
|---------------------------------------------------|-------------|
| **Pc** — [PC](algorithms/pc.md) 🔍                | Classic constraint-based CPDAG search using CI tests. |
| **Pc-Max** — [PC-Max](algorithms/pc.md) 🔍        | PC variant maximizing p-value for collider orientation. |
| **CPC** — [Conservative PC](algorithms/cpc.md) 🔍 | Conservative collider rule reducing false orientations. |
| **Pcd** ♻️                                        | PC variant robust to deterministic relations. |
| **PcMb** 🔍                                       | PC-style local Markov blanket discovery. |
| **Fas** — [FAS](algorithms/fas.md) 🔍             | Fast Adjacency Search (adjacency phase of PC). |
| **Fci** — [FCI](algorithms/fci.md) 🔍🧩           | Full PAG learning allowing latent confounding & selection. |
| **Rfci** 🔍🧩                                     | Fast approximation to FCI for large graphs. |
| **RfciBsc** 🔍🧩📦                                | RFCI with bootstrap/stability selection. |
| **FciIod** 🔍🧩🧠                                 | FCI variant for multi-dataset learning with partially overlapping variable sets. |
| **Pcmci** 🔍🔁                                    | CI-based time-series causal discovery. |

---

## 📏 Score-Based Algorithms (CPDAG)
*Optimize a score (BIC, IS-BIC, etc.) over equivalence classes or variable orderings.*

| Algorithm                                            | Description                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------|
| **Fges** — [FGES](algorithms/fges.md) 📏             | Fast Greedy Equivalence Search (scalable CPDAG search).                  |
| **FgesMb** 📏                                        | FGES specialized for Markov blankets.                                    |
| **FgesConcatenated** 📏📦                            | FGES ensemble applied to concatenated datasets.                          |
| **Boss** — [BOSS](algorithms/boss.md) 📏             | Best Order Score Search over variable orderings.                         |
| **LV-Dumb** — [LV-Dumb](algorithms/lv-dumb.md) 🪶    | Heuristic PAG from the BOSS DAG; a lightweight alternative to BFCI/FCIT. |
| **RestrictedBoss** 📏                                | BOSS with parent/tier restrictions.                                      |
| **Grasp** — [GRaSP](algorithms/grasp.md) 📏          | Greedy Relaxations of Sparsest Permutation.                              |
| **Sp** — [SP](algorithms/sp.md) 📏                   | Sparsest Permutation DAG selection.                                      |
| **Images** 🧩📏 — [IMaGES](algorithms/images.md)     | Multi-sample FGES with cross-sample consistency.                         |
| **IMaGESBoss** 🧩📏 — [IMaGES](algorithms/images.md) | Multi-sample BOSS with cross-sample consistency.                         |

---

## 🔀 Hybrid Algorithms (Score + FCI)
*Begin with a CPDAG from a score-based method and apply FCI-style corrections.*

| Algorithm                                             | Description |
|-------------------------------------------------------|-------------|
| **Gfci** — [GFCI](algorithms/gfci.md) 🔀🌀            | FGES + FCI hybrid, returns a PAG. |
| **GraspFci** — [GRaSP-FCI](algorithms/grasp-fci.md) 🔀🌀 | GRaSP → FCI refinement. |
| **BossFci** — [BOSS-FCI](algorithms/boss-fci.md) 🔀🌀 | BOSS → FCI refinement. |
| **SpFci** — [SP-FCI](algorithms/sp-fci.md) 🔀🌀       | Sparsest Permutation → FCI refinement. |
| **Fcit** — [FCIT](algorithms/fcit.md) 🔀🌀            | Score-guided selective testing for efficient PAG discovery. |

---

## 🎨 Non-Gaussian / Moment-Based / Orientation Algorithms
*Use ICA, skewness, or higher-order moments to orient edges.*

| Algorithm | Description |
|----------|-------------|
| **DirectLingam** 🎨 | Direct LiNGAM; linear non-Gaussian unique-order recovery. |
| **IcaLingam** 🎨 | ICA-based LiNGAM (classic variant). |
| **IcaLingD** 🎨 | Stabilized ICA LiNGAM (Lacerda et al.). |
| **Fask** 🎨 | FAS skeleton + skewness-based orientation. |
| **FaskPw** 🎨 | Pairwise skewness-based orientation. |
| **FaskVote** 🎨📦 | Voting ensemble of FASK. |
| **FaskConcatenated** 🎨📦 | FASK across concatenated datasets. |
| **FaskLofsConcatenated** 🎨📦 | FASK + LOFS on concatenated data. |
| **FasLofs** 🎨 | FAS → LOFS pipeline. |
| **Skew** 🎨 | Base skewness orientation algorithm. |
| **SkewE** 🎨🧪 | Experimental extension of Skew. |
| **Rskew**, **RskewE** 🎨🧪 | Robust skew variants (research). |
| **Tanh** 🎨🧪 | Tanh-transformed nonlinear orientation rules. |
| **Gin** 🎨 | Generalized Independent Noise clustering/orientation. |

---

## 🧩 Latent Variable & Measurement Model Algorithms
*Recover measurement structure, latent factors, or multi-sample latent connectivity.*

| Algorithm | Description |
|----------|-------------|
| **FactorAnalysis** 🧩 | Classical factor analysis (measurement models). |
| **MimbuildBollen** 🧩 | Bollen-style MIM builder via BlockSpec. |
| **MimbuildPca** 🧩 | PCA-based MIM construction for pure clusters. |

---

## Nonlinear & Distribution-Shift Algorithms
*Handle nonlinear functions, distribution changes, cyclic behavior.*

| Algorithm | Description |
|----------|-------------|
| **Cam** | Causal Additive Model (nonlinear additive noise SEMs). |
| **Dagma** 📏 | Continuous DAG optimization with smooth acyclicity. |
| **Cdnod** | Causal discovery under distributional changes. |
| **Ccd** | Cyclic Causal Discovery (allows feedback loops). |

---

## 📦 Stability / Resampling / Ensemble Wrappers
*Run algorithms repeatedly under resampling or varying penalties.*

| Algorithm | Description |
|----------|-------------|
| **StabilitySelection** 📦 | Stability selection for edges across resampling. |
| **StARS** 📦 | Stability Approach to Regularization Selection. |
| **PagSampleRfci** 🔍🧩📦 | RFCI applied across sampled/generated PAGs. |

---

## 🧪 Specialized / Research / Utility Algorithms
*Experimental, specialized, or workflow-specific algorithms.*

| Algorithm | Description |
|----------|-------------|
| **DmPc** 🧪 | Detect–Mimic preprocessing before PC. |
| **DmFcit** 🧪 | Detect–Mimic preprocessing before FCIT. |
| **FirstInflection** 🧪 | Heuristic for selecting penalty/regularization. |
| **Cstar** 🧪 | Bounds on causal effects via edge orientation patterns. |
| **SingleGraphAlg** 🧪 | Wrapper for a fixed imported graph. |
| **R1**, **R2**, **R3** 🧪 | Research/experimental variants. |
| **Cfci** 🧪 | Deprecated early FCI variant. |