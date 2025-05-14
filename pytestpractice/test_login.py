
import pytest

from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("setup_teardown")
class TestLogin:


    def test_register(self):
        driver = self.driver

        driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

        email = driver.find_element(By.XPATH, "//input[@id='input-email']")
        email.send_keys("uday52kumar@gmail.com")

        password=driver.find_element(By.XPATH, "//input[@id='input-password']")
        password.send_keys("987654321")

        driver.find_element(By.XPATH,"//input[@value='Login']").click()





