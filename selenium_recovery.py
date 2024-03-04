from selenium import webdriver
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

path = os.getcwd() + "/driver/firefoxdriver.exe"

binary = FirefoxBinary('path/to/installed firefox binary')
browser = webdriver.Firefox(firefox_binary=path)

browser.get("www.google.com.tw")

browser.implicitly_wait(5)

browser.quit()