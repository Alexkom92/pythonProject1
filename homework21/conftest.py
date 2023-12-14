from selenium.webdriver import Chrome
import pytest

from homework21.pages.product_page import ProductPage
from homework21.pages.personal_account_page import PersonalAccount
from homework21.pages.base_page import BasePage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver)


"""@pytest.fixture
def product_page(driver):
    driver.get('https://haircp.com.ua/collection/volossya/shampuni/')
    yield ProductPage(driver)"""


@pytest.fixture
def product_page(base_page):
    base_page.navigate_to_url('https://haircp.com.ua/collection/volossya/shampuni/')
    return ProductPage(base_page.get_driver())


@pytest.fixture
def pers_account(base_page):
    base_page.navigate_to_url('https://haircp.com.ua/index.php?route=account/login')
    yield PersonalAccount(base_page.get_driver())
