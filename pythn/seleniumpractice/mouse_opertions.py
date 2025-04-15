import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Explicit wait to ensure the elements are present and clickable
wait = WebDriverWait(driver, 10)

try:
    a = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Point Me']")))

    # Corrected scrollIntoView syntax
    driver.execute_script("arguments[0].scrollIntoView();", a)

    b = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='HTML3']/div[1]/div/div/a[1]")))
    act = ActionChains(driver)
    time.sleep(3)
    act.move_to_element(a).move_to_element(b).click().perform()
    time.sleep(3)

except Exception as e:
    print(f"Error occurred: {e}")
    driver.quit()



driver.quit()
