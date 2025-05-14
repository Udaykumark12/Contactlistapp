import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the driver
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Global implicit wait
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()


mainclick =driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']")
mainclick.click()
driver.execute_script("arguments[0].scrollIntoView();", mainclick)



# # Switch to outer frame
# outer = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
#
# driver.switch_to.frame(outer)
#
# # Scroll the outer frame into view (corrected JavaScript)
#
#
# # Switch to inner frame
# inner = driver.find_element(By.CSS_SELECTOR, "iframe[src='SingleFrame.html']")
# driver.switch_to.frame(inner)
#
#
# inbox = driver.find_element(By.XPATH, "//input[@type='text']")
# inbox.send_keys("uday kumar")
# inbox.click()


driver.find_element(By.XPATH, "//a[normalize-space()='SwitchTo']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Alerts']").click()




time.sleep(10)

driver.quit()
