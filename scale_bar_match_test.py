import cv2
import numpy as np

from scale_bar_detector import detect_scale_bar_and_get_ratio

mils_per_pixel, match_info = detect_scale_bar_and_get_ratio(
    image_path= r"img/material.png",
    template_path= r"img/200_scale.png",
    template_length_mils=200.0,
    visualize=True
)

print("Scale ratio (mils/pixel):", mils_per_pixel)