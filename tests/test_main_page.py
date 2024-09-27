import allure
import pytest

from base.base_test import BaseTest


class TestMainPage(BaseTest):
    @allure.feature('Main Page')
    @allure.title("Check Main URL after go to it")
    @allure.link('some link')
    @pytest.mark.smoke
    def test_check_url(self):
        self.main_page.open()
        assert self.main_page.check_url_is_(self.main_page.URL), \
            f"Current URL is not equal {self.main_page.URL}"


class TestLoggedUserMainPage(BaseTest):
    @pytest.fixture(scope="function")
    def user_login(self):
        self.login_page.open()
        self.login_page.user_login()

    @allure.feature('Main Page')
    @allure.title("Check Main URL after go to it")
    @allure.link('some link')
    def test_user_check_url(self, user_login):
        self.main_page.open()
        assert self.main_page.check_url_is_(self.main_page.URL)

    @allure.feature('Main Page')
    @allure.title('Check page redirection after Men menu item click' )
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-88')
    def test_men_page_redirect(self, user_login):
        self.main_page.open()
        self.main_page.click_navigation_menu_item_men()
        assert self.main_page.check_url_is_(self.men_page.URL), \
            'Target page URL is not correct'
