
import pytest
import requests
from requests import request
from selenium import webdriver


url = "https://tutorialsninja.com/demo/"

urla="https://www.selenium.dev/selenium/web/alerts.html#"


@pytest.fixture()
def setup_teardown(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()




@pytest.fixture()
def new_fixx():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()



