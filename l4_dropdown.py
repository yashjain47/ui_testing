import pytest
from playwright.sync_api import Page, expect




def test_single_dropdown(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    
    # url   
    page.goto(url)
    
    country = page.locator("#country")
    expect(country).to_be_visible()
    
    
    '3 ways to select from dropdown'
    # # 1. By visible Text (Lable)
    # country.select_option(label="India")
    # print(f"Selected Country : {country.input_value()}")
    
    # # 2. By Value
    # country.select_option(value="uk")
    # print(f"Selected Country : {country.input_value()}")
        
    # # 3. By Index
    # country.select_option(index=6)
    # print(f"Selected Country : {country.input_value()}")    
    
    'get all options from dropdown'
    
    options = page.locator("#country>option")
    expect(options).to_have_count(10)
    
    option_text = [ text.strip() for text in options.all_text_contents()]
    print(option_text, len(option_text))
    

    # timeout
    page.wait_for_timeout(2000)

    # close
    page.close()
    
  
def test_multiple_dropdown(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    
    # url   
    page.goto(url)
    
    colors = page.locator("#colors")
    expect(colors).to_be_visible()
    
    
    '3 ways to select from dropdown'
    # 1. By visible Text (Lable)
    colors.select_option(label=["Red", "Blue"])
    print(f"Selected colors : {colors.input_value()}")
    
    # 2. By Value
    colors.select_option(value=["green", "yellow"])
    print(f"Selected colors : {colors.input_value()}")
        
    # 3. By Index
    colors.select_option(index=[5,6])
    print(f"Selected colors : {colors.input_value()}")    


    # timeout
    page.wait_for_timeout(2000)

    # close
    page.close()
    
    
def test_single_unsorted_dropdown(page:Page):
    
    url = "https://testautomationpractice.blogspot.com/"
    
    # url   
    page.goto(url)
    
    country = page.locator("#country")
    expect(country).to_be_visible()
    
    
    '3 ways to select from dropdown'
    # # 1. By visible Text (Lable)
    # country.select_option(label="India")
    # print(f"Selected Country : {country.input_value()}")
    
    # # 2. By Value
    # country.select_option(value="uk")
    # print(f"Selected Country : {country.input_value()}")
        
    # # 3. By Index
    # country.select_option(index=6)
    # print(f"Selected Country : {country.input_value()}")    
    
    'get all options from dropdown'
    
    options = page.locator("#country>option")
    expect(options).to_have_count(10)
    
    option_text = [ text.strip() for text in options.all_text_contents()]
    print(option_text, len(option_text))
    

    # timeout
    page.wait_for_timeout(2000)

    # close
    page.close()
         
    
def test_practise1(page:Page):
    
    url = "https://bstackdemo.com/"
    
    # url
    page.goto(url=url)
    
    # timeout
    page.wait_for_timeout(2000)
    
    # order element
    order = page.locator("//div[@class='sort']//select")
    
    # checking visibility and enability
    expect(order).to_be_visible()
    expect(order).to_be_enabled()
    
    # selecting lowest to highest
    order.select_option(label="Lowest to highest")
    
    # timeout
    page.wait_for_timeout(2000)
    
    # All elements
    all_elements = page.locator("//div[@class='shelf-container']//div[@class='shelf-item']")
    # print(all_elements.all_text_contents(), len(all_elements.all_text_contents()))
    # print(all_elements.all_inner_texts(), len(all_elements.all_inner_texts()))

    inner_data = all_elements.all_inner_texts()
    products = []
    prices = []
    
    
    print()
    for data in inner_data:

        product_name = (data.split("\n")[0]).strip() 
        price = (data.split("\n")[2]).strip()
        
        print(f"Product : {product_name:20} | Price : {price}")
        products.append(product_name)
        prices.append(price)
        
    print(f"\nLowest price  : {prices[0]}")
    print(f"Highest price : {prices[-1]}")
    
    # close
    page.close()
    
    
    
    
    
 