from homework21.conftest import product_page, driver


def test_go_to_shampoo(product_page):
    product_page.go_to_shampoo()
    final_page_url = "https://haircp.com.ua/collection/volossya/shampuni/shampuni-dlya-shkiry-golovy/"
    assert product_page.check_current_url() == final_page_url


def test_filter(product_page):
    product_page.filter_shampoo_for_head()
    expected_text = "202 товаров"
    assert expected_text in product_page.get_page_source()



