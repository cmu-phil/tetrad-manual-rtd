# ION

**Command:** `ion`  
**Kind:** Algorithm

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: ion -->

Runs the ION (Integration of Overlapping Networks) algorithm on multiple datasets whose variable sets may overlap only partially. BFCI is run separately on each dataset using the chosen independence test and score, and the resulting PAGs are integrated by ION into a set of PAGs over the union of the variables that are consistent with every input PAG. BFCI is used for the per-dataset searches, rather than FCI, because ION requires that its inputs be legal PAGs, and FCI is not guaranteed to produce a legal PAG, whereas BFCI is designed to. For oracle experiments the analogous choice is GRaSP-FCI with the m-separation test and score. Since this interface returns a single graph, the graph with the fewest edges is returned, and the full set of graphs is printed to the log. If the input PAGs are jointly inconsistent (which can happen when they are estimated from finite samples of different datasets), ION may return no graphs at all; in that case an edgeless graph over the union of the variables is returned and a warning is logged. Note that ION is exponential in the number of variables and is intended for problems with a small number of variables. The reference is here: Danks, D., Glymour, C., & Tillman, R. E. (2008). Integrating locally learned causal structures with overlapping variables. In Advances in Neural Information Processing Systems 21 (NIPS 2008), pp. 1665-1672.

<!-- END GENERATED: ion -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
