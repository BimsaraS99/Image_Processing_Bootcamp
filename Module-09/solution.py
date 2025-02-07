import cv2
import numpy as np

# Read the image
image_path = "Module-9/xor_4CAmpH1i.jpg"  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Could not read image.")
    exit()

# Apply thresholding to create a binary image
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Convert grayscale image to BGR for visualization
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

centroids = []

for contour in contours:
    # Compute the moments of the contour
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        centroids.append((cx, cy))
        
        # Compute the area of the contour
        area = cv2.contourArea(contour)
        
        # Draw the centroid on the image
        cv2.circle(output_image, (cx, cy), 5, (0, 0, 255), -1)
        
        # Display the area as text near the centroid
        text_position = (cx + 10, cy - 10)  # Slightly offset from centroid
        cv2.putText(output_image, f"{int(area)}", text_position, 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the image with centroids and areas
cv2.imshow("Centroids & Areas", output_image)
cv2.imwrite("Module-9/centroids_areas.jpg", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Centroids and Areas:", centroids)
