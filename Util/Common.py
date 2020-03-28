
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import stdout as console


def do_wait_for_visibility(driver,element = False,by = False,time_out = 5,interval = 100):
    wait = WebDriverWait(driver, time_out)

    if (element):
        return wait.until(EC.visibility_of_element_located(element))

    else:
        return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,by)))


def check_text_in_page_headers(driver,texts):
    elems = driver.find_elements_by_css_selector('h1')
    # console.write(str(elems))
    if len(elems)>0:
        for i in range(len(elems)):
            # console.write(str(elems[i].text))
            # console.write(texts)
            if texts == elems[i].text:
                return True
    else:
        console.write("No Element found")
        return False


def is_link_visible(driver,link_text):
    try:
        return driver.find_element_by_link_text(link_text).is_displayed()
    except:
        return False

def do_click_on_link(driver,link_text):
    try:
        driver.find_element_by_link_text(link_text).click()
        return True
    except:
        return False

def get_link_count(driver,link_text):
    elems = driver.find_elements_by_link_text(link_text)

    return len(elems)
