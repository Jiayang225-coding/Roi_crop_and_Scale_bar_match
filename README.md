# ROI & Scale Bar Toolset for Microscope Images

## 🔒 Confidential Notice

This repository contains two general-purpose tools extracted from a larger automated crack measurement system developed for high-resolution microscope images.

Due to internal IP protection policies, the trained deep learning segmentation model and the post-processing logic for crack tip detection and physical measurement are **not included**.

However, the two tools provided here are fully reusable and applicable to a wide range of microscope image workflows:
- 🟦 **ROI Cropper** for hole-centered region selection
- 🟩 **Scale Bar Detector** for physical unit conversion using embedded scale bars

---

## 🧭 Module Overview

| Module | Description |
|--------|-------------|
| [`roi_crop/`](./roi_crop) | Interactive tool to crop hole-centered or defect-centered regions |
| [`scale_bar_match_automation/`](./scale_bar_match_automation) | Detect scale bar and compute mils-per-pixel ratio automatically |

---

## 🖼 Sample Workflow

1. Use the ROI Cropper tool to zoom into regions around laser/EDM-drilled holes.
2. Use the Scale Bar Detector to extract the scale bar and compute the length unit conversion.
3. Combine results for automated or manual measurement of cracks, pores, or microstructural features.

---

## ⚠️ Notes
1. The cv2.matchTemplate algorithm may return high match scores for visually similar but incorrect regions.
2. It is recommended to limit the search area or scale range in such cases.
3. These tools are modular and designed to integrate into broader ML or image-processing pipelines.


---

## 👨‍💻 Author
Developed by JiaYang Li — Materials Engineer specialized in AI-assisted image analysis for microstructure evaluation.

---

## 💻 Installation


Install dependencies manually:

```bash
pip install opencv-python numpy



