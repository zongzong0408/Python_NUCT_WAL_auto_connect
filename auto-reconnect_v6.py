from selenium import webdriver
import subprocess
import requests
import time
import sys

while (True):

    http_code = 404
    
    try:

        http_code = requests.get("https://www.google.com").status_code
    
    except Exception as e:
        
        pass

    if (http_code != 200):

        sys.stdout.write("網路連接失敗\n")

        driver = webdriver.Chrome()

        time.sleep(3)
        
        ipconfig_result = subprocess.check_output(['ipconfig'], stderr = subprocess.STDOUT, shell = True, universal_newlines = True)
        ipconfig_lines = ipconfig_result.split('\n')
        gateway_match = re.search(r"Default Gateway.*: ([\d.]+)", output)
        
        driver.get("http://172.16.170.254:1000/login?admin")


        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

        username_field.send_keys("ncutvip@ncut.edu.tw")
        password_field.send_keys("23924505")

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()

        driver.quit()

        sys.stdout.write("恢復網路連接\n")

    else:

        sys.stdout.write("連接網路正常\n")

    time.sleep(3)