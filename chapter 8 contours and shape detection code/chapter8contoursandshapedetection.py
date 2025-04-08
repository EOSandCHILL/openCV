import cv2
import numpy as np
from pyutils.stackimages import stackImages

path = '../Resources/shapes.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

imgStack = stackImages(0.5, ([img, imgGray, imgBlur]))
cv2.imshow("Stacked Images", imgStack)
cv2.waitKey(0)