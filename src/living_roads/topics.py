"""Exact poster cards from *From Sparse Road Points to Living 3D Roads*."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Topic:
    slug: str
    section: str
    name: str
    subtitle: str
    blurb: str
    real_anchor: str


METHODS: tuple[Topic, ...] = (
    Topic(
        "nerf-drive",
        "directions",
        "NeRF-Drive",
        "Differentiable Triangulation",
        "Convert sparse road and object points into optimized surfaces.",
        "Street-view NeRFs (S-NeRF, EmerNeRF) lift sparse posed images + LiDAR into a continuous volumetric field.",
    ),
    Topic(
        "urbanimplicit",
        "directions",
        "UrbanImplicit",
        "Neural Implicit Surfaces",
        "Infer continuous road and object surfaces from incomplete data.",
        "StreetSurf / neuralsim train an implicit SDF on street views so the zero-level set is a watertight road mesh.",
    ),
    Topic(
        "depthformer",
        "directions",
        "DepthFormer",
        "Learned Depth Interpolation",
        "Fill gaps between sparse camera/LiDAR depth observations.",
        "Transformer depth-completion networks densify a sparse LiDAR sweep onto the image plane before surface fitting.",
    ),
    Topic(
        "gaussiandrive",
        "directions",
        "GaussianDrive",
        "Gaussian + Mesh",
        "Combine geometry with photorealistic scene appearance.",
        "Street Gaussians / DrivingGaussian attach 3D Gaussians to tracked objects and a static background mesh.",
    ),
    Topic(
        "geoguidenet",
        "directions",
        "GeoGuideNet",
        "Depth/Normal-Guided Surface",
        "Recover accurate road, vehicle and infrastructure surfaces.",
        "Normal- and depth-guided reconstruction (StreetSurf cues, SparseRecon) regularize the surface with geometric priors.",
    ),
    Topic(
        "dynsurf",
        "directions",
        "DynSurf",
        "Dynamic Neural Surface",
        "Continuously reconstruct moving vehicles and road users.",
        "OmniRe / S3Gaussian / PVG decompose static background from deformable actors without baking motion into the road.",
    ),
    Topic(
        "4d-drivegs",
        "directions",
        "4D-DriveGS",
        "4D Gaussian Reconstruction",
        "Represent geometry and motion jointly across space and time.",
        "DeSiRe-GS, DrivingForward and ReconDrive predict 4D Gaussians that render a driving log at any time and viewpoint.",
    ),
    Topic(
        "scenesem3d",
        "directions",
        "SceneSem3D",
        "Semantic 3D Reconstruction",
        "Attach road/object meaning to reconstructed geometry.",
        "HUGS / StreetUnveiler / semantic occupancy attach lane, vehicle, pedestrian and damage labels to the 3D field.",
    ),
)

APPLICATIONS: tuple[Topic, ...] = (
    Topic(
        "autonomous-driving",
        "applications",
        "Autonomous Driving",
        "Continuous 3D environment for safe navigation",
        "A living road model is the geometry layer an AV stack plans against.",
        "nuScenes, Waymo Open, and EmerNeRF-style reconstructions feed perception and planning.",
    ),
    Topic(
        "road-surface-reconstruction",
        "applications",
        "Road Surface Reconstruction",
        "Accurate and continuous road geometry",
        "Turn sparse curb and crown samples into a driveable surface.",
        "NeRO and StreetSurf specialize in the road plane itself, not just the photoreal backdrop.",
    ),
    Topic(
        "pothole-road-damage-mapping",
        "applications",
        "Pothole & Road Damage Mapping",
        "Detect and measure surface deformation",
        "Residual height against a smooth crown flags depressions in centimetres.",
        "Dense surface + semantic labels is how inspection fleets quantify damage.",
    ),
    Topic(
        "pedestrian-cyclist-modeling",
        "applications",
        "Pedestrian & Cyclist Modeling",
        "3D representation of moving road users",
        "Non-rigid actors need a different primitive than the static road.",
        "OmniRe uses SMPL-Gaussians for pedestrians and deformable Gaussians for cyclists.",
    ),
    Topic(
        "vehicle-shape-reconstruction",
        "applications",
        "Vehicle Shape Reconstruction",
        "Complete vehicle geometry from partial views",
        "A passing car is seen from one side; the model still has to close the hull.",
        "Street Gaussians optimize a per-vehicle Gaussian cloud inside a tracked box.",
    ),
    Topic(
        "intersection-digital-twins",
        "applications",
        "Intersection Digital Twins",
        "Realistic, structured 3D junction models",
        "Junctions concentrate topology, signals and conflict points.",
        "HD-map loaders plus neural reconstruction give a queryable twin of the junction.",
    ),
    Topic(
        "hd-map-generation",
        "applications",
        "HD Map Generation",
        "Lanes, traffic signs and infrastructure mapping",
        "Vector lanes and signs sit on top of the reconstructed surface.",
        "MapTR / MapTracker emit polylines; OpenDRIVE writers persist them.",
    ),
    Topic(
        "collision-freespace-estimation",
        "applications",
        "Collision & Free-Space Estimation",
        "Dense geometry for obstacle and free-space reasoning",
        "Occupancy is the surface queried as 'can I drive here?'",
        "Height above the fitted road plus semantic class yields a free-space grid.",
    ),
    Topic(
        "av-simulation",
        "applications",
        "Autonomous-Vehicle Simulation",
        "Real-world 3D environments for testing and training",
        "Replay reconstructed drives, then insert new actors.",
        "CARLA + Street-Gaussian / NuRec pipelines close the loop from log to simulator.",
    ),
)


def all_topics() -> tuple[Topic, ...]:
    return METHODS + APPLICATIONS
