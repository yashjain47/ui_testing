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


'Click on "buttons"'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Buttons']")),"Element is not Clickable").click()



'------------------------------------------------------------------------------------------------'
# 'Click on "click"'
# explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"(//button[normalize-space()='Click Me'])[1]")),"Element is not Clickable").click()


# 'Confirming'
# resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//p[@id='dynamicClickMessage']")),"Unable to Click .").text
# print(f"response : {resp}")
# if "You have done a dynamic click" in resp:
#     print("Single Clicked Successfully")
# else:
#     print("FAILED")
'------------------------------------------------------------------------------------------------'


driver.implicitly_wait(2)

# '------------------------------------------------------------------------------------------------'
# 'Click on "double click"'
# double_click_ele = driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")
# print(f"double_click_ele : {double_click_ele}")
# action_chain.double_click(double_click_ele).perform()
# driver.implicitly_wait(2)



# 'Confirming'
# resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//p[@id='doubleClickMessage']")),"Unable to double Click.").text
# print(f"response : {resp}")
# if "You have done a double click" in resp:
#     print("Double Clicked Successfully")
# else:
#     print("FAILED")
# '------------------------------------------------------------------------------------------------'



driver.implicitly_wait(2)

'------------------------------------------------------------------------------------------------'
'Click on "double click"'
right_click_ele = driver.find_element(By.XPATH,"//button[@id='rightClickBtn']")
print(f"right_click_ele : {right_click_ele}")
action_chain.context_click(right_click_ele).perform()
driver.implicitly_wait(2)



'Confirming'
resp = explicit_wait.until(ec.presence_of_element_located((By.XPATH,"//p[@id='rightClickMessage']")),"Unable to double Click.").text
print(f"response : {resp}")
if "You have done a right click" in resp:
    print("Right Clicked Successfully")
else:
    print("FAILED")






'Closing the Browser'
sleep(5)
driver.close()
