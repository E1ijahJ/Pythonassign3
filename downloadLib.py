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
    """
    Downloads files sequentially (one after another) from a list of URLs and saves them locally.
    
    Args:
        urls (list): List of URL strings.
        save_folder (str): Folder where downloaded files are saved.
    """
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for url in urls:
        filename = os.path.join(save_folder, url.split("/")[-1])
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")



# threaded_download.py
import threading
import requests
import os

def helper_download_file(url, directory="downloads"):
    """Helper function that downloads a file from a URL and saves it to the specified directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    local_filename = os.path.join(directory, url.split("/")[-1])

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename

def threaded_download(urls, directory="downloads"):
    """
    Downloads multiple files concurrently using threads. Each download occurs on a separate thread.

    Args:
        urls (list of str): A list of URLs to download files from.
        directory (str): The folder where the files will be saved. Defaults to "downloads".

    Returns:
        None
    """
    threads = []

    for url in urls:
        thread = threading.Thread(target=helper_download_file, args=(url, directory))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()