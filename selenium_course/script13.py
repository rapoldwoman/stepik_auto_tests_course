from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    number = browser.find_element(By.ID, 'input_value')
    x = int(number.text)
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

finally:
    time.sleep(5)
    browser.quit()