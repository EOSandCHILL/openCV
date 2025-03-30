import cv2

img = cv2.imread('../Resources/linux.png', cv2.IMREAD_GRAYSCALE)

print("cv package imported: " + cv2.__version__)
if cv2.__version__ == '4.11.0':
    cv2.imshow("Output", img)
    cv2.waitKey(0)

# This code snippet does two main things:
# 	1.	Prints the OpenCV Version:
# 	•	print("cv package imported: " + cv2.__version__) prints a message along with the version of the OpenCV (cv2)
# 	package that has been imported. This helps confirm which version is in use.
# 	2.	Displays an Image Based on the Version:
# 	•	if cv2.__version__ == '4.11.0': checks if the current OpenCV version is exactly '4.11.0'.
# 	•	If the condition is true:
# 	•	cv2.imshow("Output", img) opens a window named “Output” to display the image stored in the variable img.
# 	•	cv2.waitKey(0) waits indefinitely for a key press. This ensures that the window remains open until you press any key.
#
# In summary, the code first confirms the version of OpenCV and, if it matches version 4.11.0, it displays an image and waits for a
# key press before proceeding.