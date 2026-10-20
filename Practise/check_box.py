from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
check_box = "//span[normalize-space()='Check Box']"



'Initializing the Browser'
url = "https://demoqa.com"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")


'Click on Elements'
driver.find_element(By.XPATH,elements).click()


'Click on Check Box'
explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,check_box)),"Unable to Find Check Box").click()


'Click on Check Boxes'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//span[@class='rct-checkbox']")),"Element is not Clickable").click()


'Confirming '
resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//span[normalize-space()='home']")),"Unable to Click on the Checkbox.").text
# print(f"response : {resp}")
if "You have selected" in resp:
    print("Clicked Successfully...")
else:
    print("Clicked Failed...")


'Closing the Browser'
sleep(5)
driver.close()
