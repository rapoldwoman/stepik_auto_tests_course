from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    funny_button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn')
    funny_button.click()

    new_window = browser.switch_to.window(browser.window_handles[1])

    number = browser.find_element(By.ID, "input_value")
    x = number.text
    y = calc(int(x))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()





finally:

    time.sleep(5)
    browser.quit()