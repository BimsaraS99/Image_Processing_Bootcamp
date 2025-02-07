import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the RGB image
image_path = 'Module-6/EnhanceAfter.jpg'  # Replace with your image path
rgb_image = cv2.imread(image_path)

# Convert the image from BGR (OpenCV default) to RGB
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

# Convert the RGB image to grayscale
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

# Calculate the histogram
histogram, bins = np.histogram(gray_image, bins=256, range=[0, 256])

# Plot the grayscale image and its histogram
plt.figure(figsize=(12, 6))

# Show the grayscale image
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# Plot the histogram
plt.subplot(1, 2, 2)
plt.plot(bins[:-1], histogram, color='black')
plt.title('Frequency Histogram of Pixel Intensities')
plt.xlabel('Pixel Intensity (0-255)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
