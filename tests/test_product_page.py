import allure
import pytest

from base.base_test import BaseTest
from data.links import CORPORATION_LIST_URL


class TestLoggedUserProductPage(BaseTest):
    @pytest.fixture(scope="function")
    def user_login(self):
        self.login_page.open()
        self.login_page.user_login()

    @allure.feature('Radiant Tee product page')
    @allure.title("Adding the product to the comparison list")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-134')
    def test_adding_the_product_to_the_comparison_list(self, user_login):
        self.product_page.open()
        self.product_page.click_add_to_compare_link()
        assert self.product_page.check_message_that_product_added_to_the_comparison_list(), \
            "Wrong message"
        self.product_page.click_corporation_list_link()
        assert self.corporation_list_page.check_url_is_(CORPORATION_LIST_URL), \
            "Wrong URL"
        assert self.corporation_list_page.check_number_of_products_on_page() == 1, \
            "Must be one product on the page"
