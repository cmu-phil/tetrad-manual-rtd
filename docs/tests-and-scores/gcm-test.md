# GCM (Generalized Covariance Measure)

**Command:** `gcm-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: gcm-test -->

Generalized Covariance Measure (GCM) conditional independence test. Tests conditional independence of X and Y given Z by measuring residual dependence after regressing out the effect of Z from each variable. The test follows the generalized covariance framework of Shah and Peters and is suitable for nonlinear regression models when good predictors of conditional means are available. Test construction. To test X ⟂⟂ Y \| Z: Fit regression models x̂(Z) ≈ E\[X \| Z\] and ŷ(Z) ≈ E\[Y \| Z\]. Compute residuals rX = X − x̂(Z) and rY = Y − ŷ(Z). Form the elementwise product u = rX · rY. Compute the test statistic T = sqrt(n) · mean(u) / sd(u), which is asymptotically standard normal under the null hypothesis, given mild regularity conditions. Interpretation. Under X ⟂⟂ Y \| Z, the residuals rX and rY are uncorrelated, so E\[rX · rY\] = 0. Systematic deviation from zero indicates conditional dependence. Regression models. The power and validity of the test depend critically on the quality of the regressors used to approximate E\[X \| Z\] and E\[Y \| Z\]. In this implementation, regression options include linear and nonlinear models (e.g., ridge regression with random Fourier features). Practical considerations. The test is only as reliable as the underlying regression fits. Performance in causal search depends strongly on caching: residuals should be cached by (target, conditioning set Z, rows) to avoid repeated regression during search. The test is fast and scalable when regressions are reused, making it suitable for constraint-based structure learning. Intended use. GCM is well-suited for conditional independence testing in nonlinear settings when approximate conditional mean models are available, and serves as a computationally efficient alternative to fully nonparametric kernel-based tests.

<!-- END GENERATED: gcm-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
