import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()

drop = driver.find_element(By.XPATH, "//select[@id='country']")
a = Select(drop)
a.select_by_visible_text("Option 1")


# c = a.options
#
# for i in c:
#     if i.text == "Option 1":
#         i.click()

time.sleep(5)


driver.quit()




