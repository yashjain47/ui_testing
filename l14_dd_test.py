import pytest
from playwright.sync_api import Playwright, expect, Page



search =  ["Laptop", "smartphone", "monitor"]


@pytest.mark.skip
@pytest.mark.parametrize("item", search)
def test_dd_test(item, page:Page):
    
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_load_state()
    
    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()
    
    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item)
    
    


