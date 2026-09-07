from living_roads.catalog import catalog, repos_for


def test_catalog_covers_poster() -> None:
    cards = catalog()
    assert len(cards) == 17
    names = [c["name"] for c in cards]
    assert "NeRF-Drive" in names
    assert "GaussianDrive" in names
    assert "HD Map Generation" in names


def test_seed_has_live_street_gaussians() -> None:
    repos = repos_for("gaussiandrive")
    names = {r["full_name"] for r in repos}
    assert "zju3dv/street_gaussians" in names
    assert "graphdeco-inria/gaussian-splatting" in names
