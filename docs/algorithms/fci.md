# FCI — Fast Causal Inference

🔍 **Constraint-based** • 🧩 **Latent-capable** • Output: **PAG**

FCI is the **canonical constraint-based algorithm** for learning causal structure when **hidden confounders and
selection bias may be present**. It generalizes PC from DAGs/CPDAGs to MAGs/PAGs, using conditional independence tests
plus a rich set of orientation rules.

---

## Key idea

> Use conditional independences to recover a **Partial Ancestral Graph (PAG)** that represents **all** causal models (
> MAGs) compatible with the data, even when some variables are unmeasured or selection-biased.

FCI proceeds in three broad stages:

1. **Adjacency search**  
   Start from a complete undirected graph; remove edges when variables are independent given some conditioning set.

2. **Extra-edge removal using possible-d-separation sets**  
   Go beyond PC by testing separations along paths that may involve **latent variables**, using “possible-d-sep” sets to
   identify additional edges that must be removed.

3. **Orientation rules (R0–R10)**  
   Apply a collection of sound orientation rules (including collider orientation, discriminating paths, and
   visible/invisible-edge rules) to obtain a **PAG** with tails, arrowheads, and circles encoding ancestral constraints.

The output PAG compactly encodes **all causal structures** consistent with the CI relations under the assumptions of
Causation, Prediction, and Search (CPS).

---

## When to use FCI

Use FCI when:

- You **cannot assume causal sufficiency**  
  (latent confounders of measured variables are plausible).
- **Selection bias** may be present.
- You want a **PAG** as the target representation.
- You prefer a **pure CI-based method** with well-understood theory.

Typical scenarios:

- Observational studies in epidemiology, social science, psychology.
- Combining variables from different sources where unmeasured drivers are likely.
- Exploratory causal discovery where “no latents” is clearly unrealistic.

If you are confident there are **no hidden confounders**, algorithms like **PC**, **FGES**, or **BOSS** (with DAG/CPDAG
output) are usually more appropriate.

---

## Assumptions

FCI relies on the standard assumptions from *Causation, Prediction, and Search* (CPS):

- The data come from a **causal DAG** over measured + latent + selection variables.
- The distribution is **Markov and faithful** to the corresponding **MAG** over the measured variables.
- Errors are independent (no deterministic violations, unless treated carefully).
- CI tests are sufficiently reliable in the sample limit (independence oracle in theory).

The full FCI rule set (R0–R10), as completed by Zhang (2008), is **sound**, **arrowhead-complete**, and **tail-complete** for PAGs.  This means FCI orients every arrowhead and tail that is invariant across  all MAGs in the Markov equivalence class, and orients none that are not  so invariant. The resulting graph is the maximally informative PAG.

---

## How it works (at a glance)

This is a high-level, CPS-style view; many implementation details (e.g., rule variants) are omitted for clarity.

### 1. Initial adjacency search (PC-style)

- Start with a **complete undirected graph** over the measured variables.
- For each pair of variables $X, Y$, search over conditioning sets $S$ (starting from size 0 and increasing) such that:
    - If $X \perp Y \mid S$ is found, remove the edge $X - Y$ and record $S$ as a **separating set
      ** $\text{Sepset}(X,Y)$.
- This is essentially the **Fast Adjacency Search (FAS)** phase from PC.

Result: a sparse **skeleton** plus separating sets, but still possibly containing edges that are only explainable by
latents or selection.

### 2. Extra-edge removal using possible-d-sep

PC’s skeleton is not sufficient in the presence of latents. FCI refines it via **possible-d-separation**:

- For each remaining adjacency $X - Y$, compute a **Possible-D-SEP** set, which collects nodes that could appear on a *
  *d-separating path** between $X$ and $Y$, even when latent variables are present.
- Test additional independences of the form  
  $X \perp Y \mid S$, where $S \subseteq \text{Possible-D-SEP}(X,Y)$.
- If such an $S$ is found, **remove** the edge and update the sepset.

Intuition: this stage finds edges that PC cannot remove, because the conditioning sets needed to reveal independence can
involve nodes that look “non-local” when latent variables are present.

### 3. Orientation rules (R0–R10)

With the refined skeleton and separating sets, FCI orients edges by applying a sequence of rules (R0–R10 in CPS-style
presentations). At a high level:

1. **Unshielded colliders (R0)**  
   For triples $X - Z - Y$ where $X$ and $Y$ are nonadjacent:
    - If $Z$ is **not** in any separating set $\text{Sepset}(X,Y)$, orient as  
      \[
      X \rightarrow Z \leftarrow Y.
      \]

2. **Propagation rules (R1–R4)**  
   Analogues of the Meek rules for DAGs/CPDAGs, extended to handle circles and ensure:
    - No new unshielded colliders are introduced.
    - No directed cycles arise.

3. **Latent/selection-specific rules (R5–R10)**  
   These handle:
    - **Discriminating paths** (paths that force specific orientations).
    - **Visible vs. invisible edges**, encoding when an edge cannot be explained away by a latent common cause.
    - Additional refinements that ensure the final graph is a valid **PAG** for some MAG consistent with the CI
      relations.

Rules are applied iteratively until no more orientations are possible.

### 4. PAG output

