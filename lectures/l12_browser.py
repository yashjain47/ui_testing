import pytest
from playwright.sync_api import Page, expect, Playwright




'''

Browser     -->     Google, Firefox, webkit, etc..
Pages       -->     tab, popups, window                    

Flow:
Browser >>  context(user profiles) >>  Pages


Default Browser = Chromium


'''


# browser > context > pages

@pytest.mark.skip
def testt_browsercontext(playwright: Playwright):
    
    
    # create browser
    browser = playwright.chromium.launch(headless=False)
    
    # create context
    context = browser.new_context()
    
    # create pages
    page1 = context.new_page()
    page2 = context.new_page()
    
    
    page1.goto("https://www.google.com/")
    expect(page1).to_have_title("Google")
    page1.wait_for_timeout(5000)
    
    
    page2.goto("https://www.vvdntech.com/")
    expect(page2).to_have_title("Global Provider of Software, Product Engineering, Electronics Manufacturing Services and Solutions")
    page2.wait_for_timeout(5000)
    


@pytest.mark.skip
def test_handle_popups(playwright: Playwright):
    
    
    # create browser
    browser = playwright.chromium.launch(headless=False)
    
    # create context
    context = browser.new_context()
    
    # create pages
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")


    # event
    page.on("popup", lambda popup:popup.wait_for_load_state())

    page.locator("#PopUp").click()
    page.wait_for_timeout(2000)
    
    
    # checking number of pages
    all_popups = context.pages
    print("Total number of pages/popups",  len(all_popups))
     
    for pa in all_popups:
        print(">>>", pa.url)
        print(">>>", pa.title())
        
        if "Playwright" in pa.title():
            pa.locator(".getStarted_Sjon").click()
            pa.wait_for_timeout(3000)
            expect(pa).to_have_title("Installation | Playwright")
            pa.close()
            
                
    
    page.wait_for_timeout(5000)
    context.close()
    browser.close()
        


@pytest.mark.skip
def test_auth_popups(playwright: Playwright):
    
    # create browser
    browser = playwright.chromium.launch(headless=False)
    
    # create context
    context = browser.new_context(http_credentials={"username":"admin", "password":"admin"})
    
    # create pages
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/basic_auth")

    page.wait_for_load_state()
    page.wait_for_timeout(5000)



# @pytest.mark.skip
def test_handle_tabs(playwright: Playwright):
    
    # create browser
    browser = playwright.chromium.launch(headless=False)
    
    # create context
    context = browser.new_context()
    
    # create pages
    parent_page = context.new_page()
    parent_page.goto("https://testautomationpractice.blogspot.com/")

    parent_page.wait_for_load_state()
    parent_page.on("page", lambda page:page.wait_for_load_state())
    
    parent_page.locator("button:has-text('New Tab')").click()
    
    parent_page.wait_for_timeout(5000)
    all_pages = context.pages
    print(len(all_pages))
    for page in all_pages:
        print(page.url, page.title())
        
    parent_page.wait_for_timeout(5000)









