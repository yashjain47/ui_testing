from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get()
driver.window_handles()
driver.current_window_handle()
driver.switch_to.window()


explicit_wait = WebDriverWait(driver,10,poll_frequency=2)
