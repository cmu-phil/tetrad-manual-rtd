# CD-NOD-BOSS

**Command:** `cd-nod-boss`  
**Kind:** Algorithm

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: cd-nod-boss -->

Implements a variant of the CD-NOD (Causal Discovery from Non-stationary/ heterogeneous Data) algorithm that uses BOSS (Best Order Score Search) for skeleton construction rather than FAS, combining score-based skeleton search with constraint-based collider orientation. Context variables are identified as all Tier-0 variables in the supplied Knowledge object. Any variable in Tier-0 that is also present in the dataset is treated as a context variable and is forced to be a cause of every adjacent non-context variable, reflecting the assumption that changing causal mechanisms are indexed by those context variables. The algorithm proceeds in four stages: BOSS skeleton search. BOSS is run using a SEM BIC score on the augmented dataset (X ∪ contexts), with knowledge extended to forbid all edges into context variables. The resulting CPDAG provides the initial skeleton and a set of sepsets, which are cached and supplemented by a recursive blocking heuristic and conditional independence fallback during collider orientation. Context forcing. For each context variable C and each adjacent non-context variable X, the undirected edge C --- X is replaced by the directed edge C → X, subject to any background knowledge constraints. Collider orientation. Unshielded triples are oriented as colliders or non-colliders using one of three strategies, selectable via CdnodBoss.ColliderOrientationStyle: SEPSETS: orients x → z ← y if z is not in the sepset of x and y (standard PC rule). CONSERVATIVE: orients a collider only if every sepset excludes z and no sepset includes z (Conservative PC rule). MAX\_P: selects the sepset with the highest p-value and uses it to decide orientation, with an optional tie-guard margin. Meek closure. Meek's orientation rules are applied to propagate implied orientations and complete the partially directed graph.

<!-- END GENERATED: cd-nod-boss -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
