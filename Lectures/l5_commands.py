"""
Commands for web browser:

1.  get() -- (Method)
    Opens URL in Web Browser.
    eg. driver.get("https://www.google.com")

2.  current_url -- (Property)
    Shows/Prints/Gives Current URL
    eg. print(driver.current_url)

3.  back() -- (Method)
    Press Browsers Back Button
    eg. driver.back()

4.  forward() -- (Method)
    Press Browsers Forward Button
    eg. driver.forward()

5.  refresh() -- (Method)
    Press Browsers Refresh Button
    eg. driver.refresh()

6.  title -- (Property)
    Shows current Page title
    eg. print(driver.title)

7.  maximize_window() -- (Method)
    Maximize Current browsers Window
    eg. driver.maximize_window()

8.  minimize_window() -- (Method)
    Minimize Current browsers Window
    eg. driver.minimize_window()

9.  fullscreen_window() -- (Method)
    Fullscreen the browsers window
    eg. driver.fullscreen_window()
  
10. close() -- (Method)
    close current window 
    eg. driver.close()

11. quit() -- (Method)
    close all windows and tabs
    eg. driver.quit()
"""



import time
from selenium import webdriver

def test():

    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/business")
    time.sleep(2)

    print("--------------------------------------")
    print(driver.current_url)

    # print("--------------------------------------")
    # driver.back()
    # time.sleep(2)

    # print("--------------------------------------")
    # driver.forward()
    # time.sleep(2)

    print("--------------------------------------")
    driver.refresh()
    time.sleep(2)

    print("--------------------------------------")
    print(driver.title)

    print("--------------------------------------")
    driver.maximize_window()
    time.sleep(1)

    print("--------------------------------------")
    driver.minimize_window()
    time.sleep(1)

    print("--------------------------------------")
    driver.fullscreen_window()
    time.sleep(1)

    print("--------------------------------------")
    driver.close()
    time.sleep(1)

    print("--------------------------------------")
    driver.quit()
    time.sleep(1)




# driver = webdriver.Firefox()
# driver.get("https://www.google.com")
# driver.close()