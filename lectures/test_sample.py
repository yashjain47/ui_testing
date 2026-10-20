import pytest
from playwright.sync_api import expect, Page


def test_url(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_url("https://demoblaze.com/index.html")



def test_title(page:Page):
    page.goto("https://demoblaze.com/index.html")
    expect(page).to_have_title("STORE1")
    
    
def test_login(page:Page):
    
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