from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
button = "//span[normalize-space()='Buttons']"



'Initializing the Browser'
url = "https://demoqa.com"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")
explicit_wait = WebDriverWait(driver,10)
action_chain = ActionChains(driver)

'Click on Elements'
driver.find_element(By.XPATH,elements).click()




'Click on web tables'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Web Tables']")),"Element is not Clickable").click()



'Click on "click"'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@id='addNewRecordButton']")),"Element is not Clickable").click()




driver.implicitly_wait(2)

driver.find_element(By.ID,value="firstName").send_keys("Yash")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="lastName").send_keys("Jain")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,value="//input[@id='userEmail']").send_keys("YashJain@gmail.com")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="age").send_keys("24")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="salary").send_keys("750000000")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="department").send_keys("Pts")
driver.implicitly_wait(2)


driver.find_element(By.ID,"submit").click()


table_data = driver.find_element(By.XPATH,"//div[@class='ReactTable -striped -highlight']").text
# print(f"Table data : {table_data}")


if "Yash Jain" in table_data:
    print("Entry Added Successfully")
else:
    print("Entry Failed")




'Closing the Browser'
sleep(5)
driver.close()
