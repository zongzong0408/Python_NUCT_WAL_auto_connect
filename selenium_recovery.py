from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import os
import time

path = os.getcwd() + r"\driver\geckodriver.exe"
print(path)

options = webdriver.FirefoxOptions()
options.binary_location = path

browser = webdriver.Chrome()

browser.get("www.google.com.tw")

time.sleep(10)

browser.quit()