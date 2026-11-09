#!/usr/bin/env python3
"""Check tools/method-crosswalk.tsv against the methods Tetrad actually offers.

The crosswalk records, for every method a user can select in Tetrad, which page of this
manual documents it — or that none does. It is maintained by hand; this script is what keeps
it honest. Run it when Tetrad's method list changes: `make crosswalk-check`.

Reachability is the subtle part, and getting it wrong is the known failure mode here. A method
is reachable if *either*:

  * it carries a live `@Algorithm`, `@TestOfIndependence` or `@Score` annotation, or
  * the interface dispatches it by name from somewhere of its own — at present the Latent
    Clusters box, whose `BlockClusteringWizard` offers the block discoverers from a combo box.

A **commented-out** annotation does not mean a method was retired. It may have moved to a box
with its own dispatch, as TSC, FOFC, FTFC, GFFC and BPC did, or been replaced by a parameter,
as IMaGES was by `poolDataSets`. So this script strips comments before looking for annotations,
and reads the wizard's combo box as a second source. If a third dispatch site is ever added,
teach it to this script, or the crosswalk will quietly go stale.

Usage:
    python3 tools/check_crosswalk.py                      # expects a sibling tetrad checkout
    python3 tools/check_crosswalk.py --tetrad ~/tetrad
    python3 tools/check_crosswalk.py --report             # also print the gap summary

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_TETRAD = Path("../tetrad")
CROSSWALK = Path("tools/method-crosswalk.tsv")
DOCS = Path("docs")

ALGCOMPARISON = Path("tetrad-lib/src/main/java/edu/cmu/tetrad/algcomparison")
WIZARD = Path("tetrad-gui/src/main/java/edu/cmu/tetradapp/editor/blocks/BlockClusteringWizard.java")

KINDS = [("ALG", "algorithm", "Algorithm"),
         ("TEST", "independence", "TestOfIndependence"),
         ("SCORE", "score", "Score")]


def strip_comments(source: str) -> str:
    """Remove block and line comments, so a commented-out annotation is not mistaken for a live one."""
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    source = re.sub(r"(?m)^[ \t]*//.*$", "", source)
    return re.sub(r"(?m)//.*$", "", source)


def annotated_methods(tetrad: Path) -> dict[str, tuple[str, str, str]]:
    """command -> (kind, name, flags) for every live annotation."""
    found: dict[str, tuple[str, str, str]] = {}
    for kind, subdir, annotation in KINDS:
        root = tetrad / ALGCOMPARISON / subdir
        if not root.is_dir():
            raise SystemExit(f"Not found: {root}\nPass --tetrad with the path to a tetrad checkout.")
        for path in sorted(root.rglob("*.java")):
            text = strip_comments(path.read_text(encoding="utf-8", errors="replace"))
            match = re.search(r"@(?:edu\.cmu\.tetrad\.annotation\.)?" + annotation + r"\(", text)
            if not match:
                continue
            block = text[match.end():match.end() + 600]
            command = re.search(r'command\s*=\s*"([^"]*)"', block)
            name = re.search(r'name\s*=\s*"([^"]*)"', block)
            if not command:
                continue
            flags = ""
            if re.search(r"@(?:edu\.cmu\.tetrad\.annotation\.)?Experimental\b", text):
                flags += "X"
            if re.search(r"@Deprecated\b", text):
                flags += "D"
            found[command.group(1)] = (kind, name.group(1) if name else "?", flags)
    return found


def block_discoverers(tetrad: Path) -> dict[str, tuple[str, str, str]]:
    """The block discoverers the Latent Clusters box offers, read from the wizard's combo box."""
    path = tetrad / WIZARD
    if not path.is_file():
        print(f"warning: {path} not found; block discoverers not checked", file=sys.stderr)
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    # The declaration uses the diamond operator: new JComboBox<>(new String[]{"TSC", ...}).
    # Allow any type argument so a later `JComboBox<String>` spelling still matches.
    match = re.search(r"cbAlgorithm\s*=\s*new\s+JComboBox\s*<[^>]*>\s*\(\s*new\s+String\s*\[\]\s*\{([^}]*)\}",
                      text)
    if not match:
        print(f"warning: could not read the algorithm combo box in {path.name}; "
              "block discoverers not checked", file=sys.stderr)
        return {}
    names = re.findall(r'"([^"]+)"', match.group(1))
    return {n.lower(): ("BLOCK", n, "") for n in names}


def read_crosswalk(path: Path) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header = lines[0].split("\t")
    methods, pages = {}, {}
    for line in lines[1:]:
        if not line.strip():
            continue
        row = dict(zip(header, line.split("\t")))
        if row["kind"] == "PAGE":
            pages[row["page"]] = row
        else:
            methods[row["command"]] = row
    return methods, pages


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tetrad", type=Path, default=DEFAULT_TETRAD, help=f"tetrad checkout (default: {DEFAULT_TETRAD})")
    ap.add_argument("--report", action="store_true", help="print the gap summary as well")
    args = ap.parse_args(argv)

    live = annotated_methods(args.tetrad)
    live.update(block_discoverers(args.tetrad))
    methods, page_rows = read_crosswalk(CROSSWALK)

    all_pages = {str(p.relative_to(DOCS)) for p in
                 list((DOCS / "algorithms").glob("*.md")) + list((DOCS / "tests-and-scores").glob("*.md"))
                 if p.name != "index.md"}

    problems: list[str] = []

    for command, (kind, name, flags) in sorted(live.items()):
        if command not in methods:
            problems.append(f"reachable but missing from the crosswalk: {kind} {command} ({name})")
        else:
            row = methods[command]
            if row["flags"] != flags:
                problems.append(f"{command}: flags are '{row['flags']}' in the crosswalk, '{flags}' in Tetrad")
            if row["name"] != name:
                problems.append(f"{command}: name is '{row['name']}' in the crosswalk, '{name}' in Tetrad")

    for command in sorted(methods):
        if command not in live:
            problems.append(f"in the crosswalk but no longer reachable: {command} "
                            f"(retire its page, or check for a new dispatch site)")

    referenced = {row["page"] for row in methods.values() if row["page"]}
    for page in sorted(referenced):
        if page not in all_pages:
            problems.append(f"crosswalk points at a missing page: {page}")
    for page in sorted(page_rows):
        if page not in all_pages:
            problems.append(f"crosswalk PAGE row for a missing page: {page}")
    for page in sorted(all_pages - referenced - set(page_rows)):
        problems.append(f"page accounted for by nothing in the crosswalk: {page}")

    if args.report:
        tally: dict[str, int] = {}
        for row in list(methods.values()) + list(page_rows.values()):
            tally[row["status"]] = tally.get(row["status"], 0) + 1
        print(f"{len(live)} reachable methods, {len(all_pages)} pages")
        for status in sorted(tally):
            print(f"  {status:28s} {tally[status]}")
        gaps = [r for r in methods.values() if r["status"] == "undocumented"]
        if gaps:
            print(f"\nundocumented and not experimental ({len(gaps)}):")
            for row in sorted(gaps, key=lambda r: (r["kind"], r["command"])):
                print(f"  {row['kind']:6s} {row['command']:24s} {row['name']}")
        print()

    if problems:
        print(f"{len(problems)} problem(s):")
        for problem in problems:
            print(f"  {problem}")
        return 1

    print(f"Crosswalk is consistent: {len(live)} reachable methods, {len(all_pages)} pages, all accounted for.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
