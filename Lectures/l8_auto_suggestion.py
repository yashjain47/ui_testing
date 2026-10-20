import time
from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
sleep(1)

# In Depart From, we are giving the Full Value Like New Delhi

depart_from = driver.find_element(By.ID,"BE_flight_origin_city")
depart_from.click()
sleep(1)
depart_from.send_keys("New Delhi")
sleep(1)
depart_from.send_keys(Keys.ENTER)
sleep(1)


# In Going to, we are just giving some value like New and select from suggestions like New York or New Orleans


goint_to = driver.find_element(By.ID,"BE_flight_arrival_city")
goint_to.send_keys("New")
sleep(1)
search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
print(len(search_results))
for results in search_results:
    # print(results.text)
    if "New York (JFK)" in results.text:
        sleep(1)
        results.click()
        sleep(1)
        break




"""
In Calendar date there are 2 ways to select the particular date :
"""

departure_date = driver.find_element(By.ID,"BE_flight_origin_date")
departure_date.click()
sleep(1)



# First by clickng the desired date that is:

# driver.find_element(By.ID,"13/06/2024").click()
# sleep(1)



# Second by choosing from the calender that is

all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
for date in all_dates:
    if date.get_attribute("data-date") == "30/06/2024":
        date.click()
        sleep(1)
        break

driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
time.sleep(4)




















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select




