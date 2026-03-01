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