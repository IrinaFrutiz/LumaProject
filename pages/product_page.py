import allure
from selenium.common import TimeoutException

from base.base_page import BasePage
from data.links import random_product_url

PRODUCT_NAME = ('xpath', '//span[@itemprop="name"]')
PRODUCT_PRICE = ('css selector', '.product-info-price .price')
PRODUCT_PHOTO = ('css selector', '.fotorama__img')

PRODUCT_SIZE_BLOCK = ('xpath', '//div[@attribute-code="size"]')
PRODUCT_ALL_SIZES_BUTTON = ('xpath', '//div[@aria-labelledby="option-label-size-143"]/*')

PRODUCT_COLOR_BLOCK = ('xpath', '//div[@attribute-code="color"]')
PRODUCT_ALL_COLOR_BUTTON = ('xpath', '//div[@aria-labelledby="option-label-color-93"]/*')

PRODUCT_QTY_BLOCK = ('css selector', '.field.qty')
INPUT_QTY = ('id', 'qty')

BTN_ADD_TO_CART = ('id', 'product-addtocart-button')

ADD_TO_COMPARE_LINK = ('xpath', '//a[@data-role="add-to-links"]')
CORPORATION_MESSAGE = ('css selector', 'div[data-bind^="html: "]')
CORPORATION_LIST_LINK = ('xpath', '//a[text()="comparison list"]')
PRODUCT_SIZE_OPTIONS = ('xpath', '//div[@class="swatch-option text"]')
PRODUCT_COLOR_OPTIONS = ('xpath', '//div[@class="swatch-option color"]')

ADD_TO_WISH_LIST = ('xpath', '(//a[@data-action="add-to-wishlist"])[1]')

BTN_DETAILS = ('id', 'tab-label-description-title')
DETAILS_TEXT = ('id', 'description')
BTN_MORE_INFORMATION = ('id', 'tab-label-additional-title')
MORE_INFORMATION_TEXT = ('id', 'additional')
BTN_REVIEWS = ('id', 'tab-label-reviews-title')
REVIEWS_TEXT = ('id', 'reviews')


class ProductPage(BasePage):
    URL = random_product_url

    @allure.step("Get product name")
    def get_product_name(self):
        return self.get_text(PRODUCT_NAME)

    @allure.step("Get product price")
    def get_product_price(self):
        return float(self.get_text(PRODUCT_PRICE).replace(',', '').replace('$', ''))

    @allure.step("Find all sizes options")
    def get_all_sizes(self):
        return self.check_all_visibility_(PRODUCT_SIZE_OPTIONS)

    @allure.step("Find all colors options")
    def get_all_colors(self):
        return self.check_all_visibility_(PRODUCT_COLOR_OPTIONS)

    @allure.step("Filling in product parameters and return it (connect with product type)")
    def filling_in_product_parameters(self):
        import random
        product_parameters = [None, None, None]
        try:
            size_element = random.choice(self.find_all(PRODUCT_ALL_SIZES_BUTTON))
            product_parameters[0] = size_element.text
            size_element.click()
        except TimeoutException:
            pass
        try:
            color_element = random.choice(self.find_all(PRODUCT_ALL_COLOR_BUTTON))
            product_parameters[1] = color_element.text
            color_element.click()
        except TimeoutException:
            pass
        try:
            qty_number = random.randint(1, 10000)
            product_parameters[2] = qty_number
            self.field_form(INPUT_QTY, qty_number)
        except TimeoutException:
            pass
        return product_parameters

    @allure.step("Click to 'add to cart'")
    def click_add_to_cart(self):
        self.click_button(BTN_ADD_TO_CART)

    @allure.step("Click to 'add to compare'")
    def click_add_to_compare_link(self):
        self.click_button(ADD_TO_COMPARE_LINK)

    @allure.step("Click to 'add to wish list'")
    def click_add_to_wish_list(self):
        self.click_button(ADD_TO_WISH_LIST)

    @allure.step("Click to corporation list link")
    def click_corporation_list_link(self):
        self.click_button(CORPORATION_LIST_LINK)

    @allure.step("Click to More Information")
    def click_more_information(self):
        self.click_button(BTN_MORE_INFORMATION)

    @allure.step("Check product name is presence")
    def check_product_name_presence(self):
        return self.check_element_presence(PRODUCT_NAME) is not None

    @allure.step("Check product price is presence")
    def check_product_price_presence(self):
        return self.check_element_presence(PRODUCT_PRICE) is not None

    @allure.step("Check product photo is presence")
    def check_product_photo_presence(self):
        return self.check_element_presence(PRODUCT_PHOTO) is not None

    @allure.step("The message of success 'added to the comparison list' is displayed. ")
    def check_message_that_product_added_to_the_comparison_list(self):
        product_name = self.get_product_name()
        self.check_page_loaded()
        success_text = self.get_text(CORPORATION_MESSAGE)
        return f'You added product {product_name} to the comparison list.' == success_text

    @allure.step("The text in more information block is presence")
    def check_more_information_text_clickable(self):
        return self.check_element_clickability_(MORE_INFORMATION_TEXT) is not None

    @allure.step("Check if product has size and color, choose random size and color and add to cart")
    def if_size_and_color_pick_random_size_and_color_add_to_cart(self):
        try:
            self.click_add_to_cart()

            if self.get_all_sizes() and self.get_all_colors():
                for _ in self.get_all_sizes():
                    self.click_to_random_element(PRODUCT_SIZE_OPTIONS)
                    break
                for _ in self.get_all_colors():
                    self.click_to_random_element(PRODUCT_COLOR_OPTIONS)
                    break
                self.click_add_to_cart()
        except TimeoutException:
            pass
