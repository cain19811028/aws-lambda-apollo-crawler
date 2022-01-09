import time


def scroll_down_to_bottom(driver, waiting=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # wait to load page
        time.sleep(waiting)

        # calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def parse_url(url):
    arr_url = url.split("/")
    sid = arr_url[-3]
    pid = get_integer(arr_url[-1])
    return sid, pid


def parse_address(address):
    if address.find("縣") != -1:
        city = address.split("縣")[0] + "縣"
        if address.find("鎮") != -1:
            area = address.split("縣")[1:][0].split("鎮")[0] + "鎮"
        else:
            area = address.split("縣")[1:][0].split("市")[0] + "市"
    elif address.find("市") != -1:
        city = address.split("市")[0] + "市"
        area = address.split("市")[1:][0].split("區")[0] + "區"
    return city, area


def get_integer(text):
    return int(''.join(filter(str.isdigit, text)))


def check_alert(driver):
    try:
        driver.switch_to.alert.accept()
    except:
        return None
