from PIL import Image

# Load the image
image_path = r'C:\Users\asus\Desktop\Pavement_Markings\Colors.png'
image = Image.open(image_path)

# Convert the image to RGB mode
image = image.convert('RGB')

# Get the image dimension
width_image, height_image = image.size

# Iterate over each pixel in the image
for x in range(width_image):
    for y in range(height_image):
        r, g, b = image.getpixel((x, y))

        # Check if the pixel is not black (black is (0, 0 ,0) in RGB)
        if (r, g, b) != (0, 0, 0):
            # Then paint the pixel green
            image.putpixel((x, y), (0, 255, 0))

# Save the modified image
image.save(r'C:\Users\asus\Desktop\Pavement_Markings\revised_image.png')
print('Image has been revised and saved as revised_image.png')