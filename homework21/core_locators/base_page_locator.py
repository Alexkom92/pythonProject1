from selenium.webdriver.common.by import By


class BaseLocator:
    def __init__(self):
        self.main_menu_locator = (By.XPATH, "//a[@custom-popup-link = 'mobile-menu']")
        self.search_locator = (By.XPATH, "//input[@class='input-search']")
        self.contact_locator = (By.XPATH, "//ul[@class='hide-mobile']//li//a[.='Контакти']")
        self.search_locator = (By.XPATH, "//input[@class='input-search']")