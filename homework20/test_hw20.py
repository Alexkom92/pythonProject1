from selenium.webdriver import Chrome, Keys, ActionChains
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_01():
    driver = Chrome()
    driver.get('https://haircp.com.ua/')
    search_locator = "//input[@class='input-search']"
    element = driver.find_element(by='xpath', value=search_locator)
    element.send_keys('фарба')
    element.send_keys(Keys.ENTER)
    second_page_url = "https://haircp.com.ua/index.php?route=product/search&search=%D1%84%D0%B0%D1%80%D0%B1%D0%B0"

    assert driver.current_url == second_page_url
    time.sleep(5)
    driver.quit()


def test_02():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://haircp.com.ua/')
    main_menu_locator = "//a[@custom-popup-link = 'mobile-menu']"
    main_menu_element = driver.find_element('xpath', main_menu_locator)
    main_menu_element.click()
    time.sleep(3)
    locator_for_hair = "//span[text()='Для волосся'][1]"
    for_hair_element = driver.find_element("xpath", locator_for_hair)
    for_hair_element.click()
    time.sleep(3)
    locator_hair_shampoo = "//span[text()='Шампуні для волосся']"
    hair_shampoo_element = driver.find_element("xpath", locator_hair_shampoo)
    hair_shampoo_element.click()
    time.sleep(3)
    locator_shampoo_for_head = "//span[text()='Для шкіри голови'][1]"
    shampoo_for_head_element = driver.find_element("xpath", locator_shampoo_for_head)
    shampoo_for_head_element.click()
    time.sleep(5)
    final_page_url = "https://haircp.com.ua/collection/volossya/shampuni/shampuni-dlya-shkiry-golovy/"
    assert driver.current_url == final_page_url


def test_filter_shampoo_for_head():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://haircp.com.ua/collection/volossya/shampuni/shampuni-dlya-shkiry-golovy/")
    time.sleep(5)
    locator_min_prise_filter = "//input[@name='ocf[2-0-1][min]']"
    minimum_value_element = driver.find_element(by='xpath', value=locator_min_prise_filter)
    minimum_value_element.clear()
    minimum_value_element.send_keys("500")
    time.sleep(2)
    locator_max_prise_filter = "//input[@name='ocf[2-0-1][max]']"
    maximum_value_element = driver.find_element(by='xpath', value=locator_max_prise_filter)
    maximum_value_element.clear()
    maximum_value_element.send_keys("999")
    time.sleep(2)
    locator_send_enter_filter = "//button[@class='ocf-btn ocf-btn-block ocf-search-btn-static']"
    send_enter_filter_element = driver.find_element("xpath", locator_send_enter_filter)
    send_enter_filter_element.click()
    time.sleep(5)
    expected_text = "39 товаров"
    assert expected_text in driver.page_source
    driver.quit()


def test_filter_brand_shampoo_for_head():
    driver = Chrome()
    driver.maximize_window()
    driver.get("https://haircp.com.ua/collection/volossya/shampuni/shampuni-dlya-shkiry-golovy/")
    time.sleep(5)
    locator_send_brand = "//span[text()='Бренд']"

    element_send_brand = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, locator_send_brand)))
    # Прокручиваем к элементу 'Бренд'
    driver.execute_script("arguments[0].scrollIntoView(true);", element_send_brand)

    time.sleep(5)
    element_send_brand.click()
    locator_brand_daeng_gi = "//button[@data-value-id='1456341833']"
    element_brand_daeng_gi = driver.find_element("xpath", locator_brand_daeng_gi)
    time.sleep(2)
    element_brand_daeng_gi.click()
    time.sleep(2)
    locator_search_in_filter = "//button[@class='ocf-btn ocf-search-btn-popover']"
    search_in_filter = driver.find_element("xpath", locator_search_in_filter)
    search_in_filter.click()
    time.sleep(5)
    expected_text = "Для шкіри голови бренд daeng gi meo ri"
    assert expected_text in driver.page_source
    driver.quit()
