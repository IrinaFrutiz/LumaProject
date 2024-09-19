import allure

from base.base_page import BasePage
from data.links import CORPORATION_LIST_URL

ALL_PRODUCTS = ('xpath', '//td[@data-th="Product"]')


class CorporationLIstPage(BasePage):
    URL = CORPORATION_LIST_URL

    @allure.step("Return Number of products on the corporation list page")
    def check_number_of_products_on_page(self):
        return len(self.find_all(ALL_PRODUCTS))
