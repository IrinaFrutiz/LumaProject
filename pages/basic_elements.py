import allure

from base.base_page import BasePage


CREATE_AN_ACCOUNT_LINK = ("xpath", "//div[@class ='panel header']//a[text()='Create an Account']")

BUTTON_CART = ('css selector', '.showcart')
CART_ITEM_NUMBER = ('css selector', '.counter-number')
CART_EMPTINESS = ('css selector', '.subtitle.empty')
CART_ITEM_NUMBER_UPLOADER = ('css selector', '._block-content-loading')

CART_EMPTY_TEXT = ('xpath', '//strong[text()="You have no items in your shopping cart."]')
CART_CLOSE = ('id', 'btn-minicart-close')

WOMEN_CATEGORY = ('id', 'ui-id-4')
TOPS_CATEGORY = ('id', 'ui-id-9')
TREES_CATEGORY = ('id', 'ui-id-13')


class BasicElements(BasePage):
    URL = None

    @allure.step("Open Any Page")
    def open_url(self, url):
        self.browser.get(url)

    @allure.step("Check the cart uploaded")
    def check_cart_uploaded(self):
        self.check_element_visibility_(CART_ITEM_NUMBER)
        self.check_element_not_visible_(CART_ITEM_NUMBER_UPLOADER)
        self.check_element_not_visible_(CART_EMPTINESS)

    @allure.step("Click the Cart button")
    def click_cart(self):
        self.click_button(BUTTON_CART)
        try:
            while self.check_element_visibility_(CART_EMPTY_TEXT):
                self.click_button(CART_CLOSE)
                self.click_button(BUTTON_CART)
        except:
            pass


    # need to go to other page
    @allure.step("Go to Women -> Tops -> Trees")
    def go_to_women_tops_trees(self):
        woman = self.check_element_visibility_(WOMEN_CATEGORY)
        tops = self.find(TOPS_CATEGORY)
        trees = self.find(TREES_CATEGORY)
        self.action.move_to_element(woman)\
            .move_to_element(tops)\
            .move_to_element(trees)\
            .click(trees)\
            .perform()

    @allure.step("Click The Create An Account Link")
    def click_create_an_account_link(self):
        self.click_button(CREATE_AN_ACCOUNT_LINK)

    @allure.step("Check Create An Account Link Visibility")
    def check_create_an_account_link_visibility(self):
        return bool(self.check_element_visibility_(CREATE_AN_ACCOUNT_LINK))
