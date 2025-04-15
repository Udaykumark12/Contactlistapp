from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Start the WebDriver and navigate to the website
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outer=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer)

inner=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("uday")

time.sleep(3)




