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
- Updated references to **LV-Lite** to use the current name **FCIT** in the
  interface and documentation.
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

### 5. Estimation Workflow and Simulation Pipelines

- Added an **“Estimate model parameters”** overview page to the Tetrad Interface
  section, describing how to:
    - Go from a graph to a Parametric Model,
    - Connect an Estimator to a model and either a Data or Simulation node,
    - Produce and inspect Instantiated Models with fitted parameters and fit indices.
- Refined the **Simulation and Utilities** overview to:
    - Emphasize the **box-based, modular workflow** (Graph / Parametric Model /
      Instantiated Model / Simulation / Data / Search / Grid Search / Compare),
    - Remove references to legacy Tools menus,
    - Show how simulation, resampling, and grid search fit naturally into
      workbench pipelines.

### 6. Data subset / resample editor

- Added a **Data subset / resample** detail page under the Tetrad Interface
  “box-by-box” documentation.
- Documented:
    - The two-list variable selector (Available vs. Selected) and how column
      order in *Selected variables* determines the column order in the
      output dataset.
    - The **Sort** option for alphabetizing available variables, and the
      **Paste…** action for selecting variables by pasting comma-, tab-, space-,
      or newline-separated names.
    - Row selection via 1-based, comma-separated ranges (e.g.
      `1–100, 150, 200–250`), including error handling for invalid specs.
    - Sampling modes (**Use rows as-is**, **Shuffle rows**, **Subsample**,
      **Bootstrap**), the **Sample size** control, and the **Seed** field
      for reproducible resampling.
- Clarified that the Data subset / resample node is a safe, reproducible
  alternative to manual copy/paste and delete operations in the Data box,
  and that the resulting node can be used anywhere a normal `Data` node
  can be used.

### 7. Regression box: adjustment and IDA tools

- Updated the **Regression** box documentation to reflect that both:
    - the **Adjustments and total effects** component (based on Recursive
      Adjustment / GAC sets), and
    - the **IDA Check** component  
      now live in the Regression box, rather than being scattered across other
      parts of the interface.
- Added a new **IDA Check** detail page, including:
    - An explanation of standard IDA (Maathuis et al. 2009) and optional
      **Optimal IDA** (Witte et al. 2020).
    - A description of the **Show Optimal IDA** checkbox and the regex-based
      row filter for the *Pair* column.
    - Column-by-column documentation of:
        - `Pair`, `Min TE`, `Max TE`, `IDA Min Effect`, `True TE`,
          and `Sq Dist`,
          and how these are interpreted in simulation versus real-data settings.
    - Clarification that for real data, where the true total effects are
      unknown, all columns and summary statistics requiring `True TE` are
      omitted, so the panel reports only the empirical IDA / Optimal IDA
      intervals.
- Updated the IDA Check screenshot to show **standard IDA as the default**
  (the *Show Optimal IDA* checkbox unchecked), preserving backward
  compatibility with earlier versions of the tool and documentation.

---

Further tweaks and small additions (for example, new detail callouts or
screenshots) after this point are considered minor and are not listed
individually here.