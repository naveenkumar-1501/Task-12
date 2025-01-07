"""
Locators.py
"""

class TestLocators:
    # Locator for the username field
    usernameLocator = "username"
    # Locator for the password field
    passwordLocator = "password"
    # Locator for the submit button (using XPath)
    submitButton = "//button[@type='submit']"
    # Locator for the dropdown (using Xpath)
    dropdown = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img'
    # Locator for the logout button (using XPath)
    logoutButton = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a'
