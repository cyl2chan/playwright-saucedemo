from playwright.sync_api import Page

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.get_by_role("button", name="Finish")

    def click_finish(self):
        self.finish_button.click()