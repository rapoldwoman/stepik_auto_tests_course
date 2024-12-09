import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.support.expected_conditions import none_of


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(10)
    yield browser
    print("\nend browser for test..")
    browser.quit()

@pytest.fixture(scope="function")
def time_total():
    # для проверки времени использовать https://time.is/ru/
    answer = math.log(int(time.time() + 0.4))
    return answer


