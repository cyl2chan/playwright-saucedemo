from playwright.sync_api import Page, expect

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.thank_you_text = page.get_by_text("Thank you for your order!")

    def check_thank_you_text(self):
        expect(self.thank_you_text).to_be_visible()