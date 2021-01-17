from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value")
    x_answer = calc(x.text)

    input = browser.find_element_by_id("answer")
    input.send_keys(x_answer)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
