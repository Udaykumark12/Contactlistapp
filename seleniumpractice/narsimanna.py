import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Start Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()

# Wait until the "Two Wheelers" section is visible
search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Two Wheelers']//div//span[@class='_1XjE3T']"))
)
act = ActionChains(driver)
act.move_to_element(search).perform()
time.sleep(3)

# Locate the petrol and electric vehicles links
# petrol = driver.find_element(By.XPATH, "//a[contains(text(), 'Petrol Vehicles')]")
# petrol.click()



electric = driver.find_element(By.XPATH, "//a[normalize-space()='Electric Vehicles']")
electric.click()
#
# # Perform the hover actions using ActionChains
# act = ActionChains(driver)
# act.move_to_element(search).perform()

# Wait for a few seconds before closing the browser (or performing any additional actions)
time.sleep(20)

# Close the browser
driver.quit()
