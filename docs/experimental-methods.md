# Experimental Methods

Some of the methods Tetrad offers are marked **experimental**. This page explains what that
marking means and lists the methods that carry it. It is stated once here rather than repeated
on each page.

## What the marking means

An experimental method is one that is still under development. It is included so that
researchers can try it and report what they find, not because its behavior has settled. For an
experimental method, any of the following may be true:

- Its results have not been checked against a reference implementation or a published benchmark.
- Its parameters, its defaults, or its name may change in a later release.
- It may be withdrawn from the interface entirely.

**Experimental methods are offered without a documentation commitment.** Most have no page in
this manual. A few do, and those pages may describe an earlier version of the method rather than
the one in the release you are running. Where a manual page and the program disagree about an
experimental method, the program is correct.

If you need a method whose behavior is documented and stable, choose one that is not on the list
below. The short list of recommended algorithms contains no experimental methods.

## Seeing them in the interface

Experimental methods are hidden by default. They appear in the algorithm, test, and score
choosers only when you turn on the setting that shows experimental methods. If you do not see a
method named below, that setting is probably off.

## The list, as of Tetrad 8.0.0

Nineteen algorithms, one independence test, and one score are marked experimental in this
release. Where a page exists in this manual, it is linked.

### Experimental algorithms

| Method | Manual page |
|---|---|
| BFCI | none |
| BOSS-CCD | none |
| BOSS-TopK | none |
| CAM | [CAM](algorithms/cam.md) |
| CD-NOD | [CD-NOD](algorithms/cdnod.md) |
| CD-NOD-PAG | none |
| CPW | none |
| FASK-Pool | none |
| FASK-Vote | [FASK-Vote](algorithms/fask-vote.md) |
| FCIT | [FCIT](algorithms/fcit.md) |
| FCIT-SL | none |
| FCIT-ZM | none |
| GMAS | none |
| LV-Heuristic | [LV-Heuristic](algorithms/lv-heuristic.md) |
| PC-AR | none |
| PCMCI | [PCMCI](algorithms/pcmci.md) |
| RFCI-BSC | [RFCI-BSC](algorithms/rfci-bsc.md) |
| RLCD | none |
| SP | [SP](algorithms/sp.md) |

### Experimental independence tests

| Method | Manual page |
|---|---|
| BE-GCM (Basis-Expanded GCM Test) | none |

### Experimental scores

| Method | Manual page |
|---|---|
| KML Score | none |

## Deprecated methods

A method marked **deprecated** is one that has been superseded. Deprecated methods are hidden
from the choosers, so you cannot select one in a new session. They remain in the program only so
that sessions saved by earlier versions of Tetrad still open. One algorithm is deprecated in this
release: **Two-Step (FastICA, cyclic)**.
