from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button1 = browser.find_element(By.ID, "book" )
    button1.click()
    
    x = browser.find_element(By.ID, "input_value")
    y = x.text
    number = calc(int(y))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(number)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()


    




finally:
    time.sleep(5)
    browser.quit()