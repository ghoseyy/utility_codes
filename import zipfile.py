import zipfile
import os

def unzip_file(zip_path, extract_to=None):
    """Unzips a file to the given directory."""
    if extract_to is None:
        extract_to = os.path.splitext(zip_path)[0]  # Extract to folder with ZIP name
    
    os.makedirs(extract_to, exist_ok=True)  # Ensure the folder exists
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"Extracted to: {extract_to}")

# Example usage:
zip_file_path = "/Users/bimalchhetry/Downloads/OneDrive_3_09-03-2025.zip"  # Change this path
unzip_file(zip_file_path)
