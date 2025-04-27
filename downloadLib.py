import requests
import threading
import os

def download_file(url):
    """
    Downloads a single file from the given URL and saves it with the last part of the URL as filename.
    """
    local_filename = url.split("/")[-1]  # Take last part of URL for filename
    response = requests.get(url)
    with open(local_filename, "wb") as f:
        f.write(response.content)
    pass  # TODO: implement after testing is ready


def seq_download(urls, save_folder="downloads"):
    
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for url in urls:
        filename = os.path.join(save_folder, url.split("/")[-1])
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")