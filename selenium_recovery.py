from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
import time

options = Options()
path = os.getcwd() + r"\driver\firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = path, options=options)

browser.get("www.google.com.tw")

time.sleep(10)

browser.quit()