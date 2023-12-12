from homework21.pages.base_page import BasePage
from homework21.core_locators.personal_account_locator import PersonalAccountLocator


class PersonalAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PersonalAccountLocator()
        self.email = "Alex-komiirny@gmail.com"
        self.password = "QWdscc59+"

    def account_enter_email(self):
        self.send_text_to_search_field(self.email, self.locators.locator_email)

    def account_enter_password(self):
        self.send_text_to_search_field(self.password, self.locators.locator_password)

    def authorize_click(self):
        self._click(self.locators.login_button_locator)
