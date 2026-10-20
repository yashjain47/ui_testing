import sys
from time import sleep 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/base")
from base_driver import driver_base
from search_flight_results_page import search_flight_results
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/utilities")
from utils import Utils


class pageLaunch(driver_base):
    log = Utils.custom_logger()
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    DEPART_FROM_FIELD = "BE_flight_origin_city"
    GOING_TO_FIELD = "BE_flight_arrival_city"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    SELECT_DATE_FILED = "BE_flight_origin_date"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"


    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.ID,self.DEPART_FROM_FIELD)
    
    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.ID,self.GOING_TO_FIELD)
    
    def getGoingToResults(self):
        return self.wait_for_presence_of_all_elements(By.XPATH,self.GOING_TO_RESULT_LIST)
    
    def getDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.ID,self.SELECT_DATE_FILED)
    
    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.ALL_DATES)

    def getSearchButton(self):
        return self.driver.find_element(By.XPATH,self.SEARCH_BUTTON)




    def enterDepartFromLocation(self,departlocation):
        self.getDepartFromField()[0].click()
        sleep(1)
        self.getDepartFromField()[0].send_keys(departlocation)
        sleep(1)
        self.getDepartFromField()[0].send_keys(Keys.ENTER)

    def enterGoingToLocation(self,goingtolocation):
        self.getGoingToField()[0].click()
        self.log.info("Clicked on going to")
        sleep(1)
        self.getGoingToField()[0].send_keys(goingtolocation)
        self.log.info("Typed text into going toField successfully")
        sleep(1)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                sleep(1)
                results.click()
                sleep(1)
                break

    def enterDepartureDate(self,departure_date):
            self.getDepartureDateField()[0].click()
            all_dates = self.getAllDatesField()[0].find_elements(By.XPATH,self.ALL_DATES)
            for date in all_dates:
                if date.get_attribute("data-date") == departure_date:
                    date.click()
                    sleep(1)
                    break       

    def ClickSearchFlightButton(self):
            self.getSearchButton().click()
            sleep(4)   

    def searchFlights(self,departlocation,goingtolocation,departure_date):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departure_date)
        self.ClickSearchFlightButton()
        search_flight_result = search_flight_results(self.driver)
        return search_flight_result





#####################################################################################################################

    def departfrom(self,departlocation):
        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).click()
        # sleep(3)
        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).send_keys(departlocation)
        # sleep(2)
        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_origin_city"))).send_keys(Keys.ENTER)
        # sleep(1)
        
        depart_from = self.wait_until_element_is_clickable(By.ID,"BE_flight_origin_city")
        depart_from = depart_from[0]
        # print("Depart From : ",depart_from)
        depart_from.click()
        depart_from.send_keys(departlocation)
        depart_from.send_keys(Keys.ENTER)


    def goingto(self,goingtolocatoin):


        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_arrival_city"))).click()
        # sleep(1)
        # self.wait.until(EC.element_to_be_clickable((By.ID,"BE_flight_arrival_city"))).send_keys(goingtolocatoin)
        # sleep(1)

        going_to = self.wait_until_element_is_clickable(By.ID,"BE_flight_arrival_city")
        going_to = going_to[0]
        # print("going to : ",going_to)
        going_to.click()
        going_to.send_keys(goingtolocatoin)


        # search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]/li")))
        # search_results = self.driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        search_results = self.wait_for_presence_of_all_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        
        
        for results in search_results:
            # print(results.text)
            if "New York (JFK)" in results.text:
                sleep(1)
                results.click()
                sleep(1)
                break


    def selectdate(self,departure_date):

        departuredate = self.wait_until_element_is_clickable(By.ID,"BE_flight_origin_date")
        departuredate = departuredate[0]
        departuredate.click()
        sleep(1)


        all_dates = self.driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                sleep(1)
                break


    def clicksearch(self):
        self.driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        sleep(4)


    def scroll_page(self):

        self.page_scroll()