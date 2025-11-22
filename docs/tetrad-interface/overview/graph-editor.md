# Graph Editor

The graph editor is where you **create, inspect, and modify** causal graphs (DAGs, CPDAGs, PAGs, etc.) within Tetrad.

[//]: # (```{note})

[//]: # (Suggested screenshots:)

[//]: # ()
[//]: # (1. A graph open in the editor with a few variables and directed/undirected edges.)

[//]: # (   Save as: ``../../_static/images/tetrad-interface/overview/graph-editor.png``.)

[//]: # (2. The background knowledge / tiering dialog &#40;if available&#41;.)

[//]: # (   Save as: ``../../_static/images/tetrad-interface/overview/graph-background-knowledge.png``.)

[//]: # (```)

![](../../_static/images/tetrad-interface/overview/graph-editor.png)

![](../../_static/images/tetrad-interface/overview/graph-background-knowledge.png)

## Opening and creating graphs

You can obtain a graph in several ways:

- **From a search algorithm** – most algorithms output one or more graphs that appear as nodes in the project tree.
- **By importing** from a file (e.g., Tetrad `.txt` graph format).
- **By creating a blank graph** using a menu item like **Graph → New Graph**.

Double-click a graph node in the project tree to open it in the editor.

## Basic editing operations

In the graph editor, you can typically:

- **Add variables (nodes)** – via toolbar button or right-click in empty space.
- **Rename variables** – double-click the node label or use a context menu.
- **Add edges** – click a source node, then click a target node (or use drag-and-drop), depending on the edge mode.
- **Delete edges or nodes** – select them and press Delete / Backspace, or use a context menu.

Edge types may include:

- Directed: \( X 	o Y \)
- Undirected: \( X - Y \)
- Partially oriented: e.g., \( X \circ\!\!	o Y \) in PAGs
- Bidirected endpoints (latent confounding) where applicable

Tetrad enforces that only **legal edge types** for the graph’s type (DAG, CPDAG, PAG, etc.) can be drawn.

## Layout and visualization

The editor typically supports:

- **Automatic layout** to spread nodes evenly.
- **Zoom in/out** and **fit to window**.
- **Selection tools** (marquee select, multi-select).
- Optional display features (e.g., showing edge strengths or labels from certain algorithms).

These are often accessible via toolbar buttons or the **Graph** menu.

## Background knowledge and tiers

Many algorithms allow **background knowledge**:

- **Forbidden edges** (edges that must not be present).
- **Required edges** (edges that must be present).
- **Tier constraints** (e.g., variables in Tier 1 cannot have parents in later tiers).

The graph editor usually provides a dialog to:

- Assign nodes to **tiers**.
- Mark forbidden and required edges.
- Save/load knowledge constraints with the graph.

Algorithms that support knowledge will read these constraints and respect them during search.

## Saving and exporting graphs

Graph nodes can be:

- Stored within the current project file for later reopening.
- Exported to simple text formats or images (e.g., PNG) for use in papers or external tools.

Use the graph’s context menu or the **File/Graph** menus to find *Export Graph* or *Save As* options.
