from time import sleep
from seleniumwire import webdriver
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




'Click on links'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Links']")),"Element is not Clickable").click()


'Checking window handles'
parent_window = driver.current_window_handle
print(f"Parent Window Handles : {parent_window}")



'----------------------------------------------------------------------------------'
'Click on New Tab link'
# explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//a[@id='simpleLink']")),"Element is not Clickable").click()

# all_handles = driver.window_handles

# # Show all window (1st Window and 2nd window)
# print("All Handles :",all_handles)

# for i in all_handles:
#     if parent_window != i:

#         sleep(2)

#         'Switch to next tab'
#         # driver.switch_to.window(i)
#         print(driver.title)
#         sleep(2)
#         break
'----------------------------------------------------------------------------------'



"""
FOR API WE USE
seleniumwire
"""





# 'API Response Created'
# api1 = driver.find_element(By.XPATH,"//a[@id='created']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 201 and "Created" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break



sleep(1)

# 'API No Content'
# api1 = driver.find_element(By.XPATH,"//a[@id='no-content']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 204 and "No Content" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break

sleep(1)


# 'API Moved'
# api1 = driver.find_element(By.XPATH,"//a[@id='moved']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 301 and "Moved Permanently" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break

sleep(1)



# 'API Bad request'
# api1 = driver.find_element(By.XPATH,"//a[@id='bad-request']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 400 and "Bad Request" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break

sleep(1)

# 'API Unauthorized'
# api1 = driver.find_element(By.XPATH,"//a[@id='unauthorized']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 401 and "Unauthorized" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break

sleep(1)

# 'API Forbidden'
# api1 = driver.find_element(By.XPATH,"//a[@id='forbidden']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 403 and "Forbidden" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break

sleep(1)

# 'API NotFound'
# api1 = driver.find_element(By.XPATH,"//a[@id='invalid-url']").click()
# print(f"api : {api1}")

# for request in driver.requests:
#     # print(request)
#     if request.response:
#         if "https://demoqa.com" in request.url and request.response.status_code == 404 and "Not Found" in request.response.reason:
#             print(request.url,request.response.status_code,request.response.reason,"\n") 
#             print("PASSED")
#             break





'Closing the Browser'
sleep(5)
driver.quit()





