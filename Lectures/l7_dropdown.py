from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


############################################################################################
# How to Handle Dropdown Element in selenium (SELECT TAG)

"""
for Single SELECT:

select_by_index
select_by_value
select_by_visibletext



"""



# driver = webdriver.Chrome()
# driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
# driver.maximize_window()
# dropdown = driver.find_element(By.NAME,"UserTitle")
# # print("dropdown :",dropdown)
# dd = Select(dropdown)
# # print("DD :",dd)

# dd.select_by_index(0)
# time.sleep(4)
# dd.select_by_value("Customer_Service_Manager_ANZ")
# time.sleep(4)
# dd.select_by_visible_text("Operations Manager")
# time.sleep(4)







############################################################################################
# How to Handle Dropdown Element in selenium (MULTI SELECT TAG)

"""
for Multi SELECT:

select_by_index
select_by_value
select_by_visibletext

select_all

deselect_by_index
deselect_by_value
deselect_by_visibletext

deselect_all

"""



driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
dropdown = driver.find_element(By.ID,"countriesmultiple")
dd = Select(dropdown)

dd.select_by_index(0)
time.sleep(4)
dd.select_by_index(3)
time.sleep(4)
dd.select_by_index(4)
time.sleep(4)
dd.deselect_by_index(3)
time.sleep(4)
dd.deselect_all()

# dd.select_by_value("Customer_Service_Manager_ANZ")
# time.sleep(4)
# dd.select_by_visible_text("Operations Manager")
# time.sleep(4)

# dd.select_by_index(0)
# time.sleep(4)
# dd.select_by_value("Customer_Service_Manager_ANZ")
# time.sleep(4)
# dd.select_by_visible_text("Operations Manager")
# time.sleep(4)
