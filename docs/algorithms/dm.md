# DM (Detect–Mimic)

**Type:** special-purpose latent-preprocessing  
**Output:** graph with **intermediate latent variables** inserted between measured variables

The Detect–Mimic (DM) methods are designed to detect **intermediate latent variables** in Multiple Input Multiple Indicator (MIMIC)–style settings. The goal is to find “hidden layers” where groups of measured inputs jointly feed into one or more unobserved variables, which in turn drive groups of measured outputs.

Tetrad currently includes two variants:

- **DM-PC** – a simpler PC-based variant.
- **DM-FCIT** – a PAG-based variant built on FCIT and Recursive Blocking.

Both take a constraint-based view: they use independences and graph structure to decide when groups of parents–children are better modeled via an intermediate latent.

---

## DM-PC

**Package:** `edu.cmu.tetrad.search.DmPc`  
**Input:** independence test + (optionally) background knowledge  
**Output:** graph with latent nodes (type LATENT) inserted

### What DM-PC does

DM-PC wraps the **PC algorithm** and then restructures part of the learned graph as a shallow latent layer:

1. **Initial PC at depth 0.**  
   - Run PC with depth = 0 (only unconditional tests).  
   - Use any `IndependenceTest` you like (Gaussian, discrete, kernel, etc.) and optional `Knowledge`.

2. **Classify inputs and outputs.**  
   From the depth-0 pattern:
   - **Inputs:** nodes with indegree = 0 and outdegree > 0.  
   - **Outputs:** nodes with indegree > 0.  
   Nodes isolated in the pattern are ignored for DM purposes.

3. **Cluster outputs by shared inputs.**  
   For each output, collect the set of input nodes adjacent to it in the depth-0 graph.  
   Outputs that share the *same* set of inputs are grouped into a cluster:
   - key: set of input nodes  
   - value: set of outputs jointly connected to exactly that input set.

4. **Introduce latent nodes for each input–output cluster.**  
   For each cluster with at least one input and one output:
   - Create a latent node `L1`, `L2`, … (`NodeType.LATENT`).  
   - Add edges: `input -> Li -> output` for all inputs / outputs in the cluster.  
   - This produces a **MIMIC-style** latent between the input set and the output set.

5. **Latent–latent hierarchy.**  
   If one input set is a **superset** of another, DM-PC connects the corresponding latents:
   - If input set A contains input set B, add a directed edge from latent(B) → latent(A).  
   - This builds a hierarchical “stack” of latents when clusters are nested.

6. **Refine latent–latent edges via independence tests.**  
   For each latent–latent edge:
   - Let `latentA` have measured parents `PA` and measured children `CA`.  
   - Let `latentB` have measured parents `PB` and measured children `CB`.  
   - Form `combinedInputs = PA ∪ PB`, `outputsA = CA`, `outputsB = CB`.  
   - DM-PC tests whether **all pairs** `(a in outputsA, b in outputsB)` are conditionally independent given `combinedInputs`.  
   - If they *are* all independent, the latent–latent edge is removed.

7. **Final refinement using full PC.**  
   DM-PC then runs PC **again**, now at full depth (depth = −1), using the same test and knowledge:
   - For each output node, if in the **full PC pattern** it has **no input neighbors**, DM-PC:  
     - removes any edges from latents to that output, and  
     - adds edges among outputs according to the full PC pattern (undirected edges among outputs where PC says they are adjacent).
   - Finally, any latent node that ends up with either  
     - no measured parents, or  
     - no measured children  
     is removed.

The result is a graph where parts of the structure are explicitly modeled as:

- measured inputs → latent(s) → measured outputs,  
plus any remaining direct relations among outputs discovered by PC.

---

### When to use DM-PC

DM-PC is appropriate when:

- You suspect **intermediate latent variables** sitting between “source-like” variables and “indicator-like” variables.  
- The data are such that a **PC-style constraint-based search** is appropriate.  
- You want a relatively simple, PC-based latent refinement without full PAG machinery.

You do **not** need to manually specify which variables are inputs vs outputs; DM-PC infers them from the depth-0 PC pattern (sources vs non-sources).

---

### Prior knowledge

DM-PC honors a standard `Knowledge` object:

- Required / forbidden edges influence both PC runs (depth 0 and full depth).  
- This in turn affects which nodes are treated as inputs, which outputs are clustered, and where latents are inserted.

---

### Parameters (DM-PC)

DM-PC itself does not introduce new user-facing parameters. It inherits:

- The parameters of the **independence test** (e.g., alpha, test type).  
- The **PC settings** (indirectly, though depth is hard-coded to 0 then −1 inside DM-PC).  
- Background knowledge (via `setKnowledge`).

---

## DM-FCIT

**Package:** `edu.cmu.tetrad.algcomparison.algorithm.oracle.pag.DmFcit`  
**Base algorithm:** FCIT (BOSS-based hybrid FCI)  
**Output:** PAG with intermediate latent nodes inserted

### What DM-FCIT does

DM-FCIT combines three ingredients:

- **FCIT** (a hybrid FCI-style search using BOSS / GRaSP / SP starts),  
- **Recursive Blocking** (a path-based method to find small conditioning sets), and  
- a **Detect–Mimic layer** similar in spirit to DM-PC, but now operating on a **PAG** and using path information.

The overall flow:

1. **Optional time-lag expansion.**  
   If `TIME_LAG > 0` and the data are a `DataSet`, DM-FCIT first creates a lagged time-series dataset (via `TsUtils.createLagData`) and transfers the knowledge to that lagged dataset.

