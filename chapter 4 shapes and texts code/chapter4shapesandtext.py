import cv2  # Import the OpenCV library for computer vision tasks
import numpy as np  # Import NumPy for efficient numerical operations, especially with arrays

# Create a black image of size 512x512 pixels with 3 color channels (BGR format) using unsigned 8-bit integers
img = np.zeros((512, 512, 3), np.uint8)

# Optional: Print the image dimensions to verify its size (currently commented out)
# print(img.shape)

# Optional: Fill the image with a blue color (BGR: blue, 0, 0) (currently commented out)
# img[:] = 255, 0, 0

# Draw a green line on the image:
# - Starting from point (250, 250) (approximately the center)
# - Ending at the bottom-right corner of the image (using the image's width and height)
# - The line color is green (BGR: 0, 255, 0) with a thickness of 5 pixels
cv2.line(img, (250, 250), (img.shape[1], img.shape[0]), (0, 255, 0), 5)

# Draw a filled red rectangle:
# - The rectangle starts at the top-left corner (0, 0)
# - It extends to the point (150, 250)
# - The color is red (BGR: 0, 0, 255) and it is filled using cv2.FILLED
cv2.rectangle(img, (0, 0), (150, 250), (0, 0, 255), cv2.FILLED)

# Draw a circle:
# - The center of the circle is at (400, 50)
# - The radius of the circle is 30 pixels
# - The circle is drawn in a light blue color (BGR: 255, 255, 0) with a thickness of 3 pixels
cv2.circle(img, (400, 50), 30, (255, 255, 0), 3)

# Add text to the image:
# - The text "learning opencv" is placed starting at coordinates (200, 200)
# - Uses the FONT_HERSHEY_SIMPLEX font with a scale factor of 1
# - The text color is white (BGR: 255, 255, 255) and has a thickness of 2 pixels
cv2.putText(img, "learning opencv", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image in a window titled "Image"
cv2.imshow("Image", img)

# Wait indefinitely for a key press to keep the window open until a key is pressed
cv2.waitKey(0)