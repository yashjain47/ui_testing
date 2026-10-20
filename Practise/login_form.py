from time import sleep
from cycler import V
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

"Paths"
forms = "//body/div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div[@class='category-cards']/div[2]"
prac_forms = "//div[contains(@class,'element-list collapse show')]//li[@id='item-0']"
text_box = "//span[normalize-space()='Text Box']"
path_fname = "//input[@id='firstName']"
path_lname = "//input[@id='lastName']"
path_mail = "//input[@id='userEmail']"
path_gender_m = "//label[@for='gender-radio-1']"
path_gender_f = "//label[@for='gender-radio-2']"
path_gender_o = "//label[@for='gender-radio-3']"
path_number = "//input[@id='userNumber']"
path_dob = "//input[@id='dateOfBirthInput']"
path_sub = "div[class='subjects-auto-complete__input']"
path_pic = "//input[@id='uploadPicture']"
path_address = "//textarea[@id='currentAddress']"
path_state = "//div[contains(text(),'Select State')]"
path_city = "//div[@id='stateCity-wrapper']//div[3]"
path_submit = "//button[@id='submit']"




'Data'
firstname = "Yash"
lastname = "Jain"
mail = "test@gmail.com"
number = "7689887780"
subjects = "IT"
addresss = "manesar Gurgaon"
state = "NCR"
city = "Gurgaon"
hobbies = ['Sports','Music']
gender = "Male"
date_of_birth = "04 Oct 2000"
file_path = "/home/vvdn/Downloads/sampleFile.jpeg"




'Initializing the Browser'
url = "https://demoqa.com"
driver = webdriver.Firefox()
driver.get(url)

driver.maximize_window()
driver.execute_script("document.body.style.zoom='67%'")

explicit_wait = WebDriverWait(driver,10)
action_chain = ActionChains(driver)


'Click on Elements'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,forms))).click()

'Click on Practise Forms'
explicit_wait.until(ec.element_to_be_clickable((By.XPATH,prac_forms))).click()


'Getting the title'
print("Title : ",driver.title)


'Filling the Fields'
# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_fname))).send_keys(firstname)
# driver.implicitly_wait(1)
# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_lname))).send_keys(lastname)
# driver.implicitly_wait(1)
# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_mail))).send_keys(mail)
# driver.implicitly_wait(1)

# if gender == "Male":
#     explicit_wait.until(ec.element_to_be_clickable((By.XPATH,path_gender_m))).click()
# elif gender == "Female":
#     explicit_wait.until(ec.element_to_be_clickable((By.XPATH,path_gender_f))).click()
# elif gender == "Other":
#     explicit_wait.until(ec.element_to_be_clickable((By.XPATH,path_gender_o))).click()


# driver.implicitly_wait(1)
# explicit_wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,path_sub))).send_keys(subjects)

# chech_boxes = driver.find_elements(By.XPATH,"//label[@class='custom-control-label']")
# for checkbox in chech_boxes:

#     if checkbox.text in hobbies:
#         if not checkbox.is_selected():
#             checkbox.click()
#             print(f"Selected: {checkbox.text}")


# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_number))).send_keys(number)
# driver.implicitly_wait(1)
# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_address))).send_keys(addresss)
# driver.implicitly_wait(1)
# explicit_wait.until(ec.presence_of_element_located((By.XPATH,path_pic))).send_keys(file_path)



state_list = driver.find_element(By.XPATH,"//div[@id='state']//div[contains(@class,'css-1hwfws3')]").click()


driver.find_element(By.LINK_TEXT, "Uttar Pradesh").click()

# /html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]/div[2]
# action_chain.move_to_element()

# state_lst = Select(state_list)
# state_lst.select_by_value(state)














'Tryyyyyyy'
# driver.implicitly_wait(1)
# explicit_wait.until(ec.element_to_be_clickable((By.XPATH,path_dob))).clear()
# driver.implicitly_wait(1)
# explicit_wait.until(ec.element_to_be_clickable((By.XPATH,path_dob))).send_keys(date_of_birth)









'Closing the Browser'
sleep(5)
driver.close()