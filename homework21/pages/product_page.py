from homework21.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

from homework21.core_locators.product_page_locator import ProductPageLocator


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductPageLocator()

    def choose_main_menu(self):
        self._click(self.locators.main_menu_locator)
        return MainMenuPage(self._driver)

    def send_text_to_search_field(self, text):
        element = self.wait_until_element_appears(self.locators.search_locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)