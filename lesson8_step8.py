from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

try: 

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link) 

    element = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)

    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('firstname')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('lastname')
    email = browser.find_element_by_name('email')
    email.send_keys('email')


    browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(15)
    browser.quit()

