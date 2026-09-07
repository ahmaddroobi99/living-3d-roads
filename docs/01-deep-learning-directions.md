# Deep Learning Directions

Eight methods from the poster *From Sparse Road Points to Living 3D Roads*. Eight live GitHub repos per card. Poster names stay as printed; the first repo is the closest official implementation of what the card actually describes.

## 1. NeRF-Drive — Differentiable triangulation

Convert sparse road and object points into optimized surfaces.

- [NVlabs/EmerNeRF](https://github.com/NVlabs/EmerNeRF) — self-supervised 4D street NeRF
- [fudan-zvg/S-NeRF](https://github.com/fudan-zvg/S-NeRF) — ICLR 2023 street-view NeRF + S-NeRF++
- [nerfstudio-project/nerfstudio](https://github.com/nerfstudio-project/nerfstudio) — production NeRF toolkit
- [bmild/nerf](https://github.com/bmild/nerf) — original NeRF
- [nerfstudio-project/nerfacc](https://github.com/nerfstudio-project/nerfacc) — fast NeRF acceleration
- [PJLab-ADG/neuralsim](https://github.com/PJLab-ADG/neuralsim) — StreetSurf street-view surfaces
- [meshsplatting/mesh-splatting](https://github.com/meshsplatting/mesh-splatting) — differentiable triangulation / mesh primitives
- [NVlabs/nvdiffrec](https://github.com/NVlabs/nvdiffrec) — differentiable tetrahedral meshes

## 2. UrbanImplicit — Neural implicit surfaces

Infer continuous road and object surfaces from incomplete data.

- [PJLab-ADG/neuralsim](https://github.com/PJLab-ADG/neuralsim) — official StreetSurf
- [Totoro97/NeuS](https://github.com/Totoro97/NeuS) — canonical neural SDF
- [NVlabs/neuralangelo](https://github.com/NVlabs/neuralangelo) — high-fidelity neural surfaces
- [19reborn/NeuS2](https://github.com/19reborn/NeuS2) — faster NeuS
- [autonomousvision/sdfstudio](https://github.com/autonomousvision/sdfstudio) — SDF reconstruction toolbox
- [lioryariv/volsdf](https://github.com/lioryariv/volsdf) — volume-rendered SDF
- [bennyguo/instant-nsr-pl](https://github.com/bennyguo/instant-nsr-pl) — instant neural surface
- [NVlabs/instant-ngp](https://github.com/NVlabs/instant-ngp) — instant neural graphics primitives

## 3. DepthFormer — Learned depth interpolation

Fill gaps between sparse camera / LiDAR depth observations.

- [zhyever/Monocular-Depth-Estimation-Toolbox](https://github.com/zhyever/Monocular-Depth-Estimation-Toolbox) — hosts DepthFormer
- [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2) — foundation monocular depth
- [LiheYoung/Depth-Anything](https://github.com/LiheYoung/Depth-Anything) — original Depth Anything
- [ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)
- [DepthAnything/Video-Depth-Anything](https://github.com/DepthAnything/Video-Depth-Anything)
- [princeton-vl/RAFT-Stereo](https://github.com/princeton-vl/RAFT-Stereo)
- [NVlabs/FoundationStereo](https://github.com/NVlabs/FoundationStereo)
- [colmap/colmap](https://github.com/colmap/colmap) — sparse-to-dense SfM / MVS

## 4. GaussianDrive — Gaussian + mesh

Combine geometry with photorealistic scene appearance.

- [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) — canonical 3DGS
- [zju3dv/street_gaussians](https://github.com/zju3dv/street_gaussians) — ECCV 2024 Street Gaussians
- [VDIGPKU/DrivingGaussian](https://github.com/VDIGPKU/DrivingGaussian) — CVPR 2024 surround driving GS
- [ziyc/drivestudio](https://github.com/ziyc/drivestudio) — OmniRe + multi-representation trainer
- [nerfstudio-project/gsplat](https://github.com/nerfstudio-project/gsplat) — fast GS rasterizer
- [hbb1/2d-gaussian-splatting](https://github.com/hbb1/2d-gaussian-splatting) — geometrically accurate surfaces
- [Anttwo/SuGaR](https://github.com/Anttwo/SuGaR) — surface-aligned Gaussians
- [Anttwo/MILo](https://github.com/Anttwo/MILo) — mesh + Gaussian hybrid

## 5. GeoGuideNet — Depth / normal-guided surface

Recover accurate road, vehicle and infrastructure surfaces.

- [maturk/dn-splatter](https://github.com/maturk/dn-splatter) — depth/normal-guided 3DGS
- [hbb1/2d-gaussian-splatting](https://github.com/hbb1/2d-gaussian-splatting)
- [zju3dv/PGSR](https://github.com/zju3dv/PGSR)
- [hanl2010/SparseRecon](https://github.com/hanl2010/SparseRecon) — ICCV 2025 sparse-view implicit + depth cues
- [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2)
- [NVlabs/neuralangelo](https://github.com/NVlabs/neuralangelo)
- [baegwangbin/surface_normal_uncertainty](https://github.com/baegwangbin/surface_normal_uncertainty)
- [XuqianRen/AGS_Mesh](https://github.com/XuqianRen/AGS_Mesh)

## 6. DynSurf — Dynamic neural surface

Continuously reconstruct moving vehicles and road users.

- [ziyc/drivestudio](https://github.com/ziyc/drivestudio) — OmniRe SMPL + deformable Gaussians
- [nnanhuang/S3Gaussian](https://github.com/nnanhuang/S3Gaussian) — self-supervised street dynamics
- [zju3dv/street_gaussians](https://github.com/zju3dv/street_gaussians)
- [NVlabs/EmerNeRF](https://github.com/NVlabs/EmerNeRF)
- [ingra14m/Deformable-3D-Gaussians](https://github.com/ingra14m/Deformable-3D-Gaussians)
- [JonathonLuiten/Dynamic3DGaussians](https://github.com/JonathonLuiten/Dynamic3DGaussians)
- [albertpumarola/D-NeRF](https://github.com/albertpumarola/D-NeRF)
- [qingpowuwu/emd](https://github.com/qingpowuwu/emd) — explicit motion modeling for street GS

## 7. 4D-DriveGS — 4D Gaussian reconstruction

Represent geometry and motion jointly across space and time.

- [fudan-zvg/4d-gaussian-splatting](https://github.com/fudan-zvg/4d-gaussian-splatting) — ICLR 2024 4DGS
- [chengweialan/DeSiRe-GS](https://github.com/chengweialan/DeSiRe-GS) — 4D street GS + surface
- [fangzhou2000/DrivingForward](https://github.com/fangzhou2000/DrivingForward) — feed-forward driving 3DGS
- [TuojingAI/ReconDrive](https://github.com/TuojingAI/ReconDrive) — feed-forward 4DGS for AV
- [hustvl/4DGaussians](https://github.com/hustvl/4DGaussians)
- [ziyc/drivestudio](https://github.com/ziyc/drivestudio)
- [nnanhuang/S3Gaussian](https://github.com/nnanhuang/S3Gaussian)
- [VDIGPKU/DrivingGaussian](https://github.com/VDIGPKU/DrivingGaussian)

## 8. SceneSem3D — Semantic 3D reconstruction

Attach road / object meaning to reconstructed geometry.

- [weiyithu/SurroundOcc](https://github.com/weiyithu/SurroundOcc) — surround-view semantic occupancy
- [OpenDriveLab/OpenScene](https://github.com/OpenDriveLab/OpenScene) — occupancy benchmark
- [DavidXu-JJ/StreetUnveiler](https://github.com/DavidXu-JJ/StreetUnveiler) — semantic-aware street 2DGS
- [OpenDriveLab/UniAD](https://github.com/OpenDriveLab/UniAD)
- [JeffWang987/OpenOccupancy](https://github.com/JeffWang987/OpenOccupancy)
- [worldbench/awesome-3d-4d-world-models](https://github.com/worldbench/awesome-3d-4d-world-models)
- [taco-group/GenAI4AD](https://github.com/taco-group/GenAI4AD)
- [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting)
