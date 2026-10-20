"""
Logging :

1.  DEBUG       --> Detailed Information,typically of interestonly when diagm=nosing problems.
2.  INFO        --> Confirmations that things are working as expected.   
3.  WARNING     --> An indication that someting unexpected is happened, or indicative of some problems in the near future (eg. 'disk space low'). The software is still working as expected.
4.  ERROR       --> Due to a more serious problem, the software has not been able to perform some functions.
5.  CRITICAL    --> A Serious error,indicating that problem itself may be uable to continue running.

priority:
debug < info < warning < error < critical

default loggign level = warning
"""

import logging

class DemoLogging1:
    def add_numbers(self,a,b):
        return a+b
    
    def Multiply_numbers(self,a,b):
        return a*b
    
d = DemoLogging1()
sum = d.add_numbers(2,3)
logging.debug(f"Sum : {sum}")
logging.warning(f"Sum : {sum}")

Mul = d.Multiply_numbers(2,3)
logging.warning(f"Multiply : {Mul}")

logging.error(f"Multiply : {Mul}")
logging.critical(f"Multiply : {Mul}")
