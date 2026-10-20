import pytest
from playwright.sync_api import Page, expect




def test_inputbox(page:Page):
    ''' Testing Input Boox like name, Email  etc'''
    
    url = 'https://testautomationpractice.blogspot.com/'
    
    # navigate to the page
    page.goto(url)
    
    # finding the element 
    namebox = page.locator('#name')
    
    # check if visible and enabled [GUI]
    expect(namebox).to_be_visible()
    expect(namebox).to_be_enabled() 
    
    #checking the attribute to the element
    expect(namebox).to_have_attribute("maxlength", "15")
    
    # gettting the value of the attribute
    maxlength = namebox.get_attribute("maxlength")
    print(f"Maximum Length : {maxlength}")
    
    # fill the name
    namebox.fill("Yash Jain")
    
    # getting name
    enteredname = namebox.input_value()
    print(f"Entered Value : {enteredname}")
    
    # timeout 
    page.wait_for_timeout(5000)
    
    # close
    page.close()
    
    
def test_radio_button(page:Page):
    ''' Testing Radio Buttons '''
    
    url = 'https://testautomationpractice.blogspot.com/'
        
    # navigate to the page
    page.goto(url)
    
    # finding the element 
    male_radio = page.locator('#male')
    
    # check if visible and enabled [GUI]
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled() 
    
    #checking the radio button is not checked by default
    expect(male_radio).not_to_be_checked()
    
    # clicking/selecting male radio button
    male_radio.check()
    
    # checking after clicking
    expect(male_radio).to_be_checked()
    
    # timeout
    page.wait_for_timeout(2000)
    
    # close
    page.close()
    
    
def test_check_box(page:Page):
    ''' Testing Checkboxes '''
    
    url = 'https://testautomationpractice.blogspot.com/'
        
    # navigate to the page
    page.goto(url)
    
    
    'Select specific checkbox'
    # # finding the element 
    # sunday_checkbox = page.locator('#sunday')
    
    # # check if visible and enabled [GUI]
    # expect(sunday_checkbox).to_be_visible()
    # expect(sunday_checkbox).to_be_enabled() 
    
    # #checking the radio button is not checked by default
    # expect(sunday_checkbox).not_to_be_checked()
        
    # # clicking/selecting checkboxbutton
    # sunday_checkbox.check()
    
    # # checking after clicking
    # expect(sunday_checkbox).to_be_checked()
    
    
    
    'Count number of checkboxes'
    
    days =  ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    checkboxes = [page.get_by_label(day) for day in days]
    # print(checkboxes)
    print(len(checkboxes))
    
    for checkbox in checkboxes:
        checkbox.check()
        expect(checkbox).to_be_checked()
        
    # timeout
    page.wait_for_timeout(2000)
    
    # close
    page.close()





