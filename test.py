from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.google.com")

time.sleep(100)