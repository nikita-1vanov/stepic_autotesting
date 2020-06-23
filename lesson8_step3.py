from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 

    def calc(a, b):
        return int(a) + int(b)

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    sum_num = calc(num1, num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum_num))
    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(15)
    browser.quit()

