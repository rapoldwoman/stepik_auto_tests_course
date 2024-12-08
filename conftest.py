import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nend browser for test..")
    time.sleep(5)
    browser.quit()