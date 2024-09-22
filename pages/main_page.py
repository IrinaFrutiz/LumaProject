import allure

from base.base_page import BasePage
from data.links import MAIN_PAGE_URL

ARGUS_ITEM = ('xpath', '(//li[@class="product-item"])[3]')
ARGUS_SIZE_TAG_M = ('xpath', '(//li[@class="product-item"])[3]//div[@option-label="M"]')
ARGUS_COLOR_TAG_GRAY = ('xpath', '(//li[@class="product-item"])[3]//div[@option-label="Gray"]')
ARGUS_ADD_BTN = ('xpath', '(//button[@title="Add to Cart"])[3]')

SUCCESS_MSG_ALERT = ('xpath', '//div[@role="alert"]')
SUCCESS_MSG_TEXT = 'You added Argus All-Weather Tank to your shopping cart.'


class MainPage(BasePage):
    URL = MAIN_PAGE_URL

    @allure.step("Find Argus Tank Size M")
    def find_argus_size_m(self):
        return self.check_element_visibility_(ARGUS_SIZE_TAG_M)

    @allure.step("Find Argus Tank Color Gray")
    def find_argus_color_gray(self):
        return self.check_element_visibility_(ARGUS_COLOR_TAG_GRAY)

    @allure.step("Find Argus Tank Add To Cart Button")
    def click_argus_add_to_cart_btn(self):
        return self.click_button(ARGUS_ADD_BTN)

    @allure.step("Find Success Message Text")
    def find_success_msg_text(self):
        return self.check_element_visibility_(SUCCESS_MSG_ALERT)

    @allure.step("Hover Over Argus Item Card")
    def hover_over_argus_item(self):
        self.hover(ARGUS_ITEM)

    @allure.step("Choose Argus Size M")
    def choose_argus_size_m(self):
        self.find_argus_size_m().click()

    @allure.step("Choose Argus Color Gray")
    def choose_argus_color_gray(self):
        self.find_argus_color_gray().click()
