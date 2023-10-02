import os
import time

from selenium import webdriver
def before_scenario(context, scenario):
    print("chrome driver executing")
    chrome_driver_path = os.path.abspath(os.path.join('webdriver', 'chromedriver'))
    print("Chromedriver Path:", chrome_driver_path)
    #print("System PATH:", os.environ['PATH'])
    #os.environ['PATH'] = f"{os.environ['PATH']}:{os.path.dirname(chrome_driver_path)}"
    context.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    context.driver.get("https://www.saucedemo.com")
    time.sleep(5)
    #context.driver.maximize_window()

def after_scenario(context, scenario):
    print("executing after scenario")
    context.driver.quit()


