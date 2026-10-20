"""
context_click = right click

"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
sleep(2)


# Right click

# achain = ActionChains(driver)

# right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# copy_ele = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")

# achain.context_click(right_click).perform()
# sleep(4)
# copy_ele.click()
# sleep(4)



# Double click

achain = ActionChains(driver)
double_click_element = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")

achain.double_click(double_click_element).perform()
sleep(2)
driver.switch_to.alert.accept()
sleep(2)