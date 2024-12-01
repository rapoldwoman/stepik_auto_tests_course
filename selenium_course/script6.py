from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    First_name = browser.find_element(By.XPATH, '// input[@placeholder="Input your first name"]')
    First_name.send_keys("1111")
    Last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    Last_name.send_keys("2222")
    Email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    Email.send_keys("3333")

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(1)

    success_text_el= browser.find_element(By.TAG_NAME, 'h1')
    succses_text = success_text_el.text

    assert "Congratulations! You have successfully registered!" == succses_text

finally:
    time.sleep(5)
    browser.quit()