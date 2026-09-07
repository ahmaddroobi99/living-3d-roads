"""CLI: reconstruct a synthetic corridor or print the catalog."""

from __future__ import annotations

import argparse
import json

from living_roads.catalog import catalog
from living_roads.pipeline import reconstruct


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="living-roads")
    sub = p.add_subparsers(dest="cmd", required=True)

    rec = sub.add_parser("reconstruct", help="sparse points -> surface + Gaussians")
    rec.add_argument("--seed", type=int, default=0)
    rec.add_argument("--json", action="store_true")

    sub.add_parser("catalog", help="print poster topics and seeded repos")

    args = p.parse_args(argv)
    if args.cmd == "reconstruct":
        scene = reconstruct(seed=args.seed)
        if args.json:
            print(json.dumps(scene.metrics, indent=2))
        else:
            m = scene.metrics
            print(
                f"points={m['n_points']:.0f}  gaussians={m['n_gaussians']:.0f}  "
                f"potholes={m['n_potholes']:.0f}  free={m['free_frac']:.2f}  "
                f"rmse={m['rmse_m']*100:.1f} cm"
            )
        return 0
    if args.cmd == "catalog":
        for card in catalog():
            print(f"## {card['name']} — {card['subtitle']}")
            print(f"   {card['blurb']}")
            for repo in card["repos"][:3]:
                print(f"   - {repo['full_name']} ({repo.get('stars', '?')}\u2605) {repo.get('why', '')}")
            print()
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
