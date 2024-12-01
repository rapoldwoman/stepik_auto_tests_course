from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os



link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("sss")

    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("www")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("www.ru")

    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text.txt"
    file_dir = os.path.join(current_dir, file_name)
    element.send_keys(file_dir)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()


finally:

    time.sleep(10)
    browser.quit()
    