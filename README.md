# ROI & Scale Bar Toolset for Microscope Images

## 🔒 Confidential Notice

This repository contains two general-purpose tools extracted from a larger automated crack measurement system developed for high-resolution microscope images.

Due to internal IP protection policies, the trained deep learning segmentation model and the post-processing logic for crack tip detection and physical measurement are **not included**.

However, the two tools provided here are fully reusable and applicable to a wide range of microscope image workflows:
- 🟦 **ROI Cropper** for hole-centered region selection
- 🟩 **Scale Bar Detector** for physical unit conversion using embedded scale bars

---

## 🧭 Module Overview

| Files | Description |
|--------|-------------|
| **ROI Cropper** (`roi_cropper.py`, `crop_test.py`, `w2.png`) | Interactive OpenCV-based tool for selecting region of interest (ROI) around drilled holes or defects. `roi_cropper.py` contains the core function, and `crop_test.py` is an example script using `w2.png`. |
| **Scale Bar Detector** (`scale_bar_detector.py`, `scale_bar_match_test.py`, `material.png`, `200_scale.png`) | Detects embedded scale bars via multi-scale template matching and computes physical scale in mils/pixel. `scale_bar_detector.py` is the core module, and `scale_bar_match_test.py` demonstrates detection using `material.png` and template `200_scale.png`. |


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
<h2>Program walk-through:</h2>

Image_cropping video:
https://github.com/user-attachments/assets/c207cf59-4f9f-4b42-b24e-baf25dfd097c
<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
---

## 💻 Installation


Install dependencies manually:

```bash
pip install opencv-python numpy



