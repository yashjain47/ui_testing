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
parent_window = driver.current_window_handle


'Click on links'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Broken Links - Images']")),"Element is not Clickable").click()


'----------------------------------------------------------------------------------'
'Click on broken link'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Click Here for Broken Link']")),"Element is not Clickable").click()

all_handles = driver.window_handles

# Show all window (1st Window and 2nd window)
print("All Handles :",all_handles)

for i in all_handles:
    if parent_window != i:

        sleep(2)

        'Switch to next tab'
        # driver.switch_to.window(i)
        print(driver.title)
        sleep(2)
        break
'----------------------------------------------------------------------------------'


'Closing the Browser'
sleep(5)
driver.quit()





