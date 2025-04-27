import unittest
from downloadLib import download_file
import os

class TestDownloadLib(unittest.TestCase):
    def test_download_file(self):
        test_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        download_file(test_url)
        self.assertTrue(os.path.exists("dummy.pdf"))
        os.remove("dummy.pdf")  # Clean up after test

if __name__ == "__main__":
    unittest.main()