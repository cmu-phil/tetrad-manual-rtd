## SingleGraphAlg (Imported Graph Wrapper)

**SingleGraphAlg** is *not* a causal discovery algorithm in the usual sense.  
Instead, it is a thin wrapper that lets you treat a **fixed, user-supplied graph** as if it were the output of a Tetrad algorithm.

This is useful when:

- You have already run a causal discovery method **outside Tetrad** (e.g., in R, Python, or another tool) and want to:
    - Compare that graph to Tetrad’s algorithms in the **Simulation / Algorithm Comparison** workflow, or
    - Use it as a “baseline” or reference graph in performance tables.
- You have constructed a graph **by hand** (e.g., from domain knowledge or a published model) and want it to appear in the same tables/plots as algorithm outputs.
- You want to include a **“gold standard” graph** in evaluations, but that gold standard lives in a file.

---

### What it does

- You load a graph from a file in one of Tetrad’s supported graph formats.
- SingleGraphAlg simply **returns that graph unchanged** as its “search result.”
- From the rest of Tetrad’s perspective, this looks just like the output of any other algorithm:
    - It can be included in **graph comparison tables** (adjacency/arrowhead/tail metrics, etc.).
    - It can be visualized, saved, and used in downstream workflows that expect an algorithm-produced graph.

Crucially:

- **No data are used.** SingleGraphAlg completely ignores the input dataset.
- **No edges are added, removed, or reoriented.** The imported graph is taken as-is.

---

### Typical workflow

1. **Create or learn a graph outside Tetrad**, then export it to one of Tetrad’s supported text graph formats (see *Graph Formats*).
2. In Tetrad, select **SingleGraphAlg** as one of the algorithms in your comparison.
3. Use the algorithm’s configuration to **point it at your graph file**.
4. Run the comparison as usual:
    - SingleGraphAlg will contribute exactly the imported graph.
    - Other algorithms will learn graphs from the data.
    - All graphs appear side by side in the evaluation tables and plots.

---

### When to use (and when not to)

Use SingleGraphAlg when:

- You want an **external** or **hand-built** graph to participate in Tetrad’s evaluation and visualization pipeline.
- You are doing **benchmarking** and want to include:
    - A model from another package (e.g., dagitty, pcalg, bnlearn, custom code), or
    - A known “true” graph stored on disk.

Do *not* use SingleGraphAlg if:

- You actually want Tetrad to **learn** a graph from data—choose PC, FGES, GFCI, FCIT, BOSS, etc. instead.
- You expect it to **modify** or **repair** the imported graph. It will not; it trusts the file as given.