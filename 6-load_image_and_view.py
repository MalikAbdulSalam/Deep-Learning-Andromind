import cv2
import numpy as np

# Load grayscale image
img = cv2.imread('14-object detection.jfif', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Grayscale Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()