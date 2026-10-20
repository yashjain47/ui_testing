'''

Dropdown
-------------------------------

1. Select dropdown  -  having 'select' tag
        options are embedded with 'option' tags

2. bootstrap dropdown - having 'div/ buttton' tag
        options are  embedded with 'div' tags

3. hidden dropdown - options are hidden from the DOM






inner_text()        VS  text_content()
all_inner_text()    VS  all_text_content()

inner_text()    --> return actual text
text_content()  --> return contents with sppecial characters and spaces
all()           --> list all elements in the list




'''


import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect


load_dotenv()
id = os.getenv("ORANGEHRM_ID")
password = os.getenv("ORANGEHRM_PASSWORD")



def test_login(page:Page):
    
    # launch the url
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    page.goto(url)
    
    # verify the title
    expect(page).to_have_title("OrangeHRM")
    
    # Login steps
    page.locator("input[placeholder='Username']").fill(id)
    page.locator("input[placeholder='Password']").fill(password)
    page.locator("button[type='submit']").click() 
    
    # wait for2 seconds
    page.wait_for_timeout(2000)
    # page.wait_for_load_state()
    # page.wait_for_event()
    # page.wait_for_function()
    # page.wait_for_selector()
    # page.wait_for_url()
    
    
    
def test_bootstrap_dropdown(page:Page):
    
    # login 
    test_login(page)
    
    # PIM Page
    page.get_by_text("PIM").click()
    page.wait_for_timeout(2000)
    
    
    # the option button
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(2000)
    
    
    # all options frrrom bootstrap/hidden dropdown
    options = page.locator("div[role='listbox'] span")
    count = options.count()
    
    print(f"Total options are : {count}")
    expect(options).to_have_count(count)
    print("Options content : ",options.all_text_contents())
    
    
    # print all options and click a specific option
    for i in range(count):
        text = options.nth(i).text_content()
        print(text)
        
        if text  == "QA Engineer":
            options.nth(i).click()
            break
        

    page.wait_for_timeout(2000)
    page.close()
    
    
    
    
    
    
           
    
    
    



