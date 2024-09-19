import allure

from base.base_page import BasePage
from data.links import random_product_url

ADD_TO_COMPARE_LINK = ('xpath', '//a[@data-role="add-to-links"]')
PRODUCT_NAME = ('xpath', '//span[@itemprop="name"]')
CORPORATION_MESSAGE = ('css selector', 'div[data-bind^="html: "]')
CORPORATION_LIST_LINK = ('xpath', '//a[text()="comparison list"]')


class ProductPage(BasePage):
    URL = random_product_url

    @allure.step("Click to 'add to compare'")
    def click_add_to_compare_link(self):
        self.click_button(ADD_TO_COMPARE_LINK)

    @allure.step("Click to corporation list link")
    def click_corporation_list_link(self):
        self.click_button(CORPORATION_LIST_LINK)

    @allure.step("The message of success 'added to the comparison list' is displayed. ")
    def check_message_that_product_added_to_the_comparison_list(self):
        product_name = self.get_text(PRODUCT_NAME)
        self.check_element_visibility_(CORPORATION_MESSAGE)
        success_text = self.get_text(CORPORATION_MESSAGE)
        return f'You added product {product_name} to the comparison list.' == success_text

