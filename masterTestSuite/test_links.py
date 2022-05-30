import requests
import validators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from validators import ValidationFailure
import unittest


def is_valid_url(url: str) -> bool:
    result = validators.url(url)
    # check if our result is an instance of ValidationFailure, thereby a failure:
    if isinstance(result, ValidationFailure):
        return False
    return result


class LinksCase(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)

    def test_links(self):
        self.chrome_driver.get("https://phptravels.com/demo/")

        # implicit wait is global for all elements, unlike sleep; implicit wait is like a max wait time
        self.chrome_driver.implicitly_wait(10)

        bad_links = []
        # this will gather all links for the current page, not the entire website (would require additional logic)
        page_links = self.chrome_driver.find_elements(By.XPATH, "//a[@href]")

        for link in page_links:
            if not is_valid_url(link.get_attribute("href")):
                bad_links.append(link)
                page_links.remove(link)

        for link in page_links:
            response = requests.get(link.get_attribute("href"))
            print(link.get_attribute("href") + "  | Response Code: " + str(response.status_code))
            if response.status_code != 200:
                bad_links.append(link)

        print("List of Bad Links:")
        for bad_link in bad_links:
            print(bad_link.get_attribute("href"))

        self.assertEqual(True, False)  # add assertion here

    def tearDown(self):
        self.chrome_driver.quit()


if __name__ == '__main__':
    unittest.main()

"""
Match chrome://version to driver version download from https://sites.google.com/chromium.org/driver/.
Had weird issues with setting PATH via os.environ, PATH was correct but Selenium wouldn't find the driver.
I suspect it may be from PATH containing too many things in there (such as for Java/C#) and chromedriver being
at the bottom of the list. The simple fix was to move the downloaded driver into the project's venv/Scripts folder!
"""


