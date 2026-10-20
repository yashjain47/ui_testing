from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


"Paths"
elements = "//div[@class='category-cards']//div[1]//div[1]//div[2]//*[name()='svg']"
text_box = "//span[normalize-space()='Text Box']"




'Initializing the Browser'
url = "https://demoqa.com/"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")


'Click on Elements'
driver.find_element(By.XPATH,elements).click()


'Click on upload Download'
explicit_wait = WebDriverWait(driver,10)
explicit_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,"li[id='item-7']")),"Unable to Find Text Box").click()


'----------------------------------------------------------------------------------------'
'Download'
download = driver.find_element(By.XPATH,"//a[@id='downloadButton']")
download.click()

'----------------------------------------------------------------------------------------'




'----------------------------------------------------------------------------------------'
'Upload'
# explicit_wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,"input[id='uploadFile']")),"Unable to Find Text Box").click()
upload = driver.find_element(By.XPATH,"//input[@id='uploadFile']")
file_path = "/home/vvdn/Downloads/sampleFile.jpeg"
upload.send_keys(file_path)

'----------------------------------------------------------------------------------------'













'Closing the Browser'
sleep(5)
driver.close()
