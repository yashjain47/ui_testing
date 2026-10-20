"""Loggers | Handlers | Formatters ......


logger  -->  console hanlder/File handler  -->  formatter 

formatter                         added to         console hanlder/File handler
console hanlder/File handler      added to         logger


"""

import logging

class logger_demo:
    def sample_logger(self):
        
        # create logger.
        logger = logging.getLogger(logger_demo.__name__) 
        'or logger = logging.getLogger("demolog")'
        logger.setLevel(logging.DEBUG)

        # create console handler(ch) or file handler(fh) and set the log level.
        ch = logging.StreamHandler()
        fh = logging.FileHandler("/home/vvdn/Desktop/Selenium/LoggingDemo/Logs//demologfile.log")

        # create formatter - how you wants your logs to be formatted.
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s ',datefmt='%d/%m/%Y %I:%M:%S %p')
        formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s ')

        # add formater to console or file hanlder. 
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)

        # add console handler to the logger.
        logger.addHandler(ch)
        logger.addHandler(fh)
        
        # application code - log messgaes. 
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")

ld = logger_demo()
ld.sample_logger()


"""
Output on the screen/console:

17/07/2024 11:47:14 AM - DEBUG - demolog : debug log statement 
17/07/2024 11:47:14 AM - INFO - demolog : info log statement 
17/07/2024 11:47:14 AM - WARNING - demolog : warning log statement 
17/07/2024 11:47:14 AM - ERROR - demolog : error log statement 
17/07/2024 11:47:14 AM - CRITICAL - demolog : critical log statement 


"""