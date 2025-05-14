import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://thinking-tester-contact-list.herokuapp.com/")
driver.find_element(By.CSS_SELECTOR,"button#signup").click()
driver.find_element(By.CSS_SELECTOR,"input#firstName").send_keys("uday")
driver.find_element(By.CSS_SELECTOR,"input#lastName").send_keys("kumar")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("udayjan66@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#password").send_keys("Susmita03")
driver.find_element(By.CSS_SELECTOR,"button#submit").click()
time.sleep(3)