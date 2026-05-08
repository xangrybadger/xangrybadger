import os
import numpy as np
from stl import mesh
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

stl_path = os.environ.get("STL_PATH", "assets/skyline.stl")
png_path = os.environ.get("PNG_PATH", "assets/skyline.png")

skyline_mesh = mesh.Mesh.from_file(stl_path)
vectors = skyline_mesh.vectors

all_x = vectors[:, :, 0].flatten()
all_y = vectors[:, :, 1].flatten()
all_z = vectors[:, :, 2].flatten()

x_min, x_max = all_x.min(), all_x.max()
y_min, y_max = all_y.min(), all_y.max()
z_min, z_max = all_z.min(), all_z.max()
z_range = max(abs(z_max - z_min), 0.001)

step = max(1, len(vectors) // 8000)
sampled = vectors[::step]

sage = np.array([0x45 / 255, 0x6A / 255, 0x4B / 255])
amber = np.array([0x8B / 255, 0x69 / 255, 0x14 / 255])

fig = plt.figure(figsize=(16, 8), facecolor="#0D1117")
ax = fig.add_subplot(111, projection="3d", facecolor="#0D1117")

polygons = []
face_colors = []

for tri in sampled:
    flipped = tri.copy()
    flipped[:, 2] = -flipped[:, 2]
    polygons.append(flipped)
    centroid_z = flipped[:, 2].mean()
    t = np.clip(centroid_z / z_range, 0, 1)
    c = np.clip((1 - t) * sage * 0.5 + t * amber, 0, 1)
    face_colors.append((*c, 0.9))

poly3d = Poly3DCollection(polygons, linewidths=0.1, edgecolors="#1A2A1A")
poly3d.set_facecolor(face_colors)
ax.add_collection3d(poly3d)

padding_x = (x_max - x_min) * 0.05
padding_y = (y_max - y_min) * 0.05
padding_z = z_range * 0.1

ax.set_xlim(x_min - padding_x, x_max + padding_x)
ax.set_ylim(y_max + padding_y, y_min - padding_y)
ax.set_zlim(-padding_z, z_range + padding_z * 2)
ax.view_init(elev=35, azim=-60)
ax.set_axis_off()
ax.grid(False)

try:
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor("none")
    ax.yaxis.pane.set_edgecolor("none")
    ax.zaxis.pane.set_edgecolor("none")
except Exception:
    pass

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig(png_path, dpi=150, facecolor="#0D1117", bbox_inches="tight", pad_inches=0.1)
plt.close()

img = Image.open(png_path)
w, h = img.size
max_w = 960
if w > max_w:
    ratio = max_w / w
    new_h = int(h * ratio)
    img = img.resize((max_w, new_h), Image.LANCZOS)
    img.save(png_path)

print(f"Skyline rendered: {png_path}")
