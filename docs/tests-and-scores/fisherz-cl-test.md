# Fisher Z, Causal Learn (Python)

**Command:** `fisherz-cl-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: fisherz-cl-test -->

This runs the Fisher Z conditional independence test as implemented in the Python causal-learn library, for comparison with Tetrad's own Fisher Z test (see). A persistent Python process is started from a bundled server script, independence queries are forwarded to it, and the results are returned as ordinary test results. A Python interpreter with causal-learn installed must be available on the machine, and its path must be supplied in the pythonExe parameter; there is no default that will be valid outside the developer's machine. The server script can be overridden with pythonCiServer. Continuous data.

<!-- END GENERATED: fisherz-cl-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
