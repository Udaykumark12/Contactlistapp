# import time
# from gettext import textdomain
#
# from selenium.webdriver.common.by import By
# import pytest
# from selenium import webdriver
#
# url = "https://thinking-tester-contact-list.herokuapp.com/"
#
#
# @pytest.fixture()
# def driver_init():
#     # Set up the WebDriver instance
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.maximize_window()
#     yield driver  # Yielding the driver to the test
#     driver.quit()  # Ensure the browser is closed after the test
#
#
# class TestValidLoginDetails:
#     def test_login(self, driver_init):
#         driver = driver_init
#
#         # Interactions for the sign-up form
#         driver.find_element(By.CSS_SELECTOR, "button#signup").click()
#         driver.find_element(By.CSS_SELECTOR, "input#firstName").send_keys("uday")
#         driver.find_element(By.CSS_SELECTOR, "input#lastName").send_keys("kumar")
#         driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("hema0102u737@gmail.com")
#         driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Susmita0305")
#         driver.find_element(By.CSS_SELECTOR, "button#submit").click()
#         error_message=driver.find_element(By.XPATH,"//span[@id='error']").text
#         assert error_message=="Email address is already in use","error we got"
#
#         # Allow time for submission
#         time.sleep(3)
#
#         # You can add some verification here if needed (e.g., checking that the user is redirected)
