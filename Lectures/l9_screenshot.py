import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""

Screenshot methods:

Note: The screenshot should be in the PNG format


1.  driver.get_screenshot_as_file("test1.png")
    Take whole window screenshot

2.  driver.save_screenshot("..//images/test2.png")
    Take whole window screenshot

3.  continuebutton = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
    continuebutton.screenshot("..//images/element.png")
    Take screenshot of a particular element


"""

driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

continuebutton = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
continuebutton.screenshot("/home/vvdn/Desktop/Selenium/images/element.png")
time.sleep(1)
continuebutton.click()

driver.get_screenshot_as_file("/home/vvdn/Desktop/Selenium/images/test1.png")
time.sleep(1)

driver.save_screenshot("/home/vvdn/Desktop/Selenium/images/test2.png")
time.sleep(1)

