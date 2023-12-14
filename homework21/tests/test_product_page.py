from homework21.conftest import product_page, driver, base_page


def test_go_to_shampoo(product_page):
    product_page.go_to_shampoo()
    final_page_url = "https://haircp.com.ua/collection/volossya/shampuni/shampuni-dlya-shkiry-golovy/"
    assert product_page.check_current_url() == final_page_url


def test_filter(product_page):
    product_page.filter_shampoo_for_head()
    expected_text = "202 товаров"
    assert expected_text in product_page.get_page_source()


def test_cookies(product_page):
    # Сохраняем куки
    cookies_data = {'name': 'Test_cookie', 'value': 'TEst_value'}
    product_page.cookies.save_cookie(cookies_data)

    # Получаем куки и проверяем, что они присутствуют
    saved_cookies = product_page.cookies.get_cookies()
    print(saved_cookies)
    assert any(cookie['name'] == 'Test_cookie' and cookie['value'] == 'TEst_value' for cookie in saved_cookies)


def test_local_storage(product_page):
    # Сохраняем значение в локальное хранилище
    key = 'Test_key'
    value = 'Test_value'
    product_page.local_storage.save_to_local_storage(key, value)

    # Получаем значение из локального хранилища и проверяем
    retrieved_value = product_page.local_storage.get_from_local_storage(key)
    assert retrieved_value == value
