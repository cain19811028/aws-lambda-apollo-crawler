# -*- encoding: utf-8-*-

import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utility import scroll_down_to_bottom
from ssm import SSMHelper
from workalendar.asia import Taiwan

CAL = Taiwan()

def set_chrome_options():
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    return options


def login(driver):
    ssm = SSMHelper()

    driver.get("https://asiaauth.mayohr.com/HRM/Account/Login")
    scroll_down_to_bottom(driver)

    company = driver.find_element(By.NAME, "companyCode")
    company.clear()
    company.send_keys("MOXA")

    employee = driver.find_element(By.NAME, "employeeNo")
    employee.clear()
    employee.send_keys("20180003")

    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(ssm.get_secret("apollo"))

    time.sleep(2)

    driver.find_element(By.TAG_NAME, "form").submit()


def check_in(driver):
    time.sleep(5)

    driver.get("https://apollo.mayohr.com/ta?id=webpunch")
    scroll_down_to_bottom(driver)

    time.sleep(5)

    # click check in button
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    print("finish")


def lambda_handler(event, context):
    if CAL.is_holiday(date.today()):
        print("Today is a holiday !!!")
        return True

    time_flag_1 = time.time()
    options = set_chrome_options()
    time_flag_2 = time.time()
    print("set_chrome_options: %ss" % (time_flag_2 - time_flag_1))
    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)
    time_flag_3 = time.time()
    print("webdriver.chrome: %ss" % (time_flag_3 - time_flag_2))

    login(driver)
    check_in(driver)

    return True


# driver = webdriver.Chrome('/opt/chromedriver')
# login(driver)
# check_in(driver)
