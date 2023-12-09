from selenium.webdriver import Chrome
import pytest

from homework21.pages.product_page import ProductPage
from homework21.pages.personal_account_page import PersonalAccount


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def product_page(driver):
    driver.get('https://haircp.com.ua/collection/volossya/shampuni/')
    yield ProductPage(driver)


@pytest.fixture
def pers_account(driver):
    driver.get('https://haircp.com.ua/index.php?route=account/login')
    yield PersonalAccount(driver)



