from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Start the WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Find the dropdown menu
flag = driver.find_element(By.XPATH, "//select[@id='country']")

# Scroll the dropdown into view
driver.execute_script("arguments[0].scrollIntoView();", flag)

# Initialize Select for interacting with the dropdown
drop = Select(flag)



# drop=Select(driver.find_element(By.XPATH, "//select[@id='country']"))

time.sleep(3)

# Approach 1: Select by visible text
# drop.select_by_visible_text("One")
# drop.select_by_index(1)

# Get all options and select 'United States'
x = drop.options
for opt in x:
    if opt.text == "United States":
        opt.click()

# Alternatively, print all options (if you want to see them)
# for opt in x:
#     print(opt.text)

# Wait before closing
time.sleep(10)
driver.quit()
