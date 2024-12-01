from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    check.click()

    radio_b = browser.find_element(By.ID, "robotsRule")
    radio_b.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
   time.sleep(5)
   browser.quit()

    