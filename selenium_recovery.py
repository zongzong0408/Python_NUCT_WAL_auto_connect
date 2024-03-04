from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
import os
import time

path = os.getcwd() + r"\driver\geckodriver.exe"
print(path)

options = webdriver.EdgeOptions()
options.add_argument("--enable-chrome-browser-cloud-management")

browser = webdriver.Edge(options=options)

browser.get("www.google.com.tw")

time.sleep(10)

browser.quit()