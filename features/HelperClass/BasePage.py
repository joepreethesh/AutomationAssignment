import time

from selenium.webdriver.common.by import By

from Utilities import ConfigReader
class BasePage():
    def __init__(self, driver):
        self.driver = driver
    def isElementDisplayed(self, locatorID, configFileName, locatorName):
        try:
            self.driver.find_element(locatorID, ConfigReader.readConfig(configFileName, locatorName))
            return True
        except:
            return False

    def waitUntilElementIsDisplayed(self, locatorID, configFileName, UserNamelocator, PasswordLocator):
        pass

    def enterText(self,locatorID, configFileName, userNameLocator, passwordLocator, userId):
        loginCredentialsElement = self.driver.find_element(By.ID, ConfigReader.readConfig(configFileName, "userNameList_ID"))
        credentials_text = loginCredentialsElement.text
        usernames = [username.strip() for username in credentials_text.split('\n')[1:]]
        if userId == "standard_user":
            userNameTextField = self.driver.find_element(locatorID, ConfigReader.readConfig(configFileName, userNameLocator))
            userNameTextField.clear()
            userNameTextField.send_keys(usernames[0])
        elif userId == "performance_glitch_user":
            userNameTextField = self.driver.find_element(locatorID,
                                                         ConfigReader.readConfig(configFileName, userNameLocator))
            userNameTextField.clear()
            userNameTextField.send_keys(usernames[-1])

        passwordElement = self.driver.find_element(By.CLASS_NAME, 'login_password')
        password_text = passwordElement.text
        passwordText = password_text.split(':')[1].strip()
        passwordTextField = self.driver.find_element(locatorID,
                                                     ConfigReader.readConfig(configFileName, passwordLocator))
        passwordTextField.clear()
        passwordTextField.send_keys(passwordText)

    def click(self, locator, configFileName, locatorName):
        self.driver.find_element(locator, ConfigReader.readConfig(configFileName,locatorName)).click()




