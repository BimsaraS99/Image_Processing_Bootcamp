import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
image_path = 'input.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 1.4)

# Step 4: Perform Canny Edge Detection
# Parameters: lower_threshold and upper_threshold
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

cv2.imshow('Canny Edge Detection', edges)
cv2.imwrite('output.jpg', edges)
cv2.waitKey(0)