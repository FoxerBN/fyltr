import os
import zipfile
from datetime import datetime

def save_images_to_zip(images, output_folder):
    """
    Save a list of images to a ZIP file in the specified output folder.
    
    Args:
        images (list): List of image file paths to be zipped.
        output_folder (str): Path to the folder where the ZIP file will be saved.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_filename = f"images_webp_{timestamp}.zip"
    zip_path = os.path.join(output_folder, zip_filename)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for img_name, img_data in images.items():
            zipf.writestr(img_name, img_data)
