from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    magic_button = browser.find_element_by_tag_name("button")
    magic_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element_by_id("input_value")
    x = calc(value.text)

    input = browser.find_element_by_id("answer")
    input.send_keys(x)

    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()