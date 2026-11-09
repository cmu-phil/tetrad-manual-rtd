# Trek-MIMIC

**Command:** `trek-mimic`  
**Kind:** Algorithm

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: trek-mimic -->

Implements the Trek-MIMIC algorithm for recovering latent structure from measured data, including both the latent-latent skeleton and the measured parents (inputs) of each latent variable. The algorithm proceeds in five stages: Measurement model construction. TSC (Trek Separation Clustering) is run to identify clusters of measured indicators and assign each cluster to a latent variable, yielding a block specification with per-latent ranks. PC with a trek/block independence test is then run to produce an initial latent-indicator graph. Measured parent recovery. Rank-one clique groups are identified among a pool of candidate measured variables. Each group is assigned to the latent it best explains (by block strength), and directed edges from those measured parents into the latent are added to the graph. Higher-rank expansion (optional). Candidate measured variables not yet assigned as parents are tested individually and in pairs against subsets of latents. A candidate is added as a shared parent of a latent subset when it satisfies a trek-rank condition (contributing missing channels to the joint parent set) and an explanatory condition (its presence reduces the cross-indicator rank for at least one adjacent latent pair). Transitive input edges introduced during this phase are subsequently pruned. Latent-latent edge pruning. Edges between latents that are explained by recovered measured parents — as evidenced by conditional rank dropping to zero — are removed. Orientation and final pruning (optional). Remaining latent-latent edges are oriented using parent/child correlations, and any latent-transitive edges that become non-identifiable are removed, leaving the final graph.

<!-- END GENERATED: trek-mimic -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
