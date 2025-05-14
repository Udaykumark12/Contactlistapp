import time
from itertools import count

from selenium.webdriver.common.by import By
from selenium import webdriver

# Start Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
colums=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th"))
print(rows)
print(colums)

# for r in range(2,rows+1):
#     for c in range(1,colums+1):
#         s=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]").text
#         print(s,end='  ')
#
#     print()

count = 0
for r in range(2, rows + 1):  # Skipping header (assuming row 1 is header)
    name = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr["+str(r)+"]//td[2]").text

    if name == "Mukesh":
        count += 1
        for c in range(1, colums + 1):  # Loop through all columns
            cell_text = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]").text
            print(cell_text, end=' ')
        print()  # Newline after each row

print("Total Mukesh entries:", count)




