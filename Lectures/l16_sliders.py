"""
    
"""


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com/products/mobiles-cases-covers?sort=plrty#bcrumbSearch:mobile%20phone")
driver.maximize_window()
sleep(2)

ele1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
ele2 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")


'''********************** for element 1 **********************'''
'''drag option 1'''
# ActionChains(driver).drag_and_drop_by_offset(ele1,60,0).perform()
# sleep(4)

'''drag option 2'''
# ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(30,0).release().perform()
# sleep(4)

'''drag option 3'''
ActionChains(driver).move_to_element(ele1).pause(1).click_and_hold(ele1).move_by_offset(80,0).release().perform()
sleep(4)



'''**********************for element 2 **********************'''
'''drag option 1'''
# ActionChains(driver).drag_and_drop_by_offset(ele2,-60,0).perform()
# sleep(4)

'''drag option 2'''
# ActionChains(driver).click_and_hold(ele2).pause(1).move_by_offset(-30,0).release().perform()
# sleep(4)

'''drag option 3'''
ActionChains(driver).move_to_element(ele2).pause(1).click_and_hold(ele2).move_by_offset(-20,0).release().perform()
sleep(4)
