# Updater Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/updater-box.png
:name: tetrad-updater-box-screenshot
:alt: Updater Box in the Tetrad interface.

Updater Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Updater** box is where you apply **updating procedures** to existing objects in a Tetrad project.
Depending on your version and configuration, this may include:

- Updating graphs or models when **new data** becomes available.
- Re-running certain analyses with **modified assumptions** or **changed parameters**.
- Applying specialized update rules (for example, incremental adjustments to parameter estimates).

Conceptually, the Updater box lets you say: *“Given what I have already computed, update it in light of
this new information, without starting completely from scratch.”*

## Typical workflow

1. **Select an object to update**
   - Identify the object you want to update, such as:
     - A graph from the *Graph* box.
     - A parametric or instantiated model.
     - A dataset from the *Data* box (if supported).
   - In the Updater box, choose this object as the **input** to be updated.

2. **Specify new information**
   - Depending on the update method, you may supply:
     - A new or extended dataset.
     - Revised background knowledge (e.g., additional forbidden/required edges).
     - Updated parameter constraints or priors.
   - Configure these inputs using drop-downs and fields in the Updater setup panel.

3. **Choose an update method**
   - Select an available update procedure (for example):
     - Incremental graph update.
     - Re-estimation or shrinkage of parameters given new data.
     - Hybrid update rules tailored to a particular algorithm family.
   - Adjust method-specific options (e.g., learning rate or weighting of old vs. new information),
     if your version exposes them.

4. **Run the update**
   - Click **Run** (or **Update**) to apply the chosen method.
   - Progress messages and any warnings are shown in the log or status area.

5. **Inspect updated results**
   - The result is usually:
     - A **new graph or model** (appearing in the *Graph* or *Instantiated Model* boxes), or
     - A modified version of the original object (depending on how updates are configured).
   - Inspect these updated objects as you would any other graph or model.

## Key controls

- **Toolbar**
  - **New / Configure** – create or edit an update specification.
  - **Run / Update** – apply the current update method.
  - **Stop** – interrupt a long-running update.
  - **Duplicate / Rename / Delete** – manage saved update configurations.
  - **Export** – save logs or update specifications to a file (when supported).

- **Updater setup panel**
  - Selectors for:
    - Object to update (graph, model, dataset, etc.).
    - New data or additional information (if required).
    - Update method.
  - Fields for method-specific parameters and options.

- **Results / log panel**
  - Shows:
    - Which objects and data were used.
    - Which update method was applied.
    - Any warnings or diagnostic messages.
  - References or links to the updated objects now available in other boxes.

## Common patterns & tips

- Use the Updater box when:
  - You regularly receive **new data batches** and want to update existing models rather than refit from scratch.
  - You are iteratively refining assumptions and want to track how a model changes.
- Keep **original versions** of graphs and models (for example, by duplicating before updating) so you can
  compare updated results against earlier states.
- Pay attention to how the update method **weights old vs. new information**; this can greatly affect the
  stability or responsiveness of updated models.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Updater**:
  - *Graph* (graphs to be updated).
  - *Data* (new or extended datasets used for updating).
  - *Parametric Model* and *Instantiated Model* (models whose parameters may be updated).
  - *Compare* (compare original and updated models).
