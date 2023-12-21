from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

driver = webdriver.Chrome(executable_path = "./chromedriver.exe", options = options)

driver.implicitly_wait(10)
driver.get("https://stackoverflow.com/questions/47392423/python-selenium-devtools-listening-on-ws-127-0-0-1")
print(driver.title)

# print(selenium.__version__)

time.sleep(100)