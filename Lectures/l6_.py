"""
How to get text from an element in selenium







"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# How to get text from an element in selenium:


# By XPATH

# driver = webdriver.Chrome()
# driver.get("https://yatra.com")
# text = driver.find_element(By.XPATH,"//p[contains(text(),'On Yatra.com, you can tailor your trip from end-to')]").text
# print("Text :",text)



# OR BY NAME

# driver = webdriver.Chrome()
# driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
# text = driver.find_element(By.NAME,"login-input").text
# print("Text :",text)

# OR ANY Elememt Type


 # How to get Attribute Value from an element in selenium:

# driver = webdriver.Chrome()
# driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
# attr = driver.find_element(By.ID,"login-input").get_attribute("title")
# print("Attribute Value :",attr)




############################################################################################
# How to find the state of the element (enable or disable)


# driver = webdriver.Chrome()
# driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
# state = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']").is_enabled()
# print("State of Element :",state)




############################################################################################
# How to Handle Hidden Element in selenium

# driver = webdriver.Chrome()
# driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
# driver.maximize_window()
# hidden = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print("hidden Element :",hidden)
# time.sleep(2)
# driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
# time.sleep(2)
# hidden = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
# print("hidden Element :",hidden)




############################################################################################
# How to Handle Checkbox and Radio button Element in selenium


# driver = webdriver.Chrome()
# driver.get("https://www.sugarcrm.com/au/request-demo/")
# driver.maximize_window()
# time.sleep(4)
# hidden = driver.find_element(By.ID,"doi0").is_selected()
# print("hidden Element :",hidden)
# time.sleep(4)
# driver.find_element(By.ID,"doi0").click()
# time.sleep(4)
# hidden = driver.find_element(By.ID,"doi0").is_selected()
# print("hidden Element :",hidden)




