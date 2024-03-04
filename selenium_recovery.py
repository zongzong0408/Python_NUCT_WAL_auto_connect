from selenium import webdriver
import os

path = os.getcwd() + "/driver/firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = webdriver.FirefoxOptions.binary_location(path))

browser.get("www.google.com.tw")

browser.implicitly_wait(5)

browser.quit()