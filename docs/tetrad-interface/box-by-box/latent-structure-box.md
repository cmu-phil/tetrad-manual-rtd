# Latent Structure Box (removed)

**The Latent Structure box no longer exists.** Its button was taken off the workbench palette in
October 2026, and every search it used to offer now lives in the **Search** box. This page is kept
because sessions saved before the change still contain Latent Structure boxes, and you may meet one
when you open an old session.

## Where its searches went

All search algorithms are in the **Search** box, with no separate box for latent-variable methods.
How you run one depends on what it needs:

- **Searches that take data alone** — including the latent-variable searches that produce PAGs, and
  methods such as RLCD and Factor Analysis — are in the Search box, selected like any other
  algorithm. Connect a Data box, and optionally a Knowledge box.
- **Block-based searches**, which work from clusters of indicators rather than from the raw
  variables, are a **Search box with a [Latent Clusters](latent-clusters-box.md) box as its
  parent**. Discover the clusters in the Latent Clusters box, draw an arrow from it into a Search
  box, and the block-based searches become available there.

So the two-step pattern the old box supported is unchanged; it is just assembled from the Latent
Clusters box and the Search box instead of from a box of its own.

## Opening an older session

A session saved with a Latent Structure box still loads, and the box still runs. The session node
was deliberately kept in Tetrad's configuration for that reason. Nothing is lost, and you do not
have to rebuild an old session to use it.

If you are revising such a session, the equivalent arrangement in the current interface is a Search
box, with a Latent Clusters box as its parent when the algorithm is block-based.

## Related pages

- [Search Box](search-box.md) — where all searches now live.
- [Latent Clusters Box](latent-clusters-box.md) — discovers the clusters that block-based searches
  take as input.
