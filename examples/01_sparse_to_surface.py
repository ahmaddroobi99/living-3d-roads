from living_roads.pipeline import reconstruct

if __name__ == "__main__":
    scene = reconstruct(seed=0)
    print(scene.metrics)
    if scene.potholes:
        x, y, dz = scene.potholes[0]
        print(f"pothole at ({x:.1f}, {y:.1f}) depth {dz*100:.1f} cm")
