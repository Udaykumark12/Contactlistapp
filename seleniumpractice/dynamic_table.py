import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Start Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Get all rows in the table
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print("Number of rows:", rows)

# Get the number of columns (using the first row header to count columns)
columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))
print("Number of columns:", columns)
print(type(columns))

# Loop through rows and columns to get cell data
# for i in range(2, rows + 1):  # Start from 2 to skip header row
#     for j in range(1, columns + 1):
#         cell_text = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#         print(cell_text, end=" ")
#
#     print()


for y in range(2,rows+1):
    autor=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(y)+"]/td[2]").text

    if autor=="Mukesh":
        book=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(y)+"]/td[1]").text

        print(autor,book)




time.sleep(3)


driver.close()



# # # Scroll the first row into view
# # if rows:
# #     driver.execute_script("arguments[0].scrollIntoView();", rows[0])  # Scroll the first row into view
# #
# # # Print the first row
# # print(rows[0].text)
#
# # Optionally, wait before closing







