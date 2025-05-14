import time
from selenium.webdriver.common.by import By
from selenium import webdriver

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
year = "2005"
date = "3"

# Open the datepicker
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()


while True:
    current_month = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text
    current_year = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text

    # If the correct month and year are displayed, exit the loop
    if current_month == month and current_year == year:
        break
    else:

        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()


dates = driver.find_elements(By.XPATH, "//table//tbody/tr/td/a")

# Select the desired date
for d in dates:
    if d.text == date:
        d.click()
        break


time.sleep(6)


driver.quit()
