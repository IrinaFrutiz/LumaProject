import allure

from base.base_test import BaseTest
from pages.main_page import SUCCESS_MSG_ALERT, SUCCESS_MSG_TEXT
from pages.cart_page import PRODUCT_IMG, PRODUCT_SIZE_VALUE, PRODUCT_COLOR_VALUE, PRODUCT_NAME, CART_QTY_TAG, \
    CART_IS_EMPTY_MSG


class TestCart(BaseTest):
    @allure.feature('Cart')
    @allure.title("Checking the size color product-image and product name are correct in the Cart page")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-7')
    def test_product_parameters_correct_in_cart(self):
        # Precondition:
        self.main_page.open()
        self.main_page.scroll_to_products()
        self.main_page.hover_over_argus_item()
        self.main_page.choose_argus_size_m()
        self.main_page.choose_argus_color_gray()
        self.main_page.click_argus_add_to_cart_btn()

        self.main_page.check_url_is_(self.main_page.URL)
        self.main_page.check_success_message_is_(SUCCESS_MSG_ALERT, SUCCESS_MSG_TEXT)
        assert self.cart_page.check_element_visibility_(CART_QTY_TAG).is_displayed(), \
            'Cart Quantity Tag is not displayed'
        self.cart_page.open()

        # Steps:
        assert self.cart_page.check_element_visibility_(PRODUCT_NAME).text == 'Argus All-Weather Tank', \
            'Wrong Product Name'
        assert self.cart_page.check_element_visibility_(PRODUCT_SIZE_VALUE).text == 'M', \
            'Wrong Product Size Value'
        assert self.cart_page.check_element_visibility_(PRODUCT_COLOR_VALUE).text == 'Gray', \
            'Wrong Product Color Value'
        assert self.cart_page.check_element_visibility_(PRODUCT_IMG).is_displayed() and \
               self.cart_page.check_element_visibility_(PRODUCT_IMG).get_attribute('alt') == \
               'Argus All-Weather Tank', 'Product Image is not displayed or not relevant'

        # Postcondition:
        self.cart_page.remove_item_from_cart()

    @allure.feature('Cart')
    @allure.title("Checking the product is deleted from the cart")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-116')
    def test_product_deleted_from_cart(self):
        # Precondition:
        self.main_page.open()
        self.main_page.choose_random_item_and_click()
        self.product_page.if_size_and_color_pick_random_size_and_color_add_to_cart()
        assert self.cart_page.check_element_visibility_(CART_QTY_TAG).is_displayed(), \
            'Cart Quantity Tag is not displayed'
        self.cart_page.open()

        # Steps:
        self.cart_page.remove_item_from_cart()
        assert self.cart_page.check_page_title_is_('Shopping Cart'), 'Wrong Page Title'
        assert self.cart_page.check_success_message_is_(
                CART_IS_EMPTY_MSG, 'You have no items in your shopping cart.\nClick here to continue shopping.'
            ), 'The message is not provided'
