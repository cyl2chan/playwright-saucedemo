from playwright.sync_api import Page

class YourInfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.firstname_input = page.get_by_placeholder("First Name")
        self.lastname_input = page.get_by_placeholder("Last Name")
        self.zip_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("continue")

    def enter_first_name(self, firstname: str):
        self.firstname_input.fill(firstname)

    def enter_last_name(self, lastname: str):
        self.lastname_input.fill(lastname)
    
    def enter_zip(self, zip: str):
        self.zip_input.fill(zip)

    def click_continue_button(self):
        self.continue_button.click()

    def complete_your_info(self):
        self.enter_first_name("Leon")
        self.enter_last_name("Chan")
        self.enter_zip("A1B C2D")
        self.click_continue_button.click()