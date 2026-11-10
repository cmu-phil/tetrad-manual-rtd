# Detail: Vertex Checker

```{figure} ../../_static/images/tetrad-interface/box-by-box/vertex-checker.png
:name: tetrad-vertex-checker-screenshot
:alt: Vertex Checker.

The Vertex Checker, with the first vertex selected.
```

The **Vertex Checker** takes the Markov check one step further. Where the
[Markov Checker](detail-markov-checker.md) tells you *whether* a graph is Markov to your data, the
Vertex Checker localizes the trouble to particular **vertices** and then offers to **repair** the
graph by searching for edge edits that reduce the violations.

It is the tool for the situation where a search has returned a graph that mostly looks right but
fails a Markov check, and you want to know which part of it is responsible.

Find it in a **Compare** box, under *Independence Facts Comparison*, as **Vertex Checker**.

## The two tabs

- **Check** — the per-vertex view of the Markov check. For each vertex, the independence facts the
  graph implies at that vertex are tested against the data, so you can see where the violations are
  concentrated rather than only how many there are in total.
- **Repair** — the local search described below.

## Repair

Repair is a **greedy local search over edge edits**, scored by the same Markov-check diagnostics
the Check tab reports. For the selected vertex it enumerates single-step edits — additions,
removals and reorientations — that are legal for the graph type you have chosen, applies the one
that most reduces the violations, and repeats.

This is a search, not a derivation. It finds a graph that fits the data better in the
Markov-check sense; it does not prove that graph is right, and a repair that removes violations by
removing information is always possible. Treat the result as a hypothesis to examine, and look at
what was changed rather than only at the improved score.

### Controls

**Graph type** — which class the repaired graph must stay in: **DAG**, **CPDAG**, **PDAG**,
**MAG** or **PAG**. This is not a display choice; it determines which edits are legal and how the
candidate is normalized afterwards. DAG and CPDAG assume causal sufficiency. MAG and PAG admit
latent confounders. CPDAG and PAG are canonicalized back to their class after every edit, so
non-compelled orientations may be rewritten; **PDAG** is the one that preserves orientations
exactly as edited, which is what you want if you are deliberately holding an orientation fixed.

**Node** — the vertex to work on. There are two buttons, each naming the selected node: one
searches for candidate adjustments at that vertex, and one **repairs that vertex only**. On a large
graph, repairing a single vertex of interest is much faster than a whole-graph sweep and is often
all you want.

**Attempt Repair** runs the full repair.

**Strategy** — **Local sweep** goes node by node, repeating the sweep until nothing improves.
**Global queue** keeps a priority queue across all vertices and always applies the best candidate
available anywhere next. Global queue generally reaches a better graph; local sweep is easier to
follow, since it works through the vertices in order.

**Prune alpha** — the significance level for the independence tests that score candidates. As
everywhere, a smaller alpha means fewer rejections, so fewer violations to repair and a more
conservative repair.

**Seed** — the search makes arbitrary choices among ties, so it is seeded for reproducibility.
Change the seed and repeat if you want to know whether a particular repair is stable or an artifact
of tie-breaking.

**Undo** steps back through applied edits, and **Graph** shows the current working graph. A long
run can be stopped with **Cancel**, which may take a moment, since it stops between tests.

## Two things worth knowing about the search

**Candidate scoring for PAGs is done in two passes, and this does not affect what gets applied.**
For PAG repair under the ordered-local-Markov conditioning types, candidates are first *screened*
cheaply — projected only as far as the implied MAG, with violations counted there — and the
expensive full canonicalization is skipped for candidates that are merely being ranked. Because all
MAGs in one equivalence class imply the same independence facts, screening is sound for ranking;
but the screening graph is generally not the canonical member of its class, so screening counts can
differ slightly from fully canonical ones. The consequence is confined to the **order** in which
candidates are tried. Every edit that is actually applied is re-scored on its fully canonicalized,
knowledge-refined graph first, and must beat a fresh no-op on those exact scores, so the
approximation cannot reach the working graph.

**Candidate enumeration is capped.** For the DAG, CPDAG and PDAG types the search also enumerates
multi-edge orientation patterns around a vertex, and that enumeration is bounded. A vertex with
more free edges than the cap allows falls back to a smaller set of pattern moves, so the search is
less thorough there. As with the determinism searches in the [Data Audit](../data-preparation/data-audit.md),
the absence of a proposed repair at a high-degree vertex does not mean none exists.

## Related pages

- [Markov Checker](detail-markov-checker.md) — the whole-graph version of the check.
- [Compare Box](../box-by-box/compare-box.md) — the box this tool lives in.
- [Markov Checking](../../workflows/markov-checking.md) — the workflow this fits into.
