from selenium import webdriver
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button.btn').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    input_block = browser.find_element_by_css_selector('#answer')
    input_block.send_keys(y)

    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(15)
    browser.quit()

