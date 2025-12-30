"""CLI entrypoint for the CPU-first modular music engine.

v0.1 exposes placeholder commands focused on project state inspection.
"""

import argparse
import json
from typing import Sequence

from engine.state import default_project_state


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""

    parser = argparse.ArgumentParser(description="CPU-first MoMuGen engine CLI")
    parser.add_argument(
        "--print-default-state",
        action="store_true",
        help="Print the default project state JSON and exit.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI dispatcher."""

    parser = build_parser()
    args = parser.parse_args(argv)
    if args.print_default_state:
        print(json.dumps(default_project_state(), indent=2))
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
