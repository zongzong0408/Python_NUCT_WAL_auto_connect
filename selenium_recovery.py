from selenium import webdriver
import os

path = os.getcwd() + r"\driver\firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = path, options = webdriver.firefox.options)

browser.get("www.google.com.tw")

browser.implicitly_wait(5)

browser.quit()