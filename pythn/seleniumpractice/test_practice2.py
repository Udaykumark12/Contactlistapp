# import time
# from selenium.webdriver.common.by import By
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
#         driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("hema01000u737@gmail.com")
#         driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("Susmita0305")
#         driver.find_element(By.CSS_SELECTOR, "button#submit").click()
#
#         # Allow time for submission
#         time.sleep(3)
#
#         # You can add some verification here if needed (e.g., checking that the user is redirected)
