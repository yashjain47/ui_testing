import pytest
from playwright.sync_api import Page, expect


data = {
    "Name": "Yash jain",
    "Address" : "Gurugram",
    "City" : "Gurugram",
    "State" : "Haryana",
    "ZipCode" : "122050",
    "Card_Number" : "123456789",
    "Month": "10",
    "Year": "36",
    "Name_on_card": "YJAIN",    
}

@pytest.mark.skip
def test_staic_web_table(page:Page):
    url = "https://testautomationpractice.blogspot.com/"

    page.goto(url)
    
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()
    # print(table.all_text_contents())
    # print(table.all_inner_texts())
    
    
    # count total number of rows
    # rows = page.locator("table[name='BookTable'] tbody tr")
    # or
    rows = table.locator('tr')
    count = rows.count()
    expect(rows).to_have_count(count)
    
    
    # count total number of columns or headers in a table
    column = table.locator("tr th")
    print(column.count())
    
    
    # Read data from table from row 2
    table_data = rows.nth(1).locator("td")
    for i in table_data.all_inner_texts():
        print(i)
        
    
    # Read all data
    table_datas = rows.all()
    for i in table_datas[1:]:
        col = i.locator("td")
        print(col.all_inner_texts())
    
       
       
    page.close()
    

@pytest.mark.skip  
def test_pagination_web_table(page:Page):
    
    url = "https://datatables.net/examples/core/basic_init/zero_configuration.html"
    page.goto(url)
    
    
    has_more_pages = True
    
    while has_more_pages:
    
        rows = page.locator("#example tbody tr").all()
        
        for row in rows:
            print(">>",row.inner_text())
    
        next_button = page.locator("button[aria-label='Next']")
        is_disabled = next_button.get_attribute("class")
        # print(f"button status : {is_disabled}")
        
        if "disabled" in is_disabled:
            has_more_pages = False
            
        else:
            next_button.click()    
        
            
@pytest.mark.skip          
def test_practise1(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    print()
    
    table = page.locator("#taskTable")
    
    # header
    table_header = table.locator("thead tr")
    for i in table_header.all():
        col = i.locator("th")
        # print(col.all_inner_texts())
    
    # body
    table_data = table.locator("tbody tr")
    for i in table_data.all():
        col = i.locator("td")
        data = col.all_inner_texts()
        
        if "Chrome" in data:
            for j in data:
                if "%" in j:
                    print(f"Chrome Value : {j}") 
                if "Mbps" in j:
                    print(f"Chrome Speed : {j}")

        if "Firefox" in data:
            for j in data:
                if "MB/s" in j:
                    print(f"Firefox Value : {j}") 
                if "Mbps" in j:
                    print(f"Firefox Speed : {j}")

    
    page.close()

    
@pytest.mark.skip          
def test_practise2(page:Page):
    
    has_more_pages = True
    pages = 1
    
    url = "https://testautomationpractice.blogspot.com/"
    page.goto(url)
    print()
    
    table = page.locator("#productTable")
    more_pages = page.locator("#pagination li")
    print(f"Total pages : {more_pages.count()}")
    # print(more_pages, type(more_pages))

    
    while has_more_pages:
    
        # header
        table_header = table.locator("thead tr")
        for i in table_header.all():
            col = i.locator("th")
            print(col.all_inner_texts())
        
        # body
        table_data = table.locator("tbody tr")
        for i in table_data.all():
            col = i.locator("td")
            data = col.all_inner_texts()
            print(data)
            
            
        more_pages.all()[pages].click()
        pages+=1
        if pages>=more_pages.count():
            has_more_pages = False
          
            
    page.close()
    
    
def test_practise3(page:Page):
    

    flight_prices = {}
    
    
    url = "https://blazedemo.com/"
    page.goto(url)
    expect(page).to_have_title("BlazeDemo")
    print()
    
    
    # Searching
    depature = page.locator("select[name='fromPort']")
    depature.select_option(value="Boston")
        
    destination = page.locator("select[name='toPort']")
    destination.select_option(label="London")
    
    page.locator("input[type='submit']").click()
    page.wait_for_timeout(3000)
    
    
    
    
    # finding lowest prices from flight table
    table = page.locator(".table")
    
    rows = table.locator("tbody tr")
    for index, col in enumerate(rows.all()):
        datas = col.locator("td")
        # print(datas.all_inner_texts())
        # print("--------------------------------------")
        
        prices = datas.all_inner_texts()[-1]
        flight_prices[index] = float(prices.replace('$',''))
                
        
    # print(flight_prices)
    min_price = min(flight_prices.values())
    # print(min_price)
    ele = [k for k, v in flight_prices.items() if min_price==v][0] 
    print(ele)
    
    for index, col in enumerate(rows.all()):
        datas = col.locator("td input")
        # print(datas)
        if ele == index:
            ele_loc = datas
            break
        
    if ele_loc:
        ele_loc.click()        
    
    
    # Filling the data

    page.locator("#inputName").fill(data["Name"])
    page.locator("#address").fill(data["Address"])
    page.locator("#city").fill(data["City"])
    page.locator("#state").fill(data["State"])
    page.locator("#zipCode").fill(data["ZipCode"])
    
    page.locator("#cardType").select_option(value="amex")
    
    page.locator("#creditCardNumber").fill(data["Card_Number"])
    page.locator("#creditCardMonth").fill(data["Month"])
    page.locator("#creditCardYear").fill(data["Year"])
    page.locator("#nameOnCard").fill(data["Name_on_card"])
    
    # submit
    page.locator("input[type='submit']").click()
    
    
    conf = page.get_by_text("Thank you for your purchase today!")
    expect(conf).to_be_visible()
    

    page.wait_for_timeout(3000)
            
    page.close()
    
    
 