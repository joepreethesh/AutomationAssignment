import os

from selenium import webdriver
def before_all(context):
    print("chrome driver executing")
    current_directory = os.getcwd()
    chrome_driver_path = os.path.join(current_directory, 'webdriver', 'chromedriver')
    context.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    context.driver.get("https://www.saucedemo.com")
    context.driver.maximize_window()

def after_feature(context, feature):
    print("executing after scenario")
    context.driver.close()