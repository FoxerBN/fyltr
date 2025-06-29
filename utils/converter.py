import os
from PIL import Image
import io

webp_quality = 20

def convert_images_to_webp(input_folder,quality):
    """Convert images in the specified folder to WEBP format.
    Args:
        input_folder (str): Path to the folder containing images to convert.
    Returns:
        dict: A dictionary with filenames as keys and their WEBP binary data as values.
    """

    converted_images = {}

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(input_folder, filename)
            with Image.open(image_path) as img:
                img = img.convert("RGB")
                buffer = io.BytesIO()
                img.save(buffer, format="WEBP", quality=webp_quality)
                webp_filename = os.path.splitext(filename)[0] + ".webp"
                converted_images[webp_filename] = buffer.getvalue()
    
    return converted_images