# FCI — Fast Causal Inference

Constraint-based • Latent-capable • Output: PAG

FCI is the canonical constraint-based algorithm for learning causal structure when hidden confounders and selection bias may be present. It generalizes PC from DAGs/CPDAGs to MAGs/PAGs, using conditional independence tests plus a rich set of orientation rules.

## Key idea

Use conditional independences to recover a Partial Ancestral Graph (PAG) that represents all causal models (MAGs) compatible with the data, even when some variables are unmeasured or selection-biased.

FCI proceeds in three broad stages:

1. Adjacency search  
   Start from a complete undirected graph; remove edges when variables are independent given some conditioning set.

2. Extra-edge removal using possible-d-separation sets  
   Go beyond PC by testing separations along paths that may involve latent variables, using “possible-d-sep” sets to identify additional edges that must be removed.

3. Orientation rules (R0–R10)  
   Apply a collection of sound orientation rules (including collider orientation, discriminating paths, and visible/invisible-edge rules) to obtain a PAG with tails, arrowheads, and circles encoding ancestral constraints.

The output PAG compactly encodes all causal structures consistent with the CI relations under the assumptions of Causation, Prediction, and Search (CPS).

## When to use FCI

Use FCI when:

- You cannot assume causal sufficiency (latent confounders of measured variables are plausible).
- Selection bias may be present.
- You want a PAG as the target representation.
- You prefer a pure CI-based method with well-understood theory.

Typical scenarios:

- Observational studies in epidemiology, social science, psychology.
- Combining variables from different sources where unmeasured drivers are likely.
- Exploratory causal discovery where “no latents” is clearly unrealistic.

If you are confident there are no hidden confounders, algorithms like PC, FGES, or BOSS (with DAG/CPDAG output) are usually more appropriate.

## Assumptions

FCI relies on the standard assumptions from Causation, Prediction, and Search:

- The data come from a causal DAG over measured plus latent plus selection variables.
- The distribution is Markov and faithful to the corresponding MAG over the measured variables.
- Errors are independent.
- CI tests are sufficiently reliable in the sample limit (independence oracle in theory).

The full FCI rule set (R0–R10), as completed by Zhang (2008), is sound, arrowhead-complete, and tail-complete for PAGs. This means FCI orients every arrowhead and tail that is invariant across all MAGs in the Markov equivalence class, and orients none that are not so invariant. The resulting graph is the maximally informative PAG.

## How it works (at a glance)

### 1. Initial adjacency search (PC-style)

- Start with a complete undirected graph over the measured variables.
- For each pair of variables X, Y, search over conditioning sets S (starting from size 0 and increasing) such that:  
  If X is independent of Y given S (written: X ⟂ Y | S), remove the edge X - Y and record S as the separating set Sepset(X, Y).

This stage is essentially the Fast Adjacency Search (FAS) from PC.

Result: a sparse skeleton plus separating sets, but still possibly containing edges that can only be explained by latents or selection.

### 2. Extra-edge removal using possible-d-sep

PC’s skeleton is not sufficient in the presence of latents. FCI refines it via possible-d-separation:

- For each remaining adjacency X - Y, compute a Possible-D-SEP set, which contains nodes that could appear on a d-separating path between X and Y in the presence of latent variables.
- Test additional independences of the form X ⟂ Y | S where S is a subset of Possible-D-SEP(X, Y).
- If such an S is found, remove the edge and update the separating set.

This step finds edges that PC cannot remove because the conditioning sets required to reveal independence are nonlocal when latent variables exist.

### 3. Orientation rules (R0–R10)

With the refined skeleton and separating sets, FCI orients edges using a sequence of rules (R0–R10). Highlights:

**Unshielded colliders (R0)**  
For triples X - Z - Y where X and Y are nonadjacent:  
If Z is not in Sepset(X, Y), orient as:  
X -> Z <- Y

**Propagation rules (R1–R4)**  
Generalizations of Meek-style rules but adapted for PAGs:

- Prevent creation of new unshielded colliders.
- Avoid directed cycles.
- Manage circle endpoints appropriately.

