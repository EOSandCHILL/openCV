import cv2  # Import the OpenCV library for image processing

# Load an image from the specified path in grayscale mode.
# The image file is expected to be located at '../Resources/linux.png'.
img = cv2.imread('../Resources/linux.png', cv2.IMREAD_GRAYSCALE)

# Print the version of the OpenCV package that has been imported.
print("cv package imported: " + cv2.__version__)

# Check if the OpenCV version is exactly '4.11.0'.
if cv2.__version__ == '4.11.0':
    # If the condition is met, display the image in a window titled "Output".
    cv2.imshow("Output", img)
    # Wait indefinitely for a key press, so the window remains open until the user presses a key.
    cv2.waitKey(0)