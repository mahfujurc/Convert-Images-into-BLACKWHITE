import os
from PIL import Image

# Set the folder path (update this to your desired folder path)
folder_path = r""  # Replace with your folder path

# Subfolder to save black and white images
blackwhite_folder = os.path.join(folder_path, "BLACKWHITE")

# Create the subfolder if it doesn't exist
if not os.path.exists(blackwhite_folder):
    os.makedirs(blackwhite_folder)

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if it's a valid image file
    if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            # Open the image
            with Image.open(file_path) as img:
                # Convert the image to grayscale (black and white)
                bw_img = img.convert('L')
                
                # Save the black and white image to the BLACKWHITE subfolder
                bw_file_path = os.path.join(blackwhite_folder, filename)
                bw_img.save(bw_file_path)
                print(f"Converted and saved: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
