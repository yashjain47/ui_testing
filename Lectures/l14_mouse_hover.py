"""
Mouse Hover


Action chains class helps you to :

1.  right click
2.  double click
3.  mouse hover   
and many more

"""



from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# driver = webdriver.Chrome()
# driver.get("https://yatra.com")
# driver.maximize_window()
# sleep(2)
# more_button = driver.find_element(By.XPATH,"//span[@class='more-arr']")
# account_button = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
# sleep(2)
# achain = ActionChains(driver)
# sleep(2)
# achain.move_to_element(account_button).perform()
# sleep(2)
# achain.move_to_element(more_button).perform()
# sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Cruise']").click()
# sleep(4)

########################################################################################################



driver = webdriver.Chrome()
driver.get("https://yatra.com")
driver.maximize_window()
sleep(2)
more_button = driver.find_element(By.XPATH,"//a[normalize-space()='Support']")
achain = ActionChains(driver)
achain.move_to_element(more_button).click().perform()
sleep(6)
