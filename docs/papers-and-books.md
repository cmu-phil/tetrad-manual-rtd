# References

This page collects key references for the theory and algorithms implemented in **Tetrad**.  
It is not exhaustive, but covers some foundational papers, major algorithmic developments,
and software-related publications most relevant to users and developers.

The historical narrative of Tetrad is available on the project website:  
https://www.cmu.edu/dietrich/philosophy/tetrad/about/

This is a first draft; we'll expand this list as time permits. Please submit missing papers if you note them.

---

## 1. Foundational Book

- **Spirtes, P., Glymour, C., & Scheines, R.** (2000).  
  *Causation, Prediction, and Search.* MIT Press.  
  *(The canonical reference for the Tetrad project, covering the unified theory behind PC, FCI, DAGs, MAGs, PAGs, independence tests, and causal inference with latent variables.)*

---

## 2. Constraint-Based Algorithms (PC, FCI, RFCI, variations)

### PC / PC-Stable / Variants
- **Spirtes, P., & Glymour, C.** (1991).  
  “An Algorithm for Fast Recovery of Sparse Causal Graphs.” *Social Science Computer Review*.

- **Colombo, D., & Maathuis, M.** (2014).  
  “Order-Independent Constraint-Based Causal Structure Learning.” *Journal of Machine Learning Research*.

### FCI / RFCI / GFCI
- **Spirtes, P., Richardson, T., Meek, C.** (1995; 2000).  
  FCI algorithm; see CPS (2000).

- **Zhang, J.** (2008).  
  “On the completeness of orientation rules for PAGs.” *UAI.*

- **Colombo, D., Maathuis, M., Kalisch, M., & Richardson, T.** (2012).  
  “Learning high-dimensional DAGs with latent and selection variables.” *Annals of Statistics.* (RFCI)

- **Ogarrio, J. M., Spirtes, P., & Ramsey, J.** (2016).  
  “A Hybrid Causal Search Algorithm for Latent Variable Models.” *JMLR: Workshop & Conf. Proc.* (GFCI)

---

## 3. Score-Based Algorithms (GES, FGES, BOSS, GRaSP, hybrids)

### GES / FGES
- **Chickering, D. M.** (2002).  
  “Optimal Structure Identification with Greedy Search.” *JMLR.*

- **Ramsey, J., Glymour, C., Sanchez-Romero, R., & Glymour, M.** (2017).  
  “A Million Variables and More.” *arXiv:1507.07004.* (FGES)

### BOSS
- **Ramsey, J., & Sanchez-Romero, R.** (2022–2024).  
  “BOSS: Best-Order Score Search.” (Tech reports / in-prep papers; implementation in Tetrad.)

### GRaSP
- **Huang, B., Zhang, K., & Schölkopf, B.** (2018).  
  “Generalized Score Functions for Causal Discovery.” (GRaSP-inspired; current implementation by Ramsey.)

---

## 4. Hybrid Algorithms (GFCI family, BOSS-FCI, FCIT)

- **Ogarrio, J. M., Spirtes, P., & Ramsey, J.** (2016). (GFCI)
- **Ramsey, J., et al.** (2023–2025).  
  “BOSS-FCI & GRaSP-FCI: Hybrid Score-Guided FCI Algorithms.” (Tetrad technical documentation)
- **Ramsey, J.** (2024–2025).  
  “FCIT: Fast Causal Inference with Targeted Testing.” (Working paper)

---

## 5. Adjustment Sets & Causal Effect Estimation

### Adjustment Theory (Backdoor, Frontdoor, GAC)
- **Pearl, J.** (1995, 2009).  
  Identifiability conditions.

- **Perković, E., Kalisch, M., Maathuis, M., & Bühlmann, P.** (2018).  
  “A Complete Characterization of Adjustment in Graphical Models.” *AOS.* (GAC)

### IDA & Extensions
- **Maathuis, M. H., Colombo, D., Kalisch, M., & Bühlmann, P.** (2009).  
  “Estimating High-Dimensional Intervention Effects from Observational Data.” *Annals of Statistics.* (IDA)

- **Malinsky, D., & Spirtes, P.** (2019).  
  “Estimating total effects in the presence of latent confounding in linear models.” (PAG-IDA foundations)

- **Witte, J., et al.** (2020–2024).  
  Optimal IDA and refinements for partial graph structures.

### Recursive Adjustment / Conditional Adjustment
- **LaPlante, L., & Perković, E.** (2024).  
  “Conditional Adjustment Sets.” (theory underlying RA-extensions)

[//]: # (- **Ramsey, J.** &#40;2023–2025&#41;.  )

[//]: # (  “Recursive Adjustment for Effect Estimation.” &#40;Tetrad implementation & upcoming paper&#41;)

---

## 6. Ancestral Graphs, MAGs, PAGs

- **Richardson, T., & Spirtes, P.** (2002).  
  “Ancestral Graph Markov Models.” *Annals of Statistics.*

- **Zhang, J.** (2006–2008).  
  Soundness and completeness of PAG orientation rules.

[//]: # (- **Mooij, J., & Janzing, D.** &#40;2009&#41;.  )

[//]: # (  Related MAG semantics.)

---

## 7. Nonlinear & Non-Gaussian Methods

- **Hoyer, P., Shimizu, S., et al.** (2008).  
  “LiNGAM.” (Non-Gaussian linear additive methods.)

- **Peters, J., Mooij, J., Janzing, D., & Schölkopf, B.** (2014).  
  “ANM: Causal inference with additive noise models.”

- **Ramsey, J., et al.** (2023–2025).  
  Basis-function scoring (BF-BIC), BF-LRT, nonlinear CI approximations.  
  (Ongoing Tetrad papers.)

---

## 8. Independence Tests & Scores

- **Fisher’s Z Test** (classical)
- **Kernel Conditional Independence (KCI)** — Zhang, Peters, et al. (2011–2014)
- **RCIT / RCoT** — Strobl, Zhang, et al. (2019)
- **G^2, χ², BIC, BDeu** — classical discrete/continuous tests
- **BF-BIC / BF-LRT** — Ramsey (2023–2025)

---

## 9. Software Papers

- **Ramsey, J., & Andrews, B.** (2023).  
  *Py-Tetrad and RPy-Tetrad: A New Python Interface with R Support for Tetrad Causal Search.*  
  In Proceedings of the **Causal Analysis Workshop Series** (CAWS), PMLR.

[//]: # (- **Ramsey et al.** &#40;various&#41;.  )

[//]: # (  Tetrad GUI and library updates &#40;FGES, GFCI, BOSS, RA modules&#41;.)

---

## 10. Additional Topics & Related Literature

### Selection Bias
- **Spirtes, P.** (1995–2000). Selection in FCI framework.
- **Bareinboim, E., Tian, J., & Pearl, J.** (2014–2020). Transport and selection diagrams.

### Latent Variables
- **Silva, R., & Scheines, R.** (2005).
- **Hoyer, P., et al.** (latent nonlinear models)

### Graph Theory and Orientation Rules
- **Meek, C.** (1995).  
  “Causal inference and causal explanation with background knowledge.”  
  Core orientation rules used in CPDAG construction.