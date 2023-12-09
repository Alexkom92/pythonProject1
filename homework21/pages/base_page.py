from abc import ABC

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver
        self.web_driver_wait = WebDriverWait(self._driver, 10)

    def wait_until_element_appears(self, locator):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        return self.wait_until_element_appears(locator).click()

    def send_text_to_search_field(self, text, locator):
        element = self.wait_until_element_appears(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

