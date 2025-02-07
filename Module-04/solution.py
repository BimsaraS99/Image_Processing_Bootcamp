import cv2
import numpy as np

# Load the image
image = cv2.imread('Module-3/vk.jpg')  # Replace with your image path

if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convert to LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Resize dimensions
image_size = (image.shape[1] // 5, image.shape[0] // 5)  # Width, Height for resizing

# Convert images to 3-channel BGR format for stacking
gray_image_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
lab_image_bgr = lab_image  # LAB already has 3 channels
hsv_image_bgr = hsv_image  # HSV already has 3 channels

# Resize all images to match the same dimensions
image_resized = cv2.resize(image, image_size)
gray_image_bgr = cv2.resize(gray_image_bgr, image_size)
lab_image_bgr = cv2.resize(lab_image_bgr, image_size)
hsv_image_bgr = cv2.resize(hsv_image_bgr, image_size)

# Combine images into a 2x2 grid
top_row = np.hstack((image_resized, gray_image_bgr))
bottom_row = np.hstack((lab_image_bgr, hsv_image_bgr))
combined_image = np.vstack((top_row, bottom_row))

# Display the combined image
cv2.imshow('Combined Image', combined_image)
cv2.imwrite('Module-3/result.jpg', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
