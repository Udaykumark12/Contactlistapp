import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome browser
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Explicit wait to ensure the elements are present and clickable
wait = WebDriverWait(driver, 10)

try:
    a=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@id='HTML7']//span[1]")))
    print(a.location) # {'x': 846, 'y': 1970}
    driver.execute_script("arguments[0].scrollIntoView();", a)
    b=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='slider-range']/span[2]")))
    print(b.location) #{'x': 976, 'y': 1970}
    act=ActionChains(driver)
    act.drag_and_drop_by_offset(a, 100, 0).perform()
    act.drag_and_drop_by_offset(b,-20,0).perform()
    print(a.location)
    print(b.location)
    time.sleep(9)

except Exception as e:
    print(e)


