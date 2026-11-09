# Skew

**Command:** `skew`  
**Kind:** Algorithm

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: skew -->

This is an algorithm that orients an edge X--Y for continuous variables based on non-Gaussian information. This rule in particular uses a skewness to make the orientation. Note that if the variables X and Y are both Gaussian, and the model is linear, it is not possible to orient the edge X--Y pairwise; any attempt to do so would result in random orientation. But if X and Y are non-Gaussian, in particular in this case, if X and Y are skewed, the orientation is relatively straightforward. See Hyvarinen and Smith (2013) for details.

The Skew rule is differently motivated from the RSkew rule (see), though they both appeal to the skewness of the variables.

<!-- END GENERATED: skew -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
