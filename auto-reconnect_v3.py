"""
    version FC

    using Python 3.7.0
    using Windows 11 Home
    using FireFox or Chrome browser
"""

import requests
import time
import sys
import os

try:
    
    from selenium import webdriver

except Exception as e:

    sys.stdout.write("system ERROR:\t the selenium module hasn't been installed yet.\n")
    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
    sys.stdout.write("system INFO:\t visit https://pypi.org/project/selenium/ to get more information.\n")
    sys.stdout.write("system INFO:\t you can run <$: pip install selenium > in your terminal to quick install package.\n")
    sys.stdout.write("system INFO:\t after that you need install the drive match you target browser then that's all.\n")
else:

    sys.stdout.write("system INFO:\t successfully input selenium module.\n\n")

"""
    constant values description

    TEST_IS_CONNECT_WAL_URL     : 
    TARGET_TO_CONNECT_WAL_URL   : 
    DETECT_CONNECT_ALIVE_TIME   : 
    OPEN_PAGE_WAITE_TIME        : 
    CLEAR_TERMINAL_SCR_TIMES    : 
    LOGIN_ACCOUNT               : 
"""

TEST_IS_CONNECT_WAL_URL     = "https://www.google.com"
TARGET_TO_CONNECT_WAL_URL   = "http://172.16.170.254:1000/login?admin"

DETECT_CONNECT_ALIVE_TIME   = 10
OPEN_PAGE_WAITE_TIME        = 3
CLEAR_TERMINAL_SCR_TIMES    = 50

LOGIN_ACCOUNT = {
    "account"   : "s3B217114@student.ncut.edu.tw",
    "password"  : "A131724867"
}

def connect(url: str, account: str, password: str) -> None:

    try:

        driver = webdriver.Firefox()

    except Exception as e:

        sys.stdout.write("system ERROR:\t cannot open FireFox browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t program is going to run another browser.\n")

        try:

            driver = webdriver.Chrome()

        except Exception as e:

            sys.stdout.write("system ERROR:\t cannot open Chrome browser.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write("system INFO:\t program is going to shutdown. pls using popular browser.\n")

        else:

            sys.stdout.write("system INFO:\t successfully open Chrome driver.\n")

    else:

        sys.stdout.write("system INFO:\t successfully open firefox driver.\n")

    try:

        driver.get(url)

    except Exception as e:

        sys.stdout.write("system ERROR:\t cannot connect your target url.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write(f"system INFO:\t you are trying connect {url}, pls try another LAN IP.\n")

    else:

        sys.stdout.write(f"system INFO:\t successfully connect target url. {url}\n")

    try:

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

    except Exception as e:
    
        sys.stdout.write("system ERROR:\t cannot find input field and bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n")

    else:

        sys.stdout.write("system INFO:\t successfully find input field and bottom.\n")

    try:

        username_field.send_keys(account)
        password_field.send_keys(password)

    except Exception as e:
    
        sys.stdout.write("system ERROR:\t cannot insert account and password data to input field.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n")

    else:

        sys.stdout.write("system INFO:\t successfully input account and password information.\n")

    try:

        time.sleep(OPEN_PAGE_WAITE_TIME)

    except Exception as e:

        sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

    else:

        sys.stdout.write("system ERROR:\t successfully waiting website get and refresh information.\n")

    try:

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()
    
    except Exception as e:

        sys.stdout.write("system ERROR:\t cannot click input bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time {  belongs to R }.\n")

    else:

        sys.stdout.write("system INFO: successfully send account & password information.\n")

    try:
        
        driver.quit()

    except Exception as e:

        sys.stdout.write("system ERROR:\t cannot quit selenium browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls quit it by yourself or shutdown program.\n")

    else:

        sys.stdout.write("system INFO: successfully quit selenium browser.\n")

    return
    
def detect_connection(url: str) -> bool:

    status_code = 404

    try:

        status_code = requests.get(url).status_code
    
    except Exception:

        sys.stdout.write(f"system ERROR:\t cannot ping {url}, make sure WAL connection is available.\n")
        sys.stdout.write(f"system DETAIL:\t {status_code}\n\n")
        sys.stdout.write("system INFO:\t detect WAL connection is failed. the program is going to reconnect WAL.\n")

        return False

    else:

        return True

def main() -> None:

    counting_start_time = time.time()
    detection_times = 1

    while True:

        if (detect_connection(TEST_IS_CONNECT_WAL_URL) == False):
            
            sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
            sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} times.\n")

            connect(TARGET_TO_CONNECT_WAL_URL, LOGIN_ACCOUNT["account"], LOGIN_ACCOUNT["password"])

        time_tuple  = time.localtime()
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
        sys.stdout.write(f"system INFO:\t (now time: {time_string}) WAL connection is all well.\n")
        sys.stdout.write(f"system INFO:\t it is going to check connection after {DETECT_CONNECT_ALIVE_TIME} seconds. (detection times {detection_times})\n")
        counting_end_time = time.time()
        sys.stdout.write(f"system INFO:\t program has already run {round((counting_end_time - counting_start_time) / 60 / 60)} hours.\n\n")

        time.sleep(DETECT_CONNECT_ALIVE_TIME)

        detection_times += 1

        if (detection_times >= CLEAR_TERMINAL_SCR_TIMES):
            
            try:
            
                os.system("cls")
            
            except Exception as e:
            
                sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t this program is developed under Windows system, if <cls> command isn't working, then it's going to run <clear> command.\n")

                try:
            
                    os.system("clear")

                except Exception as e:
            
                    sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                    sys.stdout.write("system INFO:\t pls using Windows or Linux system, make sure that is popular OS. the program cannot clear terminal screen.\n")

            finally:

                detection_times = 0

    # return

main()