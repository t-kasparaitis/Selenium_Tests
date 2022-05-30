import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class RegistrationCase(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
        self.action = ActionChains(self.chrome_driver)

    def test_registration(self):
        self.chrome_driver.get("https://www.phptravels.net/login")
        self.chrome_driver.implicitly_wait(15)  # max wait time

        signup = self.chrome_driver.find_element(By.XPATH, "//a[@href='https://www.phptravels.net/signup']")
        signup.click()

        form_first_name = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='first_name']")
        form_last_name = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='first_name']")
        form_phone = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='phone']")
        form_email = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='email']")
        form_password = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']")
        # form_account_type = self.chrome_driver.find_element(By.XPATH, "//input[@class='form-control'][@name='last_name']")

        self.assertEqual(True, False)  # add assertion here

    def tearDown(self):
        self.chrome_driver.quit()


if __name__ == '__main__':
    unittest.main()
