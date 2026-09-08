from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_checkout(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login()

    products_page.click_first_add_cart()
    products_page.click_cart()
    cart_page.click_cart()
    page.get_by_placeholder("Username").fill("Leon")
    page.get_by_placeholder("Password").fill("Chan")