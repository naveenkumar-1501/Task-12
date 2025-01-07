from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Locators import TestLocators

class DashboardPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def is_dashboard_displayed(self):
        # Check if the dashboard is displayed
        return "dashboard" in self.driver.current_url

    def logout(self):
        try:
            action = ActionChains(self.driver)
            #wait dropdown menu to present in the DOM and locate it by it's Xpath
            dropdown_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators.dropdown )))
            action.move_to_element(dropdown_menu).perform()
            # Wait for the logout button to be present in the DOM and locate it by its XPath
            logout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators.logoutButton)))
            # Click on the logout button to perform the logout action
            logout_button.click()
        except TimeoutError:
            print("Logout button not found.")
