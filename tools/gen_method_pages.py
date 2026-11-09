#!/usr/bin/env python3
"""Generate manual pages for methods that have none, from Tetrad's own built-in manual.

Tetrad ships a description for every method a user can select: the interface reads
`docs/manual/index.html` out of the jar and shows the block whose `id` is the method's command.
The crosswalk (`tools/method-crosswalk.tsv`) records which of those methods have a page here.
For the ones that do not, the description already exists and is simply missing from this manual.
This script copies it across.

It does **not** touch the curated pages. Where a method already has a hand-written page, that
prose is generally better than the built-in text, and overwriting it would be a loss. Only rows
whose status is `undocumented` (first run) or `documented-generated` (refresh) are written.

Each generated page carries a marked region:

    <!-- BEGIN GENERATED: boss -->
    ...
    <!-- END GENERATED: boss -->

On a refresh only that region is rewritten, so anything you add below it survives. If the
markers are missing from a file that should have them, the script refuses to write rather than
appending or clobbering.

Usage:
    python3 tools/gen_method_pages.py                       # write/refresh pages
    python3 tools/gen_method_pages.py --source path/to/tetrad-current.jar
    python3 tools/gen_method_pages.py --check               # fail if anything is out of date
    python3 tools/gen_method_pages.py --include-experimental

Experimental methods are skipped by default: the manual states that they carry no documentation
commitment (see docs/experimental-methods.md). Only the standard library is used.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path

JAR_ENTRY = "docs/manual/index.html"
DEFAULT_SOURCE = Path("../tetrad/tetrad-lib/src/main/resources/docs/manual/index.html")
CROSSWALK = Path("tools/method-crosswalk.tsv")
DOCS = Path("docs")

#: Statuses this script is responsible for.
WRITE_STATUSES = {"undocumented", "documented-generated"}

#: Where a page goes, by crosswalk kind.
SUBDIR = {"ALG": "algorithms", "BLOCK": "algorithms", "TEST": "tests-and-scores", "SCORE": "tests-and-scores"}

KIND_LABEL = {"ALG": "Algorithm", "BLOCK": "Algorithm (Latent Clusters box)",
              "TEST": "Independence test", "SCORE": "Score"}

BEGIN = "<!-- BEGIN GENERATED: {command} -->"
END = "<!-- END GENERATED: {command} -->"

_SPECIALS = "\\`*_{}[]<>|~"
_ESCAPE = str.maketrans({c: "\\" + c for c in _SPECIALS})


def escape(text: str) -> str:
    """Escape inline Markdown. Tetrad's prose is full of `x *-* y` and `Y _||_ Z | X`."""
    return text.translate(_ESCAPE)


