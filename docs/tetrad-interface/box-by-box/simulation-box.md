# Simulation Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/simulation-box.png
:name: tetrad-simulation-box-screenshot
:alt: Simulation Box in the Tetrad interface.

Simulation Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Simulation** box is where you **generate synthetic data** from graphs or models in a Tetrad project.
It connects:

- a **graph** or **parametric / instantiated model**,
- a choice of **data-generating mechanism** (e.g., linear Gaussian SEM, discrete model, nonlinear SEM),
- and **simulation settings** (sample size, number of datasets, random seed),

and produces one or more **datasets** that appear in the *Data* box.

Typical uses include:

- Testing and benchmarking search algorithms under controlled conditions.
- Exploring the behavior of estimators or adjustment procedures.
- Creating teaching or demonstration examples with known ground truth.

## Typical workflow

1. **Choose a source graph or model**
   - In the *Graph* box, define or load a graph to use as the causal structure, **or**
   - In the *Parametric Model* / *Instantiated Model* boxes, select a model with specified parameters.
   - In the Simulation box, select this graph/model as the simulation source.

2. **Configure the data-generating process**
   - Choose a simulation type, such as:
     - Linear Gaussian SEM.
     - Discrete or mixed SEM (if supported).
     - Nonlinear or custom simulators (depending on your Tetrad version).
   - Set simulation parameters, for example:
     - Sample size (number of cases).
     - Number of datasets to generate.
     - Error distributions and variances.
     - Random seed for reproducibility.

3. **Run the simulation**
   - Click **Run** to generate data.
   - The Simulation box creates one or more datasets, which are added to the *Data* box.
   - Progress and any warnings are typically shown in a log or message area.

4. **Inspect simulated data**
   - In the *Data* box, select the new datasets to:
     - Inspect variable distributions and correlations.
     - Confirm that variable names and types are as expected.

5. **Use simulated data for analysis**
   - Use the simulated datasets in:
     - *Search* (to evaluate causal discovery algorithms).
     - *Regression* or *Estimator* (to evaluate parameter estimation).
     - *Compare* (to compare different methods against the known generating graph/model).

## Key controls

- **Toolbar**
  - **New / Configure** – set up a new simulation specification.
  - **Run** – generate data using the current simulation settings.
  - **Stop** – interrupt a long-running simulation.
  - **Export** – optionally export simulation specifications or logs (depending on version).

- **Simulation setup panel**
  - Selectors for:
    - Source graph or model.
    - Simulation type.
  - Fields for:
    - Sample size.
    - Number of datasets.
    - Random seed.
    - Distribution-specific settings (e.g., error variances, discrete categories).

- **Results / log panel**
  - Summary of completed simulations, including:
    - Names of generated datasets.
    - Any warnings or errors.
  - Links or references to the datasets now available in the *Data* box.

## Common patterns & tips

- Use **fixed random seeds** when you want reproducible results across runs or when documenting examples.
- When evaluating search algorithms:
  - Simulate from a known graph and then run the algorithms on the simulated data.
  - Use *Compare* to evaluate how well the learned graphs recover the generating structure.
- For teaching or demonstrations:
  - Keep a small library of graphs and corresponding simulation settings that you reuse across sessions.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Simulation**:
  - *Graph* (provides causal structures for simulation).
  - *Parametric Model* and *Instantiated Model* (provide parameterized models for data generation).
  - *Data* (receives the simulated datasets).
  - *Search* and *Compare* (analyze and compare results on simulated data).
