"""
How to execute Javascript in sleenium python

"""

import time
from selenium import webdriver


class Demojs():
    def demo_javascript(self):
        driver = webdriver.Chrome()
        # driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.rcvacademy.com/','_self');")
        time.sleep(2)
        demo_element = driver.execute_script("return document.getElementsByTagName('a')[1];")
        driver.execute_script("argument[0].click();",demo_element)




demo_js = Demojs()
demo_js.demo_javascript()