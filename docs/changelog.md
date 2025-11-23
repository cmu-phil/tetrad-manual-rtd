# Change Log

This change log describes updates to the **Tetrad documentation** (this
ReadTheDocs manual). These changes will first appear in the **next public
release of Tetrad**; the manual is not yet linked from any released version
of the software.

---

## 2025 — Manual Overhaul for Next Release

### 1. New Tetrad Interface Manual

- Added a new **Tetrad Interface** section that replaces the old “classic”
  HTML manual for GUI usage.
- Introduced task-oriented pages for:
    - Main Window and workspace
    - Working with Data
    - Graph box and graph editor
    - Parametric Model and Instantiated Model boxes
    - Estimator, Updater, Regression
    - Data, Simulation, Search, Latent Clusters, Latent Structure, Knowledge,
      Compare, and Note boxes
- Added **box-by-box** documentation with screenshots for all core boxes.
- Created separate **detail callouts** for:
    - Parametric model families (Bayes, SEM, Hybrid, Generalized)
    - Instantiated model families (Bayes, SEM, Hybrid, Generalized)
    - Updaters (Junction Tree, Approximate, Row Summing, SEM)
    - Grid Search and Markov Checker
- Documented **Pipelines**, **Logging**, and **File → Settings** options in
  the main window description.

### 2. Tests and Scores Documentation

- Added **individual pages** for all major tests and scores, including:
    - FisherZ, GSquare, ChiSquare, CCI, KCI, Basis-Function LRT, Conditional
      Gaussian and Degenerate Gaussian LRTs, Mvplrt, MSeparationTest,
      ProbabilisticTest, SemBicTest, PoissonBicTest.
    - SemBicScore, DiscreteBicScore, BDeuScore, ConditionalGaussianBicScore,
      DegenerateGaussianBicScore, BasisFunctionBicScore, EbicScore, GicScores,
      MSepScore, MVPBicScore, PoissonPriorScore, ZhangShenBoundScore.
- Each page now includes:
    - A clear description of **when to use** the test or score.
    - Parameters derived from the code’s `getParameters()` definitions.
    - Cross-references to relevant algorithms (e.g., FGES, BOSS, GRaSP).
- Added **“Tests and Scores — Alphabetical”** index and updated the
  **“Choosing Tests and Scores”** guidance page to link to the new catalog.

### 3. Algorithm and Terminology Updates

- Renamed **LV-Dumb** to **LV-Heuristic** throughout the manual and catalog
  to reflect a clearer, more professional name.
- Standardized **summary sections** and “When to use / When not to use”
  wording across several algorithms (e.g., CStaR, Factor Analysis,
  MIM-Build variants, TSC, BOSS-related methods).
- Clarified the roles of **Py-Tetrad**, **RPy-Tetrad**, and **causal-learn**
  in the “Interfacing Tools” page.

### 4. References and Clean-Up

- Updated and completed citations for tests and scores, including:
    - BDeu, Conditional and Degenerate Gaussian methods, EBIC, GIC,
      Zhang–Shen bounds, Basis-Function methods, and others.
- Fixed numerous small issues:
    - Terminology and parameter names,
    - Minor wording errors and outdated descriptions,
    - Consistency of notation and style across pages.
- Verified that the **HTML build**, **PDF output**, and **search** all work
  cleanly, including rendering on smaller screens.

---

Further tweaks and small additions (for example, new detail callouts or
screenshots) after this point are considered minor and are not listed
individually here.