import allure
import pytest

from base.base_test import BaseTest


class TestProductPage(BaseTest):
    @allure.feature('Radiant Tee product page')
    @allure.title("Adding the product to the comparison list")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-134')
    def test_adding_the_product_to_the_comparison_list(self):
        self.product_page.open()
        self.product_page.click_add_to_compare_link()
        assert self.product_page.check_message_that_product_added_to_the_comparison_list(), \
            "Wrong message"
        self.product_page.click_corporation_list_link()
        assert self.corporation_list_page.check_url_is_(self.corporation_list_page.URL), \
            "Wrong URL"
        assert self.corporation_list_page.check_number_of_products_on_page_is_(1), \
            "Must be one product on the page"

    @allure.feature('Radiant Tee product page')
    @allure.title("Visibility of the text in more information block")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-140')
    def test_user_can_see_more_details_on_product_page(self):
        self.product_page.open()
        self.product_page.click_more_information()
        assert self.product_page.check_more_information_text_clickable(), \
            "Text is not presence in more information block on product page"

    @allure.feature('Radiant Tee product page')
    @allure.title("Visibility of the text in Reviews block")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-139')
    def test_user_can_see_reviews_on_product_page(self):
        self.product_page.open()
        self.product_page.click_reviews()
        assert self.product_page.check_reviews_text_clickable(), \
            "Text is not presence in reviews block on product page"


class TestLoggedUserProductPage(BaseTest):
    @pytest.fixture(scope="function")
    def user_login(self):
        self.login_page.open()
        self.login_page.user_login()

    @pytest.fixture(scope="function")
    def remove_products_from_corporation(self):
        self.corporation_list_page.remove_products()
        yield
        self.corporation_list_page.remove_products()

    @pytest.fixture(scope="function")
    def remove_products_from_wishlist(self):
        self.wish_list_page.remove_products()
        yield
        self.wish_list_page.remove_products()

    @pytest.fixture(scope="function")
    def remove_products_from_cart(self):
        self.mini_cart_page.delete_all_product()
        yield
        self.mini_cart_page.delete_all_product()

    @allure.feature('Radiant Tee product page')
    @allure.title("Adding the product to the comparison list")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-134')
    def test_adding_the_product_to_the_comparison_list(self, user_login, remove_products_from_corporation):
        self.product_page.open()
        self.product_page.click_add_to_compare_link()
        assert self.product_page.check_message_that_product_added_to_the_comparison_list(), \
            "Wrong message"
        self.product_page.click_corporation_list_link()
        assert self.corporation_list_page.check_url_is_(self.corporation_list_page.URL), \
            "Wrong URL"
        assert self.corporation_list_page.check_number_of_products_on_page_is_(1), \
            "Must be one product on the page"

    @allure.feature('Radiant Tee product page')
    @allure.title("Adding the product to the wish list")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-135')
    def test_adding_the_product_to_the_wish_list(self, user_login, remove_products_from_wishlist):
        self.product_page.open()
        name = self.product_page.get_product_name()
        self.product_page.click_add_to_wish_list()
        assert self.wish_list_page.check_page_title_is_("My Wish List"), \
            "Wrong title"
        assert self.wish_list_page.check_success_message_with_name_(name), \
            "Wrong success message at the wish list page"
        assert self.wish_list_page.check_wish_list_have_product_with_name_(name), \
            f"The wish list don't have product with name {name}"

    @allure.feature('Radiant Tee product page')
    @allure.title("Visibility of product name, price and photo")
    @allure.link('https://pola-gor.atlassian .net/browse/LUM-143')
    def test_visibility_of_name_price_photo(self, user_login):
        self.main_page.open()
        self.basic_elements.go_to_women_tops_trees()
        self.women_tops_trees_page.go_to_random_product()
        assert self.product_page.check_product_name_presence(), \
            "Product name is not presence"
        assert self.product_page.check_product_price_presence(), \
            "Product price is not presence"
        assert self.product_page.check_product_photo_presence(), \
            "Product photo is not presence"

    @allure.feature('Radiant Tee product page')
    @allure.title("Adding the product to the cart")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-142')
    def test_adding_product_to_cart_check_name_subtotal_qty(self, user_login, remove_products_from_cart):
        self.product_page.open()
        product_name = self.product_page.get_product_name()
        product_price = self.product_page.get_product_price()
        size, color, qty = self.product_page.filling_in_product_parameters()
        self.product_page.click_add_to_cart()
        self.basic_elements.check_cart_uploaded()
        self.basic_elements.click_cart()
        assert self.mini_cart_page.check_cart_have_product_(product_name), \
            f"Not find product with the name {product_name} in the cart"
        assert self.mini_cart_page.check_subtotal_(product_price, qty), \
            f"Total price is not match with {product_price * qty} ({product_name}, {product_price}, {qty})"
        assert self.mini_cart_page.check_product_number_(qty), \
            f"Number of added {product_name} is not match with number in the cart {qty}"
        self.mini_cart_page.click_cart()

    @allure.feature('Radiant Tee product page')
    @allure.title("Quantity of items added to cart")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-141')
    def test_adding_product_to_cart_check_qty(self, user_login, remove_products_from_cart):
        self.product_page.open()
        size, color, qty = self.product_page.filling_in_product_parameters()
        self.product_page.click_add_to_cart()
        self.basic_elements.check_cart_uploaded()
        assert self.basic_elements.check_products_numbers_in_cart_is_(qty), \
            f"Number of added product is not match with number {qty} in the mini cart"

    @allure.feature('Radiant Tee product page')
    @allure.title("Visibility of the text in more information block")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-140')
    def test_user_can_see_more_details_on_product_page(self, user_login):
        self.product_page.open()
        self.product_page.click_more_information()
        assert self.product_page.check_more_information_text_clickable(), \
            "Text is not presence in more information block on product page"

    @allure.feature('Radiant Tee product page')
    @allure.title("Visibility of the text in Reviews block")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-139')
    def test_user_can_see_reviews_on_product_page(self, user_login):
        self.product_page.open()
        self.product_page.click_reviews()
        assert self.product_page.check_reviews_text_clickable(), \
            "Text is not presence in reviews block on product page"
