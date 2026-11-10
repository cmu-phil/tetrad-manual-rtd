# Working with Data

Tetrad supports several ways of bringing data into the interface and organizing it for analysis.
Most workflows start by placing a **Data** box on the workbench and loading a data set into it.

![](../../_static/images/tetrad-interface/overview/data-import-dialog.png)

![](../../_static/images/tetrad-interface/overview/data-table.png)

## Importing data

A typical workflow for bringing data into Tetrad is:

1. Place a **Data** box on the workbench, double-click it, and choose **File → Load Data** in the
   window that opens.
2. Select a file (for example, `.txt`, `.csv`, or a Tetrad-specific format).
3. In the import wizard, confirm:
    - The **delimiter** (tab, comma, etc.).
    - Whether there is a **header row** with variable names.
    - How **missing values** are encoded (for example, empty cells or a special code).
4. Review the automatically inferred **variable types** (continuous, discrete, etc.) and adjust if necessary.
5. Finish the wizard. The data set is now held in the Data box.

Tetrad distinguishes between several kinds of data:

- **Raw data sets** – rectangular case-by-variable tables (rows = cases, columns = variables).
- **Covariance or correlation matrices** – used by algorithms that operate directly on summary statistics (e.g., some SEM or factor-analysis methods).
- **Mixed data** – tables where some variables are continuous and others are discrete.

The type of data you import determines which **tests**, **scores**, and **algorithms** are available later.

## Viewing and editing data

To inspect a data set, **double-click** its Data box on the workbench:

- The main table shows **rows as observations** and **columns as variables**.
- A side panel (or header area) shows **metadata** such as variable names, types, and, for discrete variables, category levels.

From the data view and its context menus you can typically:

- Rename variables.
- Change variable types (for example, from continuous to discrete) when appropriate.
- Inspect basic information like the number of rows, number of columns, or presence of missing values.

Any changes you make here affect how the data set is treated by search algorithms and other tools.

## Linking data and graphs

Most search and modeling workflows require at least:

- One **Data** box (holding continuous, discrete, or mixed data), and
- A **test/score** that matches the data type (for example, FisherZ for continuous, GSquare for discrete).

When you configure a search algorithm or other tool in the GUI:

- You choose the data by drawing an arrow from the **Data** box to the box that will use it.
- Tetrad restricts the available tests and scores to those that are compatible with the chosen data type.
- The resulting graph or model is held in the box that produced it, such as the Search box.

You can load multiple data sets in the same session and run different algorithms (or different configurations of the same algorithm) on each.

## Saving and exporting data

Data can be:

- **Saved as part of a Tetrad session file**, so the data and all derived graphs/results can be reloaded together.
- **Exported** to a tab-delimited text format (and sometimes other formats) for use in R, Python, or other tools.

Look under the **File** menu for options to save the current session and to export data. This makes it easy to move between Tetrad and external analysis environments while keeping a record of which data sets were used for which graphs and models.