# Compare Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/compare-box.png
:name: tetrad-compare-box-screenshot
:alt: Compare Box in the Tetrad interface.

Compare Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Compare** box is where you compare **multiple graphs or models** side by side. It shows
a list of objects selected for comparison, lets you configure what aspects to compare, and
presents numerical and graphical summaries of similarities and differences.

Typical uses include:

- Comparing the outputs of different search algorithms on the same data.
- Comparing graphs learned from different datasets or parameter settings.
- Comparing a learned graph to a ground-truth or "reference" graph.

## Typical workflow

1. **Select objects to compare**
   - From other boxes (e.g., *Graph*, *Search*), create or load the graphs/models you
     want to compare.
   - In the Compare box, use the **Add** or **Select** buttons to choose which graphs
     or models to include in the comparison.

2. **Choose comparison metrics**
   - Configure the comparison options, which may include:
     - Structural distance metrics (e.g., adjacency differences, orientation differences).
     - Fit or score-based comparisons (if applicable).
     - Edge-wise agreement tables or counts.

3. **Run the comparison**
   - Click the **Run** or **Compare** button.
   - The main panel updates with tables, counts, or summaries describing how the selected
     graphs/models agree or differ.

4. **Inspect results**
   - Review summary statistics (e.g., number of differing edges, SHD-like counts).
   - Drill down into per-edge or per-variable differences, where available.
   - Optionally export tables or screenshots for use in papers or reports.

## Key controls

- **Toolbar**
  - **Add / Select** – choose graphs or models to include in the comparison.
  - **Remove** – take selected items out of the comparison set.
  - **Configure** – open dialogs to choose comparison metrics or options.
  - **Run / Compare** – perform the comparison using the current configuration.
  - **Export** – save comparison tables or summaries to a file (when supported).

- **Comparison list**
  - Shows the graphs/models currently selected for comparison.
  - Allows reordering or deselecting items if the comparison method is order-sensitive.

- **Main panel**
  - Displays the comparison results:
    - Summary statistics (e.g., total edge differences).
    - Tables showing which edges or parameters differ.
    - Optional visual overlays or side-by-side views (depending on the method).

## Common patterns & tips

- When evaluating new algorithms, keep a **reference graph** (e.g., from simulation ground truth
  or a well-understood baseline method) and always include it in comparisons.
- Use **consistent naming** for graphs and models so that comparison tables are easier to interpret.
- If results are confusing, double-check that all compared graphs were learned from the **same data**
  and under compatible assumptions (e.g., same variable set, same treatment of latents and selection).

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Compare**:
  - *Graph* and *Search* (provide graphs to be compared).
  - *Grid Search* (may generate many models whose results you inspect via comparison).
