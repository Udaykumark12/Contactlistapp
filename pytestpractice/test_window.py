import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class Test_practice:
    def test_register(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

        main_window = driver.current_window_handle
        all_windows = driver.window_handles

        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                print(driver.title)
                break

        driver.close()
        driver.switch_to.window(main_window)
        print(driver.title)

        time.sleep(2)
