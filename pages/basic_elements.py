import allure

from base.base_page import BasePage

CREATE_AN_ACCOUNT_LINK = ("xpath", "//div[@class ='panel header']//a[text()='Create an Account']")
WOMEN_CATEGORY = ('id', 'ui-id-4')
TOPS_CATEGORY = ('id', 'ui-id-9')
TREES_CATEGORY = ('id', 'ui-id-13')


class BasicElements(BasePage):
    URL = None

    @allure.step("Open Any Page")
    def open_url(self, url):
        self.browser.get(url)

    @allure.step("Go to Women -> Tops -> Trees")
    def go_to_women_tops_trees(self):
        woman = self.find(WOMEN_CATEGORY)
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
