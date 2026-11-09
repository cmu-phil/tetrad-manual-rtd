
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

# Root of a tetrad checkout, used to check the method crosswalk.
TETRAD        ?= ../tetrad

# Source for the generated method pages: index.html from a tetrad checkout, or a
# tetrad-current.jar. This is the file Tetrad itself reads to show method descriptions.
TETRAD_INDEX  ?= ../tetrad/tetrad-lib/src/main/resources/docs/manual/index.html

.PHONY: help clean html params params-check crosswalk-check crosswalk-report \
        method-pages method-pages-check

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo
	@echo "  params             regenerate docs/parameter.definitions.md from Tetrad's own"
	@echo "                     parameter.definitions.html (set TETRAD_HTML), then commit it"
	@echo "  params-check       fail if that page is out of date; does not write"
	@echo "  crosswalk-check    fail if tools/method-crosswalk.tsv disagrees with the methods"
	@echo "                     Tetrad offers, or with the pages here (set TETRAD)"
	@echo "  crosswalk-report   the same check, plus the documentation-gap summary"
	@echo "  method-pages       write or refresh the pages whose descriptions come from"
	@echo "                     Tetrad's built-in manual (set TETRAD_INDEX), then commit them"
	@echo "  method-pages-check fail if any of those pages is out of date; does not write"

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

crosswalk-check:
	@$(PYTHON) tools/check_crosswalk.py --tetrad "$(TETRAD)"

crosswalk-report:
	@$(PYTHON) tools/check_crosswalk.py --tetrad "$(TETRAD)" --report

method-pages:
	@$(PYTHON) tools/gen_method_pages.py --source "$(TETRAD_INDEX)"

method-pages-check:
	@$(PYTHON) tools/gen_method_pages.py --source "$(TETRAD_INDEX)" --check
