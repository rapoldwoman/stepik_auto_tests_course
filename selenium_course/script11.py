from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = 'https://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    value = browser.find_element(By.ID, "input_value")
    value_number = value.text
    x = calc(value_number)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)

    check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()




finally:

    time.sleep(3)
    browser.quit()