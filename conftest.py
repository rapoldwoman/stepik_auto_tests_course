import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nend browser for test..")
    browser.quit()

@pytest.fixture(scope="function")
def time_total():
    # для проверки времени использовать https://time.is/ru/
    answer = math.log(int(time.time() + 0.4))
    return answer