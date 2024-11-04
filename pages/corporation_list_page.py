import allure
from selenium.common import TimeoutException

from base.base_page import BasePage
from data.links import CORPORATION_LIST_URL

ALL_PRODUCTS = ('xpath', '//td[@data-th="Product"]')
ALL_REMOVE_PRODUCT = ('css selector', '.action.delete')
ACTION_OK = ('css selector', '.action-accept')
MSG_NO_ITEM = ('css selector', '.message.empty')


class CorporationListPage(BasePage):
    URL = CORPORATION_LIST_URL

    @allure.step("Return Number of products on the corporation list page")
    def check_number_of_products_on_page_is_(self, number):
        return len(self.find_all(ALL_PRODUCTS)) == number

    @allure.step("Delete all products from Corporation List")
    def remove_products(self):
        try:
            self.check_element_not_visible_(MSG_NO_ITEM)
            for button in self.find_all(ALL_REMOVE_PRODUCT):
                button.click()
                self.click_button(ACTION_OK)
                self.check_page_loaded()
        except TimeoutException:
            pass
        self.check_element_visibility_(MSG_NO_ITEM)
