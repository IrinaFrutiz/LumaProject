import allure

from base.base_page import BasePage
from data.links import CART_URL

CART_QTY_TAG = ('xpath', '//span[@class="counter-number"]')

PRODUCT_NAME = ('xpath', '//tr[@class="item-info"]//strong[@class="product-item-name"]')
PRODUCT_SIZE_VALUE = ('xpath', '//tr[@class="item-info"]//dd[1]')
PRODUCT_COLOR_VALUE = ('xpath', '//tr[@class="item-info"]//dd[2]')
PRODUCT_IMG = ('xpath', '//tr[@class="item-info"]//img[@class="product-image-photo"]')

REMOVE_FROM_CART_BTN = ('xpath', '//a[@class="action action-delete"]')


class CartPage(BasePage):
    URL = CART_URL

    @allure.step("Check Cart Tag")
    def check_cart_tag_displayed(self):
        assert self.check_element_visibility_(CART_QTY_TAG).is_displayed()

    @allure.step("Verify Product Name")
    def verify_product_name(self):
        assert self.check_element_visibility_(PRODUCT_NAME).text == 'Argus All-Weather Tank', \
            'Wrong Product Name'

    @allure.step("Verify Product Size")
    def verify_product_size(self):
        assert self.check_element_visibility_(PRODUCT_SIZE_VALUE).text == 'M', \
            'Wrong Product Size Value'

    @allure.step("Verify Product Color")
    def verify_product_color(self):
        assert self.check_element_visibility_(PRODUCT_COLOR_VALUE).text == 'Gray', \
            'Wrong Product Color Value'

    @allure.step("Verify Product Image")
    def verify_product_image(self):
        assert self.check_element_visibility_(PRODUCT_IMG).is_displayed() and \
            self.check_element_visibility_(PRODUCT_IMG).get_attribute('alt') == 'Argus All-Weather Tank', \
            'Product Image is not displayed or not relevant'

    @allure.step("Remove Item from Cart")
    def remove_item_from_cart(self):
        self.click_button(REMOVE_FROM_CART_BTN)
