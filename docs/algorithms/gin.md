# GIN (Generalized Independent Noise)

## Overview

GIN is a causal discovery algorithm for finding latent variables and determining their causal ordering under a linear, non-Gaussian measurement model. It assumes that sets of observed variables arise from shared latent causes, and uses an independent-noise criterion to identify both the latent clusters and the relationships among them.

The algorithm proceeds in two major phases:

1. **Clustering:** identifies groups of observed variables that share a single latent parent.
2. **Latent ordering:** determines a causal order among those latent variables using a root-peeling procedure based on independence tests.

The output is a latent-variable DAG with directed edges among latent nodes and directed edges from each latent to its observed indicators.

This implementation follows the practical GIN procedure described in Xie et al. (2020, NeurIPS) and clarified in Xie et al. (2024, JMLR). It applies specifically to a **single layer of latent variables** above the observed variables.

## Requirements

GIN is appropriate when the following modeling assumptions are approximately satisfied:

- The data follow a linear model with **non-Gaussian noise**.
- Observed variables can be grouped into **latent clusters**, each representing indicators of one latent cause.
- Indicators satisfy a **double-pure measurement assumption**: each indicator depends on only one latent variable, and indicators are non-redundant.
- The latent causal structure is **acyclic**.

## Parameters

GIN exposes two user-configurable parameters:

| Parameter | Description |
|----------|-------------|
| `alpha`  | Significance threshold used when combining p-values via Fisher’s method to test the GIN condition. |
| `verbose` | If true, prints diagnostic messages during clustering and ordering. |

Independence-test parameters are configured separately through the selected independence test (e.g., KCI).

## How the Algorithm Works

### 1. Clustering observed variables

GIN searches for latent clusters by examining candidate subsets of observed variables:

1. For each candidate subset, a one-dimensional projection is computed from the covariance between that subset and the remaining variables.
2. The projection is tested for independence against each remaining observed variable.
3. P-values are combined with Fisher’s method. If the combined p-value is greater than or equal to `alpha`, the subset is accepted as a latent cluster.

Clusters with overlapping membership are merged so that each observed variable appears in at most one cluster.

Observed variables that do not appear in any cluster remain in the final graph without latent parents.

### 2. Ordering latent clusters

Once clusters are formed, GIN tests which latent variables are causal roots:

1. Each cluster is split into two halves to create surrogate variables for independence testing.
2. Surrogate sets from previously ordered clusters are included as conditioning components.
3. A cluster is a **root** if its surrogate variable is independent of the second halves of all other remaining clusters.

Roots are appended to the ordered list and removed from the pool. Clusters that cannot be ordered form an **unordered group**.

### 3. Constructing the latent graph

The final graph contains:

- A latent node for each cluster.
- Directed edges among latent nodes according to the discovered causal order.
- Undirected edges among latent nodes in the unordered group.
- Directed edges from each latent node to its observed indicators.
- Isolated observed nodes corresponding to variables that were not clustered.

## Output

GIN returns a graph consisting of:

- Latent nodes representing discovered latent clusters,
- Directed edges among latent variables reflecting the recovered causal order,
- Undirected edges among unordered latent variables, and
- Directed edges from latent variables to their observed indicators.

## When to Use

Use GIN when:

- You expect **one latent layer** generating clusters of indicators.
- Non-Gaussianity is plausible.
- Indicators are reasonably pure (each indicator loads on only one latent).
- A causal ordering among latent variables is desired.

## When Not to Use

GIN is not suitable when:

- There are **multiple hierarchical latent layers** (the full LaHiCaSl algorithm is required and not yet implemented in Tetrad).
- Indicators load on multiple latent variables.
- Noise is approximately Gaussian.
- Strong nonlinearity violates the linear model assumptions.

## Notes

- This implementation corresponds to the **single-layer** algorithm described in Xie et al. (2020) and the practical guidance provided in Xie et al. (2024).
- The hierarchical extension (LaHiCaSl) is **not** included.
- Independence testing uses the user-selected test, such as KCI.

## References

- Xie, L., Meng, C., Kanagawa, M., & Schölkopf, B. (2020). *Generalized Independent Noise Condition for Causal Discovery.* NeurIPS.
- Xie, L., Schölkopf, B., & Kanagawa, M. (2024). *A Versatile Causal Discovery Framework to Allow Causally-Related Hidden Variables.* JMLR.
