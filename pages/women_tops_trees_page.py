import allure

from base.base_page import BasePage
from data.links import WOMEN_TOPS_TEES_URL

ALL_PRODUCTS_NAME = ('css selector', '.product-item-name a')


class WomenTopsTreesPage(BasePage):
    URL = WOMEN_TOPS_TEES_URL

    @allure.step("Test choose one of the product on the page and go there")
    def go_to_random_product(self):
        self.click_to_random_element(ALL_PRODUCTS_NAME)
