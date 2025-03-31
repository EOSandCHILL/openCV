import cv2  # Import the OpenCV library for image processing
import numpy as np  # Import NumPy for numerical operations, particularly useful for array manipulation

# Load the image from the specified path.
# The image "Jesko.jpeg" should be located in the "../Resources/" directory.
img = cv2.imread("../Resources/Jesko.jpeg")

# Print the shape (dimensions) of the original image.
# The output will be in the form (height, width, number of color channels).
print(img.shape)

# Resize the image to a new size of 500 pixels width and 300 pixels height.
imgResize = cv2.resize(img, (500, 300))

# Print the shape of the resized image to verify the new dimensions.
print(imgResize.shape)

# Crop the image by selecting a region of interest.
# Here, we select rows 0 to 200 and columns 200 to 500 from the original image.
imgCropped = img[0:200, 200:500]

# Display the original image in a window titled "Jesko"
cv2.imshow("Jesko", img)
# Display the resized image in a window titled "Jesko Resize"
cv2.imshow("Jesko Resize", imgResize)
# Display the cropped image in a window titled "Jesko Cropped"
cv2.imshow("Jesko Cropped", imgCropped)

# Wait indefinitely until a key is pressed.
# This keeps the image windows open until you manually close them.
cv2.waitKey(0)