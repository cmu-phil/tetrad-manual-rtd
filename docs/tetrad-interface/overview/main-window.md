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

The **menu bar** has seven menus: **Tetrad**, **File**, **Edit**, **Logging**, **Pipelines**,
**Window** and **Help**.

- **Tetrad**  
  The application menu, first in the bar. It holds **About Tetrad**, **Warranty**, **License** and
  **Contributors**, then **Settings...**, then **Quit Tetrad**. On macOS the system's own
  application menu is wired to the same About and Settings items, so either route works.
- **File**  
  Session handling: **New Session**, **Load Session**, **Close Session**, **Save Session**,
  **Save Session As**, and **Save Session Workspace Image...**, which writes a picture of the
  workbench.
- **Edit**  
  Basic editing commands for the workbench.
- **Logging**  
  **Start Logging** opens a logging pane at the bottom of the main window and begins routing log
  messages from algorithms and tools to it. If logging to a file has been configured on the
  **Logging** tab of the Settings dialog, this also starts a new log file on disk. **Stop
  Logging** hides the pane and closes the file.
- **Pipelines**  
  Pre-wired workbench pipelines, in two labelled groups. Under **Analyze a real dataset**: *Load
  data and search*; *Load data, add knowledge, then search*; *Load data, search, then run a Markov
  check*; *Search then estimate*; *Search, estimate, then update*; and *Latent Clustering and
  Structure Search*. Under **Simulation studies**: *Simulate from a given graph, then search*; and
  *Simulate, search, then compare*. Choosing an entry places a connected set of boxes on the
  workbench, which you then fill in by double-clicking each one.
- **Window**  
  Window-management actions.
- **Help**  
  **Website**, **Manual** (which opens this site), **Algorithm Flowchart**, and **Suggestion
  Box!**, which opens Tetrad's issue tracker so you can send a suggestion or report a problem.

## Settings

**Tetrad → Settings...** opens a dialog with three tabs:

- **General** — **Dark Mode**, **Show experimental algorithms everywhere** (which is what reveals
  the methods marked experimental; see [Experimental Methods](../../experimental-methods.md)), and
  **UI font size**.
- **Numbers** — the numeric formatting used throughout the application.
- **Logging** — where log output is written: only to the logging pane, or also to a log file.

In earlier versions these settings were a **File → Settings** submenu. That submenu is gone; use
the Tetrad menu.

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