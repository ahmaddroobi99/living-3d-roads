"""Sparse road points -> continuous surface, Gaussians, semantics.

This is the poster pipeline in miniature. It is *not* a NeRF: the surface
is an RBF interpolant of sparse XYH samples, Gaussians are analytic
proxies on that surface, and semantics are rule-labelled. The point is
to make every poster box executable and testable.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum

import numpy as np
from scipy.interpolate import RBFInterpolator


class Semantic(IntEnum):
    ROAD = 0
    LANE = 1
    DAMAGE = 2
    VEHICLE = 3
    PEDESTRIAN = 4
    FREESPACE = 5
    CURB = 6


SEMANTIC_NAMES = {s: s.name.lower() for s in Semantic}


@dataclass
class SparseCloud:
    """N x 3 points in metres: x along-track, y cross-track, z up."""

    xyz: np.ndarray
    labels: np.ndarray | None = None

    def __post_init__(self) -> None:
        self.xyz = np.asarray(self.xyz, dtype=float)
        if self.xyz.ndim != 2 or self.xyz.shape[1] != 3:
            raise ValueError("xyz must be (N, 3)")
        if self.labels is not None:
            self.labels = np.asarray(self.labels, dtype=int)
            if self.labels.shape[0] != self.xyz.shape[0]:
                raise ValueError("labels length must match points")


@dataclass
class Surface:
    xs: np.ndarray
    ys: np.ndarray
    height: np.ndarray
    normals: np.ndarray

    @property
    def grid(self) -> tuple[np.ndarray, np.ndarray]:
        return np.meshgrid(self.xs, self.ys, indexing="xy")


@dataclass
class GaussianSplat:
    """Isotropic 3D Gaussian proxy sitting on the reconstructed surface."""

    mean: np.ndarray
    scale: float
    opacity: float
    semantic: Semantic
    color: tuple[float, float, float] = (0.4, 0.4, 0.4)


@dataclass
class Scene:
    cloud: SparseCloud
    surface: Surface
    gaussians: list[GaussianSplat]
    occupancy: np.ndarray
    potholes: list[tuple[float, float, float]]
    metrics: dict[str, float] = field(default_factory=dict)


def analytic_road(xy: np.ndarray) -> np.ndarray:
    """Ground-truth road height: 2% crown + pothole at (12, 0.4) + bump at x=22."""
    x = xy[:, 0]
    y = xy[:, 1]
    crown = 0.02 * (1.75**2 - y**2)
    pothole = -0.08 * np.exp(-((x - 12.0) ** 2) / 1.6 - (y - 0.4) ** 2 / 0.25)
    bump = 0.03 * np.exp(-((x - 22.0) ** 2) / 0.4)
    return crown + pothole + bump


def sample_sparse(n: int = 180, seed: int = 0, noise: float = 0.008) -> SparseCloud:
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.0, 30.0, n)
    y = np.clip(rng.normal(0.0, 0.7, n), -1.75, 1.75)
    z = analytic_road(np.column_stack([x, y])) + rng.normal(0.0, noise, n)
    labels = np.full(n, int(Semantic.ROAD), dtype=int)
    lane_n = n // 8
    lx = np.linspace(0.0, 30.0, lane_n)
    ly = np.full(lane_n, 0.0)
    lz = analytic_road(np.column_stack([lx, ly]))
    xyz = np.vstack([np.column_stack([x, y, z]), np.column_stack([lx, ly, lz])])
    labels = np.concatenate([labels, np.full(lane_n, int(Semantic.LANE))])
    extras = np.array([[8.0, -1.1, 1.4], [8.4, -1.1, 1.4], [18.0, 1.2, 1.7]])
    extra_labels = np.array([int(Semantic.VEHICLE), int(Semantic.VEHICLE), int(Semantic.PEDESTRIAN)])
    xyz = np.vstack([xyz, extras])
    labels = np.concatenate([labels, extra_labels])
    return SparseCloud(xyz=xyz, labels=labels)


def fit_surface(cloud: SparseCloud, nx: int = 80, ny: int = 28, smoothing: float = 0.01) -> Surface:
    xyz = cloud.xyz
    road = xyz[xyz[:, 2] < 0.35]
    if road.shape[0] < 8:
        road = xyz
    rbf = RBFInterpolator(road[:, :2], road[:, 2], kernel="thin_plate_spline", smoothing=smoothing)
    xs = np.linspace(float(road[:, 0].min()), float(road[:, 0].max()), nx)
    ys = np.linspace(-1.75, 1.75, ny)
    xx, yy = np.meshgrid(xs, ys, indexing="xy")
    query = np.column_stack([xx.ravel(), yy.ravel()])
    height = rbf(query).reshape(ny, nx)
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    dzdx, dzdy = np.gradient(height, dy, dx)
    nxn = -dzdx
    nyn = -dzdy
    nzn = np.ones_like(height)
    norm = np.sqrt(nxn**2 + nyn**2 + nzn**2)
    normals = np.stack([nxn / norm, nyn / norm, nzn / norm], axis=-1)
    return Surface(xs=xs, ys=ys, height=height, normals=normals)


def detect_potholes(surface: Surface, drop_m: float = 0.03) -> list[tuple[float, float, float]]:
    xx, yy = surface.grid
    crown = 0.02 * (1.75**2 - yy**2)
    residual = surface.height - crown
    if not (residual < -drop_m).any():
        return []
    iy, ix = np.unravel_index(np.argmin(residual), residual.shape)
    return [(float(surface.xs[ix]), float(surface.ys[iy]), float(residual[iy, ix]))]


def occupany_from_surface(surface: Surface, max_abs_y: float = 1.6) -> np.ndarray:
    xx, yy = surface.grid
    crown = 0.02 * (1.75**2 - yy**2)
    residual = surface.height - crown
    free = (np.abs(yy) <= max_abs_y) & (residual > -0.04)
    return free.astype(np.uint8)


def gaussians_from_scene(cloud: SparseCloud, surface: Surface, stride: int = 6) -> list[GaussianSplat]:
    palette = {
        Semantic.ROAD: (0.45, 0.45, 0.48),
        Semantic.LANE: (0.95, 0.85, 0.2),
        Semantic.DAMAGE: (0.75, 0.25, 0.15),
        Semantic.VEHICLE: (0.15, 0.35, 0.75),
        Semantic.PEDESTRIAN: (0.9, 0.4, 0.15),
        Semantic.FREESPACE: (0.3, 0.7, 0.35),
        Semantic.CURB: (0.6, 0.6, 0.55),
    }
    out: list[GaussianSplat] = []
    xyz = cloud.xyz
    labels = cloud.labels if cloud.labels is not None else np.zeros(len(xyz), dtype=int)
    for i in range(0, len(xyz), stride):
        sem = Semantic(int(labels[i])) if int(labels[i]) in Semantic._value2member_map_ else Semantic.ROAD
        scale = 0.35 if sem in (Semantic.VEHICLE, Semantic.PEDESTRIAN) else 0.18
        out.append(GaussianSplat(mean=xyz[i].copy(), scale=scale, opacity=0.85, semantic=sem, color=palette[sem]))
    for x, y, dz in detect_potholes(surface):
        mid = surface.height[len(surface.ys) // 2]
        out.append(
            GaussianSplat(
                mean=np.array([x, y, float(np.interp(x, surface.xs, mid))]),
                scale=0.4,
                opacity=0.9,
                semantic=Semantic.DAMAGE,
                color=palette[Semantic.DAMAGE],
            )
        )
    return out


def reconstruct(cloud: SparseCloud | None = None, seed: int = 0) -> Scene:
    if cloud is None:
        cloud = sample_sparse(seed=seed)
    surface = fit_surface(cloud)
    potholes = detect_potholes(surface)
    occupancy = occupany_from_surface(surface)
    gaussians = gaussians_from_scene(cloud, surface)
    xx, yy = surface.grid
    gt = analytic_road(np.column_stack([xx.ravel(), yy.ravel()])).reshape(surface.height.shape)
    rmse = float(np.sqrt(np.mean((surface.height - gt) ** 2)))
    metrics = {
        "n_points": float(cloud.xyz.shape[0]),
        "n_gaussians": float(len(gaussians)),
        "n_potholes": float(len(potholes)),
        "free_frac": float(occupancy.mean()),
        "rmse_m": rmse,
    }
    return Scene(cloud=cloud, surface=surface, gaussians=gaussians, occupancy=occupancy, potholes=potholes, metrics=metrics)
