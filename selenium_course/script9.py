from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

try:

    x = browser.find_element(By.ID, "num1")
    num1 = x.text
    y = browser.find_element(By.ID, "num2")
    num2 = y.text

    total = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

                    