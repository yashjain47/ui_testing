import sys
from time import sleep 
from selenium.webdriver.common.by import By
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/base")
from base_driver import driver_base
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/utilities")
from utils import Utils

class search_flight_results(driver_base):
    log = Utils.custom_logger()

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FILTER_BY_1_STOP_ICON = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_1_STOP_ICON)
    
    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_2_STOP_ICON)
    
    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH,self.FILTER_BY_NON_STOP_ICON)
    
    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.SEARCH_FLIGHT_RESULTS)
    
    def filter_flights_By_stop(self,by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            print("Selected Flights with 1 Stop")
            self.log.warning("Selected Flights with 1 Stop")
            sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            print("Selected Flights with 2 Stop")
            self.log.warning("Selected Flights with 2 Stop")
            sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click()
            print("Selected Flights with Non Stop")
            self.log.warning("Selected Flights with Non Stop")
            sleep(2)
        else:
            print("Please Provide valid filter option")
            self.log.warning("Please Provide valid filter option")

    def driver_close(self):
        self.driver.close()


#####################################################################################################################
    def filter_flights(self):
        self.driver.find_element(By.XPATH,"//p[normalize-space()='1']").click()
        sleep(4)



