"""
How to handle iframes in selenium 

"""
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
time.sleep(2)

# switch with iframe locator
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

# switch with index
# driver.switch_to.frame(0)

# switch with ID
# driver.switch_to.frame("iframeResult")

# switch by name
# driver.switch_to.frame("iframeResult")


# inside the iframe
driver.find_element(By.XPATH,"//body/iframe[1]").click()
time.sleep(2)






