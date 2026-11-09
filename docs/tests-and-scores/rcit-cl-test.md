# RCIT, Causal Learn (Python)

**Command:** `rcit-cl-test`  
**Kind:** Independence test

The description below is Tetrad's own, shown in the interface when you select this method. It is reproduced here so that the method is documented; it has not yet been edited for the manual, and it has no "when to use" guidance of the kind the hand-written pages carry.

<!-- BEGIN GENERATED: rcit-cl-test -->

An IndependenceWrapper that runs the Randomized Conditional Independence Test (RCIT) implemented in the Python causal-learn library, bridging it into Tetrad's IndependenceTest framework. How it works Each call to getTest launches (or connects to) a persistent Python process running a bundled server script (python/rcit\_server.py). CI queries from Java are forwarded to that process via ProcessPythonCiService, and results are returned as standard IndependenceTest responses through PythonRcitIndependenceTest. Python environment A Python interpreter that has causal-learn and its dependencies installed must be available on the host machine. The path to that interpreter is supplied via the Params.PYTHON\_EXE parameter. There is no default that is likely to be valid on any machine other than the developer's, so this parameter should always be set explicitly before use. Server script resolution The Python server script is resolved in the following order: If Params.PYTHON\_CI\_SERVER is set to a non-empty path (and not the sentinel value "Use bundled script"), that path is used directly. Otherwise, the bundled resource python/rcit\_server.py is extracted to the user's local cache directory (via PythonResource.extractToUserCache) and that extracted copy is used.

<!-- END GENERATED: rcit-cl-test -->

<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, worked examples or references here. -->
