from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestClassName(unittest.TestCase):
    def test_1url(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        First_name = browser.find_element(By.XPATH, '// input[@placeholder="Input your first name"]')
        First_name.send_keys("1111")
        Last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        Last_name.send_keys("2222")
        Email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        Email.send_keys("3333")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual('Congratulations! You have successfully registered!', browser.find_element(By.TAG_NAME, 'h1').text)


    def test_2url(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        First_name = browser.find_element(By.XPATH, '// input[@placeholder="Input your first name"]')
        First_name.send_keys("1111")
        Last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        Last_name.send_keys("2222")
        Email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        Email.send_keys("3333")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual('Congratulations! You have successfully registered!', browser.find_element(By.TAG_NAME, 'h1').text)

if __name__ == '__main__':
        unittest.main()