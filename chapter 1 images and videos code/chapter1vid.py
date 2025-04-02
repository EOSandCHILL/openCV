import cv2  # Import the OpenCV library for computer vision tasks

# Create a VideoCapture object to read the video file located at '../Resources/kj.MOV'
vid = cv2.VideoCapture('../Resources/kj.MOV')

# Start an infinite loop to process video frames continuously
while True:
    # Read a frame from the video; 'success' is True if the frame was read correctly,
    # and 'image' contains the current frame.
    success, image = vid.read()

    # Display the current frame in a window titled "Video"
    cv2.imshow("Video", image)

    # Wait for 1 millisecond for a key press, and check if the pressed key is 'q'.
    # The bitwise operation ensures the key chapter 1 images and videos code is compared correctly.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If 'q' is pressed, break out of the loop to stop the video playback.
        break