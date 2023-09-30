from selenium.webdriver.common.by import By

from features.HelperClass.BasePage import BasePage


class loginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def checkWebPageIsDisplayed(self):
        elementStatus = self.isElementDisplayed(By.ID, "Login", "loginButton_ID")
        print(elementStatus)
        return elementStatus

    def enterTextInUserNameAndPasswordField(self, user):
        self.enterText(By.ID, "Login", "userNameTextField_ID", "passwordTextField_ID",user)





