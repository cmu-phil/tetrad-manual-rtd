# Detail: Graph Menu (Graph Box)

The **Graph** menu in the **Graph box** provides tools for **analyzing and manipulating graphs you already
have**. It is especially useful for **large graphs**, where structural properties and admissible paths are not
immediately obvious from the visual layout.

From a Graph box, open the **Graph** menu in the menubar to access the commands below.

```{figure} ../../_static/images/tetrad-interface/box-by-box/graph-menu.png
:name: tetrad-graph-menu-screenshot
:alt: Graph Menu

Graph Menu
```

## Random Graph

**Graph → Random Graph**

Creates a **new random graph** directly in the current Graph box. You can choose among several random-graph
generators, typically including:

- **DAG** – random directed acyclic graph with user-specified parameters such as:
    - Number of measured nodes,
    - Number of additional latent confounders,
    - Number of edges,
    - Maximum indegree, outdegree, and total degree,
    - Whether the graph should be connected.
- **MIM** – random **Multiple Indicator Model**, with latent variables and measured indicators.
- **Scale Free** – random **scale-free graph** with a heavy-tailed degree distribution.

After choosing a generator, you can edit its parameters in a dialog; clicking **Done** replaces the current graph
with a newly generated one.

## Graph Properties

**Graph → Graph Properties**

Displays a summary of **graph statistics**, including for example:

- Number of nodes (and number of latent nodes),
- Number of edges and adjacencies,
- Number of two-cycles,
- Number of directed, bidirected, and undirected edges,
- Maximum indegree, maximum outdegree, and maximum degree,
- Average degree and density,
- Whether the graph is acyclic.

This is a convenient way to check basic properties of a large graph at a glance.

## Underlinings

**Graph → Underlinings**

Shows any **underlinings** produced by certain algorithms (for example, CCD or CPC), which mark special
edge patterns or decisions. If the current graph contains underlinings, they are listed here for inspection.

## Paths

**Graph → Paths**

Opens the **Paths** dialog, which lets you list various **paths and path-based sets** between a chosen
pair of nodes (From, To), optionally conditioned on a set of variables. A drop-down menu lets you select
what to list:

- **Directed Paths** – directed paths from the source to the target.
- **Semidirected Paths** – paths that are directed “forward” apart from possible undirected edges.
- **Treks** – paths without colliders.
- **Confounder Paths** – paths reflecting common causes between variables.
- **Latent Confounder Paths** – paths where confounding is due to latent variables.
- **Cycles** – cyclic paths.
- **All Paths** – all (simple) paths between the chosen nodes.
- **Adjacents** – nodes adjacent to the chosen node(s).
- **Adjustment Sets (for Total Effect)** – sets of variables that qualify as adjustment sets for the total
  effect from X to Y.
- **Direct-Effect Adjustment Sets (Edge-Specific)** – edge-specific adjustment sets for direct effects.
- **Amenable paths** – semidirected paths from X to Y that start with a visible edge out of X; an adjustment
  set should not block any of these paths.
- **Backdoor paths** – non-causal (backdoor) paths from X to Y that should be blocked by an adjustment set.

This tool is central for understanding causal paths and potential adjustment sets in complex graphs.

## Highlight

**Graph → Highlight**

Highlights particular **structures or edge types** in the current graph, such as:

- Directed, bidirected, undirected, partially oriented, or non-directed edges,
- Triangles and maximal cliques,
- Cycles and “almost cyclic” paths,
- Latent nodes or measured nodes.

Highlighting is especially useful for spotting patterns that are hard to see visually in large graphs.

## Check Graph Type

**Graph → Check Graph Type**

Tests whether the current graph satisfies the conditions for one of several standard graph classes:

- DAG (directed acyclic graph),
- CPDAG (completed partially directed acyclic graph),
- PDAG (partially directed acyclic graph),
- MAG (maximal ancestral graph),
- PAG (partial ancestral graph).

Choosing an option runs the check and reports whether the current graph qualifies. This is helpful when
you have manipulated a graph and want to confirm that it is still a valid member of a particular class.

## Manipulate Graph

**Graph → Manipulate Graph**

Provides tools to **transform the current graph** while staying within a particular equivalence class or
graph type. Options include, for example:

- For CPDAGs:
    - Revert to unshielded colliders,
    - Apply Meek rules,
    - Revert to CPDAG,
    - Pick a random DAG in the CPDAG.
- For PAGs:
    - Revert to unshielded colliders in a PAG,
    - Apply the final FCI rules,
    - Revert to PAG,
    - Pick a Zhang MAG represented by the PAG.
- Additional utilities:
    - Correlate exogenous variables,
    - Uncorrelate exogenous variables.

These operations are useful for exploring particular members of an equivalence class or enforcing
standard orientation rules.

## PAG Edge Specialization Markups

**Graph → PAG Edge Specialization Markups**

Adds or removes **PAG edge specialization markups** for PAGs and provides help on how to interpret them:

- **Add/Remove PAG Specialization Markups** – toggles specialized edge markings that encode additional
  information about possible underlying MAGs.
- **PAG Edge Type Instructions** – opens a short help dialog explaining the meaning of these specialized
  PAG edge types.

This menu is mainly used when working with PAGs and their refinements, for more detailed causal interpretation.

## Summary

The **Graph** menu turns the Graph box into a powerful **graph analysis workbench**, letting you:

- Generate random graphs for experiments or teaching,
- Inspect structural statistics,
- Explore all relevant causal paths and adjustment sets,
- Highlight complex substructures,
- Check and manipulate graph types,
- And work with specialized PAG annotations.

It is particularly valuable when working with **large or intricate graphs** where visual inspection alone
is not sufficient.