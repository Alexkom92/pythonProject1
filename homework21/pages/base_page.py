from abc import ABC

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def save_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def get_cookies(self):
        return self.driver.get_cookies()


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def save_to_local_storage(self, key, value):
        script = f"localStorage.setItem('{key}', '{value}');"
        self.driver.execute_script(script)

    def get_from_local_storage(self, key):
        script = f"return localStorage.getItem('{key}');"
        return self.driver.execute_script(script)


class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver
        self.web_driver_wait = WebDriverWait(self._driver, 10)
        self.cookies = Cookies(driver)
        self.local_storage = LocalStorage(driver)

    def get_driver(self):
        return self._driver

    def navigate_to_url(self, url):
        self._driver.get(url)

    def wait_until_element_appears(self, locator):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        return self.wait_until_element_appears(locator).click()

    def send_text_to_search_field(self, text, locator):
        element = self.wait_until_element_appears(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def get_page_source(self):
        return self._driver.page_source

    def check_current_url(self):
        return self._driver.current_url
