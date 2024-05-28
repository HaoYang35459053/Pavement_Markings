# The function of the program
# The program crops the screenshot of the map to remove the UI of the Brave app (Upper part of screenshot) 
# and the Taskbar and Navigation (Lower part of screenshot)

# The image cropping codes is derived from the video made by TheBinaryBits
# The video link:
# https://www.youtube.com/watch?v=NvtAYT1GIpg

from PIL import Image

# Enter the image name
print("Note: You need to revise the code if the file is not a PNG file")
image_name = input("Please enter the image file name (without extension): ")

# Construct the full path to the image
# Revise the codes here for png file
image_path = rf'C:\Users\asus\Desktop\Pavement_Markings\{image_name}.png'

# Load the image with error handling
try:
    image = Image.open(image_path)
    print(f"Image loaded from {image_path}")

    # Step 1: Crop the upper part of the image to 1920 x 900 (The resolution needs to change for each user)
    # The crop box is (left, upper, right, lower)
    upper_cropped_image = image.crop((0, 180, 1920, 1080))
    
    # Step 2: Crop the resulting image to 1920 x 860 (cropping the lower part)
    # Since we want to crop from the top, we adjust the lower boundary to 860
    final_cropped_image = upper_cropped_image.crop((0, 0, 1920, 860))

    # Save the final cropped image with the file name
    final_cropped_image_name = f"final_cropped_{image_name}.png"
    final_cropped_image_path = rf'C:\Users\asus\Desktop\Pavement_Markings\{final_cropped_image_name}'
    final_cropped_image.save(final_cropped_image_path)
    print(f'Final cropped image has been saved as {final_cropped_image_path}')

except FileNotFoundError:
    print(f"File not found: {image_path}. Please check the file name and try again.")

except Exception as e:
    print(f"An error occurred: {e}")