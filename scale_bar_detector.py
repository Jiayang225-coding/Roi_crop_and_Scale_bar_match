
import cv2
import numpy as np
import os

def detect_scale_bar_and_get_ratio(image_path, template_path, template_length_mils, visualize=False):
    """
    Detects a scale bar from a template in a high-resolution microscope image,
    and calculates the mils-per-pixel ratio.

    Args:
        image_path (str): Path to the main microscope image.
        template_path (str): Path to the template image (e.g., "200 mils" bar).
        template_length_mils (float): Physical length of the scale bar in mils.
        visualize (bool): If True, saves a visualization of the best match.

    Returns:
        mils_per_pixel (float): Conversion ratio from pixel to mils.
        match_info (dict): Details of the best match (position, size, score).
    """
    # Load images
    main_img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if main_img is None:
        raise FileNotFoundError(f"Main image not found at: {image_path}")
    template_img = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template_img is None:
        raise FileNotFoundError(f"Template image not found at: {template_path}")

    # Convert to grayscale
    main_gray = cv2.cvtColor(main_img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)

    # Normalize
    main_gray = cv2.normalize(main_gray, None, 0, 255, cv2.NORM_MINMAX)
    template_gray = cv2.normalize(template_gray, None, 0, 255, cv2.NORM_MINMAX)

    best_score = -1
    best_match = None

    # Try both enlarging and shrinking the template
    for direction in ["up", "down"]:
        factor = 1.0
        for _ in range(90):
            if direction == "up":
                factor += 0.01
            else:
                factor -= 0.01
                if factor <= 0:
                    break

            # Ensure valid resize dimensions
            new_h = int(template_gray.shape[0] * factor)
            new_w = int(template_gray.shape[1] * factor)
            if new_h < 1 or new_w < 1:
                continue

            resized_template = cv2.resize(template_gray, (new_w, new_h))
            if resized_template.shape[0] > main_gray.shape[0] or resized_template.shape[1] > main_gray.shape[1]:
                continue

            result = cv2.matchTemplate(main_gray, resized_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > best_score:
                best_score = max_val
                best_match = {
                    "resize_factor": factor,
                    "max_val": max_val,
                    "top_left": max_loc,
                    "width": resized_template.shape[1],
                    "height": resized_template.shape[0]
                }

    if not best_match:
        raise RuntimeError("Failed to detect the scale bar.")

    # Calculate mils-per-pixel
    mils_per_pixel = template_length_mils / best_match["width"]

    if visualize:
        bottom_right = (
            best_match["top_left"][0] + best_match["width"],
            best_match["top_left"][1] + best_match["height"]
        )
        visual = main_img.copy()
        cv2.rectangle(visual, best_match["top_left"], bottom_right, (0, 0, 255), 3)
        vis_path = os.path.join(os.path.dirname(image_path), "scale_bar_detected.jpg")
        cv2.imwrite(vis_path, visual)
        print(f"Match visual saved to: {vis_path}")

    return mils_per_pixel, best_match
