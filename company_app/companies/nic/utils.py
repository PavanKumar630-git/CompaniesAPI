import os
import requests
from urllib.parse import urlparse

BASE_DIR = "media/nic_pdfs"

def download_pdf_from_url(pdf_url: str):

    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    parsed = urlparse(pdf_url)
    file_name = os.path.basename(parsed.path)
    file_path = os.path.join(BASE_DIR, file_name)

    response = requests.get(pdf_url, stream=True)

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)

    return {"file_name": file_name, "file_path": file_path}


def save_txt_file(filename: str, data: str, folder: str = "test") -> str:
    """
    Saves data to a .txt file inside the given folder.
    
    :param filename: Name of the file without extension
    :param data: Content to write into file
    :param folder: Folder name (default: test)
    :return: Full file path
    """

    # Ensure folder exists
    os.makedirs(folder, exist_ok=True)

    # Add .txt extension if not present
    if not filename.endswith(".txt"):
        filename = f"{filename}.txt"

    file_path = os.path.join(folder, filename)

    # Write data
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(data))

    return file_path