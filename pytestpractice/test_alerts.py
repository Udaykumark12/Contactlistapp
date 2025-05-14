import time
from os import times

import pytest
from selenium.webdriver.common.by import By



# Use the fixture defined in conftest.py
@pytest.mark.usefixtures("new_fixx")
def test_alert(new_fixx):
    driver = new_fixx  # Get the driver from the fixture
    driver.find_element(By.XPATH, "//a[@id='prompt']").click()

    my_alert = driver.switch_to.alert
    time.sleep(3)
    my_alert.send_keys("udayhjshgdgh")
    # print(my_alert.text)
    my_alert.accept()



@pytest.mark.usefixtures("new_fixx")
def test_alerta(new_fixx):
    driver = new_fixx
    driver.get("https://uday:uday6666@the-internet.herokuapp.com/basic_auth")
    driver.implicitly_wait(10)

    time.sleep(10)

