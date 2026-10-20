"""Logging into a file...."""

import logging


logging.basicConfig(level=logging.DEBUG,filename="/home/vvdn/Desktop/Selenium/LoggingDemo/Logs/demologs1.log",filemode="a",format='%(asctime)s - %(levelname)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p')

class DemoLogging1:
    def add_numbers(self,a,b):
        return a+b
    
    def Multiply_numbers(self,a,b):
        return a*b
    
d = DemoLogging1()
sum = d.add_numbers(2,3)

logging.debug(f"Debug -- Sum : {sum}")
logging.info(f"Info -- Sum : {sum}")
logging.warning(f"Warning -- Sum : {sum}")
logging.error(f"Error -- Sum : {sum}")
logging.critical(f"Critical -- Sum : {sum}")

