# m-Separation Score

## Summary

The m-Separation Score evaluates a candidate graph by comparing its implied
**m-separation relations** to a target set of (in)dependence relations. It is
primarily used in oracle or simulation settings where the true m-separations
are known.

## When to use

- You have a known set of ground-truth independences (for example, from a true
  graph) and want to score candidate graphs.
- You are evaluating or comparing algorithms under a fixed independence
  oracle.
- You want a structural score that does not depend directly on data.

## Model class

- Graphical models represented as DAGs, MAGs, or PAGs, evaluated via m-
  separation.

## Score form (conceptual)

The score typically rewards graphs whose m-separation relations match those of
the oracle and penalizes mismatches (false independences or false
dependencies).

## Parameters in Tetrad

No parameters.

## Strengths

- Clean separation of structural correctness from statistical estimation.
- Ideal for simulation studies and theoretical investigations.

## Limitations

- Not applicable when oracle m-separations are unknown.
- Does not use real data; purely structural.
