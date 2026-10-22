import cv2
import matplotlib.pyplot as plt

# Load image (OpenCV loads in BGR format)
image = cv2.imread('14-object detection.jfif')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display grayscale
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()


# Display grayscale
plt.imshow(hsv, cmap='gray')
plt.title('hsv Image')
plt.axis('off')
plt.show()


# Display grayscale
plt.imshow(image, cmap='gray')
plt.title('BGR Image')
plt.axis('off')
plt.show()