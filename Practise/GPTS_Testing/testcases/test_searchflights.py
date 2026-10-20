"""
DDT -- Data Driven Test

@ddt ---- before the class

@data(("New Delhi","New York", "30/07/2024","1 Stop"),("Mumbai","New York", "28/07/2024","1 Stop"))
@unpack                                                                                               

---- before the function whose has these as the variables


'for direct data'
@data(("New Delhi","New York", "30/07/2024","1 Stop"),("Mumbai","New York", "28/07/2024","1 Stop"))
@unpack

'data from json file'
@file_data('../testdata/test_data.json')

'data from yaml file'
@file_data('../testdata/testym.yaml')

'data from excel file'
@data(*Utils.read_data_from_excel('../testdata/testxl.xlsx','Sheet'))
@unpack

'data from csv file'
@data(*Utils.read_data_from_csv('../testdata/testcsv.csv'))
@unpack


-----------------------------------------------------------------------------------------------------------
for creating html reports of the testcase:

pytest --html=report.html --self-contained-html





to run perfectly --
pytest -vs --browser firefox --url http://yatra.com --html=../reports/report2.html --self-contained-html 


"""

import sys,ddt
import pytest
from time import sleep 
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/pages")
from yatra_launch_page import pageLaunch
from search_flight_results_page import search_flight_results
sys.path.append("/home/vvdn/Desktop/Selenium/TestFrameWorkDemo/utilities")
from utils import Utils
import softest
from ddt import ddt,data,unpack,file_data



# @pytest.mark.usefixtures("setup")
@ddt
class TestSearchandVerifyFilter(softest.TestCase):
    

    log = Utils.custom_logger()

    # @pytest.mark.usefixtures("setup")
    # @pytest.fixture(autouse=True)
    # def class_setup(self):
        # print("self Driver : ",self.driver)
        # self.lp = pageLaunch(self.driver)
        # self.ut = Utils()

    'for direct data'
    # @data(("New Delhi","New York", "30/07/2024","1 Stop"),("Mumbai","New York", "28/07/2024","1 Stop"))
    # @unpack

    'data from json file'
    # @file_data('../testdata/test_data.json')
    
    'data from yaml file'
    # @file_data('../testdata/testym.yaml')
    
    'data from excel file'
    # @data(*Utils.read_data_from_excel('../testdata/testxl.xlsx','Sheet'))
    # @unpack

    'data from csv file'
    @data(*Utils.read_data_from_csv('../testdata/testcsv.csv'))
    @unpack
    @pytest.mark.usefixtures("setup")
    def test_search_flights_1_stop(self,goingfrom, goingto, date, stops):

        self.lp = pageLaunch(self.driver)
        self.ut = Utils()
        sleep(1)
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)
        self.lp.scroll_page()
        search_flight_result.filter_flights_By_stop(stops)
        allstop1 = search_flight_result.get_search_flight_results()
        print(len(allstop1))
        self.log.info(len(allstop1))
        self.ut.assertListItemText(allstop1,stops)
        



    'for test'
    # @pytest.mark.usefixtures("setup")
    # def test_a(self):
    #     print("self Driver : ",self.driver)
    #     print("okkk")


    # def test_search_flights_2_stop(self):
    #     search_flight_result = self.lp.searchFlights("Banglore","New York", "28/07/2024")
    #     self.lp.scroll_page()
    #     search_flight_result.filter_flights_By_stop("2 Stop")
    #     allstop1 = search_flight_result.get_search_flight_results()
    #     print(len(allstop1))
    #     self.ut.assertListItemText(allstop1,"2 Stops ")
