import re
from playwright.sync_api import Page, expect

def test_login_single(page: Page) -> None:
    page.goto("http://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button").click()
    #expect(page.get_by_text("Swag Labs")).to_be_visible()

