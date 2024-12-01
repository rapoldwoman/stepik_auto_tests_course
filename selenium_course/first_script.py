import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


driver.get("https://suninjuly.github.io/text_input_task.html")


textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

textarea.send_keys("get()")


submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()


driver.quit()
