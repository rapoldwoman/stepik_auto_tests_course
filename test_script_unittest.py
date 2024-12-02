from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Test_class_name(unittest.TestCase):
    def test1url(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        input2.send_keys("Sysan")
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        input3.send_keys("xz")
        input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone"]')
        input4.send_keys("123")
        input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address"]')
        input5.send_keys("RUS")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual('successfully' in browser.find_element(By.CSS_SELECTOR, ".container").text)


    def test2url(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration2.html')

        input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address"]')
        input3.send_keys("address")
        input4 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
        input4.send_keys("123")
        input5 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
        input5.send_keys("RUS")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        self.assertEqual('successfully' in browser.find_element(By.CSS_SELECTOR, ".container").text)

    if __name__ == '__main__':
        unittest.main()