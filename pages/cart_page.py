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

    @allure.step("Remove Item from Cart")
    def remove_item_from_cart(self):
        self.click_button(REMOVE_FROM_CART_BTN)
