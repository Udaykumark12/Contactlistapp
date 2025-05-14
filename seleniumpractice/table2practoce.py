import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
driver.maximize_window()

row = len(driver.find_elements(By.XPATH, "//table[@class='tsc_table_s13']//tr"))
col = len(driver.find_elements(By.XPATH, "//table[@class='tsc_table_s13']//tr[2]/td"))

print("Total Rows:", row)
print("Total Columns:", col)


count=0
for i in range(2, row + 1):  # start from 2 to skip header row
    for c in range(1, col + 1):
        try:
            x = driver.find_element(By.XPATH, "//table[@class='tsc_table_s13']//tr[" + str(i) + "]/td[" + str(c) + "]").text
            print(x, end=' | ')
        except NoSuchElementException as e:
            print("Missing Element", end=' | ')
            count+=1
    print()

print(count)
