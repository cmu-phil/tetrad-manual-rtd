# Instance-specific BDeu Score

**Command:** `is-bdeu-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: is-bdeu-score -->

The instance-specific BDeu score augments the BDeu score (see) with a term rewarding structures that predict a particular instance well, so that the learned structure is tailored to that instance rather than to the population alone. The local score is IS(i \| Pa) = BDeu(i \| Pa) + alpha log P(instance), where log P(instance) is the Dirichlet-multinomial posterior predictive probability of the instance's value of variable i given its parent configuration, (N\_ijk + ESS/(r\_i q)) / (N\_ij + ESS/q), and alpha (instanceSpecificAlpha) weights the instance term. A missing value in the instance for the variable or any parent contributes zero. The instance is a row of a testing data set (instanceRow), matched to the training variables by name with category indices remapped if the label orders differ.

See Jabbari, F., Visweswaran, S., & Cooper, G. F. (2018). Instance-specific Bayesian network structure learning. Proceedings of Machine Learning Research, 72 (PGM 2018). Discrete data.

<!-- END GENERATED: is-bdeu-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
