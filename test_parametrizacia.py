import pytest
import json
import time
import math
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def load_config():
    with open("userconfig.json", "r") as json_file:
        config = json.load(json_file)
        return config


class TestParametrizaciaAuth:

    @pytest.mark.parametrize('url', [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesdson/236905/step/1"])
    def test_login_and_input_answer(self,browser,load_config,url,time_total):
        link = f"{url}"
        browser.get(link)
        browser.find_element(By.ID, "ember470").click()
        browser.find_element(By.ID, "id_login_email").send_keys(load_config["login_stepik"])
        browser.find_element(By.ID, "id_login_password").send_keys(load_config["password_stepik"])
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]').send_keys(time_total)
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        notification = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")

        assert "Correct!" == notification.text
        print("Утверждение верно")

