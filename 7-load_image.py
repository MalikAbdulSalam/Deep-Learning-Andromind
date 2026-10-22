import cv2
import matplotlib.pyplot as plt

# Load image (OpenCV loads in BGR format)
image = cv2.imread('14-object detection.jfif')

# Convert BGR to RGB for correct display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display using Matplotlib
plt.figure(figsize=(8, 6))
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()

# Print image properties
print(f"Shape: {image.shape}")      # (height, width, channels)
print(f"Data type: {image.dtype}")  # uint8
print(f"Size: {image.size}")        # total pixels