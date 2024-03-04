from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import os
import time

path = os.getcwd() + r"\driver\firefoxdriver.exe"
print(path)

options = webdriver.FirefoxOptions()
options.binary_location = path

browser = webdriver.Firefox(service_log_path=path, options=options)

browser.get("www.google.com.tw")

time.sleep(10)

browser.quit()