"""

-->> Both waits are dynamic waits(Implicit and Explicit)

------------------------------------------------------------------------------------------------------

Implicit Waits:

(Applicable for all)

1.  Implicit waits tells the webdriver maximum wait time when searching for elements before throwing exception.
2.  Implicit wait is global, it is applicable to all the webelements in the script.
3.  Implicit waits applies to all webelements you do not specify "Expected Condition" on the element to be located.


------------------------------------------------------------------------------------------------------

Explicit Waits:

(Applicable on desired web element based on the specified condition)

1.  Explicit waits tells the webdriver to halt the execution until a particular condition is met or maximum time has passed.
2.  Explicit wait time is applicable only to those webelements which are specified by the users.
3.  Explicit wait requires the expected condition to be specified for elements like "wait untill element is enabled".


------------------------------------------------------------------------------------------------------

Fluent Waits:

We can specify polling frequency for the fluent wait (Its something same as explicit wait)



"""


from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



#################################################################################################

# IMPLICIT WAITS:

"""
driver.implicitly_wait(10) -->

IMPLICIT wait till 10 seconds and find the webelement from the script ,till 10 seconds it will not close the window, 
if it doesn't find the webelements in 10 seconds it will close the window with some error,
if it find the webelement than it will not wait till 10 seconds to complete.

thats called dynamic wait because it changes its property according to the scenario.

"""


# driver = webdriver.Chrome()

# driver.implicitly_wait(10)
# driver.get("https://login.salesforce.com/?locale=in")
# driver.maximize_window()
# driver.find_element(By.ID,"username").send_keys("YASH JAIN")
# driver.find_element(By.ID,"password").send_keys("YASH JAIN")



#################################################################################################

# EXPLICIT WAITS:

"""
explicit_wait = WebDriverWait(driver,10)
"""


driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()


explicit_wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[ElementClickInterceptedException])

explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).click()
explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).send_keys("New Delhi")
explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).send_keys(Keys.ENTER)


# depart_from = driver.find_element(By.ID,"BE_flight_origin_city")
# depart_from.click()
# depart_from.send_keys("New Delhi")
# depart_from.send_keys(Keys.ENTER)


explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_arrival_city"))).send_keys("New York (JFK)")
explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_arrival_city"))).send_keys(Keys.ENTER)


# goint_to = driver.find_element(By.ID,"BE_flight_arrival_city")
# goint_to.send_keys("New")

# sleep(2)
# search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
# print(len(search_results))
# for results in search_results:
#     # print(results.text)
#     if "New York (JFK)" in results.text:
#         results.click()
#         break





explicit_wait.until(ec.element_to_be_clickable((By.ID,"BE_flight_origin_date"))).click()

'''It will eliminate these 2 below lines'''
# departure_date = driver.find_element(By.ID,"BE_flight_origin_date")
# departure_date.click()



all_dates = explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

'''It will eliminate this below line'''
# all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")


for date in all_dates:
    if date.get_attribute("data-date") == "30/06/2024":
        date.click()
        break


driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
time.sleep(4)

