from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


a=driver.find_element(By.XPATH, "//input[@placeholder='Username']")
a.send_keys("hjhg")

driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

main_window = driver.current_window_handle
all_windows = driver.window_handles


for window in all_windows:
    if window !=main_window:
        driver.switch_to.window(window)
        print(driver.title)
        break



driver.close()
driver.switch_to.window(main_window)


time.sleep(2)
