import cv2  # Import OpenCV library for image processing and computer vision
import numpy as np  # Import NumPy library for numerical operations, especially on arrays

# Create a 5x5 kernel (matrix) of ones with data type uint8 for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Load an image from the specified path. The image is expected to be in color.
img = cv2.imread('../Resources/linux.png')

# Convert the color image to grayscale, which simplifies further processing
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the grayscale image with a 7x7 kernel to reduce noise
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# Detect edges in the original color image using the Canny edge detector
imgCanny = cv2.Canny(img, 100, 100)

# Dilate (expand) the edges found by Canny using the kernel to make the edges thicker
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# Erode (shrink) the dilated image, which can help remove small imperfections
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# Display the original image in a window titled "Original"
cv2.imshow('Original', img)
# Display the grayscale image in a window titled "Gray Image"
cv2.imshow("Gray Image", imgGray)
# Display the blurred image in a window titled "Blur Image"
cv2.imshow("Blur Image", imgBlur)
# Display the edge-detected image in a window titled "Canny Image"
cv2.imshow("Canny Image", imgCanny)
# Display the dilated image in a window titled "Dialation Image"
cv2.imshow("Dialation Image", imgDialation)
# Display the eroded image in a window titled "Eroded Image"
cv2.imshow("Eroded Image", imgEroded)

# Wait indefinitely until a key is pressed, so that the windows stay open
cv2.waitKey(0)