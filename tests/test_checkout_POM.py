from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.your_info_page import YourInfoPage

def test_checkout(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    your_info_page = YourInfoPage(page)

    login_page.login()

    products_page.click_first_add_cart()
    products_page.click_cart()
    cart_page.click_cart()
    your_info_page.complete_your_info()
    
