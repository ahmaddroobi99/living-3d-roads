# Contributing

1. Open an issue with `owner/repo`, the poster card it belongs under, and one sentence on why.
2. Ranking: `log(stars+1) + recency(<2y) + README mentions roads/driving/reconstruction + has tests + not a fork`.
3. Diversity: mix official paper code, datasets/tools, and simulators. Cap tutorial clones.
4. Every repo must resolve on `api.github.com` — no unpublished or hallucinated links.
5. Poster method names (NeRF-Drive, UrbanImplicit, …) stay as printed; map them to the real paper in `why`.
6. Run `pytest -q` and include the README diff in the PR.
