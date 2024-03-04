from selenium import webdriver
import os

path = os.getcwd() + "/driver/firefoxdriver.exe"

print(path)

browser = webdriver.Firefox(executable_path = r"D:\GitHub\zongzongchu0408@gmail.com\Python_NUCT_WAL_auto_connect\driver\firefoxdriver.exe")

browser.get("www.google.com.tw")

browser.implicitly_wait(5)

browser.quit()