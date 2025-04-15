import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time




@pytest.mark.usefixtures("setup_teardown")
class Test_practice:

    def test_register(self):
        driver = self.driver

        # Click on 'My Account' and 'Register'
        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.XPATH, "//a[text()='Register']").click()

        # Fill out the registration form
        driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("K Uday")
        driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("Kumar")
        email=driver.find_element(By.XPATH, "//input[@id='input-email']")
        email.send_keys(self.random_email())
        email_value=email.get_attribute('value')

        driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("9876543210")

        # Password and confirmation
        a = driver.find_element(By.XPATH, "//input[@id='input-password']")
        a.send_keys("987654321")
        b = a.get_attribute('value')

        c = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
        c.send_keys("987654321")
        d = c.get_attribute('value')

        # Agree to terms and conditions
        driver.find_element(By.XPATH, "//input[@name='agree']").click()

        # Click the Continue button
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()


        print("Filling registration form...")


        assert b == d, "Passwords do not match"

        print(email_value)

        time.sleep(5)



    def random_email(self):
        i = random.randint(0, 100)
        return "uday{}kumar@gmail.com".format(i)



    def test_invalid(self):
        driver = self.driver

        # Click on 'My Account' and 'Register'
        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.XPATH, "//a[text()='Register']").click()

        driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys("")
        driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys("")
        driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys()
        driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("")

        # Password and confirmation
        a = driver.find_element(By.XPATH, "//input[@id='input-password']")
        a.send_keys("")


        c = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
        c.send_keys("")


        # Agree to terms and conditions
        driver.find_element(By.XPATH, "//input[@name='agree']").click()

        # Click the Continue button
        driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        try:
           elements=driver.find_elements(By.XPATH,"//div[@class='text-danger']")

           for x in elements:
               if x.is_displayed():
                   print("Error displayed")
                   print(x.text)
               else:
                   print("Elements not visible")

        except:
            print("no error messages")

        allure.attach(driver.get_screenshot_as_png(), name="nirmal", attachment_type=AttachmentType.PNG)


        time.sleep(10)






