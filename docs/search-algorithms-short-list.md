# Choosing an Algorithm
*A curated guide to the algorithms most Tetrad users should start with.*

Tetrad provides many structure-learning algorithms. This short list highlights the **most recommended** ones, with crisp summaries and links to full per-algorithm pages.

If you're new to Tetrad, start here.

---

## 🔍 Choosing an Algorithm

Most users choose between:

- **DAG/CPDAG algorithms** (assume *no hidden confounders*)
- **PAG algorithms** (allow *hidden confounders* and *selection bias*)

A quick rule of thumb:

- **No hidden confounders** → Use **DAG/CPDAG** methods  
  (FGES, BOSS, PC, PC-Max)

- **Hidden confounders possible** → Use **PAG** methods  
  (FCI, GFCI, BFCI, FCIT)

---

## 🧭 Recommended Algorithms (At a Glance)

This section lists the top algorithms most users should consider first.

---

## 🔍 DAG / CPDAG Methods (No Latent Confounders)

**PC — Peter–Clark Algorithm**  
🔍 Constraint-based • 🎛️ α-controlled • Output: CPDAG  
Removes edges using CI tests and orients them using collider and propagation rules. A classic method offering explicit statistical control via α.  
→ Full page: [PC](algorithms/pc.md)

**PC-Max**  
🔍 Constraint-based • 🎛️ α-controlled • Output: CPDAG  
Variant of PC that selects separating sets with **maximum p-value**, improving orientation accuracy.  
→ Full page: [PC-Max](algorithms/pc.md)

---

**FGES — Fast Greedy Equivalence Search**  
📏 Score-based • ⚡ Highly scalable • Output: CPDAG  
Greedy forward–backward search optimizing BIC. Very fast and scalable; a strong general-purpose default.  
→ Full page: [FGES](algorithms/fges.md)

**BOSS — Best Order Score Search**  
📏 Score-based • 🎯 Order-based • Output: CPDAG  
Searches over variable orders and uses Grow–Shrink Trees to score efficiently; often produces sharper orientations than FGES.  
→ Full page: [BOSS](algorithms/boss.md)

---

## 🌀 PAG Methods (Hidden Confounders Allowed)

**FCI — Fast Causal Inference**  
🔍 Constraint-based • 🧩 Latent-capable • Output: PAG  
Extends PC with additional pruning and orientation rules (R0–R10) to represent latent confounding and selection bias correctly. The canonical PAG discovery algorithm.  
→ Full page: [FCI](algorithms/fci.md)

**GFCI — Greedy Fast Causal Inference**  
🌀 Hybrid • 🧩 Latent-capable • Output: PAG  
Uses FGES to obtain a CPDAG, then upgrades it to a PAG via FCI-style pruning/orientation. Parent design for newer hybrids.  
→ Full page: [GFCI](algorithms/gfci.md)

**BFCI**  
🌀 Hybrid • 🧩 Latent-capable • Output: PAG  
Replaces FGES with BOSS, producing a sharper starting point and improved pruning/orientation accuracy. Excellent general-purpose PAG learner.  
→ Full page: [BFCI](algorithms/bfci.md)

**FCIT — FCI with Targeted Testing**  
🌀 Hybrid • 🧩 Latent-capable • 🎯 Targeted CI tests • Output: PAG  
Uses score-guided selective testing to avoid low-value CI tests, improving stability and accuracy while guaranteeing a **legal PAG**. Often outperforms both FCI and GFCI.  
→ Full page: [FCIT](algorithms/fcit.md)

---

## 🔧 Other Useful Algorithm Classes

Several other methods specialize in:

- **Orientation only** (FASK, LOFS, skew-based methods)
- **Non-Gaussian structure** (LiNGAM, ICA-based models)
- **Time-series** (PCMCI)
- **Markov blankets**
- **Deterministic relations**

These are powerful in the right contexts but are not typical starting points.

→ See full catalog: **[Full Algorithm List](search-algorithms-full-list.md)**

---

## 🎛 Choosing CI Tests & Scores (Quick Guide)

- **Continuous (Gaussian-ish):** Fisher Z, SEM-BIC
- **Discrete:** G-test or Chi-square; BDeu/BIC
- **Mixed or nonlinear:** KCI / RCIT (slower), basis-function methods (scalable)
- **Covariance-only datasets:** Use methods accepting covariance matrices (e.g., BOSS, FGES)

---

## ⚠️ Common Pitfalls and Fixes

- **Graph too dense:** lower α (PC/FCI) or increase penalty (FGES/BOSS)
- **Graph too sparse:** raise α or decrease penalty
- **Odd orientations:** try PC-Max, BOSS, or minimal prior knowledge
- **Slow runtime:** limit depth; use RFCI or FCIT; increase threads