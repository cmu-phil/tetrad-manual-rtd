# Latent Structure Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/latent-structure-box.png
:name: tetrad-latent-structure-box-screenshot
:alt: Latent Structure Box in the Tetrad interface.

Latent Structure Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Latent Structure** box is where you work with **explicit latent-variable models** in Tetrad.
Whereas the *Latent Clusters* box focuses on clustering variables or cases, the Latent Structure box
focuses on **structural relationships involving latent variables**—for example, multiple-indicator models,
latent DAGs, or more complex latent structures.

You use this box to:

- Build, edit, or inspect models that include latent variables.
- Run specialized search or modeling procedures for latent structures.
- Prepare latent-variable models for estimation, simulation, or comparison.

### Latent structure and simulation

To run latent models in **Simulation**:

1. Specify a **structure over the latent variables** in this box (latent nodes and edges among them),
   together with their observed indicators.
2. Convert or link this latent structure to a parametric model (e.g., SEM or Hybrid).
3. Use that parametric model as a source in the *Simulation* box.

Without a specified structure over the latents, Simulation cannot generate full joint data for
observed + latent variables.

See also:

- `Tetrad Interface → Detail Callouts → Latent Models and Simulation`


## Typical workflow

1. **Prepare inputs (graphs, clusters, or data)**
   - In the *Graph* box, define a graph that includes latent variables, or
   - In the *Latent Clusters* box, derive clusters that you will treat as latent factors, or
   - In the *Data* box, prepare the dataset whose covariance structure suggests latent structure.

2. **Create or import a latent structure model**
   - In the Latent Structure box, use **New** to:
     - Build a latent-variable model from:
       - An existing graph with latent nodes, or
       - Clusters produced by the Latent Clusters box, or
       - A template for common structures (e.g., multiple-indicator models).
   - Optionally import a latent structure model from a file if your version supports it.

3. **Inspect and edit the latent structure**
   - Select a latent structure in the list to display it in the main panel.
   - Use the editor to:
     - Add or remove latent variables.
     - Link latent variables to observed indicators.
     - Specify relationships among latent variables (e.g., directional edges).
     - Adjust measurement or structural assumptions.

4. **Use with estimation and simulation**
   - Pass the latent structure to:
     - The *Parametric Model* or *Estimator* boxes for parameter estimation.
     - The *Simulation* box to generate data from the latent model.
   - Combine with *Compare* or *Search* (where appropriate) to evaluate or refine the model.

## Key controls

- **Toolbar**
  - **New** – create a new latent structure model (from graphs, clusters, data, or templates).
  - **Duplicate / Rename / Delete** – manage existing latent structure models.
  - **Export** – save a latent structure model to a file, when supported.

- **Latent structure list**
  - Shows all latent structure models currently defined in the project.
  - Each entry may correspond to:
    - A specific dataset or covariance structure,
    - A chosen set of indicators and latent factors,
    - A particular structural hypothesis about relationships among latents.

- **Main panel**
  - Displays the selected latent structure in a graphical or tabular editor, with:
    - Latent nodes and their indicator variables.
    - Edges among latent variables.
    - Any annotations or constraints relevant to the model.

## Common patterns & tips

- Use latent structure models when you believe that **unmeasured constructs** explain
  patterns of correlation among observed variables.
- A common workflow:
  - Discover variable groupings using *Latent Clusters*.
  - Convert clusters into latent variables in the Latent Structure box.
  - Refine the structure among latent variables using domain knowledge.
  - Estimate and test the model using the *Estimator* box.
- Be careful to distinguish between:
  - **Measurement structure** (which variables indicate which latent factors).
  - **Structural relations** among latent variables (causal or correlational).

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Latent Structure**:
  - *Latent Clusters* (provides clustered groupings that can be turned into latent variables).
  - *Graph* (can represent latent structures directly).
  - *Parametric Model* and *Estimator* (fit latent structure models to data).
  - *Simulation* (generate data from specified latent structures).
