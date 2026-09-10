from playwright.sync_api import Page, expect

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.swag_labs_text = page.get_by_text("Swag Labs")
        self.first_add_to_cart_button = page.get_by_role("button", name="Add to cart").nth(1)
        self.cart_button = page.locator("#shopping_cart_container")

    def display_swag_labs(self, page: Page):
        #expect(self.swag_labs_text).to_be_visible()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    def click_first_add_to_cart(self):
        self.first_add_to_cart_button.click()

    def click_cart(self):
        self.cart_button.click()