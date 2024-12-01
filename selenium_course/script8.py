from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "treasure")
    number = x.get_attribute("valuex")
    y = calc(number)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    chek = browser.find_element(By.ID, "robotCheckbox")
    chek.click()

    radio =  browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()


finally:
   time.sleep(4)
   browser.quit()