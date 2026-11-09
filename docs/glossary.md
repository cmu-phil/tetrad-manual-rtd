# Glossary

Terms used throughout this manual and in Tetrad's output.

## Adjacent

Two vertices in a graph are adjacent if there is a directed, or undirected, or double-headed edge between them.

## Degree

The total number of edges directed both into and out of a vertex.

## Indegree

The number of edges directed into a vertex.

## Markov Blanket

In a variable set V, with joint probability Pr, the Markov Blanket of a variable X in V is the smallest subset M of V \ {X} such that X II V \ M | M. In a DAG model, the Markov Blanket of X is the union of the set of direct causes (parents) of X, the set of direct effects (children) of X, and the set of direct causes of direct effects of X.

## Markov Equivalent Graphs

Two directed acyclic graphs (DAGS) are Markov Equivalent if they have the same adjacencies and for every triple X – Y – Z of adjacent vertices, if X and Z are not adjacent, X -> Y <- Z in both graphs or in neither graph.

## Meek Orientation Rules

Rules for finding all directions of edges implied by a CPDAG, consistent with any specified “knowledge” constraints on directions. See https://arxiv.org/pdf/1302. 4972.pdf

## Mixed Ancestral Graph (MAG)

An acyclic graph with directed and undirected edges. Directed edges have the same interpretation as in DAGs. Undirected edges represent common causes. See Richardson, T. (2003). Markov properties for acyclic directed mixed graphs. *Scandinavian Journal of Statistics*, 30(1), 145-157.

## Multiple Indicator Model

A graphical model in which unmeasured variables each have multiple measured effects. There may be directed edges between unmeasured variables, but no directed edges from measured variables to unmeasured variables are allowed.

## Outdegree

The number of edges directed out of a vertex.

## Partial Ancestral Graph (PAG)

See PAG description in this manual.

## CPDAG

A graphical representation of a Markov Equivalence Class or Classes, having both directed and undirected edges, with an undirected edge indicating that for each possible direction of the edge, there is a graph in the class or classes having that edge direction.

## Scale Free Graph

A network in which the frequency of nodes with degree k obeys a power law--the relation between log of degree and log of frequency is roughly linear. See https://cs.brynmawr.edu/Courses/cs380/ spring2013/section02/slides/10_ScaleFreeNetworks.pdf.

## Trek

A trek between X and Y is a directed path from X to Y or from Y to X, or two directed paths from a third variable Z into X and Y that do not intersect except at Z.
