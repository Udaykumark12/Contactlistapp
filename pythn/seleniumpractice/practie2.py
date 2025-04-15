
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
a=driver.find_elements(By.CLASS_NAME,'welcome-message')
for i in a:
    print(i.text)
    