# 
# This script is to be ran at the root of mmsegmentation/
#

import os
from PIL import Image

base_dir = "./data/sydneyscapes"

for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.lower().endswith('.png'):
            file_path = os.path.join(dirpath, filename)
            # Process image
            try:
                with Image.open(file_path) as img:
                    # Crop the image to 2:1 ratio while cropping out the bottom first
                    new_img = img.crop((0, 0, 1920, 960))
                    # Overwrite the original image
                    new_img.save(file_path)
                    print(f"Cropped: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")