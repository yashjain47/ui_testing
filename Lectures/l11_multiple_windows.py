"""
How to handle multiple windows in sleenium python

"""

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.window import WindowType


driver = webdriver.Chrome()

# Open 1st Window
driver.get("https://yatra.com/")
driver.maximize_window()

# Show current or parent window (1st Window)
parent_handle = driver.current_window_handle
print("Parent Handle :",parent_handle)

time.sleep(2)

# Open 2nd Window
driver.find_element(By.XPATH,"//a[@title='Spiritual Divine Yatra']//img[@class='conta iner large-banner']").click()
all_handles = driver.window_handles

# Show all window (1st Window and 2nd window)
print("All Handles :",all_handles)
time.sleep(2)

for handle in all_handles:
    if handle != parent_handle:
        time.sleep(2)
        
        # Switch to 2nd window
        driver.switch_to.window(handle)

        # Open Third Window
        driver.find_element(By.XPATH,"//a[@href='https://www.yatra.com/india-tour-packages/holidays-in-ayodhya']//div[@class='Card']//span[contains(text(),'Book Now')]").click()
        time.sleep(2)
        # close the second window
        driver.close()
        time.sleep(2)
        break


driver.switch_to.window(parent_handle)
time.sleep(2)
driver.find_element(By.XPATH,"//a[@title='Spiritual Divine Yatra']//img[@class='conta iner large-banner']").click()
time.sleep(2)



# Open a new tab and switch to it
# driver.switch_to.new_window(WindowType.TAB)


