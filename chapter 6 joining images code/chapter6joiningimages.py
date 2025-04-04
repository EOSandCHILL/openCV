import cv2  # Import OpenCV for image processing functions
import numpy as np  # Import NumPy for numerical operations and array handling

# Load an image from the specified path; this image will be used for stacking
img = cv2.imread("../Resources/linux.png")


# Define a function to stack multiple images in a grid-like arrangement
def stackImages(scale, imgArray):
    # Get the number of rows and columns from the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if the first element of the array is a list (i.e., 2D array of images)
    rowsAvailable = isinstance(imgArray[0], list)
    # Get the width and height of the first image (used as a reference)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        # If imgArray is 2D, iterate through each image
        for x in range(rows):
            for y in range(cols):
                # Resize each image:
                # If the current image's dimensions match the reference, resize by the scale factor
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # Otherwise, force resize to the reference image's dimensions (scaled)
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (width, height), None, scale, scale)
                # Convert grayscale images to BGR format to ensure consistency when stacking
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image placeholder with the same size as the reference image
        imageBlank = np.zeros((height, width, 3), np.uint8)
        # Prepare a list to hold horizontally stacked images for each row
        hor = [imageBlank] * rows
        # Stack images horizontally for each row
        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack the rows vertically to get the final combined image
        ver = np.vstack(hor)
    else:
        # For a 1D array of images, process each image similarly
        for x in range(rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Stack the images horizontally if there is only one row
        hor = np.hstack(imgArray)
        ver = hor
    # Return the final stacked image
    return ver


# Reload the image for further processing
img = cv2.imread("../Resources/linux.png")
# Convert the image to grayscale for demonstration purposes
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a grid of images using the stackImages function
# The grid consists of two rows:
# - First row: [original color image, grayscale image, original color image]
# - Second row: [original color image, original color image, original color image]
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))

# The following commented code shows alternative ways to stack images horizontally or vertically
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))
#
# cv2.imshow("Horizontal", imgHor)
# cv2.imshow("Vertical", imgVer)

# Display the stacked image grid in a window titled "ImageStack"
cv2.imshow("ImageStack", imgStack)

# Wait indefinitely for a key press to keep the window open until the user decides to close it
cv2.waitKey(0)