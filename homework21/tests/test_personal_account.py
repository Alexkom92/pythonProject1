from homework21.conftest import pers_account, driver, base_page


def test_authorization(pers_account):
    pers_account.account_enter_email()
    pers_account.account_enter_password()
    pers_account.authorize_click()
    expected_text = "Вхід до кабінету покупця"
    assert expected_text in pers_account.get_page_source()


def test_cookies(pers_account):
    # Сохраняем куки
    cookies_data = {'name': 'Test_cookie', 'value': 'TEst_value'}
    pers_account.cookies.save_cookie(cookies_data)

    # Получаем куки и проверяем, что они присутствуют
    saved_cookies = pers_account.cookies.get_cookies()
    print(saved_cookies)
    assert any(cookie['name'] == 'Test_cookie' and cookie['value'] == 'TEst_value' for cookie in saved_cookies)


def test_local_storage(pers_account):
    # Сохраняем значение в локальное хранилище
    key = 'Test_key'
    value = 'Test_value'
    pers_account.local_storage.save_to_local_storage(key, value)

    # Получаем значение из локального хранилища и проверяем
    retrieved_value = pers_account.local_storage.get_from_local_storage(key)
    assert retrieved_value == value
