from selenium import webdriver
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input_block = browser.find_element_by_css_selector('#answer')
    input_block.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

