from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
import pytest

@pytest.mark.parametrize("product_name", ProductsPage.get_inventory_data())

class CartPage:
    def __init__(self, page: Page, product_name=None):
        self.page = page
        products_page = ProductsPage(page, product_name)
        self.product_name = page.locator(".inventory_item_name")
        #self.product_price = page.locator(".inventory_item_price").text_content()
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def check_product_name(self, product_name):
        #soft_assert(product_name == self.product_name.text_content())
        print("name in test:", self.product_name)
        expect.soft(self.product_name).to_have_text(product_name)
    
    #def check_price():


    def click_checkout(self):
        self.checkout_button.click()