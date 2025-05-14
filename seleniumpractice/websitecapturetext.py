import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://tutorialsninja.com/demo/")
a=driver.find_element(By.XPATH,"//input[@placeholder='Search']")
a.send_keys("hp")
b=driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']")
b.click()


time.sleep(10)

