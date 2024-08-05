import allure
import pytest

from base.base_test import BaseTest
from data.links import MAIN_PAGE_URL


class TestMainPage(BaseTest):
    @allure.feature('Main Page')
    @allure.title("Check Main URL after go to it")
    @allure.link('some link')
    @pytest.mark.smoke
    def test_check_url(self):
        self.main_page.open()
        # вариант адын: писать ассерты в тесте
        assert self.main_page.get_url() == MAIN_PAGE_URL, \
            f"Current URL {self.main_page.get_url()} is not equal {MAIN_PAGE_URL}"
        # вариант два: писать ассерты в функциях
        self.main_page.check_url_(MAIN_PAGE_URL)
        # вариант 3: функция возвращает только тру/фолс
        assert self.main_page.check_url_is_(MAIN_PAGE_URL), \
            f"Current URL is not equal {MAIN_PAGE_URL}"

    def test_test_ci(self):
        assert 2 == 2, \
            "Something went wrong"


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
        self.main_page.check_url_(MAIN_PAGE_URL)
