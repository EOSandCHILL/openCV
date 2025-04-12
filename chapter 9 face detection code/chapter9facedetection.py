import cv2  # Import OpenCV for computer vision tasks

# Load the Haar cascade for face detection from the specified XML file
faceCascade = cv2.CascadeClassifier('../Resources/haarcascade_frontalface_default.xml')

# Read the image from disk (in this case, the image is "lena.png")
img = cv2.imread("../Resources/lena.png")

# Convert the image to grayscale since the face detector works on gray images
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the gray image using the Haar cascade detector
# The scaleFactor parameter (1.1) compensates for differences in face sizes,
# while minNeighbors (4) defines how many neighbors each candidate rectangle should have to retain it.
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Loop over the list of faces detected
for (x, y, w, h) in faces:
    # Draw a blue rectangle around each detected face
    # (x, y) is the top-left coordinate and (x+w, y+h) is the bottom-right coordinate of the rectangle
    # The rectangle is drawn with a line thickness of 2
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the resulting image with detected faces in a window titled 'Result'
cv2.imshow('Result', img)

# Wait indefinitely for a key press so that the window stays open
cv2.waitKey(0)