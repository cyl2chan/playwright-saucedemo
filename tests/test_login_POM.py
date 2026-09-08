import re
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    
    page.goto("http://www.saucedemo.com")
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    products_page.display_swag_labs()
