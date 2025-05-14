from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@class, 'form-check-input')]")

# Approach
for i in checkbox:
    a=i.get_attribute("id")
    if a=="wednesday" or a=="tuesday":
        i.click()

time.sleep(10)

# Approach 2

# for i in range(len(checkbox)-2,len(checkbox)):
#     checkbox[i].click() 


# for i in range(len(checkbox)):
#     if i<2:
#         checkbox[i].click()


