# My OpenCV Course Projects

## Overview
I’ve spent time diving into OpenCV (Open Source Computer Vision Library) to build a strong foundation in computer vision and image processing. Through a series of hands‑on examples, I learned how to manipulate images and video streams in real time, enabling me to create projects ranging from simple filters to object detection applications.

## What I Learned
Throughout this course, I gained practical experience with:

- **Image I/O:** I read, display, and save images using `cv2.imread`, `cv2.imshow`, and `cv2.imwrite`.
- **Video Streams:** I captured frames from webcams and video files with `cv2.VideoCapture` and processed them in a loop.
- **Color Space Conversions:** I explored BGR, Grayscale, and HSV conversions via `cv2.cvtColor`.
- **Noise Reduction:** I applied Gaussian blur (`cv2.GaussianBlur`) to smooth images before analysis.
- **Edge Detection:** I used the Canny algorithm (`cv2.Canny`) to highlight edges.
- **Morphological Operations:** I performed dilation and erosion (`cv2.dilate`, `cv2.erode`) to refine features.
- **Drawing Primitives:** I annotated images with lines, rectangles, circles, and text (`cv2.line`, `cv2.rectangle`, `cv2.circle`, `cv2.putText`).
- **Perspective Transforms:** I corrected image perspective with `cv2.getPerspectiveTransform` and `cv2.warpPerspective`.
- **Image Stacking:** I created composite displays of multiple processing stages using a reusable `stackImages` utility.
- **Interactive Controls:** I built trackbars (`cv2.createTrackbar`) to tune HSV-based color detection in real time.
- **Contour Analysis:** I detected and classified shapes by computing contour area, perimeter, and vertex approximation.
- **Haar Cascade Detection:** I implemented face and license‑plate detection with pre‑trained classifiers (`cv2.CascadeClassifier`, `detectMultiScale`).
- **Region of Interest (ROI):** I extracted and saved specific subregions from images and video frames.

## Project Structure
```bash
project-root/
├── Resources/                       # Sample images, videos, and Haar cascades
├── utils/                           # Reusable utilities
│   └── stackimages.py               # Function to stack images for comparison
├── chapter1_read_and_display.py     # Basic image I/O examples
├── chapter2_video_loop.py           # Real-time webcam video loop
├── chapter3_filters_and_edges.py    # Noise reduction and edge detection
├── chapter4_drawing.py              # Drawing shapes and adding text
├── chapter5_perspective.py          # Perspective transformation examples
├── chapter6_color_detection.py      # HSV color detection with trackbars
├── chapter7_contours.py             # Contour detection and shape classification
├── chapter8_face_detection.py       # Face detection using Haar cascades
└── chapter9_license_plate.py        # License plate detection and ROI extraction
```

## Installation
1. **Clone this repository:**
   ```bash
   git clone https://your-repo-url.git
   cd your-repo
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install opencv-python numpy
   ```
4. **Verify resources:**
   Make sure the `Resources/` folder contains all required images and cascade XML files.

## Usage
I can run any chapter script to see its functionality. For example:
```bash
python chapter8_face_detection.py
```
If I want to compare several processing steps side by side, I import and use my stacking utility:
```python
from utils.stackimages import stackImages
imgStack = stackImages(0.5, ([img, imgGray], [imgCanny, imgResult]))
cv2.imshow('Comparison', imgStack)
```

## Contributing
I welcome suggestions, improvements, and new OpenCV recipes. Feel free to open an issue or submit a pull request.

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for more details.

