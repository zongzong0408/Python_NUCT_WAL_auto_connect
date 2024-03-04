from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os

path = os.getcwd() + r"\driver\firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = path, options = Options())

browser.get("www.google.com.tw")

browser.implicitly_wait(5)

browser.quit()