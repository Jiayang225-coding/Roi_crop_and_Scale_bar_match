import cv2
import numpy as np
from roi_cropper import interactive_crop


interactive_crop(r"img/w2.png", output_dir=r"crop_result", resize_factor=0.3, crop_size_factor=0.05)


