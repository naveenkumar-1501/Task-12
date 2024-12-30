""""
Main.Py
"""

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import TestLocators
from Data import WebData
from Excel_function import Naveen_Excel_Function

#Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get(WebData().URL)

excel_file = WebData.EXCEL_FILE
sheet_number = WebData.SHEET_NUMBER
excel_helper = Naveen_Excel_Function(excel_file, sheet_number)
rows = excel_helper.row_count()

for row in range(2, rows+1):
    #Read username and password from Excel
    username = excel_helper.read_data(row, 7)
    password = excel_helper.read_data(row, 8)

    #Locate elements on the page
    username_input = wait.until(EC.presence_of_element_located((By.NAME, TestLocators.usernameLocator)))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, TestLocators.passwordLocator)))
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, TestLocators.submitButton)))

    #Perform login
    username_input.send_keys(username)
    password_input.send_keys(password)
    submit_button.click()

    #Check login result
    if WebData().DASHBOARD_URL in driver.current_url:
        print(f"SUCCESS: Login success with USERNAME = {username} and PASSWORD = {password}")
        excel_helper.write_data(row, 9, "TEST PASSED")

        #Perform logout
        try:
            action = ActionChains(driver)
            dropdown_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p')))
            action.move_to_element(dropdown_menu).perform()
            logout_button = wait.until(EC.presence_of_element_located((By.XPATH, TestLocators.logoutButton)))
            logout_button.click()
        except TimeoutException:
            print("Logout button not found. Taking a screenshot for debugging.")
            driver.save_screenshot('error_screenshot.png')


    elif WebData.URL in driver.current_url:
        print(f"FAIL: Login failed with USERNAME = {username} and PASSWORD = {password}")
        excel_helper.write_data(row, 9, "TEST FAILED")
#Quit the driver after all iterations
driver.quit()
