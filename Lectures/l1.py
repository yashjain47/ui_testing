"""
Selenium:

Selenium is a powerful tool for controlling web browsers through programs and performing browser automation. It is functional for all browsers, works on all major OS and its scripts are written in various languages i.e Python, Java, C#, etc, we will be working with Python. Selenium Tutorial covers all topics such as --WebDriver, WebElement, Unit Testing with selenium. This Python Selenium Tutorial covers Selenium from basics to advanced and professional uses.





Why learn Selenium Python ?

1.  Open Source and Portable 
    Selenium is an open source and portable Web testing Framework.

2.  Combination of tool and DSL 
    Selenium is combination of tools and DSL (Domain Specific Language) in order to carry out various types of tests.

3.  Easier to understand and implement 
    Selenium commands are categorized in terms of different classes which make it easier to understand and implement.

4.  Less burden and stress for testers 
    As mentioned above, the amount of time required to do testing repeated test scenarios on each and every new build is reduced to zero, almost. Hence, the burden of tester gets reduced.

5.  Cost reduction for the Business Clients -
    The Business needs to pay the testers their salary, which is saved using automation testing tool. The automation not only saves time but gets cost benefits too, to the business.







    

"""

import time
from selenium import webdriver 




# driver = webdriver.Firefox()
# driver.get("https://www.irctc.com")
# driver.maximize_window()
# time.sleep(10)
# print(driver.title)
# driver.close()

print("------------------------------------------------")


driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(10)
print(driver.title)
driver.close()


