import pytest
from playwright.sync_api import expect, Page, Playwright
from playwright_captcha import ChallengeSolver

task = ""
time_in_hour = ""
time_in_minutes = ""
assigned_project = ""
assigned = True



url = "https://orbit.vvdntech.com"
username  = "yjain"
password = "Welcome@2026"


def test_timesheet(playwright:Playwright):
    
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    
    # going go the url
    page.goto(url)
    
    # verifying title
    expect(page).to_have_title("Orbit HRMS")
    
    
    page.locator("#id_username").fill(username)
    page.locator("#id_password").fill(password)
    
    
    solver = ChallengeSolver(page)
    try:
        # Automatically detects, solves, and submits the token
        solver.solve()
        print("CAPTCHA successfully solved!")
        
        page.wait_for_timeout(3000)
        
        # Proceed with your post-CAPTCHA automation steps
        page.click("button[class='btn btn-primary pt-2 pb-2 pl-5 pr-5 rounded']")
        
    except Exception as e:
        print(f"Solver failed: {e}")
    
    
    # robo_check = page.locator("img[alt='World Map']")
    # expect(robo_check).to_be_visible()
    # print(robo_check)
    
    
    # robo_check.click()
    # expect(robo_check).to_be_checked()
    # page.locator("button[class='btn btn-primary pt-2 pb-2 pl-5 pr-5 rounded']").click()
    
    page.wait_for_timeout(5000)
        
    
    
    
    
    
    
    
    
    page.wait_for_timeout(5000)
    
    
    
    