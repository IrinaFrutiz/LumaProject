import allure

from base.base_page import BasePage
from data.links import CORPORATION_LIST_URL

ALL_PRODUCTS = ('xpath', '//td[@data-th="Product"]')
ALL_REMOVE_PRODUCT = ('css selector', '.action.delete')
ACTION_OK = ('css selector', '.action-accept')


class CorporationListPage(BasePage):
    URL = CORPORATION_LIST_URL

    @allure.step("Return Number of products on the corporation list page")
    def check_number_of_products_on_page(self):
        return len(self.find_all(ALL_PRODUCTS))

    @allure.step("Delete all products from Corporation List")
    def remove_products(self):
        self.check_all_visibility_(ALL_REMOVE_PRODUCT)
        for button in self.find_all(ALL_REMOVE_PRODUCT):
            button.click()
            self.click_button(ACTION_OK)
            self.check_page_loaded()


