import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.HelperClass.BasePage import BasePage
class productPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def checkProductPageIsDisplayed(self):
        time.sleep(5)
        productPageStatus = self.isElementDisplayed(By.CLASS_NAME, "Login", "loginHomePage_CLASSNAME")
        assert productPageStatus, "Product page is not displayed"
        return productPageStatus

    def clickOnSortOrder(self, index):
        self.selectItemFromDropdown(By.CLASS_NAME, "Products", "pdctSortContainer", index)
    def getInventoryLists(self, item):
        InventoryItemList = self.getInventoryItemNamesInProductScreen(By.CLASS_NAME, "Products", item)
        print(InventoryItemList)
        is_alphabetical_order = InventoryItemList == sorted(InventoryItemList)
        print(is_alphabetical_order)
        return InventoryItemList



# current_directory = os.getcwd()
# chrome_driver_path = os.path.join(current_directory, 'webdriver', 'chromedriver')
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# helper = productPage(driver)
# # helper.clickOnSortOrder(3)
# helper.getInventoryItemNamesInProductScreen()