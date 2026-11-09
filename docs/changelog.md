# Change Log

This change log describes updates to the Tetrad documentation (this ReadTheDocs manual).

This manual is what **Help → Manual** opens in Tetrad, from version 8.0.0 onward. Entries are
newest first.

⸻

## 8.0.0 — November 2026

Tetrad 8.0.0 was published to Maven Central on 9 November 2026, and is the first release whose
Help menu links to this site. The manual had not been updated since January 2026, so this round
brought it back in line with the software.

**Reference material is now generated from Tetrad itself rather than maintained by hand.**

- The **Parameters** page is generated from the same `parameter.definitions.html` that Tetrad reads
  at runtime, so the two cannot disagree. It went from 316 to 529 parameters, and every entry now
  has a heading and an anchor, grouped A–Z with a jump list; previously none of them did.
- Pages for 27 methods that had no documentation here were generated from Tetrad's own built-in
  descriptions. Every method a user can select is now documented, apart from those marked
  experimental.
- A **method crosswalk** (`tools/method-crosswalk.tsv`) records, for all 106 selectable methods,
  which page documents it, and a checker fails if the two drift apart.

**Methods.**

- New page: [Experimental Methods](experimental-methods.md), stating once that experimental
  methods carry no documentation commitment, and listing all of them.
- **BOSS-FCI** renamed to **BFCI** throughout, matching the name Tetrad now uses. The old name was
  retained in the program only so that sessions saved by 7.6.10 and earlier still open.
- **IMaGES** is no longer a separate algorithm; its page now explains how to get it from the
  `poolDataSets` parameter on any score- or test-based algorithm.
- Pages retired for methods no longer offered: PCD, DM, GIN, CCI Test, MVPLRT, MVP BIC Score.
- `StARS` and `StabilitySelection` are now labelled as available from scripts only.
- Fifteen pages whose titles did not match the chooser now state the interface name and the
  command.

**The interface section.**

- The **menu bar** documentation was rewritten: there is now a **Tetrad** application menu, and the
  old **File → Settings** submenu has been replaced by a Settings dialog with General, Numbers and
  Logging tabs.
- The **Latent Structure** box was removed from Tetrad in October 2026; its page now explains where
  its searches went and that older sessions still open.
- New page: [Data Audit](tetrad-interface/data-preparation/data-audit.md), covering all 28 finding
  codes and what to do about each.
- New page: [Causal Unmix](tetrad-interface/data-preparation/causal-unmix.md).
- New page: [NN Estimator](tetrad-interface/detail-callouts/detail-nn-estimator.md).
- The **Layout** section of the graph editor was rewritten around Richard's layout, now the default.

**The classic manual retired.**

- The `classic-manual` section has been removed. It was a one-time export of Tetrad's built-in
  HTML manual, it had diverged from both the software and the rest of this site, and the
  `tetrad-interface` section now covers the same ground.
- Three things it held that nothing else did were kept and promoted out of it: the
  [Quickstart](quickstart.md), the [Glossary](glossary.md), and the
  [Appendices](appendices.md) — an introduction to PAGs, the arc specializations, and the
  out-of-memory note.
- The glossary's terms had been lost when the section was first converted from HTML, leaving
  definitions with nothing to define. They have been recovered from the original.

**Housekeeping.**

- Eight toctree blocks were missing their closing fence.
- Pages that were built but unreachable from the navigation have been wired in, marked as
  deliberate orphans, or retired. The two extended worked examples are now in the Workflows
  section.

Screenshots have deliberately **not** been retaken in this round. All 140 predate the menu
refactor, the layout change and the box consolidation, and they are best redone in one pass once
the interface has settled.

⸻

2025 — Manual Overhaul for Next Release

1. New Tetrad Interface Manual
   •	Added a new Tetrad Interface section that replaces the old “classic” HTML manual for GUI usage.
   •	Introduced task-oriented pages for:
   •	Main Window and workspace
   •	Working with Data
   •	Graph box and graph editor
   •	Parametric Model and Instantiated Model boxes
   •	Estimator, Updater, Regression
   •	Data, Simulation, Search, Latent Clusters, Latent Structure, Knowledge, Compare, and Note boxes
   •	Added box-by-box documentation with screenshots for all core boxes.
   •	Created separate detail callouts for:
   •	Parametric model families (Bayes, SEM, Hybrid, Generalized)
   •	Instantiated model families (Bayes, SEM, Hybrid, Generalized)
   •	Updaters (Junction Tree, Approximate, Row Summing, SEM)
   •	Grid Search and Markov Checker
   •	Documented Pipelines, Logging, and File → Settings options in the main window description.

