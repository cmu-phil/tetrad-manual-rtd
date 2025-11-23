## 2025-03 — Additional Updates and Refinements

### 🔄 1. Renamed LV-Dumb → LV-Heuristic
- Updated the algorithm name throughout:
    - RTD manual
    - Code documentation
    - Algorithm catalog
    - Internal references (e.g., BOSS-FCI, searches involving LV methods)
- Chosen to reflect a clearer, more professional name (following discussion with Peter and Bryan).

### 🧪 2. Comprehensive Documentation for Tests and Scores
- Added **full individual pages** for every test and score in Tetrad:
    - FisherZ, CCI, KCI, G², χ²
    - All BIC and likelihood-ratio scores (SEM BIC, Degenerate Gaussian BIC/LRT, Conditional Gaussian, MVP, EBIC, GIC, etc.)
    - New Basis-Function Tests & Scores (BF-BIC, BF-LRT)
    - Poisson Prior Score & Poisson BIC Test
    - Zhang–Shen Bound Score
    - Probabilistic Test
- Each page now includes:
    - Accurate **parameter tables** generated from `getParameters()`
    - Clean references (JMLR, arXiv, classic literature)
    - Updated descriptions consistent with modern Tetrad usage
    - Notes on when the test/score should or should not be used

### 📘 3. Updated "Choosing Tests and Scores" Page
- Added correct hyperlinks to detailed pages.
- Corrected earlier misleading text (e.g., regarding Poisson and non-Gaussian use cases).
- Integrated BOSS paper results (SemBIC vs. DirectLiNGAM performance comparison).

### 🧩 4. New Summary Sections for Algorithms
- Added uniform **“## Summary”** sections to:
    - CStaR
    - Factor Analysis
    - Mimbuild-Bollen
    - Mimbuild-PCA
    - TSC
- Ensures consistency with other algorithm pages like DAGMA, BOSS, etc.

### 🔗 5. Expanded Interfacing Tools Page
- Added new documentation page linking:
    - **Py-Tetrad**
    - **RPy-Tetrad**
    - **causal-learn** (as a related tool)
- Clarified intended usage:
    - Py/RTetrad for **direct access to Java algorithms**
    - causal-learn as Python-native implementations

### 📄 6. References Updated Across Many Pages
- Added missing citations for:
    - BDeu (Heckerman, Geiger & Chickering 1995)
    - Degenerate Gaussian scores/tests (Ramsey, Andrews & Spirtes 2024)
    - Conditional Gaussian scores/tests (Andrews, Ramsey & Cooper 2018)
    - EBIC (Chen & Chen 2008)
    - GIC (Kim, Kwon & Choi 2012)
    - Zhang–Shen Bound Score (Zhang & Shen 2010)
    - Basis Function methods (Ramsey, Andrews & Spirtes 2025)
- Cleaned formatting and ensured consistent bibliographic style.

### 🧼 7. Numerous Minor Fixes and Cleanups
- Corrected terminology in algorithm pages (e.g., BPC, CCI).
- Added missing parameter explanations (e.g., timeLag for SP).
- Fixed misinterpreted biological notes in algorithm “When to Use” sections.
- Refined PCA/MIM documentation for clarity.

### 🖥️ 8. New “Tetrad Interface” Section (first draft)
- Added a new **Tetrad Interface** section with task-oriented pages:
    - Main Window Overview
    - Working with Data
    - Graph Editor
    - Running Algorithms
    - Viewing and Exporting Results
    - Simulation and Utilities
    - Grid Search
    - Markov Checker
- Each page focuses on **GUI workflows** (loading data, configuring searches, inspecting results, running simulations, checking Markov properties, etc.) rather than algorithmic theory.
- Established screenshot conventions and paths under `/_static/images/tetrad-interface/` for future illustrative figures (main window, data table, graph editor, algorithm dialogs, etc.).
- Left the legacy **Classic Manual** as a separate section for now; the new Tetrad Interface pages are intended to replace it once they have settled.

---

### Notes
This concludes the major documentation rewrite cycle for tests, scores, latent-variable tools, and the first draft of the new Tetrad Interface section.  
Further refinements will follow after peer review of the updated manual and feedback from users (including Peter and collaborators).

## 2025-11 — Tetrad Interface Manual Near Completion

### 📚 1. Box-by-Box Interface Documentation Filled In
- Completed detailed **Tetrad Interface** pages for core GUI boxes, including:
    - Data, Simulation, Search, Latent Structure, Knowledge, Estimator, Updater, Graph, and Display Subgraphs.
- Added corresponding **detail callouts** for:
    - Parametric and Instantiated Model types,
    - Estimators (ML Bayes, Dirichlet, EM Bayes, SEM, Hybrid CG, Generalized SEM),
    - Updaters (Junction Tree, Approximate, Row Summing, SEM),
    - Graph menu tools and Display Subgraphs.
- Ensured consistent wording, parameter references, and cross-links to the global **Parameters** listing.

### ✅ 2. Manual Build and UX Checks
- Verified that the **HTML build** is clean and that the generated **PDF manual** renders correctly.
- Confirmed that **search functionality** in the built docs works as expected.
- Checked the appearance of the manual on a **mobile phone**; layout and navigation look good on small screens.

### 🔜 3. Remaining TODOs
- Plan to add a small number of additional **detail callouts** for:
    - **Pipelines** functionality,
    - **Logging** functionality.
- After those callouts are in place, the new Tetrad Interface manual will be considered feature-complete pending minor polish and feedback from users (Peter, collaborators, and external readers).

