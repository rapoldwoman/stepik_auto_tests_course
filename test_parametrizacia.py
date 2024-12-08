import pytest
import json
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def load_config():
    with open("userconfig.json", "r") as json_file:
        config = json.load(json_file)
        return config

class TestParametrizaciaAuth:

    def test_login(self,browser,load_config):
        browser.get(link)
        browser.find_element(By.ID, "ember470").click()
        browser.find_element(By.ID, "id_login_email").send_keys(load_config["login_stepik"])
        browser.find_element(By.ID, "id_login_password").send_keys(load_config["password_stepik"])
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()