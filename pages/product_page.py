import allure

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

BUTTON_ADD_TO_CART = ('id', 'product-addtocart-button')

ADD_TO_COMPARE_LINK = ('xpath', '//a[@data-role="add-to-links"]')
CORPORATION_MESSAGE = ('css selector', 'div[data-bind^="html: "]')
CORPORATION_LIST_LINK = ('xpath', '//a[text()="comparison list"]')

ADD_TO_WISH_LIST = ('xpath', '(//a[@data-action="add-to-wishlist"])[1]')


class ProductPage(BasePage):
    URL = random_product_url

    @allure.step("Get product name")
    def get_product_name(self):
        return self.get_text(PRODUCT_NAME)

    @allure.step("Get product price")
    def get_product_price(self):
        return float(self.get_text(PRODUCT_PRICE).replace(',', '').replace('$', ''))

    @allure.step("Filling in product parameters and return it (connect with product type)")
    def filling_in_product_parameters(self):
        import random
        product_parameters = [None, None, None]
        try:
            size_element = random.choice(self.find_all(PRODUCT_ALL_SIZES_BUTTON))
            product_parameters[0] = size_element.text
            size_element.click()
        except:
            pass
        try:
            color_element = random.choice(self.find_all(PRODUCT_ALL_COLOR_BUTTON))
            product_parameters[1] = color_element.text
            color_element.click()
        except:
            pass
        try:
            qty_number = random.randint(1, 10000)
            product_parameters[2] = qty_number
            self.field_form(INPUT_QTY, qty_number)
        except:
            pass
        return product_parameters

    @allure.step("Click to 'add to cart'")
    def click_add_to_cart(self):
        self.click_button(BUTTON_ADD_TO_CART)

    @allure.step("Click to 'add to compare'")
    def click_add_to_compare_link(self):
        self.click_button(ADD_TO_COMPARE_LINK)

    @allure.step("Click to 'add to wish list'")
    def click_add_to_wish_list(self):
        self.click_button(ADD_TO_WISH_LIST)

    @allure.step("Click to corporation list link")
    def click_corporation_list_link(self):
        self.click_button(CORPORATION_LIST_LINK)

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
        self.check_element_visibility_(CORPORATION_MESSAGE)
        success_text = self.get_text(CORPORATION_MESSAGE)
        return f'You added product {product_name} to the comparison list.' == success_text
