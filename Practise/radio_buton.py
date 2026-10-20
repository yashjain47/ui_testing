from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
radio_button = "//span[normalize-space()='Radio Button']"



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
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,radio_button)),"Unable to Find Radio Box").click()


'Click on "Yes"'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//label[@for='yesRadio']")),"Element is not Clickable").click()


'Confirming'
resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//span[@class='text-success']")),"Unable to Click on the Checkbox.").text
print(f"response : {resp}")
if "Yes" in resp:
    print("YES Clicked Successfully")
else:
    print("FAILED")


driver.implicitly_wait(2)


'Click on "Impressive"'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//label[@for='impressiveRadio']")),"Element is not Clickable").click()


'Confirming'
resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//span[@class='text-success']")),"Unable to Click on the Checkbox.").text
print(f"response : {resp}")
if "Impressive" in resp:
    print("Impressive Clicked Successfully")
else:
    print("FAILED")


driver.implicitly_wait(2)


'Click on "Impressive"'
a = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//label[@for='noRadio']")),"Element is not Clickable").is_enabled()
print(a,"---")
if a == True:
    print("No is Already enabled")


'Closing the Browser'
sleep(5)
driver.close()