def squash(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


class Node:
    """A very small tree, built so we can convert the description to Markdown."""

    def __init__(self, tag: str, attrs: dict[str, str] | None = None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list["Node | str"] = []


class DescriptionParser(HTMLParser):
    """Collects the element whose id is the wanted command, as a small tree.

    The file has unclosed <p> and <li> tags, so rather than trusting end tags we treat a new <p>
    or <li> as closing the previous one, and stop at the close of the element we opened.
    """

    VOID = {"br", "hr", "img"}
    IMPLICIT_CLOSE = {"p", "li"}

    def __init__(self, wanted: str):
        super().__init__(convert_charrefs=True)
        self.wanted = wanted
        self.root: Node | None = None
        self.stack: list[Node] = []
        self.done = False

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        attr = {k: (v or "") for k, v in attrs}
        if self.root is None:
            if attr.get("id") == self.wanted:
                self.root = Node(tag, attr)
                self.stack = [self.root]
            return
        if tag in self.VOID:
            self.stack[-1].children.append(Node(tag, attr))
            return
        if tag in self.IMPLICIT_CLOSE:
            while len(self.stack) > 1 and self.stack[-1].tag in self.IMPLICIT_CLOSE:
                self.stack.pop()
        node = Node(tag, attr)
        self.stack[-1].children.append(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        if self.done or self.root is None:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i].tag == tag:
                if i == 0:
                    self.done = True
                    self.stack = [self.root]
                else:
                    del self.stack[i:]
                return

    def handle_data(self, data):
        if self.root is not None and not self.done:
            self.stack[-1].children.append(data)


def inline(node: "Node | str") -> str:
    """Convert an inline node to Markdown."""
    if isinstance(node, str):
        return escape(node)
    if node.tag == "br":
        return "\n"
    if node.tag in ("code", "tt"):
        return "`" + squash(text_of(node)) + "`"
    inner = "".join(inline(c) for c in node.children)
    if node.tag in ("em", "i"):
        return f"*{inner.strip()}*" if inner.strip() else ""
    if node.tag in ("b", "strong"):
        return f"**{inner.strip()}**" if inner.strip() else ""
    if node.tag == "a":
        href = node.attrs.get("href", "")
        label = inner.strip() or href
        # Links in the built-in manual point inside that single page; keep the text, drop the
        # anchor, since it does not resolve here.
        return label if href.startswith("#") or not href else f"[{label}]({href})"
    return inner


def text_of(node: "Node | str") -> str:
    if isinstance(node, str):
        return node
    return "".join(text_of(c) for c in node.children)


def to_markdown(root: Node) -> str:
    """Convert a description block to Markdown paragraphs, lists and code blocks."""
    blocks: list[str] = []
    loose: list[str] = []

    def flush_loose():
        if loose:
            joined = squash("".join(loose))
            if joined:
                blocks.append(joined)
            loose.clear()

    for child in root.children:
        if isinstance(child, str):
            loose.append(child)
            continue
        if child.tag == "p":
            flush_loose()
            body = squash("".join(inline(c) for c in child.children))
            if body:
                blocks.append(body)
        elif child.tag == "pre":
            flush_loose()
            blocks.append("```\n" + text_of(child).strip("\n") + "\n```")
        elif child.tag in ("ul", "ol"):
            flush_loose()
            items = [squash("".join(inline(c) for c in li.children))
                     for li in child.children if isinstance(li, Node) and li.tag == "li"]
            items = [i for i in items if i]
            if items:
                marker = (lambda n: f"{n}.") if child.tag == "ol" else (lambda n: "-")
                blocks.append("\n".join(f"{marker(n)} {item}" for n, item in enumerate(items, 1)))
        elif child.tag in ("div", "span"):
            flush_loose()
            nested = to_markdown(child)
            if nested:
                blocks.append(nested)
        else:
            loose.append("".join(inline(c) for c in child.children))
    flush_loose()
    return "\n\n".join(b for b in blocks if b)


def read_source(source: Path) -> str:
    if source.suffix == ".jar":
        with zipfile.ZipFile(source) as jar:
            try:
                return jar.read(JAR_ENTRY).decode("utf-8", errors="replace")
            except KeyError:
                raise SystemExit(f"{source} does not contain {JAR_ENTRY}")
    return source.read_text(encoding="utf-8", errors="replace")


def page_text(row: dict[str, str], body: str, source_label: str) -> str:
    command, name, kind = row["command"], row["name"], row["kind"]
    out = [
        f"# {name}",
        "",
        f"**Command:** `{command}`  ",
        f"**Kind:** {KIND_LABEL.get(kind, kind)}",
        "",
        "The description below is Tetrad's own, shown in the interface when you select this "
        "method. It is reproduced here so that the method is documented; it has not yet been "
        "edited for the manual, and it has no \"when to use\" guidance of the kind the "
        "hand-written pages carry.",
        "",
        BEGIN.format(command=command),
        "",
        body,
        "",
        END.format(command=command),
        "",
        "<!-- Anything below this line is kept by tools/gen_method_pages.py. Add guidance, "
        "worked examples or references here. -->",
        "",
    ]
    return "\n".join(out)


def splice(existing: str, command: str, body: str) -> str | None:
    """Replace the marked region in an existing page. None if the markers are missing."""
    begin, end = BEGIN.format(command=command), END.format(command=command)
    i, j = existing.find(begin), existing.find(end)
    if i < 0 or j < 0 or j < i:
        return None
    return existing[:i] + begin + "\n\n" + body + "\n\n" + existing[j:]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                    help=f"index.html, or a Tetrad jar containing it (default: {DEFAULT_SOURCE})")
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if anything would change")
    ap.add_argument("--include-experimental", action="store_true",
                    help="also generate pages for methods marked experimental")
    args = ap.parse_args(argv)

    if not args.source.exists():
        raise SystemExit(f"Source not found: {args.source}\nPass --source with a path to index.html or a jar.")
    html = read_source(args.source)

    rows = [r for r in csv.DictReader(CROSSWALK.open(encoding="utf-8"), delimiter="\t")
            if r["kind"] != "PAGE" and r["status"] in WRITE_STATUSES]
    if not args.include_experimental:
        rows = [r for r in rows if "X" not in r["flags"]]
    rows = [r for r in rows if "D" not in r["flags"]]

    wrote, stale, missing_desc, no_markers = [], [], [], []

    for row in sorted(rows, key=lambda r: r["command"]):
        command = row["command"]
        parser = DescriptionParser(command)
        parser.feed(html)
        parser.close()
        if parser.root is None:
            missing_desc.append(command)
            continue
        body = to_markdown(parser.root)
        if not body:
            missing_desc.append(command)
            continue

        target = DOCS / SUBDIR[row["kind"]] / f"{command}.md"
        if target.exists():
            current = target.read_text(encoding="utf-8")
            updated = splice(current, command, body)
            if updated is None:
                no_markers.append(str(target))
                continue
        else:
            updated = page_text(row, body, args.source.name)

        if target.exists() and target.read_text(encoding="utf-8") == updated:
            continue
        if args.check:
            stale.append(str(target))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(updated, encoding="utf-8")
            wrote.append(str(target))

    for command in missing_desc:
        print(f"warning: no description for '{command}' in {args.source.name}; no page written",
              file=sys.stderr)
    for path in no_markers:
        print(f"error: {path} has no generated markers; refusing to write", file=sys.stderr)

    if args.check:
        if stale or no_markers:
            for path in stale:
                print(f"{path} is out of date; run `make method-pages`.", file=sys.stderr)
            return 1
        print(f"Generated method pages are up to date ({len(rows)} checked).")
        return 0

    if no_markers:
        return 1
    print(f"Wrote {len(wrote)} page(s) of {len(rows)} considered.")
    for path in wrote:
        print(f"  {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
