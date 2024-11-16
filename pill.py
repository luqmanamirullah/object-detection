from PIL import Image, ImageFilter

# Load the resized image
image = Image.open("resized_padded_image.jpg")

# Apply a sharpening filter
sharpened_image = image.filter(ImageFilter.SHARPEN)

# Save the enhanced image
sharpened_image.save("enhanced_image.jpg")

print("Enhanced image saved as 'enhanced_image.jpg'")
