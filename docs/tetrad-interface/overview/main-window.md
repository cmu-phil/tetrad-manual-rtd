# Main Window

The Tetrad main window is the starting point for most workflows. It provides:

- A **menu bar** and **toolbar** for global actions (open/save, logging, pipelines, etc.).
- A **project tree** listing data sets, graphs, models, and results.
- A **work area** where editors and result views appear in tabs.
- A **status bar** (and optional logging pane) with progress and message reporting.

![](../../_static/images/tetrad-interface/overview/main-window-overview.png)

In a typical session you will:

1. Load or create data and graphs.
2. Configure algorithms in boxes (Data, Search, Compare, etc.).
3. Run algorithms and inspect their outputs in tabs.
4. Save the session for later.

## Project tree

On the left, the **project tree** shows the objects in your current Tetrad session. Each entry
corresponds to something you can open, run, or use as input to another tool:

- **Data nodes**  
  Continuous data sets, mixed data sets, or covariance matrices.
- **Graph nodes**  
  DAGs, CPDAGs, PAGs, and other graph objects produced by search or imported from files.
- **Algorithm and configuration nodes**  
  Search boxes, simulation setups, estimators, updaters, and other configured tools.
- **Result nodes**  
  Graphs, tables, and reports created by algorithms and utilities.

You can usually:

- **Double-click** a node to open it in the work area (for example, double-click a graph to open
  the graph editor).
- **Right-click** a node to access context actions such as rename, delete, export, or run.
- **Drag** certain nodes (such as graphs or data sets) into boxes on the workbench that accept them.

Deleting a node from the project tree removes it from the session; closing a tab in the work area
does not.

## Work area and tabs

The central work area displays one or more tabs. Each tab shows an editor or a result view associated
with a node in the project tree:

- **Graph editors** – interactive views where you can add, remove, and orient edges.
- **Data views** – tables showing raw data, summary statistics, or covariance matrices.
- **Configuration dialogs** – parameter settings for search algorithms, simulations, estimators, etc.
- **Result views** – edge lists, fit indices, comparison tables, or logs of algorithm behavior.

Tabs can be opened and closed independently. Closing a tab does **not** delete the underlying node
in the project tree; you can always re-open it by double-clicking the node again.

A common pattern is:

1. Double-click a configuration node (e.g., a Search box) to adjust parameters.
2. Run the configuration from the toolbar or context menu.
3. Double-click the resulting graph or table node to view the results in a new tab.

## Menus and toolbar

The **menu bar** in the version of Tetrad described in this manual includes:

- **File**  
  Open and save sessions, import/export data and graphs, save a workspace image, show the session
  version, and exit the application.  
  The **File → Settings** submenu controls:
    - **Logging** – where log output is written (only to the logging pane, or also to a log file).
    - **Number Format** – the numeric formatting used throughout the application.
    - **Enable Experimental** – whether experimental algorithms and options are shown
      (for example, in the *Search* box).
- **Edit**  
  Undo/redo (where supported) and basic editing commands.
- **Logging**  
  Controls runtime logging:
    - **Start Logging** opens a logging pane at the bottom of the main window and begins routing
      log messages from algorithms and tools to it.  
      If logging to files has been configured in **File → Settings → Logging**, this also starts
      a new log file on disk.
    - **Stop Logging** stops sending messages to the logging pane and, if a log file is open,
      closes the file.
- **Pipelines**  
  Offers templates for **pre-wired workbench pipelines**. Choosing an entry places a fully
  connected set of session boxes on the workbench (for example, Data → Search → Compare).
  Each box in the pipeline can then be **double-clicked and filled in** with your chosen
  data, algorithms, and models.
- **Window**  
  Standard window-management actions, such as showing or hiding panes and focusing different
  parts of the interface.
- **Help**  
  Version information and links to this manual and the Tetrad website.

The **toolbar** (below the menu) exposes common shortcuts such as opening/saving sessions, running
the currently selected configuration, and graph layout/zoom controls. Hover over a button to see
its tooltip.

## Status bar, logging pane, and messages

At the bottom of the main window, a status area reports:

- Running tasks (for example, “Executing FGES…”).
- Progress indicators, where available.
- Warnings or errors reported by algorithms and tools.

When you choose **Logging → Start Logging**, a **logging pane** appears (typically docked above the
status bar). This pane shows streaming log output from algorithms and utilities while they run.
Choosing **Logging → Stop Logging** hides the logging pane and, if file logging is enabled,
closes the current log file.

For long-running algorithms, you can watch both the status area and the logging pane to monitor
progress, see any warnings, and, in some cases, cancel the run from the associated controls.