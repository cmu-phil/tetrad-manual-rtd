# Simulation and Utilities

In addition to search algorithms, Tetrad provides several **utility tools** that support simulation,
resampling, model checking, and parameter sweeps. Many of these are accessible from the **Tools** menu
and from dedicated boxes on the workbench.

![](../../_static/images/tetrad-interface/overview/simulate-data-dialog.png)

![](../../_static/images/tetrad-interface/overview/utility-dialog.png)

## Simulating data from a graph

There are two closely related ways to simulate data from a model in Tetrad:

1. **From the Tools menu**

   A common workflow is:

    1. Start from a **causal graph** (for example, a DAG with parameterized edge coefficients or distributions).
    2. Choose **Tools → Simulate Data from Graph**.
    3. Configure:
        - Number of samples.
        - Error distributions (Gaussian, non-Gaussian, etc.).
        - Whether to add measurement error or missingness.
    4. Run the simulation to produce a new **data node** in the project tree.

2. **Using boxes on the workbench**

   For more complex workflows, you can connect boxes:

    - Use a **Graph** box and a **Parametric Model** or **Instantiated Model** box to define your model.
    - Connect that model to a **Simulation** box.
    - Connect the **Simulation** box to a **Data** box (to hold the simulated data) and then to a **Search** box.

   In this setup, you can:

    - Generate simulated data directly from a specified model.
    - Immediately run search algorithms on the simulated data in the same pipeline.
    - Repeat runs by changing parameters in the Simulation or Search boxes and re-running the pipeline.

Simulation is useful for:

- Benchmarking algorithms on known ground-truth graphs.
- Creating teaching examples.
- Exploring the impact of different noise models, sample sizes, and missingness mechanisms.

## Resampling and bootstrap tools

Some Tetrad tools support:

- **Bootstrap resampling** of an existing data set.
- Subsampling strategies to assess the stability of learned graphs or parameter estimates.

These tools typically:

- Take a data node and sometimes a graph or algorithm configuration as input.
- Produce collections of graphs or tables summarizing variability across resamples.
- Integrate naturally with methods like **CStaR** and **Grid Search**, which analyze:
    - Stability of adjacencies and orientations,
    - Performance of algorithms across different samples and parameter settings.

## Grid Search (overview)

The **Grid Search** facility (available as its own box and described in a separate detail page) lets you:

- Choose a **base algorithm configuration** (for example, a Search box using FGES or PC).
- Specify a grid of parameter values (such as different `alpha` levels or penalty discounts).
- Run the algorithm for every combination in the grid.
- Collect results as:
    - Tables of performance or fit statistics,
    - Sets of graphs that can be compared or summarized.

In the workbench, Grid Search fits naturally into pipelines such as:

- Data → Search → Compare (single configuration),
- Data → Grid Search → Compare (multiple configurations),
- Data → Simulation → Grid Search → Compare (simulation studies over parameter grids).

For details, see **Detail: Grid Search**.

## Other utilities

In the version of Tetrad described in this manual, datasets can be preprocessed and transformed using additional
utilities, often by **connecting Data boxes**:

- Attach a new **Data** box to an existing one and choose a **transformation** (for example, variable selection,
  standardization, or simple recoding).
- Use graph conversion or simplification tools to change graph types or remove certain edge types.
- Use graph-checking utilities to verify that graphs satisfy **type-specific constraints** (for example,
  DAG-ness, acyclicity, or valid PAG markings).

Several utilities are documented in their own pages elsewhere in the manual
(for example, **Detail: Grid Search** and **Detail: Markov Check**). Refer to
the table of contents for links to those tools and their usage patterns.