**Latent/selection-specific rules (R5–R10)**  
These operate on discriminating paths, visible versus invisible edges, and ensure the resulting orientation is valid for some MAG compatible with the detected CI pattern.

Rules are applied iteratively until no further orientations apply.

### 4. PAG output

A PAG uses three endpoint marks:

- Tail (“—”) on X —? Y: X is an ancestor of Y in all MAGs in the equivalence class.
- Arrowhead (“->”) on X ?-> Y: Y is not an ancestor of X in any compatible MAG.
- Circle (“o”): Orientation is not determined (both possibilities occur across compatible MAGs).

The PAG captures all invariant ancestral relations implied by the observed CIs.

## How it relates to other Tetrad algorithms

- PC: special case assuming no latent confounders or selection bias; outputs a CPDAG.
- RFCI: faster but sometimes more conservative.
- GFCI, BOSS-FCI, GRaSP-FCI: hybrids that use score-based initialization followed by FCI-style refinement.
- FCIT: retains FCI’s PAG semantics but uses targeted, score-guided test scheduling.

## Strengths

- Handles hidden confounders and selection bias explicitly.
- Produces a PAG that encodes all invariant ancestral relations.
- Provably sound and arrow/tail complete with an independence oracle.
- Foundational algorithm in causal discovery with latent variables.

## Limitations

- CI-test intensive; expensive for large graphs or high maximum conditioning-set sizes.
- Finite-sample CI errors can propagate.
- PAGs are more complex to interpret than CPDAGs.
- Assumes acyclicity and faithfulness.

RFCI, GFCI, or FCIT may be preferred for larger problems.

## Prior knowledge

FCI in Tetrad typically supports:

- Required and forbidden edges.
- Tiers (variables in earlier tiers cannot have later ones as ancestors).

Required edges are usually applied early so that subsequent rules propagate consequences.

## Key parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `depth` | Maximum conditioning-set size for adjacency search and possible-d-sep refinement. Use `-1` for unlimited depth. |
| `stableFas` | If `true`, uses the *stable* (order-independent) version of the Fast Adjacency Search (FAS). |
| `colliderOrientationStyle` | Determines how colliders are oriented: `SEPSETS`, `CONSERVATIVE` (CPC-style), or `MAX_P`. |
| `maxDiscriminatingPathLength` | Limits the length of discriminating paths considered in orientation rules. Use `-1` for no limit. |
| `doPossibleDsep` | If `true`, performs the full Possible-D-SEP search to remove additional edges missed by PC; if `false`, uses only PC-style adjacencies. |
| `completeRuleSetUsed` | If `true`, applies the full (Zhang 2008) rule set R0–R10; if `false`, applies only the basic rules. |
| `fdrQ` | False discovery rate threshold `q` used for FDR-controlled independence testing. Only relevant when FDR is enabled. |
| `timeLag` | Time-series lag parameter. If positive, applies the time-lag transform to produce lagged copies of each variable. |
| `timeLagReplicatingGraph` | If `true`, replicates the full graph structure across lags instead of shifting only adjacencies. |
| `guaranteePag` | If `true`, forces the output to be a legal PAG by preventing or reversing orientations that would violate acyclicity or maximality. |
| `verbose` | If `true`, prints detailed logs of skeleton search, possible-d-sep pruning, and rule applications. |

Note that for the collider orientation style, a choice of `CONSERVATIVE` yields an algorithm that has been called CFCI (Conservative FCI), whereas a choice of `MAX-P` yields an algorithm that has been called FCI-Max. The reference for FCI-Max is given below (Raghu et al., 2018).

## References

Spirtes, Glymour, and Scheines.  
Causation, Prediction, and Search. MIT Press.

Zhang, J. (2008). “On the completeness of orientation rules for causal discovery in the presence of latent confounders and selection bias.” Artificial Intelligence, 172(16–17), 1873–1896.

Raghu, V. K., Ramsey, J. D., Morris, A., Manatakis, D. V., Sprites, P., Chrysanthis, P. K., ... & Benos, P. V. (2018). Comparison of strategies for scalable causal discovery of latent variable models from mixed data. International journal of data science and analytics, 6(1), 33-45.