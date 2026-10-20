import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_simple_dialog(page: Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    
    # # Approach 1 [before clicking the button] [not recommended]
    # # registering an event
    # def handle_dialog(dialog):
    #     dialog.accept()
    
    # page.on("dialog", handle_dialog)
    
    # page.locator("#alertBtn").click()
    # page.wait_for_timeout(5000)
    
    
    # Approach 2 using lamdba function
    # lambda parameter: expression 
    page.on("dialog", lambda dialog: dialog.accept())
    
    page.locator("#alertBtn").click()
    page.wait_for_timeout(5000)
    
    
@pytest.mark.skip
def test_confirmation_dialog(page: Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    # For accepting
    # page.on("dialog", lambda dialog: dialog.accept())
    
    # for rejecting
    page.on("dialog", lambda dialog: dialog.dismiss())
     
    page.locator("#confirmBtn").click()
    page.wait_for_timeout(5000)
    
    
    conf = page.locator("#demo")
    # expect(conf).to_contain_text("You pressed OK!")
    expect(conf).to_contain_text("You pressed Cancel!")
    
    
@pytest.mark.skip
def test_prompt_dialog(page: Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    name = "Yash"
    
    
    # For accepting with fill
    # page.on("dialog", lambda dialog: dialog.accept(name))
    
    # for rejecting
    page.on("dialog", lambda dialog: dialog.dismiss())
     
    page.locator("#promptBtn").click()
    page.wait_for_timeout(5000)
    
    
    conf = page.locator("#demo")
    # expect(conf).to_contain_text(f"Hello {name}! How are you today?")
    expect(conf).to_contain_text("User cancelled the prompt.")







@pytest.mark.skip
def test_frames(page:Page):
    
    url = "https://ui.vision/demo/webtest/frames/"
    page.goto(url)
    
    
    all_frames = page.frames
    print("total frames : ", len(all_frames))
    
    
    # frame1
    # option1
    # frame1 = page.frame("name  of the frame")
    
    # option2
    # frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")
    
    # option3
    frame1 = page.frame_locator('frame[src="frame_1.html"]')
        
    
    input_box = frame1.locator("input[name='mytext1']")
    input_box.fill("Yash")
    page.wait_for_timeout(3000)
    expect(input_box).to_have_value("Yash")
        
        
    
    
def test_inside_frames(page:Page):
    
    url = "https://ui.vision/demo/webtest/frames/"
    page.goto(url)
    
    
    all_frames = page.frames
    print("total frames : ", len(all_frames))
    
    
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")
    
    child = frame3.child_frames
    print("child frames", len(child))
    
    innerframe = child[0]
    
    radio = innerframe.get_by_label("I am a human")
    radio.check()
    
    expect(radio).to_be_checked()
    
    
    
    
    
    # frame5
    frame5 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_5")
    
    frame5.locator("a[href='https://a9t9.com']").click()
    
    page.wait_for_timeout(3000)
    
    expect(page.locator("img[src='/content/images/ui.vision.logo2.webp']")).to_be_visible()
    