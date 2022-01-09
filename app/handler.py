# -*- encoding: utf-8-*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def set_chrome_options():
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    return options


def lambda_handler(event, context):
    time_flag_1 = time.time()
    options = set_chrome_options()
    time_flag_2 = time.time()
    print("set_chrome_options: %ss" % (time_flag_2 - time_flag_1))
    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)
    time_flag_3 = time.time()
    print("webdriver.chrome: %ss" % (time_flag_3 - time_flag_2))

    driver.get("https://asiaauth.mayohr.com/")

    # set_chrome_options: 1.33514404296875e-05s
    # webdriver.chrome: 4.760722398757935s
    # webdriver get url: 4.318072319030762s
    # scroll down to bottom: 3.224916458129883s
    # webdriver parse data: 4.119561195373535s
    # webdriver close: 0.11644101142883301s
    # webdriver quit: 0.004262208938598633s
    # total duration: 16545.72 ms

    return True


time_flag_1 = time.time()
options = set_chrome_options()
time_flag_2 = time.time()
print("set_chrome_options: %ss" % (time_flag_2 - time_flag_1))
driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)
time_flag_3 = time.time()
print("webdriver.chrome: %ss" % (time_flag_3 - time_flag_2))

driver.get("https://asiaauth.mayohr.com/")