⸻

2. Tests and Scores Documentation
   •	Added individual pages for all major tests and scores, including:
   •	FisherZ, GSquare, ChiSquare, CCI, KCI, Basis-Function LRT, Conditional Gaussian and Degenerate Gaussian LRTs, Mvplrt, MSeparationTest, ProbabilisticTest, SemBicTest, PoissonBicTest.
   •	SemBicScore, DiscreteBicScore, BDeuScore, ConditionalGaussianBicScore, DegenerateGaussianBicScore, BasisFunctionBicScore, EbicScore, GicScores, MSepScore, MVPBicScore, PoissonPriorScore, ZhangShenBoundScore.
   •	Each page now includes:
   •	A clear description of when to use the test or score.
   •	Parameters derived from the code’s getParameters() definitions.
   •	Cross-references to relevant algorithms (e.g., FGES, BOSS, GRaSP).
   •	Added a “Tests and Scores — Alphabetical” index and updated “Choosing Tests and Scores” to point to the new catalog.

⸻

3. Algorithm and Terminology Updates
   •	Renamed LV-Dumb to LV-Heuristic throughout the manual and catalog to reflect a clearer, more professional name.
   •	Updated references to LV-Lite to use the current name FCIT in the interface and documentation.
   •	Added a full GIN (Generalized Independent Noise) algorithm page, including a paper-compliant description of the clustering step, root-peeling causal ordering, latent-DAG construction, parameters (alpha, verbose), and examples; updated Search-box cross-references to reflect the new implementation.
   •	Standardized summary sections and “When to use / When not to use” wording across several algorithms (e.g., CStaR, Factor Analysis, MIM-Build variants, TSC, BOSS-related methods).
   •	Clarified the roles of Py-Tetrad, RPy-Tetrad, and causal-learn in the “Interfacing Tools” page.

⸻

4. References and Clean-Up
   •	Updated and completed citations for tests and scores, including:
   •	BDeu, Conditional and Degenerate Gaussian methods, EBIC, GIC, Zhang–Shen bounds, Basis-Function methods, and others.
   •	Fixed numerous small issues:
   •	Terminology and parameter names,
   •	Minor wording errors and outdated descriptions,
   •	Consistency of notation and style across pages.
   •	Verified that the HTML build, PDF output, and search all work cleanly, including proper rendering of equations and tables.

⸻

5. Estimation Workflow and Simulation Pipelines
   •	Added an “Estimate model parameters” overview page describing:
   •	Conversion from graph → Parametric Model,
   •	Using an Estimator with a Data or Simulation node,
   •	Producing Instantiated Models with fitted parameters and fit indices.
   •	Refined the Simulation and Utilities overview to:
   •	Emphasize the box-based workflow (Graph → Parametric Model → Instantiated Model → Simulation → Data → Search → Grid Search → Compare),
   •	Remove legacy references to Tools menus,
   •	Show how simulation, resampling, and grid search integrate into workbench pipelines.

⸻

6. Data subset / resample editor
   •	Added a Data subset / resample detail page under the Tetrad Interface “box-by-box” documentation.
   •	Documented:
   •	Two-list variable selector (Available vs. Selected) and column-order semantics.
   •	Sorting options, paste-based variable selection, and error handling for malformed input.
   •	Row-selection syntax (1–100, 150, 200–250) and behavior for invalid ranges.
   •	Sampling modes (Use rows as-is, Shuffle rows, Subsample, Bootstrap), the Sample size field, and the Seed option.
   •	Clarified that this component is a safe, reproducible alternative to manual row/column deletion in the Data box.

⸻

7. Regression box: adjustment and IDA tools
   •	Updated the Regression box documentation to reflect that:
   •	The Adjustments and total effects component (based on Recursive Adjustment / GAC sets), and
   •	The IDA Check component
   now both reside in the Regression box with consistent UI and shared notation.
   •	Added a new IDA Check detail page, including:
   •	The distinction between standard IDA (Maathuis et al. 2009) and Optimal IDA (Witte et al. 2020),
   •	Description of the Show Optimal IDA checkbox and regex-based Pair filter,
   •	Column-by-column explanations of:
   Pair, Min TE, Max TE, IDA Min Effect, True TE, Sq Dist,
   and clarified which apply only in simulated-data settings.
   •	Revised the IDA Check layout and updated screenshots to reflect the modern interface.

⸻

Further tweaks and minor additions (e.g., small screenshot updates, style harmonization) are not listed individually.
