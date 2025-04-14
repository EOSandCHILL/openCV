import cv2  # Import OpenCV for computer vision tasks

# ----------------
# Parameters
# -----------------
frameWidth = 640  # Width of the captured frame
frameHeight = 480  # Height of the captured frame

# Load the Haar cascade classifier for detecting Russian license plates
# The cascade file is located in the Resources directory.
russianLicensePlateCascade = cv2.CascadeClassifier('../Resources/haarcascade_russian_plate_number.xml')

minArea = 500  # Minimum area threshold to filter out small detections
color = (255, 0, 255)  # Color for drawing rectangles (pink)

# Create a VideoCapture object to access the default webcam (index 0)
cap = cv2.VideoCapture(0)

# Configure the video capture settings:
cap.set(3, frameWidth)  # Set the width of the frames
cap.set(4, frameHeight)  # Set the height of the frames
cap.set(10, 150)  # Set the brightness level of the captured frames

count = 0  # Initialize a counter for saved license plate images

# Start an infinite loop to continuously capture video frames
while True:
    # Capture a frame from the webcam; 'success' is True if the frame is captured successfully
    success, img = cap.read()

    # Convert the captured frame to grayscale for the license plate detector
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect Russian license plates in the grayscale image using the Haar cascade detector
    # The parameters adjust how the detector scales and groups candidate detections
    russianLicensePlates = russianLicensePlateCascade.detectMultiScale(imgGray, 1.1, 4)

    # Loop over each detected license plate
    for (x, y, w, h) in russianLicensePlates:
        area = w * h  # Calculate the area of the detected region
        if area > minArea:  # Process only regions with an area larger than the specified threshold
            # Draw a rectangle around the detected license plate on the original image
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            # Place text above the rectangle to label it as a "License Plate"
            cv2.putText(img, "Russian License Plate", (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            # Extract the region of interest (i.e. the license plate area) from the image
            imageRegionOfInterest = img[y:y + h, x:x + w]
            # Display the extracted region in a window titled "Region of Interest"
            cv2.imshow("Region of Interest", imageRegionOfInterest)

    # Display the processed image with drawn rectangles and labels in a window titled 'Result'
    cv2.imshow('Result', img)

    # Wait indefinitely for a key press (this will pause the video until a key is pressed)
    cv2.waitKey(0)

    # Display the current frame again after key press (note: this is redundant but kept as in original logic)
    cv2.imshow("Result", img)

    # Check if the user pressed the 's' key (for "save")
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the region of interest (the detected license plate) as an image file
        cv2.imwrite("Resources/ScannedRussianLicensePlates/NoPlate_" + str(count) + ".jpg", imageRegionOfInterest)
        # Draw a filled green rectangle as a visual confirmation that the license plate was saved
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        # Overlay text on the image indicating that the license plate has been saved
        cv2.putText(img, "Scanned License Plate Saved", (150, 265),
                    cv2.FONT_HERSHEY_DUPLEX, (2, (0, 0, 255), 2))
        # Show the confirmation image in a window titled "Scanned License Plate"
        cv2.imshow("Scanned License Plate", img)
        # Wait 500 milliseconds so the confirmation message is visible
        cv2.waitKey(500)
        count += 1  # Increment the counter for the next saved image