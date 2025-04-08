import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations
from pyutils.stackimages import stackImages

# Load an image from the specified path (used for stacking demonstration)
img = cv2.imread("../Resources/linux.png")

# Reload the image for further processing
img = cv2.imread("../Resources/linux.png")
# Convert the image to grayscale for demonstration purposes
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Create a stacked image grid with two rows:
# First row: original image, grayscale image, original image
# Second row: original image, original image, original image
imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))

# The following commented code shows alternative stacking methods:
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)

# Display the final stacked image grid in a window titled "ImageStack"
cv2.imshow("ImageStack",imgStack)

# Wait indefinitely until a key is pressed before closing the window
cv2.waitKey(0)