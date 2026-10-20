"""
LOCATORS
---------------------------------------------
1.  Identifying/Locating the Web elements
2.  Performing Actions
3.  Validations (Assertions)




LOCATING THE WEBELEMENTS
---------------------------------------------
1.  Playwright built-in Locators 
2.  XPath
3.  CSS   


Priority in playwright  -->     built-In > CSS > Xpath


DOM  = Document object model
On runtime the DOM is created (when page is loading...)
DOM is like

<html>
<body>
    ...
</body>
</html>



$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


Playwright built-in Locators
---------------------------------------------

page.get_by_alt_text()      =   to locate an element, usually image, by its text alternative.
page.get_by_text()          =   to locate by text content.
page.get_by_role()          =   to locate by explicit and implicit accessibility attributes.   [Not available in DOM]
page.get_by_label()           =   to locate a form control by associated label's text.
page.get_by_placeholder()     =   to locate an input by placeholder.
page.get_by_title()           =   to locate an element by its title attribute.
page.get_by_test_id()          =   to locate an element based on its data-testid attribute (other attributes can be configured).  




Build-In Dynamic Elements

page.get_by_role("button", re.compile(r'ST.*'))



$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



CSS Selectors (Cascading style sheets)
---------------------------------------------

HTML    -   Design the elements (textbox, checkbox, list, etc)
JS      -   Functionality 
CSS     -   Attractive/beautiful (works based on DOM)


Relative CSS: 

tag id                  -   tag#id
tag class               -   tag.class
tag attribute           -   tag[attribute=value]
tag class attribute     -   tag.class[attribute=value]


Like  : 
        input#small-searchterms   [tag is optional]
it can be like 
        #small-searchterms
both OK.

NOTE : IF any space in value, try to use first phase before space because it treats both differenct 
like 'Search store', use it as 'Search' only or inside some quotation ",'.


Absolute CSS:

html > body > div > div > p[id='para1']
html > body > div > div > p[id='para1'][class='main']
<----- absoute css -----> <------ relative css ----->

'>' represents the immediate child element
body p[id='para1']  --> also correct


p[class^='pa']  -->     '^' startwith
p[class$='ra']  -->     '$' endwith
p[class*='ar']  -->     '*' middle charater

p:not([id='oara1'])[class='main']  

head+*          -->     siblings






Build-In Dynamic Elements

button[name^='st']





$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



XPath   --  Address/Path of an Element
---------------------------------------------
XML Path Language

1.  Absolute Xpath  -   Full path
/html/body/div[4]/div[1]/div[2]/a/img


2.  Relative Xpath  -   Partial path    --> //tagname[@attribut='value']
//img[@alt='Tricentis Demo Web Shop']


3.  Xpath with contains()
//h2//a[contains(@href,'computer')]
//h2//a[starts-with(@href,'/build')]
//a[text()='Register']
//div[@class='column follow-us']//li[last()]
//div[@class='column follow-us']//li[position()=2]


4.  xpath with dynamic path
//button[text()='START' or text()='STOP']
//button[@name='start' or @name='stop']
//button[contains(@name,'st')]
//button[starts-with(@name,'st')]





"""

from playwright.sync_api import Page, expect
import re



'For built In Selectors'
def test_verify_pwlocators(page:Page):

    url = "https://demo.nopcommerce.com/"
    url = "https://demoqa.com"
    url = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"

    'launching the URL'
    page.goto(url)

    'For Timeout 5s'
    # page.wait_for_timeout(5000)

    print(f"TITLE : {page.title()}")

    '1. get_by_alt_text -- ALT TAG (Images)'
    # logo = page.get_by_alt_text("nopCommerce demo store")
    # expect(logo).to_be_visible()


    '2. get_by_text -- Text'
    # expect(page.get_by_text("Alerts, Frame & Windows")).to_be_visible()     # full text
    # expect(page.get_by_text("Alerts")).to_be_visible()                      # partial text
    # expect(page.get_by_text(re.compile(".*Alerts*."))).to_be_visible()      # regular expression


    '3. get_by_role -- header, button, checkbox etc'
    # expect(page.get_by_role(role="heading", name="Tabs")).to_be_visible()
    # expect(page.get_by_role(role="textbox", name="Username:")).to_be_visible()


    '4. get_by_label -- name, email etc'
    # page.get_by_label("Email Address:").fill("test@gmail.com")
    # page.wait_for_timeout(500)


    '5. get_by_placeholder -- searches'
    # page.get_by_placeholder("Enter your full name").fill("Yash jain")
    # page.wait_for_timeout(500)


    '6. get_by_title'
    # expect(page.get_by_title("Home page link")).to_have_text("Home")
    # expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")


    '7. get_by_test_id'
    # expect(page.get_by_test_id("edit-profile-btn")).to_have_text("Edit Profile")

    'For closing the Web Page'
    page.close()


