import pytest
from playwright.sync_api import expect, Page

@pytest.mark.skip  
def test_uploadfiles(page:Page):
    
    
    url = "https://testautomationpractice.blogspot.com/#"
    page.goto(url)       
    
    
    
    
    # for Single File
    choosefile = page.locator("#singleFileInput")
    
    # Choosing File 
    choosefile.set_input_files("/home/yjain/minicom.log")
    
    # click on upload button
    page.locator('button:has-text("Upload Single File")').click()
    
    
    
    
    # for Multiple File
    choosefile = page.locator("#multipleFilesInput")
    
    files = ["/home/yjain/minicom.log", "/home/yjain/plo.py"]
    # Choosing File 
    choosefile.set_input_files(files)
        
    # click on upload button
    page.locator('button:has-text("Upload Multiple File")').click()
        
    
    # timeout
    page.wait_for_timeout(8000)     
    
    
def test_downloadfile(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/p/download-files_25.html"
    page.goto(url)
    
    
    # fill text   
    page.locator("#inputText").fill("Yash")
        
        
    # event ON
    page.on("download", lambda download: download.save_as("/home/yjain/info.txt"))
        
            
    page.locator("#generateTxt").click()
    
    page.wait_for_timeout(1000)
    
    link = page.locator("#txtDownloadLink")
    expect(link).to_be_visible()
    
    link.click()
    

    page.wait_for_timeout(5000)
    
    
    