from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.your_info_page import YourInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    your_info_page = YourInfoPage(page)
    overview_page = CheckoutOverviewPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    page.goto("http://www.saucedemo.com")
    login_page.login()

    products_page.click_first_add_to_cart()
    products_page.click_cart()
    cart_page.click_checkout()
    your_info_page.complete_your_info()
    overview_page.click_finish()
    checkout_complete_page.check_thank_you_text()

