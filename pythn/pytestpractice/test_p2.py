# import test
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
#
#
# def test_one():
#     driver=webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get("https://tutorialsninja.com/demo/")
#     driver.maximize_window()
#
#     driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("hp")
#     driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
#     print(driver.title)
#     element=driver.find_element(By.XPATH,"//a[text()='HP LP3065']")
#     driver.execute_script("arguments[0].scrollIntoView();", element)
#     try:
#         assert driver.find_element(By.XPATH,"//a[text()='HP LP365']"),"Error uday"
#         print("test passed")
#     except:
#         print("failed due to assertion fails")
#
#     print(driver.title,"uday")
#
