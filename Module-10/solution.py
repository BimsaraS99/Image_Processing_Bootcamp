import cv2
import numpy as np

# Load the image
image = cv2.imread("Module-10/xor_4CAmpH1i.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define area threshold
area_threshold = 500  # Adjust this value as needed

# Process and filter contours
for contour in contours:
    area = cv2.contourArea(contour)
    if area >= area_threshold:
        # Compute centroid
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Draw contour
            cv2.drawContours(image, [contour], -1, (0, 255, 0), -1)
            
            # Draw centroid
            cv2.circle(image, (cx, cy), 4, (0, 0, 255), -1)

# Save and display the final processed image
cv2.imwrite("Module-10/filtered.jpg", image)
cv2.imshow("Filtered Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
