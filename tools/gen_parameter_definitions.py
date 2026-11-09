#!/usr/bin/env python3
"""Generate docs/parameter.definitions.md from Tetrad's parameter.definitions.html.

Tetrad reads its own parameter documentation at runtime: ``ParamDescriptions`` parses
``docs/manual/parameter.definitions.html`` out of the jar and looks up, for each parameter
name, the spans ``<name>_short_desc``, ``<name>_long_desc``, ``<name>_default_value``,
``<name>_lower_bound``, ``<name>_upper_bound`` and ``<name>_value_type``. That HTML file is
therefore the authoritative list of parameters, and this manual page is a projection of it.
Hand-maintaining the page meant it drifted; this script removes the need to.

Run it yourself and commit the result. ReadTheDocs does not run it: RTD builds only this
repository, and it never sees the Tetrad jar. See ``make params``.

Usage:
    python3 tools/gen_parameter_definitions.py                      # default source and output
    python3 tools/gen_parameter_definitions.py --source path/to/tetrad-current.jar
    python3 tools/gen_parameter_definitions.py --check              # fail if the page is stale

Only the Python standard library is used, so this adds nothing to requirements.txt.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

# Where the HTML lives inside a Tetrad jar.
JAR_ENTRY = "docs/manual/parameter.definitions.html"

# Default source: a sibling checkout of cmu-phil/tetrad.
DEFAULT_SOURCE = Path("../tetrad/tetrad-lib/src/main/resources/docs/manual/parameter.definitions.html")

DEFAULT_OUT = Path("docs/parameter.definitions.md")

# Suffix -> label used on the generated page. Order here is the order fields are printed.
# "Minimum" and "Maximum" keep the wording the hand-written page used for the bounds.
FIELDS = [
    ("short_desc", "Short description"),
    ("long_desc", "Long description"),
    ("value_type", "Value type"),
    ("default_value", "Default value"),
    ("lower_bound", "Minimum"),
    ("upper_bound", "Maximum"),
]

SUFFIXES = {suffix for suffix, _ in FIELDS}

BANNER = """<!-- GENERATED FILE - DO NOT EDIT BY HAND.
     Produced by tools/gen_parameter_definitions.py from Tetrad's
     parameter.definitions.html, which is the file Tetrad itself reads at runtime.
     Regenerate with `make params`, then commit the result. -->"""


class ParameterParser(HTMLParser):
    """Pulls parameter names and their field spans out of parameter.definitions.html.

    Names come from ``<h3 class="parameter_description" id="NAME">``; fields come from
    ``<span id="NAME_suffix">``. Text is accumulated across any nested tags, so markup
    inside a description does not truncate it.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.order: list[str] = []
        self.fields: dict[tuple[str, str], str] = {}
        self._capture: tuple[str, str] | None = None
        self._depth = 0
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {k: (v or "") for k, v in attrs}

        if tag == "h3" and "parameter_description" in attr.get("class", "") and attr.get("id"):
            name = attr["id"]
            if name not in self.order:
                self.order.append(name)
            return

        if self._capture is not None:
            # Already reading a field. Only nested spans matter for finding the right close;
            # this file contains unclosed <li> and <p> tags, so counting every tag would
            # desynchronise and swallow the following entries.
            if tag == "span":
                self._depth += 1
            return

        if tag == "span" and attr.get("id"):
            split = self._split_field_id(attr["id"])
            if split is not None:
                self._capture = split
                self._depth = 1
                self._buffer = []

    def handle_endtag(self, tag: str) -> None:
        if self._capture is None or tag != "span":
            return
        self._depth -= 1
        if self._depth == 0:
            # Join without a separator: inline markup inside a description must not gain a
            # space, or "X and Y</code>." becomes "X and Y .".
            self.fields[self._capture] = normalize("".join(self._buffer))
            self._capture = None
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._capture is not None:
            self._buffer.append(data)

    @staticmethod
    def _split_field_id(span_id: str) -> tuple[str, str] | None:
        """Split ``someParam_short_desc`` into ``("someParam", "short_desc")``."""
        for suffix in SUFFIXES:
            tail = "_" + suffix
            if span_id.endswith(tail):
                name = span_id[: -len(tail)]
                if name:
                    return name, suffix
        return None


