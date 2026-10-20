from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class driver_base:
    def __init__(self,driver):
        self.driver = driver

    def page_scroll(self):
        pagelength = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
        match = False
        while match == False:
            lastcount= pagelength
            sleep(3)

            pagelength = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight")
            if lastcount == pagelength:
                match = True
            print("lastcount",lastcount,"pagelength",pagelength)

        sleep(4)

    def wait_for_presence_of_all_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        
        return list_of_elements
    
    def wait_until_element_is_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        
        return element