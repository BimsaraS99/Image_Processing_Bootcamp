import os
import cv2

# Define input and output folders
input_folder = 'Module-3/image_data'  # Folder containing raw images
output_folder = 'Module-3/results'  # Folder to save processed images

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get the list of files in the input folder
file_list = os.listdir(input_folder)
count = 1  # Initialize a counter for naming output files

for file_name in file_list:
    # Create the full input file path
    input_path = os.path.join(input_folder, file_name)

    # Process each file
    try:
        # Read the image
        image = cv2.imread(input_path)
        
        # Check if the file is a valid image
        if image is None:
            print(f"Skipping non-image file: {file_name}")
            continue

        # Resize the image to 500x500 pixels
        resized_image = cv2.resize(image, (500, 500))

        # Define the output file path with sequential naming
        output_path = os.path.join(output_folder, f"{count}.jpg")

        # Save the resized image in .jpg format
        cv2.imwrite(output_path, resized_image)
        print(f"Processed: {file_name} -> {count}.jpg")

        # Increment the counter
        count += 1

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("Image processing complete!")
