from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
text_box = "//span[normalize-space()='Text Box']"




'Initializing the Browser'
url = "https://demoqa.com"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")


'Click on Elements'
driver.find_element(By.XPATH,elements).click()


'Click on Text box'
explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,text_box)),"Unable to Find Text Box").click()


'Fill Text Boxes'
driver.find_element(By.ID,value="userName").send_keys("Yash Jain")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="userEmail").send_keys("YashJain@gmail.com")
driver.implicitly_wait(2)
driver.find_element(By.XPATH,value='//*[@id="currentAddress"]').send_keys("Yash Jain")
driver.implicitly_wait(2)
driver.find_element(By.ID,value="permanentAddress").send_keys("Yash Jain")
driver.implicitly_wait(2)


'Click on Submit Button'
driver.find_element(By.XPATH,value='//*[@id="submit"]').click()
driver.implicitly_wait(2)


'Confirming te Details are filled Correctly and Submitted Successfully'
resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//p[@id='currentAddress']")),"Submit Failed,Please check the inputs...").text
print(f"response : {resp}")
if "Yash Jain" in resp:
    print("Form Submitted Successfully...")
else:
    print("Form Submitted Failed...")


'Closing the Browser'
sleep(5)
driver.close()
