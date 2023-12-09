from homework21.conftest import pers_account


def test_authorization(pers_account):
    pers_account.account_enter_email()
    pers_account.account_enter_password()
    pers_account.authorize_click()
    expected_text = "Вхід до кабінету покупця"
    assert expected_text in pers_account.get_page_source()