2. **Build independence test and score.**  
   DM-FCIT uses:
   - an `IndependenceWrapper` to construct the independence test, and  
   - a `ScoreWrapper` to construct the score used by BOSS / FCIT.  

   For d-separation oracle input (`MsepTest`), DM-FCIT enforces that you start with GRaSP rather than BOSS.

3. **Run FCIT to get a PAG.**  
   A standard FCIT run is performed:
   - Choice of start: BOSS, GRaSP, or SP (via `FCIT_STARTS_WITH`).  
   - BOSS options: `USE_BES`, `USE_DATA_ORDER`, `NUM_STARTS`.  
   - General options: `VERBOSE`, `KNOWLEDGE`, `TIME_LAG`, etc.  
   The result is a **PAG** over the measured variables.

4. **Detect–Mimic on the PAG (`getDmGraph`).**  
   DM-FCIT then operates on this PAG to insert intermediate latents:

   - It builds a helper graph `potentiallyDirected` consisting only of **directed** edges from the PAG (tails to arrowheads).  
   - For each node `x`, it collects:
     - `possibleChildren` = directed children of `x` in `potentiallyDirected`.  
     - `possibleParents` = parents of those children (and then children of those parents are also added to `possibleChildren`).

   - It then searches for **bipartite blocks**:
     - Candidate parent sets and child sets are formed from those neighborhoods.  
     - A candidate (parents, children) is accepted only if every parent–child pair is connected by a directed edge in `potentiallyDirected` (a kind of “dense” MIMIC pattern).

5. **Legitimacy check using Recursive Blocking.**  
   For each candidate parents–children block:

   - DM-FCIT uses the current PAG and **Recursive Blocking** to find a **minimal conditioning set** between each pair of children (childA, childB).  
   - It then tests independence between each child pair given that minimal conditioning set.  
   - If *any* pair becomes independent, the candidate latent is rejected.  
   - If **no** independence is found across all child pairs, the latent is considered legitimate.

6. **Insert the latent and re-orient the PAG.**  
   Once a candidate block passes the legitimacy check:

   - A new latent node `L1`, `L2`, … is created (`NodeType.LATENT`).  
   - For every parent `p` and child `c` in the block:
     - the edge `p–c` is removed, and  
     - edges `p -> Lk` and `Lk -> c` are added.  
   - DM-FCIT then calls `FciOrient` to re-apply FCI orientation rules (R0, R4, etc.) and maintain a **legal PAG** after inserting the latent.  
   - The corresponding parent–child links are removed from `potentiallyDirected` so they are not re-used.

7. **Latent–latent edges.**  
   As in DM-PC, latent–latent edges are added based on subset inclusion of the parent sets:
   - If parent set A contains parent set B, then `latent(B) -> latent(A)` is added, provided it does not create a directed cycle.

8. **Layout.**  
   Latent nodes are repositioned for visualization (`LayoutUtil.repositionLatents`), but this does not affect the semantics.

The output is a **PAG with latent nodes** explicitly inserted where FCIT’s oriented structure and the independence tests jointly support an intermediate latent explanation.

---

### When to use DM-FCIT

DM-FCIT is appropriate when:

- You want a **PAG-based** DM method that respects the full FCI/FCIT orientation logic.  
- You care about **maximally preserving PAG legality**, including latent confounding and partial orientation.  
- You want the latent detection step to use **small conditioning sets** based on Recursive Blocking rather than brute-force search over large sets.

It is especially natural in hybrid score–test workflows where you are already using FCIT.

---

### Prior knowledge

DM-FCIT uses the same `Knowledge` mechanism as FCIT:

- Knowledge is passed into FCIT and influences the initial PAG.  
- The DM step always operates on that knowledge-respecting PAG.

---

### Parameters (DM-FCIT)

DM-FCIT itself does not add new GUI parameters beyond those of FCIT and the underlying test/score. The algorithm’s `getParameters()` includes:

**BOSS / FCIT search behavior**

| Parameter              | Meaning                                                 |
|------------------------|---------------------------------------------------------|
| `USE_BES`              | Use BOSS edge swaps.                                   |
| `USE_DATA_ORDER`       | Whether to exploit data order in BOSS.                 |
| `NUM_STARTS`           | Number of random restarts for BOSS.                    |
| `FCIT_STARTS_WITH`     | Start with BOSS, GRaSP, or SP.                         |
| `GRASP_DEPTH`          | Depth for GRaSP when used.                             |
| `GUARANTEE_PAG`        | Enforce PAG legality in FCIT output.                   |
| `PRESERVE_MARKOV`      | Preserve Markov equivalence when possible.             |

**General**

| Parameter         | Meaning                                      |
|-------------------|----------------------------------------------|
| `TIME_LAG`        | Number of lags for time-series expansion.    |
| `VERBOSE`         | Print detailed search and DM diagnostics.    |
| `TEST_TIMEOUT`    | Timeout for expensive independence tests.    |

Plus all parameters of the **independence test** and **score** you choose via the wrappers.

---

### Summary: DM-PC vs DM-FCIT

- **DM-PC**  
  - Simpler, PC-based.  
  - Works on a CPDAG-like pattern.  
  - Infers inputs/outputs from depth-0 PC and builds a latent layer on top.  
  - Good as a lightweight MIMIC-style latent detector.

- **DM-FCIT**  
  - Built on FCIT and PAGs.  
  - Uses Recursive Blocking to keep conditioning sets small.  
  - Maintains PAG legality throughout.  
  - Better suited when you are already in the FCI/FCIT world and want a principled intermediate-latent extension.
