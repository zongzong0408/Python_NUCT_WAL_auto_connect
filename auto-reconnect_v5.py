"""
    version C v5.0

    using Python 3.7.0
    using Windows 11 Home
    
    using selenium 3.14
    using urllib 1.2.01

    using Chrome browser driver
"""

from inspect import currentframe, getframeinfo
import requests
import time
import sys
import os

try:
    
    from selenium import webdriver                              # this for version below v4.6.0
    # from selenium.webdriver.chrome.service import Service
    # from webdriver_manager.chrome import ChromeDriverManager

    sys.stdout.write("system OK:\t successfully input selenium module.\n\n")

except Exception as e:

    sys.stdout.write("system ERROR:\t error on LINE <16>\n")
    sys.stdout.write("system ERROR:\t the selenium module hasn't been installed yet.\n")
    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
    sys.stdout.write("system INFO:\t visit https://pypi.org/project/selenium/ to get more information.\n")
    sys.stdout.write("system INFO:\t you can run <$: pip install selenium > in your terminal to quick install package.\n")
    sys.stdout.write("system INFO:\t after that you need install the drive match you target browser then that's all.\n")

"""
    constant values description

    TEST_IS_CONNECT_WAL_URL     : (str) the URL that you can check if you are disconnect to WAL or not.
    TARGET_TO_CONNECT_WAL_URL   : (str) the URL that you connect WAL.
    DETECT_CONNECT_ALIVE_TIME   : (int uint8_t) the range that you detect is connecting to WAL or not.
    OPEN_PAGE_WAITE_TIME        : (int uint8_t) the time that you wait program insert information to website then close page.
    CLEAR_TERMINAL_SCR_TIMES    : (int uint8_t) the time that you clear your local terminal screen.
    LOGIN_ACCOUNT               : (dic) the dictionary store your login account and password information.
"""

TEST_IS_CONNECT_WAL_URL     = "https://www.google.com"
TARGET_TO_CONNECT_WAL_URL   = "http://172.16.170.254/login?admin"

DETECT_CONNECT_ALIVE_TIME   = 10
OPEN_PAGE_WAITE_TIME        = 3
CLEAR_TERMINAL_SCR_TIMES    = 50

LOGIN_ACCOUNT = {
    "account"   : "ncutvip@ncut.edu.tw",
    "password"  : "23924505"
}

def connect(url: str, account: str, password: str) -> None:

    try:

        a = time.time()
        
        # driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options = option)
        
        b = time.time()
        init = round(b - a)

        sys.stdout.write(f"system INFO:\t initialize Chrome drive cost {init} second(s).\n")
        sys.stdout.write("system OK:\t successfully open Chrome driver.\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot open Chrome browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t ...\n")
        # sys.stdout.write("system OK:\t now is going to open FireFox.\n")

    try:

        driver.implicitly_wait(5)
        driver.get(url)

        sys.stdout.write(f"system OK:\t successfully connect target url. {url}\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        
        status_code = get_http_code(url)

        if (status_code != 200):

            sys.stdout.write(f"system ERROR:\t cannot connect your target url, error http code {status_code}.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write(f"system INFO:\t you are trying connect {url}, pls try another LAN IP.\n")

        driver.quit()

    try:

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

        sys.stdout.write("system OK:\t successfully find input field and bottom.\n")

    except Exception as e:
        
        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot find input field and bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n")

    try:

        username_field.send_keys(account)
        password_field.send_keys(password)

        sys.stdout.write("system OK:\t successfully input account and password information.\n")

    except Exception as e:
        
        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot insert account and password data to input field.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")

    try:

        time.sleep(OPEN_PAGE_WAITE_TIME)

        sys.stdout.write("system OK:\t successfully waiting website get and refresh information.\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

    try:

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()

        sys.stdout.write("system OK : successfully send account & password information.\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot click input bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time {  belongs to R }.\n")

    try:
        
        driver.quit()

        sys.stdout.write("system OK: successfully quit selenium browser.\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot quit selenium browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls quit it by yourself or shutdown program.\n")

    return
    
def detect_connection(url: str) -> bool:

    status_code = get_http_code(url)

    if status_code == 200:

        sys.stdout.write("system OK:\t successfully get WAL.\n")

        return True
    
    else:

        sys.stdout.write(f"system ERROR:\t cannot ping {url}, make sure WAL connection is available.\n")
        sys.stdout.write(f"system DETAIL:\t {status_code}\n\n")
        sys.stdout.write("system INFO:\t detect WAL connection is failed. the program is going to reconnect WAL.\n")

        return False 

def detect_http_connection(url: str) -> int:

    try:

        return requests.get(TEST_IS_CONNECT_WAL_URL).status_code

    except requests.exceptions.HTTPError as e:
    
        return e
    
    except requests.exceptions.SSLError as e:
    
        return e
    
    except requests.exceptions.ConnectionError as e:
    
        return e
    
    except requests.exceptions.Timeout as e:
    
        return e

def add_environment_variable_path() -> bool:

    os.path

def main() -> None:

    if (LOGIN_ACCOUNT["account"] == "..." or LOGIN_ACCOUNT["password"] == "..."):

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t your are not input login account & password yet.\n")
        sys.stdout.write(f"system INFO:\t pls key your data to LOGIN_ACCOUNT[] list.\n")

        return

    counting_start_time = time.time()
    detection_times = 1

    while True:

        if (detect_connection(TEST_IS_CONNECT_WAL_URL) != False):
            
            sys.stdout.write("system ERROR:\t program cannot connect WAL.\n")
            sys.stdout.write("system INFO:\t program is trying reconnect WAL.\n")

            try:
                
                connect(TARGET_TO_CONNECT_WAL_URL, LOGIN_ACCOUNT["account"], LOGIN_ACCOUNT["password"])
            
            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot run function -> connect()\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")

                sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
                sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} seconds.\n\n")
                time.sleep(OPEN_PAGE_WAITE_TIME)

                # break

                while detect_connection(TEST_IS_CONNECT_WAL_URL) == False:

                    sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
                    sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} seconds.\n\n")
                    time.sleep(OPEN_PAGE_WAITE_TIME)

        else:

            time_tuple  = time.localtime()
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
            sys.stdout.write(f"system INFO:\t (now time: {time_string}) WAL connection is all well.\n")
            sys.stdout.write(f"system INFO:\t it is going to check connection after {DETECT_CONNECT_ALIVE_TIME} seconds. (detection times {detection_times})\n")
            counting_end_time = time.time()
            
            try:

                sys.stdout.write(f"system INFO:\t program has already run {round((counting_end_time - counting_start_time) / 60 / 60)} hours.\n\n")

            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

            try:

                time.sleep(DETECT_CONNECT_ALIVE_TIME)

            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

            detection_times += 1

            if (detection_times >= CLEAR_TERMINAL_SCR_TIMES):
                
                try:
                
                    os.system("cls")
                
                except Exception as e:
                
                    frameinfo = getframeinfo(currentframe())
                    sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                    sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                    sys.stdout.write("system INFO:\t this program is developed under Windows system, if <cls> command isn't working, then it's going to run <clear> command.\n")

                    try:
                
                        os.system("clear")

                    except Exception as e:

                        frameinfo = getframeinfo(currentframe())              
                        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                        sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                        sys.stdout.write("system INFO:\t pls using Windows or Linux system, make sure that is popular OS. the program cannot clear terminal screen.\n")

                finally:

                    detection_times = 0

    # return

main()