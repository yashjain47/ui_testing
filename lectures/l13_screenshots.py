'''
Types of screenshots

1.  page screenshot (partially/visible)    
2.  Full page screenshot 
3.  screenshot of a particular Element
    
    
    
    
    
    
Trace file -> always in .zip

2 ways to  open zip file
1. using cli        --->    playwright show-trace trace.zip
2. using websites.  --->    trace.playwright.dev  
    
    
capture the screenshot  - code
capture the video       - code
capture the             - trace    


Auto_retry (Re-run)

To achieving auto retry in playwright we need to install additional plugins
>> pip install pytest-rerunfailures


pytest l13_screenshots.py -v -s --headed --reruns 3 --reruns-delay 2



1. Flaky Tests --> sometimes Pass, sometimes Fails

    Fail > rerun > Pass > rerun > Fail          [Flaky tests]    




fail -> rerun
fail -> rerun
fail -> rerun
fail -> no


fail -> rerun
pass > no





    
'''






import pytest
from playwright.sync_api import Playwright, expect
from datetime import datetime


@pytest.mark.skip
def test_record_video(playwright:Playwright):
    
    browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1024, "height":768}
    )
    
    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.wait_for_load_state()
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)
    
    
    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")
    page.wait_for_timeout(3000)
    
    # close
    page.close()
    context.close()
    browser.close()
    
    

@pytest.mark.skip
def test_screenshots(playwright:Playwright):
    
    browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.wait_for_load_state()
    
    # 1.  page screenshot (partially/visible
    page.screenshot(path=f"images/homepage_{datetime.now()}.png")
    
    
    # 2.  Full page screenshot 
    page.screenshot(path=f"images/homepage_{datetime.now()}.png", full_page=True)

    
    # 3.  screenshot of a particular Element
    logo = page.locator("a[id='nava'] img")
    logo.screenshot(path=f"images/logo_{datetime.now()}.png")
    

    
    # close
    page.close()
    context.close()
    browser.close()
    
    

@pytest.mark.skip
def test_trace(playwright:Playwright):
    
    browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context()
    
    # tracing start
    context.tracing.start(screenshots=True, snapshots=True)
    
    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.wait_for_load_state()
    page.locator("#login2").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)
    

    # tracing stop
    context.tracing.stop(path="trace.zip")
    
    # close
    page.close()
    context.close()
    browser.close()
    
    
    
        

# @pytest.mark.skip
def test_flaky(playwright:Playwright):
    
    browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context()    
    page = context.new_page()

    page.goto("https://demoblaze.com/index.html")
    page.wait_for_load_state()
    page.locator("#login2").click()
    
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)
    
    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")
    page.wait_for_timeout(3000)
    
    
    
    # close
    page.close()
    context.close()
    browser.close()
    
    
      
    
    
    
    
    
    
    
    