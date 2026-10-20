"""
Web-element in Selenium:

Whatever we do manually on the webpage is done by web element in the selenium .

example -- Click on the serach button, writting the text on the text bar,etc


send_keys("test@test.com") -- Enter the Value in the text bar
click() -- Click the Button


FindElement class is using to find the single element by using id,name,class,link etc

FindElements class is using to get the list of all the web elements by using/ id,name,class,link etc





CSS Selectors

    ID              >> #
    Class           >> .
    Attribute
    Combining
    Sub String

    
ex -- <li id="item-7" class="btn btn-light" href="/favorites">Download</li>

id          >>  li[id="item-7"]
class       >>  li[class="btn btn-light"]  
attribute   >>  li[href="/favorites"]
combining   >>  li#item-7[href="/favorites"]
sub_string  >>  li[class^='btn btn_']
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElement():

    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element(by=By.ID, value='login-continue-btn').click()
        driver.find_element(by=By.ID, value='login-input').send_keys("test@test.com")
        time.sleep(2)

    def locate_by_name(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(by=By.NAME, value='login-input').send_keys("test@test.com")
        time.sleep(2)

    def locate_by_xpath(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(by=By.XPATH, value="//input[@id='login-input']").send_keys("test@test.com")
        time.sleep(2)

    def locate_by_cssselectors(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(by=By.CSS_SELECTOR, value="#login-input").send_keys("test@test.com")
        time.sleep(2)

    def locate_by_link(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(by=By.LINK_TEXT, value="Yatra for Business").click()
        time.sleep(6)

    def locate_by_plink(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(by=By.PARTIAL_LINK_TEXT, value="Yatra for Busine").click()
        time.sleep(6)

    def locate_by_tagname(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.find_element(by=By.TAG_NAME, value="input").send_keys("test@test.com")
        time.sleep(2)

    def locate_by_classname(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.find_element(by=By.CLASS_NAME, value="email-login-box").send_keys("test@test.com")
        time.sleep(2)

        # Note : For className use any class seperated by space like "yt-sme-mobile-input required_field email-login-box" use any one
        # yt-sme-mobile-input or required_field or email-login-box

    

a = FindElement()
# a.locate_by_id()
# a.locate_by_name()
# a.locate_by_xpath()
# a.locate_by_cssselectors()
# a.locate_by_link()
# a.locate_by_plink()
# a.locate_by_tagname()
# a.locate_by_classname()


# -------------------------------------------------------------------------------------------------------------


class FindElements():

    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        lista = driver.find_elements(By.ID, 'login-input')
        print(len(lista))
        time.sleep(2)

    def locate_by_name(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        lista = driver.find_elements(By.NAME, 'login-input')
        print(len(lista))
        time.sleep(2)

    def locate_by_xpath(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        lista = driver.find_elements(By.XPATH, "//input[@id='login-input']")
        print(len(lista))
        time.sleep(2)

    def locate_by_cssselectors(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        lista = driver.find_elements(By.CSS_SELECTOR, "#login-input")
        print(len(lista))
        time.sleep(2)

    def locate_by_link(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        lista = driver.find_elements(By.LINK_TEXT, "Yatra for Business")
        print(len(lista))
        time.sleep(6)

    def locate_by_plink(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        lista = driver.find_elements(By.PARTIAL_LINK_TEXT, "Yatra for Busine")
        print(len(lista))
        time.sleep(6)

    def locate_by_tagname(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        # driver.maximize_window()
        lista = driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        # for i in lista:
        #     print(i.text)
        time.sleep(2)

    def locate_by_classname(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        lista = driver.find_elements(By.CLASS_NAME, "email-login-box")
        print(len(lista))
        time.sleep(2)

        # Note : For className use any class seperated by space like "yt-sme-mobile-input required_field email-login-box" use any one
        # yt-sme-mobile-input or required_field or email-login-box

    

# b = FindElements()
# b.locate_by_id()
# b.locate_by_name()
# b.locate_by_xpath()
# b.locate_by_cssselectors()
# b.locate_by_link()
# b.locate_by_plink()
# b.locate_by_tagname()
# b.locate_by_classname()


