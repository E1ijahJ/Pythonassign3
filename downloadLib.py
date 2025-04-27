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

