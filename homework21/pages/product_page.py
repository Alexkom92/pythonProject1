from homework21.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import time
from homework21.core_locators.product_page_locator import ProductPageLocator


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductPageLocator()
        self.text_min = "500"
        self.text_max = "999"

    def choose_main_menu(self):
        self._click(self.locators.main_menu_locator)

    def send_text_to_field(self, text, locator):
        element = self.wait_until_element_appears(locator)
        element.clear()
        element.send_keys(text)

    def go_to_shampoo(self):
        main_menu_element = self._click(self.locators.main_menu_locator)
        time.sleep(5)
        for_hair_element = self._click(self.locators.locator_for_hair)
        time.sleep(2)
        hair_shampoo_element = self._click(self.locators.locator_hair_shampoo)
        time.sleep(2)
        shampoo_for_head_element = self._click(self.locators.locator_shampoo_for_head)

    def filter_shampoo_for_head(self):
        min_prise_element = self.wait_until_element_appears(self.locators.locator_min_prise_filter)
        self.send_text_to_field(self.text_min, self.locators.locator_min_prise_filter)
        time.sleep(2)
        max_prise_element = self.wait_until_element_appears(self.locators.locator_max_prise_filter)
        self.send_text_to_field(self.text_max,self.locators.locator_max_prise_filter)
        time.sleep(2)
        send_enter_filter_element = self._click(self.locators.locator_send_enter_filter)


