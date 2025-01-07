from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Locators import TestLocators


class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def login(self, username, password):
        # Locate the elements for username, password, and submit button
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators.usernameLocator)))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators.passwordLocator)))
        submit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators.submitButton)))

        # Perform login actions
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
