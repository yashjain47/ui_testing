import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_mouse_hover(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    btn = page.locator(".dropbtn")
    
    btn.hover()
    
    details = page.locator(".dropdown-content").all()
    for i in details:
        # print(i.inner_text())
        if i.inner_text() == "Laptops":
            i.hover()
            break

    page.wait_for_timeout(5000)
    
   
    
@pytest.mark.skip    
def test_mouse_rightclick(page:Page):
    
    
    url = "https://swisnl.github.io/jQuery-contextMenu/demo.html"
    page.goto(url)
    
    btn = page.locator(".context-menu-one")
    btn.click(button="right")   # perform click acttion - right, left, middle

    page.wait_for_timeout(5000)
    
    
    
@pytest.mark.skip     
def test_mouse_doubleclick(page:Page):
    
    
    url = "https://testautomationpractice.blogspot.com/#"
    page.goto(url)
    
    btn = page.locator("button[ondblclick='myFunction1()']")
    
    # option1
    # btn.click(click_count=2)   

    # option2
    btn.dblclick()

    page.wait_for_timeout(5000) 
    
    field2 = page.locator("#field2")
    expect(field2).to_have_value("Hello World!")
    
       
    
def test_mouse_draganddrop(page:Page):
    
    
    url = "https://testautomationpractice.blogspot.com/#"
    page.goto(url)
    
    drag = page.locator("#draggable")
    drop = page.locator("#droppable")


    # approach 1 [not recommended]
    # drag.hover()
    # page.mouse.down()
    # drop.hover()
    # page.mouse.up()
    
        

    # approach 2
    drag.drag_to(drop)
    


    page.wait_for_timeout(5000) 
    
    
    
