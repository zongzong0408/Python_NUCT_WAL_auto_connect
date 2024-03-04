from selenium import webdriver
import os

driver = webdriver.Firefox()

driver.get("www.google.com.tw")

driver.implicitly_wait(5)

driver.quit()