import os
import shutil

def ensure_folder(path):
    """Creates a folder if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def clear_folder(path):
    """Deletes and recreates a folder."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def list_images(folder):
    """Returns a list of image files in a folder."""
    valid_ext = [".jpg", ".jpeg", ".png", ".bmp"]
    return [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() in valid_ext]
