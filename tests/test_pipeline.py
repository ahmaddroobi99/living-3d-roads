from __future__ import annotations

import numpy as np

from living_roads.pipeline import Semantic, analytic_road, reconstruct, sample_sparse
from living_roads.topics import APPLICATIONS, METHODS, all_topics


def test_analytic_has_pothole() -> None:
    z_in = analytic_road(np.array([[12.0, 0.4]]))
    z_out = analytic_road(np.array([[2.0, 0.0]]))
    assert z_in[0] < z_out[0] - 0.04


def test_reconstruct_rmse_under_3cm() -> None:
    scene = reconstruct(seed=1)
    assert scene.metrics['rmse_m'] < 0.03
    assert scene.metrics['n_gaussians'] > 10
    assert scene.metrics['n_potholes'] >= 1
    assert 0.4 < scene.metrics['free_frac'] < 1.0


def test_sparse_labels_include_actors() -> None:
    cloud = sample_sparse(seed=0)
    assert set(cloud.labels.tolist()) >= {int(Semantic.ROAD), int(Semantic.VEHICLE), int(Semantic.PEDESTRIAN)}


def test_poster_topic_counts() -> None:
    assert len(METHODS) == 8
    assert len(APPLICATIONS) == 9
    slugs = {t.slug for t in all_topics()}
    assert 'nerf-drive' in slugs
    assert 'gaussiandrive' in slugs
    assert 'hd-map-generation' in slugs
    assert '4d-drivegs' in slugs


def test_surface_normals_point_up() -> None:
    scene = reconstruct(seed=2)
    assert scene.surface.normals[..., 2].min() > 0.7
