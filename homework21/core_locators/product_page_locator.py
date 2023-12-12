from selenium.webdriver.common.by import By

from homework21.core_locators.base_page_locator import BaseLocator


class ProductPageLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.locator_for_hair = (By.XPATH, "//span[text()='Для волосся'][1]")
        self.locator_hair_shampoo = (By.XPATH, "//span[text()='Шампуні для волосся']")
        self.locator_shampoo_for_head = (By.XPATH, "//span[text()='Для шкіри голови'][1]")
        self.locator_filter_shampoo_chi = (By.XPATH, "//span[. ='CHI']")
        self.locator_search_with_filter = (By.XPATH, "//button[@data-ocf='button']")
        self.locator_chi_shampoo_product = (By.XPATH, "//a[@data-prod-title = 'Шампунь відновлюючий з олією аргани ("
                                                      "340 мл)']")
        self.locator_min_prise_filter = (By.XPATH, "//input[@name='ocf[2-0-1][min]']")
        self.locator_max_prise_filter = (By.XPATH, "//input[@name='ocf[2-0-1][max]']")
        self.locator_send_enter_filter = (By.XPATH, "//button[@class='ocf-btn ocf-btn-block ocf-search-btn-static']")