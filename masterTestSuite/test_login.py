import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# imports for dealing with Stale Element Reference (turned out not needed due to implicitly_wait:
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions


class LoginCase(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)

    def test_valid_credentials(self):
        self.chrome_driver.get("https://www.phptravels.net/login")
        self.chrome_driver.implicitly_wait(10)  # max wait time

        email = "user@phptravels.com"
        password = "demouser"
        form_email = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='email']")
        form_password = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='password']")
        form_submit = self.chrome_driver.find_element(By.XPATH, "//button[@type='submit']")
        form_email.send_keys(email)
        form_password.send_keys(password)
        form_submit.click()
        expected_url = "https://www.phptravels.net/account/dashboard"
        actual_url = self.chrome_driver.current_url

        # Logic is: if you can see your dashboard, then you are logged in:
        self.assertEqual(expected_url, actual_url, "Login failed with valid credentials")

    def test_invalid_credentials(self):
        self.chrome_driver.get("https://www.phptravels.net/login")
        self.chrome_driver.implicitly_wait(10)  # max wait time

        # could randomize email & password if I had more time:
        email = "wrong@meow.com"
        password = "meowmoocow22"
        form_email = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='email']")
        form_password = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='password']")
        form_submit = self.chrome_driver.find_element(By.XPATH, "//button[@type='submit']")
        form_email.send_keys(email)
        form_password.send_keys(password)
        form_submit.click()
        expected_url = "https://www.phptravels.net/account/dashboard"
        actual_url = self.chrome_driver.current_url

        # Logic is: if you can't see the dashboard, you are not logged in:
        self.assertNotEqual(expected_url, actual_url, "Login succeeded with invalid/random credentials")

    def test_bad_email_good_password(self):
        self.chrome_driver.get("https://www.phptravels.net/login")
        self.chrome_driver.implicitly_wait(10)  # max wait time

        email = "wrong@meow.com"
        password = "demouser"

        form_email = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='email']")
        form_password = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='password']")
        form_submit = self.chrome_driver.find_element(By.XPATH, "//button[@type='submit']")
        form_email.send_keys(email)
        form_password.send_keys(password)
        form_submit.click()
        expected_url = "https://www.phptravels.net/account/dashboard"
        actual_url = self.chrome_driver.current_url

        # Logic is: if you can't see the dashboard, you are not logged in:
        self.assertNotEqual(expected_url, actual_url, "Login succeeded with invalid/random credentials")

    def test_bad_password_good_email(self):
        self.chrome_driver.get("https://www.phptravels.net/login")
        self.chrome_driver.implicitly_wait(10)  # max wait time

        email = "user@phptravels.com"
        password = "meowmoocow22"

        form_email = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='email']")
        form_password = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@type='password']")
        form_submit = self.chrome_driver.find_element(By.XPATH, "//button[@type='submit']")
        form_email.send_keys(email)
        form_password.send_keys(password)
        form_submit.click()
        expected_url = "https://www.phptravels.net/account/dashboard"
        actual_url = self.chrome_driver.current_url

        # Logic is: if you can't see the dashboard, you are not logged in:
        self.assertNotEqual(expected_url, actual_url, "Login succeeded with invalid/random credentials")

    def tearDown(self):
        self.chrome_driver.quit()


if __name__ == '__main__':
    unittest.main()
