from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://total-qa.com/checkbox-example/")
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for i in range(len(checkbox)-3,len(checkbox)):
    checkbox[i].click()



