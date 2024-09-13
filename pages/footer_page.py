import allure

from base.base_page import BasePage

NOTES_LINK = ('xpath', "//a[contains(@href,'notes_promotion')]")
API_TESTING_LINK = ('xpath', "//a[contains(@href,'API_Testing_Promo')]")
WRITE_FOR_US_LINK = ('xpath', "//a[contains(@href,'write4us')]")
SUBSCRIBE_LINK = ('xpath', "//a[contains(@href,'email_subscribe')]")
SEARCH_TERMS_LINK = ('xpath', "//a[text()='Search Terms']")
PRIVACY_COOKIES_LINK = ('xpath', "//a[text()='Privacy and Cookie Policy']")
ADVANCED_SEARCH_LINK = ('xpath', "//a[text()='Advanced Search']")
ORDERS_RETURNS_LINK = ('xpath', "//a[text()='Orders and Returns']")


class FooterPage(BasePage):
    URL = None

    @allure.step("Check the footer's Notes link")
    def check_notes_link(self):
        return self.check_element_visibility_(NOTES_LINK)

    @allure.step("Check the footer's API Testing link")
    def check_api_testing_link(self):
        return self.check_element_visibility_(API_TESTING_LINK)

    @allure.step("Check the footer's Write for us link")
    def check_write_for_us_link(self):
        return self.check_element_visibility_(WRITE_FOR_US_LINK)

    @allure.step("Check the footer's Subscribe link")
    def check_subscribe_link(self):
        return self.check_element_visibility_(SUBSCRIBE_LINK)

    @allure.step("Check the footer's Search terms link")
    def check_search_terms_link(self):
        return self.check_element_visibility_(SEARCH_TERMS_LINK)

    @allure.step("Check the footer's Privacy policy and cookies link")
    def check_privacy_cookies_link(self):
        return self.check_element_visibility_(PRIVACY_COOKIES_LINK)

    @allure.step("Check the footer's Advanced search link")
    def check_advanced_search_link(self):
        return self.check_element_visibility_(ADVANCED_SEARCH_LINK)

    @allure.step("Check the footer's Orders and returns link")
    def check_orders_returns_link(self):
        return self.check_element_visibility_(ORDERS_RETURNS_LINK)
