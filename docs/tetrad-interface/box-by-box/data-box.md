# Data Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/data-box.png
:name: tetrad-data-box-screenshot
:alt: Data Box in the Tetrad interface.

Data Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Data** box is where you work with **datasets** in a Tetrad project. It shows
the list of all datasets in the current session, lets you load new ones, transform existing ones,
and inspect their contents.

In a typical workflow you will load data here first, then use it in *Search*, *Regression*,
*Estimator*, *Simulation*, and other boxes.

## Typical workflow

1. **Load or import a dataset**
   - Use the **Load** or **Import** button in the toolbar of the Data box.
   - Choose a supported file format (e.g., tab-delimited text, CSV).
   - Specify options such as:
     - Whether the first row is a header with variable names.
     - Delimiter or separator.
     - Encoding for missing values.

2. **Inspect and clean**
   - Select a dataset in the list to show it in the main panel.
   - Use the data viewer to inspect:
     - Variable names and types (continuous, discrete, mixed).
     - Basic summaries (e.g., number of cases, missingness).
   - Apply any available transformations (depending on the tools exposed in your version), such as:
     - Dropping or reordering variables.
     - Subsetting rows (e.g., filtering cases).
     - Discretizing or standardizing variables.

3. **Use in other boxes**
   - In *Search*, *Regression*, *Estimator*, and *Simulation*, choose datasets from drop-down lists
     that are populated from the Data box.
   - Run analyses, searches, and simulations using these datasets as inputs.

4. **Save your project**
   - When you save a Tetrad project, the datasets defined in the Data box (including any transformed copies)
     are saved along with graphs, models, and other objects.

## Key controls

- **Toolbar**
  - **Load / Import** – load data from a file.
  - **Duplicate / Rename / Delete** – manage existing datasets.
  - **Export** – write a dataset to a file.
  - (When available) **Transform** – open dialogs for common data transformations.

- **Data list**
  - Shows all datasets currently in the project.
  - Selecting an entry updates the main panel with that dataset.

- **Main panel**
  - Displays the selected dataset in a tabular viewer.
  - May include:
    - Variable-level information (name, type, domain).
    - Case-by-case values.
    - Summary information or diagnostic messages.

## Common patterns & tips

- Ensure that **variable names** are informative and consistent, especially when using multiple datasets
  or exporting results.
- When exploring model robustness:
  - Create **duplicated datasets** with different preprocessing (e.g., standardized vs. raw) and run searches
    on each version.
- Be careful when editing variable types:
  - Some algorithms assume continuous variables; others are designed for discrete or mixed data.
  - Mismatched types can lead to errors or misleading results.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Data**:
  - *Search* (uses datasets as input for causal discovery).
  - *Regression* and *Estimator* (fit models to data).
  - *Simulation* (may generate synthetic datasets for comparison).
  - *Instantiated Model* (binds parametric models to specific datasets and estimates).
