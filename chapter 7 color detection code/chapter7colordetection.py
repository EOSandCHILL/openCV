import cv2  # Import OpenCV for image processing and computer vision tasks
import numpy as np  # Import NumPy for numerical operations

# Import empty from numpy.ma.core (not used since we define our own empty function)
from numpy.ma.core import empty


# Define an empty callback function for trackbar events (does nothing)
def empty(e):
    pass


# Define a function to stack multiple images into a single image grid
def stackImages(scale, imgArray):
    # Get the number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if the image array is a 2D list (i.e., a list of lists)
    rowsAvailable = isinstance(imgArray[0], list)
    # Get the width and height from the first image in the array (used as a reference)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        # Loop through each row and column of the image array
        for x in range(0, rows):
            for y in range(0, cols):
                # If the current image size matches the reference image's size, resize by the given scale factor
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    # Otherwise, force resize the image to the reference image's dimensions and apply the scale factor
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                # If the image is grayscale (only 2 dimensions), convert it to BGR color format
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image with the same dimensions as the reference image for use as a placeholder
        imageBlank = np.zeros((height, width, 3), np.uint8)
        # Initialize lists to hold the horizontally stacked images for each row
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows  # Note: hor_con is not used further in the code
        # Stack images horizontally for each row
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack the rows vertically to form the final image grid
        ver = np.vstack(hor)
    else:
        # If imgArray is a 1D list of images, process each image similarly
        for x in range(0, rows):
            # If the current image size matches the reference image's size, resize by the scale factor
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                # Otherwise, force resize the image to the reference image's dimensions and apply the scale factor
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Convert grayscale images to BGR color format if necessary
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Stack the images horizontally if there is only one row
        hor = np.hstack(imgArray)
        ver = hor
    # Return the final stacked image grid
    return ver


# Define the path to the image file used for color detection
path = "../Resources/Jesko.jpeg"

# Create a window named "TrackBars" for controlling HSV thresholds via trackbars
cv2.namedWindow("TrackBars")
# Resize the "TrackBars" window to 640x240 pixels
cv2.resizeWindow("TrackBars", 640, 240)

# Create trackbars for adjusting the Hue, Saturation, and Value ranges
# Trackbar for minimum Hue value (initial value 27, max value 179)
cv2.createTrackbar("Hue Min", "TrackBars", 27, 179, empty)
# Trackbar for maximum Hue value (initial value 171, max value 179)
cv2.createTrackbar("Hue Max", "TrackBars", 171, 179, empty)
# Trackbar for minimum Saturation value (initial value 0, max value 255)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
# Trackbar for maximum Saturation value (initial value 255, max value 255)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
# Trackbar for minimum Value (brightness) (initial value 143, max value 255)
cv2.createTrackbar("Val Min", "TrackBars", 143, 255, empty)
# Trackbar for maximum Value (brightness) (initial value 255, max value 255)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

# Start an infinite loop to continuously update the color detection based on trackbar positions
while True:
    # Read the image from the specified path
    img = cv2.imread(path)
    # Convert the image from BGR to HSV color space for easier color detection
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the current positions of the trackbars for Hue, Saturation, and Value
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    # Print the current HSV threshold values to the console (for debugging purposes)
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # Create NumPy arrays for the lower and upper bounds of the HSV thresholds
    # Note: The order of elements is set as [Saturation, Value, Hue] for the lower bound and [Hue, Saturation, Value] for the upper bound
    lower = np.array([s_min, v_min, h_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask that identifies the parts of the image within the specified HSV range
    mask = cv2.inRange(imgHSV, lower, upper)
    # Use the mask to extract the relevant parts of the image using a bitwise AND operation
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # Stack the original image, HSV image, mask, and the result image into a single grid for display
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    # Display the stacked images in a window titled "Stacked Images"
    cv2.imshow("Stacked Images", imgStack)

    # Wait 1 millisecond for a key press, allowing the image windows to update continuously
    cv2.waitKey(1)