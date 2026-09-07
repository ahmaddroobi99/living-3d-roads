"""Offline catalog: poster topics + live-verified seed repos."""

from __future__ import annotations

import json
from pathlib import Path

from living_roads.topics import Topic, all_topics

ROOT = Path(__file__).resolve().parents[2]
SEED_PATH = ROOT / "data" / "seed_catalog.json"


def load_seed() -> dict:
    if not SEED_PATH.exists():
        return {"topics": {}}
    return json.loads(SEED_PATH.read_text())


def repos_for(slug: str) -> list[dict]:
    seed = load_seed()
    topics = seed.get("topics", {})
    return list(topics.get(slug, []))


def catalog() -> list[dict]:
    out = []
    for topic in all_topics():
        out.append(
            {
                "slug": topic.slug,
                "section": topic.section,
                "name": topic.name,
                "subtitle": topic.subtitle,
                "blurb": topic.blurb,
                "real_anchor": topic.real_anchor,
                "repos": repos_for(topic.slug),
            }
        )
    return out


def top_repos(topic: Topic, k: int = 3) -> list[dict]:
    repos = sorted(repos_for(topic.slug), key=lambda r: r.get("stars") or 0, reverse=True)
    return repos[:k]
