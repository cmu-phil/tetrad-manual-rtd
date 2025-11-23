# Main Window

The Tetrad main window is the starting point for most workflows. It provides:

- A **menu bar** and **toolbar** for global actions (open/save, logging, pipelines, etc.).
- A **project tree** listing data sets, graphs, models, and results.
- A **work area** where editors and result views appear in tabs.
- A **status bar** (and optional logging pane) with progress and message reporting.

[//]: # (```{note})

[//]: # (Suggested screenshot: a full view of the main window with the project tree on the left, a graph in the center,)

[//]: # (and menus/toolbar visible.)

[//]: # ()
[//]: # (Save as: ``../../_static/images/tetrad-interface/overview/overview/main-window-overview.png``.)

[//]: # (```)

![](../../_static/images/tetrad-interface/overview/main-window-overview.png)

## Project tree

On the left, the **project tree** shows the objects in your current Tetrad session:

- **Data nodes** (e.g., continuous data sets, mixed data sets, covariance matrices).
- **Graph nodes** (e.g., DAGs, CPDAGs, PAGs).
- **Algorithm nodes** (search configurations).
- **Result nodes** (graphs, tables, reports created by algorithms and tools).

You can usually:

- **Double-click** a node to open it in the work area.
- **Right-click** a node to access context actions (rename, delete, export, run, etc.).
- **Drag** some nodes (such as graphs) into tools that accept them.

## Work area and tabs

The central work area displays one or more tabs:

- Graph editors
- Tables of data
- Algorithm configuration dialogs
- Result views (edge lists, parameter tables, diagnostics)

Tabs can usually be closed independently; closing a tab does **not** delete the underlying node in the project tree.

## Menus and toolbar

The **menu bar** in the version of Tetrad described in this manual includes:

- **File** – open/save sessions, import/export data and graphs, save a workspace image, show the session version, and exit the application.  
  - The **File → Settings** submenu controls:
    - **Logging** – where log output is written (only to the logging pane, or also to a log file).
    - **Number Format** – the numeric formatting used throughout the application.
    - **Enable Experimental** – whether experimental algorithms and options are shown (for example, in the *Search* box).
- **Edit** – undo/redo (where supported) and basic editing commands.
- **Logging** – controls **runtime logging**:
  - **Start Logging** opens a logging pane at the bottom of the main window and begins routing log messages from algorithms and tools to it.  
    If logging to files has been configured in **File → Settings → Logging**, this also starts a new log file on disk.
  - **Stop Logging** stops sending messages to the logging pane and, if a log file is open, closes the file.
- **Pipelines** – offers templates for **pre-wired workbench pipelines**.  
  Choosing an entry places a fully connected set of session boxes on the workbench (for example, Data → Search → Compare).  
  Each box in the pipeline can then be **double-clicked and filled in** with your chosen data, algorithms, and models.
- **Window** – standard window-management actions (show/hide panes, focus different parts of the interface, etc.).
- **Help** – version information and links to this manual and other online resources.

The **toolbar** (below the menu) exposes common shortcuts (open, save, run, layout graph, zoom in/out, etc.).
Hovering over a button usually shows a tooltip explaining its function.

## Status bar, logging pane, and messages

At the bottom of the main window, a status area reports:

- Running tasks (e.g., “Executing FGES…”)
- Progress indicators where available
- Warnings or errors

When you choose **Logging → Start Logging**, a **logging pane** appears (typically docked above the status bar).  
This pane shows streaming log output from algorithms and utilities while they run. Choosing **Logging → Stop Logging** hides the logging pane and, if file logging is enabled, closes the current log file.

Long-running algorithms often update the status area and/or logging pane, and some provide **cancellable** operations from here.
