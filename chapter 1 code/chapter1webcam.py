import cv2  # Import the OpenCV library for computer vision tasks

# Create a VideoCapture object to access the default webcam (index 0)
vid = cv2.VideoCapture(0)

# Configure the video capture settings:
# Set the width of the frames to 640 pixels
vid.set(3, 640)
# Set the height of the frames to 480 pixels
vid.set(4, 480)
# Set the brightness of the video capture to 100 (scale may vary by camera)
vid.set(10, 100)

# Start an infinite loop to continuously capture video frames
while True:
    # Read a frame from the video capture; 'success' indicates if the frame was captured successfully
    success, image = vid.read()
    # Display the current frame in a window titled "Video"
    cv2.imshow("Video", image)
    # Wait for 1 millisecond for a key press; if 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break