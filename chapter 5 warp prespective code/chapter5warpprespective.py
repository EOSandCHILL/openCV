import cv2  # Import the OpenCV library for image processing
import numpy as np  # Import NumPy for numerical operations, particularly with arrays

# Load the image from the specified path (in this case, "cards.jpg")
img = cv2.imread("../Resources/cards.jpg")

# Define the dimensions for the output image after perspective transformation
width, height = 250, 350

# Specify the four source points from the input image that define the region of interest.
# These points should ideally correspond to the corners of the object you want to transform.
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])

# Specify the four destination points where the source points will be mapped.
# The points define the corners of the output image with the specified width and height.
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Calculate the perspective transformation matrix using the source and destination points.
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation to the input image using the computed matrix.
# The resulting image (imgOutput) will have a size defined by (width, height).
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Display the original image in a window titled "Image"
cv2.imshow("Image", img)

# Display the transformed (warped) image in a window titled "Output"
cv2.imshow("Output", imgOutput)

# Wait indefinitely for a key press so the windows stay open until the user decides to close them.
cv2.waitKey(0)