from playwright.sync_api import Page, expect
import pytest

class ProductsPage:
    def get_inventory_data() -> list:
        import csv 
        inventory_data = []
        with open("./test_data/inventory_data.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                inventory_data.append(row[0])
            return inventory_data

    @pytest.mark.parametrize("product_name", get_inventory_data())
    
    def __init__(self, page: Page, product_name=None):
        self.product_name = product_name if product_name is not None else {}
        
        self.page = page
        self.inventory_item = self.page.locator(".inventory_item")
        self.product_name = self.inventory_item.filter(has_text=product_name)
        self.product_add_to_cart = self.product_name.get_by_role("button", name="Add to cart")
        self.first_add_to_cart_button = page.get_by_role("button", name="Add to cart").nth(1)
        self.cart_button = page.locator("#shopping_cart_container")

    def display_inventory(self, page: Page):
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    def click_product_add_to_cart(self, product_name): #click add to cart of specific product
        self.product_add_to_cart.click()
        
    def click_first_add_to_cart(self):
        self.first_add_to_cart_button.click()

    """
    def store_product_price(self):
        const product_price = page.locator("#").all_text_contents()
        print(product_price)
    """

    def click_cart(self):
        self.cart_button.click()