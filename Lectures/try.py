
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)


################################################################################################################################################
"""SCROLL TRY........................................................................................."""


# driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
# driver.maximize_window()

# sleep(1)

'''scroll down page by pixel'''
# driver.execute_script("window.scrollTo(0,5000)","")

'''scroll down page till the element is visible'''
# flag = driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)

'''scroll down page till end'''
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# sleep(4)

################################################################################################################################################
"""Dynamic Scroll......................................................................................."""



# driver.get("https://flight.yatra.com/air-search-ui/int2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=NYC&destinationCountry=US&flight_depart_date=30/07/2024&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=135684568888")
# driver.maximize_window()
# sleep(2)

# pagelength = driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
# match = False
# while match == False:
#     lastcount= pagelength
#     sleep(3)

#     pagelength = driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
#     if lastcount == pagelength:
#         match = True
#     print("lastcount",lastcount,"pagelength",pagelength)


# sleep(4)