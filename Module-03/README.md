### **Task: Batch Image Conversion and Resizing**

**Objective**:  
The goal of this task is to teach students how to work with multiple images in a directory, handle different file formats, and standardize them by converting and resizing them into a uniform format.

---

### **Task Overview**  
You are given a folder containing images in various formats (e.g., `.png`, `.bmp`, `.tiff`, etc.). Your task is to write a Python script that performs the following steps:

1. Read all the images in the folder one by one.
2. Convert each image into `.jpg` format.
3. Resize each image to a resolution of **500x500 pixels**.
4. Save the processed images into a folder named `results` with filenames numbered sequentially: `1.jpg`, `2.jpg`, `3.jpg`, etc.

See the 'result' and 'image_data' folder and you will understand the task better. 

Download Image_data using "image_data_download.zip"

---

### **Learning Outcomes**
By completing this task, students will:
1. Learn to process multiple files in a directory using Python.
2. Understand how to convert images between formats.
3. Gain experience in resizing images with OpenCV.
4. Practice saving images with specific names and formats.

---

### **Step-by-Step Instructions**

1. **Set Up the Environment**:
   - Create two folders: `input_images` (containing the raw images) and `results` (to save the processed images).

2. **Read Images from the Folder**:
   - Use the `os` module to list all files in the `input_images` folder.
   - Filter out non-image files if necessary.

3. **Process Each Image**:
   - Load the image using OpenCV (`cv2.imread()`).
   - Convert the image to `.jpg` format.
   - Resize the image to **500x500 pixels** using `cv2.resize()`.

4. **Save the Image**:
   - Save the processed image in the `results` folder.
   - Name each file sequentially (`1.jpg`, `2.jpg`, `3.jpg`, etc.).

---

### **Hints for Implementation**

**Iterate Through Files Using For Loop**: