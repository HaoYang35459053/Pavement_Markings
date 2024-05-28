from PIL import Image

# Load the image
image_path = r'C:\Users\asus\Desktop\Pavement_Markings\Test_0528.png'
image = Image.open(image_path)

# Step 1: Crop the upper part to 1920 x 900
width, height = image.size
upper_cropped_image = image.crop((0, 0, width, 900))

# Save the upper cropped image
upper_cropped_image_path = r'C:\Users\asus\Desktop\Pavement_Markings\upper_cropped_image.png'
upper_cropped_image.save(upper_cropped_image_path)
print(f'Upper cropped image has been saved as {upper_cropped_image_path}')

# Step 2: Crop the resulting image to 1920 x 860 (cropping the bottom part)
final_cropped_image = upper_cropped_image.crop((0, 0, width, 860))

# Save the final cropped image
final_cropped_image_path = r'C:\Users\asus\Desktop\Pavement_Markings\final_cropped_image.png'
final_cropped_image.save(final_cropped_image_path)
print(f'Final cropped image has been saved as {final_cropped_image_path}')
