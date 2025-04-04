import cv2  # Import OpenCV for image processing
import numpy as np  # Import NumPy for numerical operations

# Load an image from the specified path (used for stacking demonstration)
img = cv2.imread("../Resources/linux.png")

# Define a function to stack multiple images into a single image grid
def stackImages(scale,imgArray):
    # Determine the number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if the image array is a 2D list (i.e., list of lists)
    rowsAvailable = isinstance(imgArray[0], list)
    # Get the width and height from the first image in the array
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        # Loop through each row and column of the image array
        for x in range ( 0, rows):
            for y in range(0, cols):
                # If the current image size matches the reference size, resize by the given scale
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # Otherwise, force resize the image to the reference image's dimensions and scale it
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # If the image is grayscale (only 2 dimensions), convert it to BGR color format
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image with the same dimensions as the reference image
        imageBlank = np.zeros((height, width, 3), np.uint8)
        # Initialize lists to hold the horizontally stacked images for each row
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        # Stack images horizontally for each row
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack the rows vertically to create the final image grid
        ver = np.vstack(hor)
    else:
        # If imgArray is a 1D list of images, process each image similarly
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            # Convert grayscale images to BGR color format if necessary
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Stack the images horizontally if only one row is provided
        hor= np.hstack(imgArray)
        ver = hor
    # Return the final stacked image grid
    return ver

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