

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get("https://onlinenotepad.org/notepad")
driver.maximize_window()
achain = ActionChains(driver)


notepad = driver.find_element(By.XPATH,"//div[@class='ql-editor']")


sleep(2)
notepad.send_keys("Yash Jain")
sleep(5)

