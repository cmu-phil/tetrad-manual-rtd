
# Minimal Sphinx makefile
.ONESHELL:
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = _build
PYTHON        ?= python3

# Source for the generated parameter page: parameter.definitions.html from a tetrad
# checkout, or a tetrad-current.jar. Override on the command line, e.g.
#   make params TETRAD_HTML=~/tetrad/tetrad-lib/src/main/resources/docs/manual/parameter.definitions.html
#   make params TETRAD_HTML=~/py-tetrad/pytetrad/resources/tetrad-current.jar
TETRAD_HTML   ?= ../tetrad/tetrad-lib/src/main/resources/docs/manual/parameter.definitions.html

.PHONY: help clean html params params-check

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo
	@echo "  params        regenerate docs/parameter.definitions.md from Tetrad's own"
	@echo "                parameter.definitions.html (set TETRAD_HTML), then commit it"
	@echo "  params-check  fail if that page is out of date; does not write"

clean:
	rm -rf $(BUILDDIR)

html:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

# ReadTheDocs does not run these; it builds only the committed Markdown. Run them here
# and commit the result.
params:
	@$(PYTHON) tools/gen_parameter_definitions.py --source "$(TETRAD_HTML)" --out docs/parameter.definitions.md

params-check:
	@$(PYTHON) tools/gen_parameter_definitions.py --source "$(TETRAD_HTML)" --out docs/parameter.definitions.md --check
