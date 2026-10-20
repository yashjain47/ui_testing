import pytest
from playwright.sync_api import expect, Page




@pytest.mark.skip
def test_keyboard(page:Page):
    
    
    url = "https://testautomationpractice.blogspot.com/#"
    page.goto(url)       
    
    # input 1 - focus
    page.locator("#input1").focus()
    
    # input 1 - enter text 
    page.keyboard.insert_text("Welcome Yash")                                                                                       
    
    # control all
    page.keyboard.press("Control+A")
    
    # control c
    page.keyboard.press("Control+C")
        
    # Tab
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
        
    # control V
    page.keyboard.press("Control+V")
            
    # Tab
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
        
    # control V
    page.keyboard.press("Control+V")
            
            
            
    # verification
    expect(page.locator("#input2")).to_have_value("Welcome Yash")
    expect(page.locator("#input3")).to_have_value("Welcome Yash")
    
    # timeout
    page.wait_for_timeout(3000)     
    
    

    