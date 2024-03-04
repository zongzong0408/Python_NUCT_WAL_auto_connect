from selenium import webdriver
import os

path = os.getcwd() + "/driver/firefoxdriver.exe"

driver = webdriver.Firefox(executable_path = path)

driver.get("www.google.com.tw")

driver.implicitly_wait(5)

driver.quit()