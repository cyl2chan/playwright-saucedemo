import re
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import pytest

def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_data/data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.parametrize("username, password", get_csv_data())

def test_login(page: Page, username, password) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    
    page.goto("http://www.saucedemo.com")
    #login_page.enter_username("standard_user")
    #login_page.enter_password("secret_sauce")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    products_page.display_swag_labs()

