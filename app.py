

import sys
import time
from downloadLib import seq_download, threaded_download

if __name__ == "__main__":
    urls = sys.argv[1:]  # Skip the script name

    if not urls:
        print("Please provide URLs as command line arguments.")
        sys.exit(1)

    print("Starting SEQUENTIAL downloads...")
    start_time = time.time()
    seq_download(urls)
    seq_duration = time.time() - start_time
    print(f"Sequential downloads completed in {seq_duration:.2f} seconds.\n")

    print("Starting THREADED downloads...")
    start_time = time.time()
    threaded_download(urls)
    threaded_duration = time.time() - start_time
    print(f"Threaded downloads completed in {threaded_duration:.2f} seconds.\n")