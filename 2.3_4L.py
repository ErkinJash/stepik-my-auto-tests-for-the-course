from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "empty.txt")

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    input_1st_name = browser.find_element_by_name("firstname")
    input_1st_name.send_keys("Shamil")

    input_last_name = browser.find_element_by_name("lastname")
    input_last_name.send_keys("Erkenov")

    input_mail = browser.find_element_by_name("email")
    input_mail.send_keys("ksdfjh@gmail.com")

    input_file = browser.find_element_by_id("file")
    input_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()