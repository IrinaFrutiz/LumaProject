import allure

from base.base_test import BaseTest


class TestCart(BaseTest):
    @allure.feature('Cart')
    @allure.title("Checking the size color product-image and product name are correct in the Cart page")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-7')
    def test_product_parameters_correct_in_cart(self):
        # Precondition:
        self.main_page.open()
        self.main_page.hover_over_argus_item()
        self.main_page.choose_argus_size_m()
        self.main_page.choose_argus_color_gray()
        self.main_page.click_argus_add_to_cart_btn()

        self.main_page.check_url_is_(self.main_page.URL)
        self.main_page.check_success_message()
        self.cart_page.check_cart_tag_displayed()
        self.cart_page.open()

        # Steps:
        self.cart_page.verify_product_name()
        self.cart_page.verify_product_size()
        self.cart_page.verify_product_color()
        self.cart_page.verify_product_image()

        # Postcondition:
        self.cart_page.remove_item_from_cart()
