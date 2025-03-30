import cv2

vid = cv2.VideoCapture('../Resources/kj.MOV')

while True:
    success, image = vid.read()
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# This code continuously reads and displays video frames until you press the “q” key. Here’s a simple breakdown:
# 	•	while True:
# Starts an endless loop, which keeps the video running.
# 	•	success, image = vid.read()
# Reads a frame from the video source (vid).
# 	•	success is a flag indicating if the frame was read successfully.
# 	•	image contains the actual frame (picture).
# 	•	cv2.imshow("Video", image)
# Displays the current frame in a window titled “Video”.
# 	•	if cv2.waitKey(1) & 0xFF == ord('q'):
# Waits 1 millisecond for a key press. The expression checks if the pressed key is “q”.
# 	•	cv2.waitKey(1) returns the key code.
# 	•	& 0xFF isolates the key code’s lower 8 bits.
# 	•	ord('q') is the ASCII value of “q”.
# 	•	break
# Exits the loop if “q” is pressed, stopping the video display.
#
# In summary, this loop shows a video frame by frame and stops when you hit “q”.
