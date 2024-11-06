import allure
from selenium.common import TimeoutException

from pages.basic_elements import BasicElements

NUMBER_ITEMS_IN_CART = ('css selector', 'span.count')
EMPTY_CART = ('css selector', '.subtitle.empty')
CART_SUBTOTAL = ('css selector', '.subtotal span.price')
CART_PRODUCTS_NAMES = ('xpath',
                       '//ol[@id="mini-cart"]//a[contains(@data-bind, "name")][not(@class="product-item-photo")]')
BUTTON_DELETE = ('css selector', 'a.delete')
BUTTON_DELETE_ACCEPT = ('css selector', '.action-accept')


class MiniCartPage(BasicElements):
    URL = None

    @allure.step("Get number of the items in the cart")
    def get_number_items_in_cart(self):
        return int(self.get_text(NUMBER_ITEMS_IN_CART))

    @allure.step("Get subtotal in the cart")
    def get_subtotal_in_cart(self):
        return float(self.get_text(CART_SUBTOTAL)[1:].replace(',', ''))

    @allure.step("Get the product's name in the cart")
    def get_list_products_names_in_cart(self):
        return self.get_all_text(CART_PRODUCTS_NAMES)

    @allure.step("Check the product with some name is in the cart")
    def check_cart_have_product_(self, name):
        return name in self.get_list_products_names_in_cart()

    @allure.step("Check subtotal is the product price * qty")
    def check_subtotal_(self, product_price, qty):
        return self.get_subtotal_in_cart() == round(product_price * qty, 2)

    @allure.step("Check number in the cart is the same as qty")
    def check_product_number_(self, qty):
        return self.get_number_items_in_cart() == qty

    @allure.step("Delete all products from mini cart")
    def delete_all_product(self):
        try:
            self.check_cart_uploaded()
        except TimeoutException:
            pass
        if self.get_products_numbers_in_cart() != '':
            self.click_cart()
            for button in self.find_all(BUTTON_DELETE):
                button.click()
                self.click_button(BUTTON_DELETE_ACCEPT)
                self.check_cart_uploaded()
