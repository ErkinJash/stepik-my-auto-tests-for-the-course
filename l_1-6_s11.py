from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x_answer = calc(x_element.text)
    print(x_answer)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x_answer)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()

    robot = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot)
    robot.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

