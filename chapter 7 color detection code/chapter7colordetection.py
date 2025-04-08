import cv2  # Import OpenCV for image processing and computer vision tasks
import numpy as np  # Import NumPy for numerical operations
from pyutils.stackimages import stackImages

# Define an empty callback function for trackbar events (does nothing)
def empty(e):
    pass

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