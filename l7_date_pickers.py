import pytest
from playwright.sync_api import expect, Page





def select_date(page, target_date, target_month, target_year, is_future):
    
    while True:
        
        current_month = page.locator(".ui-datepicker-month").text_content()
        current_year = page.locator(".ui-datepicker-year").text_content()
        
        # print("Current : ", current_month, current_year)
        
        if current_month == target_month and current_year == target_year:
            break

        if is_future:
           page.locator(".ui-icon.ui-icon-circle-triangle-e").click()
        else:            
            page.locator(".ui-icon.ui-icon-circle-triangle-w").click()
            
            
            
    date_elements = page.locator(".ui-datepicker-calendar td").all()
    for date in date_elements:
        if date.text_content() == target_date:
            date.click()
            break
            

@pytest.mark.skip
def test_jquery_datepicker(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    date_input = page.locator("#datepicker")
    
    # Approach 1
    # date_input.fill("10/04/2000")  #mm/dd/yyyy
    # expect(date_input).to_have_value("10/04/2000")
    
    
    # Approach 2
    is_future = True
    date = "22"
    month = "April"
    year =  "2028"
    
    date_input.click()
    select_date(page, date, month, year, is_future)
    expect(date_input).to_have_value("04/22/2028")

    page.wait_for_timeout(3000)
    page.close()





def close_signin_popup(page: Page):

    popup = page.get_by_text("Sign in, save money")
    if popup:
        page.keyboard.press("Escape")

def select_checkin_date(page, Date, target_month, target_year):
    
    while True:
            
        checkin_data = page.locator("h3[class$='e7addce19e af236b7586']").nth(0).inner_text()
        checkin_month, checkin_year = checkin_data.split(" ")
        
        # print("Current : ", checkin_month, checkin_year)
        
        if checkin_month == target_month and checkin_year == target_year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()  
            
            
    all_dates = page.locator("table.b8fcb0c66a tbody").nth(0).locator("td").all()
    for date in all_dates:
        if date.inner_text() == Date:
            date.click()
            break              
    
def select_checkout_date(page, Date, target_month, target_year, check_calendar=1):
    
    while True:
            
        checkin_data = page.locator("h3[class$='e7addce19e af236b7586']").nth(check_calendar).inner_text()
        checkin_month, checkin_year = checkin_data.split(" ")
        
        # print("Current : ", checkin_month, checkin_year)
        
        if checkin_month == target_month and checkin_year == target_year:
            break
        else:
            page.locator("button[aria-label='Next month']").click()

    all_dates = page.locator("table.b8fcb0c66a tbody").nth(check_calendar).locator("td").all()
    for date in all_dates:
        if date.inner_text() == Date:
            date.click()
            break     
     
@pytest.mark.skip             
def test_bootstrap_datepicker(page:Page):
    
    url = "https://www.booking.com/?chal_t=1788264708149&force_referer="
    page.goto(url)
    
    page.wait_for_timeout(3000)
    close_signin_popup(page)
    
    page.get_by_test_id("searchbox-dates-container").click()
    
    
    
    checkin_details = ["5", "February", "2027"]
    checkout_details = ["5", "March", "2027"]
    
    check_calendar = 1
    if checkin_details[1] == checkout_details[1]:
        check_calendar = 0
        
    
    
    select_checkin_date(page, checkin_details[0], checkin_details[1], checkin_details[2])
    checkin_date = page.locator("span[data-testid='date-display-field-start']").inner_text()
    print("checkIn Date :",checkin_date)
    
    select_checkout_date(page, checkout_details[0], checkout_details[1], checkout_details[2], check_calendar)
    checkout_date = page.locator("span[data-testid='date-display-field-end']").inner_text()
    print("CheckOut Date : ", checkout_date)
    
    expect(page.locator("span[data-testid='date-display-field-start']")).to_contain_text(checkin_date)
    expect(page.locator("span[data-testid='date-display-field-end']")).to_contain_text(checkout_date)
    
    page.wait_for_timeout(3000)
    page.close()

     
     
     
@pytest.mark.skip      
def test_practise1(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    
    page.locator("#txtDate").click()
    
    tar_date = "5"
    tar_month = "Feb"
    tar_year = "2027"
    
    
    
    month = page.locator("select.ui-datepicker-month")
    month.select_option(value=tar_month)
    
    year = page.locator("select.ui-datepicker-year")
    year.select_option(value=tar_year)
    
    date = page.locator("table.ui-datepicker-calendar tbody").locator("tr td").all()
    
    for d in date:
        if d.inner_text() == tar_date:
            d.click() 
            break 
         
         
    page.wait_for_timeout(3000)
     
     
@pytest.mark.skip      
def test_practise2(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    
    date = page.locator("#start-date")
    date.fill("01/01/2027")
    
    page.wait_for_timeout(3000)
     
     
def test_practise3(page:Page):
    
    url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
    page.goto(url)
    
    
    all_options = page.locator("#checkout-products").locator("li").all()
    # print(all_options)
    for option in all_options:
        # print(option.inner_text())
        if "Dummy ticket for Visa Application" in option.inner_text():
            option.locator("label").check()
            break


    page.wait_for_timeout(1000)
    alert = page.locator("div[role='alert']")
    expect(alert).to_be_visible()
    expect(alert).to_contain_text("Dummy ticket for Visa Application")

    
    page.locator("#travname").fill("Yash")
    page.locator("#travlastname").fill("Jain")
    
    page.locator("#dob").click()
    page.locator('select[class="ui-datepicker-month"]').select_option(value="Oct")
    page.locator('select[class="ui-datepicker-year"]').select_option(value="2000")
    
    all_date = page.locator(".ui-datepicker-calendar tbody").locator("tr td").all()
    for date in all_date:
        date = date.locator("a")
        if date.text_content() == "4":
            date.click()
            break
     
    
    genders = page.locator('label[class="radio required_field"]').all()
    for gender in genders:
        if gender.text_content() == "Male":
            gender.check()
        
         
    page.wait_for_timeout(3000)
     