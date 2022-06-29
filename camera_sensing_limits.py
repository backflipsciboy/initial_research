#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

UM_TO_MM = 1/1000
MM_TO_M = 1/1000

# Camera Info
# IMX265
# pixel_size_um = np.array([3.45, 3.45])
# pixel_num = np.array([2064, 1544])
# # sensor_diag_mm = 8.9
# # sensor_ratio = 1/1.8
# # sensor_length_y_mm = sensor_diag_mm * np.sin(np.arctan(sensor_ratio))
# # sensor_length_mm = np.array([sensor_length_y_mm / sensor_ratio, sensor_length_y_mm])
# sensor_length_mm = pixel_num * pixel_size_um * UM_TO_MM
# focal_length_mm = 12
# n = 1.8
# fps = 30

# # BOSON 95 degree FOV
# pixel_size_um = np.array([[12, 12]])
# pixel_num = np.array([[640, 512]])
# sensor_length_mm = pixel_num * pixel_size_um * UM_TO_MM
# focal_length_mm = 4.9
# n = 1.1
# fps = 60

# BOSON 24 degree FOV
pixel_size_um = np.array([[12, 12]])
pixel_num = np.array([[640, 512]])
sensor_length_mm = pixel_num * pixel_size_um * UM_TO_MM
focal_length_mm = 18
n = 1.0
fps = 60

#Scene Info
z_m = np.array([np.linspace(10, 200, num=200)]).T
velocity_m_per_s = np.array([[35, 0]])

pixel_resolution_m_per_px = (z_m * sensor_length_mm) / (focal_length_mm * pixel_num)

scene_size_m = z_m * sensor_length_mm / focal_length_mm
# scene_overlap = (scene_size_m - (velocity_m_per_s / fps)) / scene_size_m
scene_area_m_2 = scene_size_m[:, 0] * scene_size_m[:, 1]
scene_change_m = velocity_m_per_s / fps
scene_overlap = (scene_area_m_2 - (scene_change_m[:, 0] * scene_size_m[:, 1] + scene_change_m[:, 1] * scene_size_m[:, 0] - scene_change_m[:, 0] * scene_change_m[:, 1])) / scene_area_m_2

fig = plt.figure()
fig.set_size_inches(20, 5)
plt.subplot(131)
plt.plot(z_m, scene_overlap, 'o')
plt.xlabel("AGL (m)")
plt.ylabel("Scene Overlap (%)")
plt.title(f"Scene Overlap At Speeds: X={velocity_m_per_s[:, 0].item()} m/s, Y={velocity_m_per_s[:, 1].item()} m/s")

plt.subplot(132)
plt.plot(z_m, pixel_resolution_m_per_px, "o")
plt.xlabel("AGL (m)")
plt.ylabel("Pixel Resolution (m/px)")
plt.title(f"Pixel Resolution")
plt.legend(["X", "Y"])

plt.subplot(133)
plt.plot(z_m, scene_area_m_2, 'o')
plt.xlabel("AGL (m)")
plt.ylabel("Scene Area (m^2)")
plt.title(f"Scene Size")
plt.show()