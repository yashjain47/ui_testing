from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
text_box = "//span[normalize-space()='Text Box']"
username = "Yash Jain"




'Initializing the Browser'
url = "https://demoqa.com"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")

explicit_wait = WebDriverWait(driver,10)


'Click on Elements'
driver.find_element(By.XPATH,elements).click()


'Click on dynamic properties'
explicit_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,"li[id='item-8']")),"Element is not Clickable").click()


'click on wait button'
a = explicit_wait.until(ec.element_to_be_clickable((By.XPATH,"//button[@id='enableAfter']")),"Element is not visible").is_enabled()
print(a)