import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to iframe containing the datepicker
a = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
driver.switch_to.frame(a)

# Define target month, year, and date
month = "May"
year = "2025"
date = "3"

# Open the datepicker
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    # If the correct month and year are displayed, exit the loop
    if current_month == month and current_year == year:
        # Use WebDriverWait to ensure the date element is visible and clickable
        date_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[normalize-space()='{date}']"))
        )
        date_element.click()
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

# Wait for the datepicker to close and for the element to be updated
time.sleep(6)

driver.quit()
