import re
from playwright.sync_api import Page, expect

def test_checkout_single(page: Page) -> None:
    #login to inventory
    page.goto("http://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button").click()

    #checkout process
    page.get_by_role("button", name="Add to cart").nth(1).click()
    page.locator("#shopping_cart_container").click()
    page.get_by_role("button", name="Checkout").click()
    page.get_by_placeholder("First Name").fill("Leon")
    page.get_by_placeholder("Last Name").fill("Chan")
    page.get_by_placeholder("Zip/Postal Code").fill("A1BC2D")
    page.locator("#continue").click()
    page.get_by_role("button", name="Finish").click()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()

    