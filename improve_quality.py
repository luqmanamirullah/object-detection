import cv2
import numpy as np

# Load the resized image
image = cv2.imread("processed_image.jpg")

# Define a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# Apply the sharpening kernel to the image
sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)

# Save the sharpened image
cv2.imwrite("sharpened_image.jpg", sharpened_image)

print("Sharpened image saved as 'sharpened_image.jpg'")
