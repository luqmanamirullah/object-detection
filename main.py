import tensorflow as tf

# Load and preprocess the image
image = tf.io.read_file("./images/captcha_1.jpg")
image = tf.image.decode_jpeg(image, channels=3)
image = tf.image.resize(image, [round(150*4.5), round(280*4.5)])  # Resize
image = image / 255.0  # Normalize to range [0, 1]

# Reverse normalization (back to 0-255 range)
image = tf.clip_by_value(image * 255.0, 0, 255)
image = tf.cast(image, tf.uint8)  # Convert to integer type

# Save the processed image back to a file
encoded_image = tf.image.encode_jpeg(image)  # Encode as JPEG
tf.io.write_file("processed_image.jpg", encoded_image)  # Save to disk

print("Image saved as 'processed_image.jpg'")
