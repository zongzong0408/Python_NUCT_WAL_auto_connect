# from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

# driver = webdriver.Chrome(executable_path = "./chromedriver.exe", options = options)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

driver.implicitly_wait(10)
driver.get("www.google.com")
time.sleep(10)
print(driver.title)

# print(selenium.__version__)

time.sleep(100)