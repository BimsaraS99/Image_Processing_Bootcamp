import cv2

# Load the image
image = cv2.imread('Module-2/vk.jpg')  # Replace with your image path

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError("Image not found. Please check the path.")

# Show the image in a window
cv2.imshow('Loaded Image', image)

# Wait for a key press to close the window
cv2.waitKey(0)

# Save the image to a file
cv2.imwrite('Module-2/output_image.jpg', image)  # Replace with your desired output path

# Close all OpenCV windows
cv2.destroyAllWindows()
