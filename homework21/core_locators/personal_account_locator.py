from selenium.webdriver.common.by import By

from homework21.core_locators.base_page_locator import BaseLocator


class PersonalAccountLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.locator_email = (By.XPATH, "//input[@id='email']")
        self.locator_password = (By.XPATH, "//input[@id='password']")
        self.login_button_locator = (By.XPATH, "//button[@name='commit']")
