# Blocks-Test-TS (Trek separation)

**Command:** `blocks-test-ts`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: blocks-test-ts -->

Blocks-Test-TS is the trek-separation block independence test (TSBI, see) in the form used by block searches: it takes a block specification (a clustering of the measured variables into pure clusters, one latent per cluster, with a rank for each block) from a connected clustering result, and tests independence between the latents behind two blocks given the latents behind a set of conditioning blocks. Each conditioning block is split into two halves; the rank of the cross-covariance between the left side (X plus one half of each conditioning block) and the right side (Y plus the other halves) is estimated by a Wilks rank test, and independence is declared when that rank equals the sum of the conditioning blocks' ranks, as trek separation implies under a linear measurement model.

See Sullivant, S., Talaska, K., & Draisma, J. (2010). Trek separation for Gaussian graphical models. Annals of Statistics, 38(3), 1665-1685. This wrapper is only offered when the search box is connected to a clustering result; for the plain covariance form use TSBI.

<!-- END GENERATED: blocks-test-ts -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
