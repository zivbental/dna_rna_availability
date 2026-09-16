"""Documentation checks for links and CLI defaults that commonly drift."""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from rnavail.cli import build_parser


ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md", ROOT / "RNA_Target_Region_Accessibility_Katzir_CGMD.md"]
DOCS += sorted((ROOT / "docs").glob("*.md"))


def _slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = "".join(
        char for char in unicodedata.normalize("NFKD", heading)
        if not unicodedata.combining(char)
    )
    heading = re.sub(r"[^\w\- ]", "", heading)
    return re.sub(r" +", "-", heading)


def test_internal_markdown_links_and_anchors_exist():
    anchors = {
        path.resolve(): {
            _slug(match.group(1))
            for match in re.finditer(
                r"^#{1,6}\s+(.+?)\s*$", path.read_text(), re.MULTILINE
            )
        }
        for path in DOCS
    }
    problems: list[str] = []
    for source in DOCS:
        for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", source.read_text()):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            relative, _, fragment = target.partition("#")
            destination = (
                (source.parent / relative).resolve() if relative
                else source.resolve()
            )
            if not destination.exists():
                problems.append(f"{source.name}: missing {target}")
            elif fragment and destination in anchors and fragment not in anchors[destination]:
                problems.append(f"{source.name}: missing anchor {target}")
    assert not problems, "\n".join(problems)


def test_documented_scan_defaults_match_parser():
    parser = build_parser()
    args = parser.parse_args(["scan", "ACGUACGUACGUACGUACGUACGUACGUACG"])
    reference = (ROOT / "docs/11-command-reference.md").read_text()
    assert args.window == 25 and "| scan window | 25 nt |" in reference
    assert args.step == 1 and "| scan step | 1 nt |" in reference
    assert args.keep == 25 and "| shortlist | 25 |" in reference
    assert args.seed_length == 10 and "| seed length | 10 nt |" in reference
    assert args.top == 10 and "| displayed top | 10 |" in reference
    assert args.samples == 2000 and "| samples | 2,000 |" in reference


def test_every_scan_long_option_is_named_in_command_reference():
    parser = build_parser()
    command_action = next(action for action in parser._actions if action.dest == "command")
    scan_parser = command_action.choices["scan"]
    long_options = {
        option
        for action in scan_parser._actions
        for option in action.option_strings
        if option.startswith("--")
    }
    reference = (ROOT / "docs/11-command-reference.md").read_text()
    assert not sorted(option for option in long_options if option not in reference)
