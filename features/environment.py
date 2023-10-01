import os
import time

from selenium import webdriver
def before_scenario(context, scenario):
    print("chrome driver executing")
    current_directory = os.getcwd()
    chrome_driver_path = os.path.join(current_directory, 'webdriver', 'chromedriver')
    context.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    context.driver.get("https://www.saucedemo.com")
    time.sleep(5)
    #context.driver.maximize_window()

def after_scenario(context, scenario):
    print("executing after scenario")
    context.driver.quit()