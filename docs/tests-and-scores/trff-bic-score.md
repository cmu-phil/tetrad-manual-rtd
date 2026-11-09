# TRFF BIC Score

**Command:** `trff-bic-score`  
**Kind:** Score

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: trff-bic-score -->

TRFF BIC score (mixed) Local Bayesian Information Criterion (BIC)–style score for structure learning with mixed continuous and discrete variables. The score combines nonlinear mean modeling via Random Fourier Features (RFF) with Student-t likelihoods for robustness to heavy-tailed residuals, while remaining computationally stable and fully local. Local conditional models. For each candidate parent set Pa(Y), the conditional distribution of Y is modeled as: Continuous child Y: Student-t location model of the form Y = f(Pa) + ε. Continuous parents enter through RFF; discrete parents enter via one-hot encoding. Parameters are estimated by iteratively reweighted ridge regression (IRLS), yielding robustness to heavy-tailed residuals. Discrete child Y: Multinomial logistic (softmax) regression with ridge regularization. Continuous parents are represented via RFF; discrete parents via one-hot encoding. Fitting is performed using IRLS. Score definition. The local score takes a generalized BIC form score(Y \| Pa(Y)) = logLik\_hat − 0.5 · edf · log(n), where logLik\_hat is the maximized penalized log-likelihood, n is the effective sample size for the local family, and edf is the ridge-based effective degrees of freedom. For multinomial logistic models, the effective degrees of freedom are approximated by summing the ridge edf contributions of the K − 1 one-vs-reference logistic blocks using the final IRLS weights. Student-t robustness. The Student-t likelihood induces residual-dependent reweighting that downweights extreme observations, reducing sensitivity to outliers relative to Gaussian BIC variants while preserving a location-model structure. Missing data handling. Rows with missing values in the local family \{Y\} ∪ Pa(Y) are excluded on a per-score basis (testwise deletion). Intended use. Intended for robust causal structure learning in mixed-type data when nonlinear mean effects are expected and residual distributions may be heavy-tailed.

<!-- END GENERATED: trff-bic-score -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
