import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Data import WebData
from Excel_function import Naveen_Excel_Function
from LoginPage import LoginPage
from Dashboard import DashboardPage
from Locators import TestLocators

# Test setup using pytest fixture
@pytest.fixture(scope="module")
def setup():
    # Initialize WebDriver and WebDriverWait
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    # Navigate to the login page
    driver.get(WebData.URL)
    # Return necessary components
    yield driver, wait
    # Teardown
    driver.quit()


@pytest.mark.parametrize("row", range(2, 7))  # Parametrize for rows 2 and 6 in the test data
def test_login(setup, row):
    driver, wait = setup
    excel_file = WebData.EXCEL_FILE
    sheet_number = WebData.SHEET_NUMBER
    excel_helper = Naveen_Excel_Function(excel_file, sheet_number)

    # Read test data (username and password)
    username = excel_helper.read_data(row, 7)
    password = excel_helper.read_data(row, 8)

    # Initialize page objects
    login_page = LoginPage(driver, wait)
    dashboard_page = DashboardPage(driver, wait)

    # Perform login
    login_page.login(username, password)

    # Assert login success
    if dashboard_page.is_dashboard_displayed():
        print(f"SUCCESS: Login success with USERNAME = {username} and PASSWORD = {password}")
        excel_helper.write_data(row, 9, "TEST PASSED")
        try:
            logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators.logoutButton)),message="Logout button not visible after login.")
            logout_button.click()
        except TimeoutException:
            print("Logout button not found")

    else:
        print(f"FAIL: Login failed with USERNAME = {username} and PASSWORD = {password}")
        excel_helper.write_data(row, 9, "TEST FAILED")
