import allure

from base.base_page import BasePage

CREATE_AN_ACCOUNT_LINK = ("xpath", "//div[@class ='panel header']//a[text()='Create an Account']")


class BasicElements(BasePage):
    URL = None

    @allure.step("Open Any Page")
    def open_url(self, url):
        self.browser.get(url)

    @allure.step("Click The Create An Account Link")
    def click_create_an_account_link(self):
        self.click_button(CREATE_AN_ACCOUNT_LINK)

    @allure.step("Check Create An Account Link Visibility")
    def check_create_an_account_link_visibility(self):
        return bool(self.check_element_visibility_(CREATE_AN_ACCOUNT_LINK))
