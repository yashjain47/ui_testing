from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By




browser = webdriver.Chrome()
browser.get("https://demoqa.com/text-box")
browser.maximize_window()
print(browser.title)
browser.execute_script("document.body.style.zoom='75%'")
sleep(1)

# 'Click on Elements'
# browser.implicitly_wait(2)
# browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]/svg/path').click()
# sleep(2)

'Click on Text Box'
browser.implicitly_wait(2)
browser.find_element(By.XPATH,value='//*[@id="item-0"]/span').click()
sleep(1)

'Text Box'
browser.find_element(By.ID,value="userName").send_keys("Yash Jain")
browser.implicitly_wait(2)

browser.find_element(By.ID,value="userEmail").send_keys("YashJain@gmail.com")
browser.implicitly_wait(2)

browser.find_element(By.XPATH,value='//*[@id="currentAddress"]').send_keys("Yash Jain")
browser.implicitly_wait(2)

browser.find_element(By.ID,value="permanentAddress").send_keys("Yash Jain")
browser.implicitly_wait(2)

browser.find_element(By.XPATH,value='//*[@id="submit"]').click()
browser.implicitly_wait(2)



'Click on Check Box'
browser.implicitly_wait(2)
browser.find_element(By.XPATH,value='//*[@id="item-1"]/span').click()
sleep(1)

'Checking if checked or not '
browser.find_element(By.XPATH,value='//*[@id="tree-node"]/ol/li/span/label').click()



'Click on Radio Box'
browser.implicitly_wait(2)
browser.find_element(By.XPATH,value='//*[@id="item-2"]/span').click()
sleep(1)

'Checking if checked or not '
browser.find_element(By.XPATH,value='//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label').click()












'sleep'
sleep(5)

browser.close()