'practise 1'
def test_orangehr(page:Page):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    page.goto(url)
    page.wait_for_timeout(500)

    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    expect(page.get_by_role(role="button", name="Login")).to_be_visible()
    page.get_by_role(role="button", name="Login").click()
    page.wait_for_timeout(5000)

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    page.wait_for_timeout(5000)

    page.close()


'For CSS Selectors'
def test_verify_csslocators(page:Page):

    url = "https://demowebshop.tricentis.com/"

    page.goto(url)

    'tag id'
    # page.locator("input#small-searchterms").fill("t-shirts")
    # page.locator("#small-searchterms").fill("t-shirts")

    'tag class'
    # page.locator("input.search-box-text").fill("shirts")
    # page.locator(".search-box-text").fill("shirts")
    # page.wait_for_timeout(5000)


    'tag attribute'
    # page.locator("input[name=q]").fill("Trousers")
    # page.locator("input[name='Search store']").fill("Trousers")
    # page.wait_for_timeout(5000)


    'tag class atrribute'
    # page.locator("input.search-box-text[name=q]").fill("Jeans")
    # page.wait_for_timeout(5000)


    page.close()


'practise 2'
def test_demowebshop(page:Page):

    # Launch Webpage 
    url = "https://demowebshop.tricentis.com/"
    page.goto(url)

    page.wait_for_timeout(500)

    # Verify Logo Visibility 
    # expect(page.locator("img[alt^='Tricentis']")).to_be_visible()


    # Capture all computer related products and count it
    all_locators = page.locator("div[class='product-grid home-page-product-grid'] a:not([title*='computer']):not([title*='Computer'])[href*='computer'] ")
    print(f"All locators : {all_locators} $$$$$$$$$$$$$$$$$$$$$$$ {type(all_locators)}")

    for i in all_locators.all_text_contents():
        print(f"Text : {i}")


    # Get Footer Details
    f_locators = page.locator("div[class*='follow']")
    print(f"F Locators : {f_locators} $$$$$$$$$$$$$$$$$$$$$$$ {type(f_locators)}")

    print(f_locators.all_text_contents())
    print(f_locators.all_inner_texts())

    page.close()


'For XPaths'
def test_verify_xpathlocators(page:Page):

    url = "https://demowebshop.tricentis.com/"

    page.goto(url, timeout=100000)

    'Absolute Xpath (full xpath)'
    # expect(page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")).to_be_visible()


    "Relative xpath //tagname[@attribut='value']"
    # expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()


    'xpath with contains()'
    products = page.locator("//h2//a[contains(@href,'computer')]")
    print(products.count())
    expect(products).to_have_count(4)

    print("first product",products.first.text_content())
    print("Last product",products.last.text_content())
    print("Nth product",products.nth(2).text_content())


    product_title = products.all_text_contents()
    for i in product_title:
        print(f"Titles : {i}")


    # xpath with starts-wtih
    building_products = page.locator("//h2//a[starts-with(@href,'/build')]")
    print(building_products.count())

    expect(building_products).to_have_count(3)


    # xpath with text()
    expect(page.locator("//a[text()='Register']")).to_be_visible()


    # xpath with last
    google = page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google).to_have_text("Google+")

    # expect(page.locator("//div[@class='column follow-us']//li[5]")).to_be_visible()

    
    # xpath with position
    twitter = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter).to_have_text("Twitter")
    print(twitter.text_content())
    print(twitter.all_text_contents)
    print(twitter.inner_text)
        
    page.close()