def normalize(text: str) -> str:
    """Collapse whitespace and strip, so descriptions wrapped over several lines read as one."""
    return re.sub(r"\s+", " ", text).strip()


#: Characters that would otherwise be read as inline markup. Descriptions come from Tetrad
#: and contain plenty of them: "x <-> y", "Y _||_ Z | X", "Parents(X) \\ {X}", "x *-* y".
#: Backslash-escaping ASCII punctuation is valid CommonMark and renders the literal character.
_MARKDOWN_SPECIALS = "\\`*_{}[]<>|~"

_ESCAPE_TABLE = str.maketrans({ch: "\\" + ch for ch in _MARKDOWN_SPECIALS})


def escape_markdown(text: str) -> str:
    """Make description text safe to drop into a Markdown bullet.

    Without this, a description such as "When x <-> y, x ~~> y, removes any unshielded
    triples" loses the arrow to the HTML parser, and "testing Y _||_ Z | X" renders in
    italics with the bars missing.
    """
    return text.translate(_ESCAPE_TABLE)


def read_source(source: Path) -> str:
    """Read the HTML, either from a file or from inside a Tetrad jar."""
    if source.suffix == ".jar":
        with zipfile.ZipFile(source) as jar:
            try:
                return jar.read(JAR_ENTRY).decode("utf-8", errors="replace")
            except KeyError:
                raise SystemExit(f"{source} does not contain {JAR_ENTRY}")
    return source.read_text(encoding="utf-8", errors="replace")


def group_letter(name: str) -> str:
    """The A-Z section a parameter belongs under."""
    first = name[0].upper()
    return first if first.isalpha() else "#"


def render(parser: ParameterParser, source_label: str) -> str:
    names = sorted(parser.order, key=lambda n: (n.lower(), n))

    groups: dict[str, list[str]] = {}
    for name in names:
        groups.setdefault(group_letter(name), []).append(name)

    letters = sorted(groups)
    jump = " · ".join(f"[{letter}](#{letter.lower()})" for letter in letters if letter != "#")

    out: list[str] = []
    out.append("# Parameters")
    out.append("")
    out.append(BANNER)
    out.append("")
    out.append(
        "Every search parameter Tetrad documents, taken from the release this page was "
        "generated from. There are "
        f"{len(names)} of them. Parameter names are the names used in scripts and in the "
        "`Parameters` object, so they are also what you pass from py-tetrad."
    )
    out.append("")
    if jump:
        out.append(f"**Jump to:** {jump}")
        out.append("")

    for letter in letters:
        out.append(f"## {letter}")
        out.append("")
        for name in groups[letter]:
            out.append(f"### {name}")
            out.append("")
            wrote_any = False
            for suffix, label in FIELDS:
                value = parser.fields.get((name, suffix), "")
                if not value:
                    continue
                out.append(f"- **{label}:** {escape_markdown(value)}")
                wrote_any = True
            if not wrote_any:
                out.append("- No description recorded for this parameter.")
            out.append("")

    out.append("---")
    out.append("")
    out.append(f"Generated from `{source_label}`.")
    out.append("")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"parameter.definitions.html, or a Tetrad jar containing it (default: {DEFAULT_SOURCE})",
    )
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help=f"output Markdown (default: {DEFAULT_OUT})")
    ap.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit 1 if the output file is missing or would change",
    )
    args = ap.parse_args(argv)

    if not args.source.exists():
        raise SystemExit(
            f"Source not found: {args.source}\n"
            "Pass --source with the path to parameter.definitions.html in a tetrad checkout, "
            "or to a tetrad-current.jar."
        )

    parser = ParameterParser()
    parser.feed(read_source(args.source))
    parser.close()

    if not parser.order:
        raise SystemExit(f"No parameters found in {args.source}; has the HTML structure changed?")

    text = render(parser, args.source.name)

    if args.check:
        if not args.out.exists():
            print(f"{args.out} does not exist; run `make params`.", file=sys.stderr)
            return 1
        if args.out.read_text(encoding="utf-8") != text:
            print(f"{args.out} is out of date; run `make params`.", file=sys.stderr)
            return 1
        print(f"{args.out} is up to date ({len(parser.order)} parameters).")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text, encoding="utf-8")
    print(f"Wrote {args.out} with {len(parser.order)} parameters from {args.source}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
