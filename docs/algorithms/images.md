# IMaGES — Pooled Multi-Dataset Scoring

**Type:** Scoring mode, not a separate algorithm  
**Output:** Same graph class as the algorithm you pool (CPDAG for BOSS or FGES, and so on)

IMaGES is no longer a separate entry in Tetrad's algorithm list. It is now a parameter,
`poolDataSets`, which any score-based or test-based algorithm can use. Running BOSS with a
pooled score **is** IMaGES with that score, and the same idea extends to tests: running PC with
a pooled test is a pooled PC.

If you are looking for the old **IMaGES**, **IMaGES-BOSS** or **IMaGES-FGES** entries, this is
where they went. Nothing was lost; the capability was generalized so that it works with any
score rather than only with the one IMaGES shipped with.

## How to use it

1. Supply more than one dataset, measured on the same variables. One dataset is not enough, and
   with a single dataset the option has no effect.
2. Choose a score-based or test-based algorithm — BOSS, FGES, GRaSP, PC, FCI and the like.
3. Set `poolDataSets` to Yes in the algorithm's parameter panel.

The algorithm then runs **once**, with its score replaced by a single score formed from the
per-dataset scores, and its independence test, if it uses one, replaced by the Fisher
combination of the per-dataset p-values. With the option off, which is the default, the
algorithm runs separately on each dataset and you get one graph per dataset.

Not every algorithm can pool. Tetrad requires one that takes a score or a test, and it reports
an error naming the option if you ask an algorithm that cannot.

## What the pooled score is

By default the pooled score is an equally weighted average of the per-dataset scores, so each
sample counts equally and a dataset influences the result in proportion to its sample size. An
alternative weighting rescales each dataset's contribution so that its vote does not depend on
its sample size.

## When pooling is the right choice

Pooling suits data that were collected in separate batches but are believed to share one causal
structure:

- fMRI data from several subjects performing the same task
- multi-site or multi-scanner studies
- repeated measurements, sessions, or regions
- several small datasets that you do not want to concatenate

Concatenating such datasets instead would mix their means and variances and can create
associations that exist in no single dataset. Pooling the score avoids that.

## Assumptions and limits

- The datasets share one causal structure. If their mechanisms differ in ways you care about,
  pool nothing and compare the separate graphs instead.
- The datasets are independent of one another.
- Pooling does not address latent confounding. For that, pool a latent-variable algorithm such
  as GFCI, BFCI or FCIT rather than a CPDAG search.
- Time lags are applied to each dataset separately before pooling.
- Bootstrapping resamples rows within each dataset.

## Prior knowledge

Background knowledge is honored. Connect a Knowledge box, or supply a `Knowledge` object from
Java, py-tetrad or rpy-tetrad, and the constraints are applied to every scoring step, so the
pooled score respects them across all datasets. If no Knowledge box is connected, Tetrad will
use knowledge carried on the first dataset.

## Reference

Ramsey, J. D., Hanson, S. J., & Glymour, C. (2011).
**Multi-subject search correctly identifies causal connections and most causal directions in the
DCM models of the Smith et al. simulation study.**
*NeuroImage*, 58(3), 838–848.

## Summary

**IMaGES = any score-based or test-based algorithm + `poolDataSets`.** Set the parameter rather
than looking for an algorithm by that name.
