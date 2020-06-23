from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    browser.find_element_by_css_selector('#book').click()

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input_block = browser.find_element_by_css_selector('#answer')
    input_block.send_keys(y)

    browser.find_element_by_css_selector('#solve').click()

finally:
    time.sleep(15)
    browser.quit()

