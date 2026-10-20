"""
Javascript popups or alerts


"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
time.sleep(4)

# accept alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(4)

# dismiss alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
driver.switch_to.alert.dismiss()
time.sleep(4)

# send text in alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
driver.switch_to.alert.send_keys("YASH JAIN")
time.sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()
time.sleep(4)

