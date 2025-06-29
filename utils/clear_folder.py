import shutil, os
def clear_folders(input_folder, output_folder,):
    for folder in [input_folder, output_folder]:
        shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder, exist_ok=True)