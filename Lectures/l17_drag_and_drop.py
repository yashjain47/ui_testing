from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains




driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
sleep(2)

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
drag_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")

'''drag and drop option 1'''
# ActionChains(driver).drag_and_drop(drag_ele,drop_ele).perform()
# sleep(4)

'''drag and drop by coordinates (x,y)'''
ActionChains(driver).drag_and_drop_by_offset(drag_ele,150,20).perform()
sleep(4)