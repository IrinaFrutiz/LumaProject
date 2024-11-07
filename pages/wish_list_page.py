import allure
from selenium.common import TimeoutException

from base.base_page import BasePage
from data.links import WISH_LIST_URL

SUCCESS_MESSAGE = ('css selector', 'div[data-bind^="html: $parent.prepareMessageForHtml"]')
ALL_IMG_ICONS = ('css selector', '.main img')
ALL_PRODUCT_NAMES = ('css selector', '.main strong')
ALL_DELETE_BUTTONS = ('xpath', '//a[@data-role="remove"]')
LAST_ADDED_ITEM_NAME = ('css selector', '.block-wishlist .product-item-link span')


class WishListPage(BasePage):
    URL = WISH_LIST_URL

    @allure.step("Check the success message that product added to the wish list")
    def check_success_message_with_name_(self, product_name):
        self.check_element_visibility_(SUCCESS_MESSAGE)
        message_text = self.get_text(SUCCESS_MESSAGE)
        return f"{product_name} has been added to your Wish List. Click here to continue shopping." == message_text

    @allure.step("Check that added product is in My Wish List(main block) by name")
    def check_wish_list_have_product_with_name_(self, product_name):
        all_products = self.find_all(ALL_PRODUCT_NAMES)
        all_products_name = [i.text for i in all_products]
        return product_name in all_products_name

    @allure.step("Check that last added item have the name")
    def check_last_added_item_name_is_(self, product_name):
        self.check_element_visibility_(LAST_ADDED_ITEM_NAME)
        last_added_item_name = self.get_text(LAST_ADDED_ITEM_NAME)
        print(last_added_item_name)
        return product_name == last_added_item_name

    @allure.step("Delete all products from user's wish list")
    def remove_products(self):
        self.open()
        try:
            img_icons = self.check_all_visibility_(ALL_IMG_ICONS)
            for id in range(len(img_icons)):
                img_icon = self.find(ALL_IMG_ICONS)
                delete_button = self.find(ALL_DELETE_BUTTONS)
                self.action.move_to_element(img_icon)\
                    .move_to_element(delete_button)\
                    .click(delete_button).perform()
                self.check_page_loaded()
        except TimeoutException:
            pass

