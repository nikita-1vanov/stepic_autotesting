from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input_block = browser.find_element_by_css_selector('#answer')
    input_block.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    button = browser.find_element_by_css_selector('button.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button.click()


finally:
    time.sleep(15)
    browser.quit()

