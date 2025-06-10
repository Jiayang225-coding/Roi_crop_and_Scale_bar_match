import cv2
import os
import numpy as np

def interactive_crop(image_path, output_dir="cropped", resize_factor=0.3, crop_size_factor=0.05):
    """
    Launch an interactive cropping tool for high-resolution images.

    Parameters:
    - image_path (str): Path to the input image.
    - output_dir (str): Directory to save cropped results.
    - resize_factor (float): Resizing scale for visualization.
    - crop_size_factor (float): Initial size of cropped square relative to image.
    """
    os.makedirs(output_dir, exist_ok=True)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Could not read image from path: {image_path}")

    img_name = os.path.splitext(os.path.basename(image_path))[0]
    img_resize = cv2.resize(img, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_NEAREST)
    cropping_size_factor = crop_size_factor
    cropped_image_counter = [1]  # mutable for nested scope

    def mid_point_crop(image, point):
        nonlocal cropping_size_factor
        h, w = image.shape[:2]
        length_half = round(max(h, w) * cropping_size_factor)
        cx, cy = point

        x1 = max(cx - length_half, 0)
        x2 = min(cx + length_half, w)
        y1 = max(cy - length_half, 0)
        y2 = min(cy + length_half, h)
        return image[y1:y2, x1:x2]

    def mouse_callback(event, x, y, flags, param):
        nonlocal cropping_size_factor
        if event == cv2.EVENT_LBUTTONDOWN:
            cx, cy = int(x / resize_factor), int(y / resize_factor)
            cropped = mid_point_crop(img, (cx, cy))
            fname = f"{img_name}_crop{cropped_image_counter[0]}.jpg"
            cv2.imwrite(os.path.join(output_dir, fname), cropped)
            print(f"[Saved] {fname} | size: {cropped.shape}")
            cropped_image_counter[0] += 1
        elif event == cv2.EVENT_MOUSEWHEEL:
            cropping_size_factor += 0.005 if flags > 0 else -0.005
            cropping_size_factor = max(0.01, min(cropping_size_factor, 0.2))  # clamp
            print(f"[Crop size factor] {cropping_size_factor:.3f}")

    print("[Instructions] Click to crop | Scroll to resize crop window | ESC to exit")
    cv2.namedWindow("ROI Cropper")
    cv2.setMouseCallback("ROI Cropper", mouse_callback)

    while True:
        cv2.imshow("ROI Cropper", img_resize)
        key = cv2.waitKey(20) & 0xFF
        if key == 27:  # ESC
            break

    cv2.destroyAllWindows()
