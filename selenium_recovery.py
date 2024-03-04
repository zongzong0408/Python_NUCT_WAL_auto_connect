from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import os
import time

options = webdriver.FirefoxOptions()
path = os.getcwd() + r"\driver\firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = path, options=options)

browser.get("www.google.com.tw")

time.sleep(10)

browser.quit()