The final graph is a **PAG**, whose edge marks (tails, arrowheads, circles) mean:

- **Tail (—)** at $X$ on $X —? Y$:  
  $X$ is an ancestor of $Y$ (in all compatible MAGs).
- **Arrowhead (→)** at $Y$ on $X ?→ Y$:  
  $Y$ is **not** an ancestor of $X$ (in all compatible MAGs).
- **Circle (o)** at an endpoint:  
  Orientation is not fixed across all compatible MAGs.

This PAG summarizes everything FCI can reliably infer about ancestral relations among measured variables given the
assumptions and observed CIs.

---

## How it relates to other Tetrad algorithms

- **PC**
    - PC is the **special case** of FCI when you assume **no latent confounders and no selection bias**.
    - PC outputs a **CPDAG**; FCI outputs a **PAG**.

- **RFCI**
    - RFCI uses fewer conditional independence tests than FCI by restricting some of the Possible-D-SEP logic.
    - It is **faster** but can be more conservative (fewer orientations, sometimes more adjacencies).

- **GFCI, BOSS-FCI, GRaSP-FCI**
    - These are **hybrid** methods: they start from a score-based CPDAG (FGES, BOSS, GRaSP) and then apply **FCI-style**
      pruning/orientation to obtain a PAG.
    - FCI can be viewed as the **pure CI-based backbone** that these hybrids extend.

- **FCIT**
    - FCIT keeps the **PAG semantics and rules** of FCI but uses **targeted, score-guided testing**, often improving
      finite-sample behavior and scalability.
    - Conceptually: “FCI with smarter test scheduling + PAG repair.”

If you want the canonical, theory-first PAG algorithm, use **FCI**; if you want a hybrid with improved finite-sample
performance, consider **BOSS-FCI** or **FCIT**.

---

## Strengths

- Handles **latent confounders** and **selection bias** explicitly.
- Produces a **PAG**, which:
    - Encodes **all** causal structures consistent with the CI relations under CPS assumptions.
    - Clearly distinguishes what is known (tails/arrowheads) from what is unresolved (circles).
- **Provably sound** and arrow and tail complete with an independence oracle.
- Well-studied and widely cited in the causal discovery literature (CPS and follow-up work).

---

## Limitations

- **CI-test intensive**
    - FCI can be computationally expensive, especially for large graphs and high maximum conditioning-set sizes.
- **Sample sensitivity**
    - Finite-sample errors in CI tests can lead to missing or spurious edges and orientations.
- **Complexity of interpretation**
    - PAGs are more intricate than DAGs/CPDAGs; users must understand tails, arrowheads, and circles.
- Assumes **acyclicity** and the Markov + faithfulness conditions for MAGs.

For large problems, you may prefer **RFCI**, **GFCI**, or **FCIT** as more scalable alternatives.

---

## Prior knowledge support

In Tetrad, FCI typically supports:

- **Required and forbidden edges** (e.g., “X must cause Y”, “X must not cause Y”).
- **Tiered background knowledge**
    - You can constrain variables to earlier or later tiers so that edges only go from earlier to later tiers.

Background knowledge is enforced in a way that avoids contradicting the PAG semantics as much as possible. In
particular, required orientations are typically applied early so that FCI’s rules can propagate consequences correctly.

---

## Key parameters in Tetrad

Names may vary slightly in the GUI vs. Java API, but typical controls include:

- **Independence test**
    - e.g., Fisher Z (continuous), G-test/Chi-square (discrete), KCI/RCIT (nonlinear), basis-function tests.
- **Significance level (α)**
    - Controls how aggressively edges are removed; lower α → sparser graphs.
- **Maximum conditioning-set size / depth**
    - Caps the size of conditioning sets considered during adjacency search and Possible-D-SEP-based tests.
- **Allow selection bias** (if available in your build)
    - Toggles whether selection variables are allowed/encoded in the PAG semantics.
- **Number of threads**
    - Parallelizes CI tests where possible.
- **Verbose / logging options**
    - Helpful for debugging or inspecting which CI tests drove key decisions.

For many users, the most important knobs are **independence test**, **α**, and **maximum depth**.

---

## Reference

The FCI algorithm was introduced and developed in:

Spirtes, P., Glymour, C., & Scheines, R.
Causation, Prediction, and Search, 2nd edition.
MIT Press.

The modern, complete set of orientation rules for PAGs is given in:

Zhang, J. (2008).
On the completeness of orientation rules for causal discovery in the presence of latent confounders and selection bias.
Artificial Intelligence, 172(16–17), 1873–1896.

This is the authoritative reference establishing the soundness and completeness of the R0–R10 rule set used in FCI,
RFCI, and hybrid FCI-style algorithms.

---

## Summary

FCI is the **workhorse constraint-based algorithm** for causal discovery with latent variables and selection bias. It
extends PC to the MAG/PAG setting by:

- Using **Possible-D-SEP** sets to find all adjacencies compatible with hidden confounders, and
- Applying a rich family of **orientation rules** (R0–R10) to produce a **PAG** that faithfully represents all
  compatible causal structures.

If you need a principled, CI-based approach to causal discovery with **unmeasured confounding**, FCI is the standard
baseline against which newer methods are compared.