import allure
import pytest

from base.base_test import BaseTest
from data.links import *


class TestBasicElements(BaseTest):
    @allure.feature('Basic Elements')
    @allure.title("The 'Create an Account' link is visible and clickable on multiple pages")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-150')
    @pytest.mark.parametrize('url',
                             [
                                 MAIN_PAGE_URL, WOMEN_PAGE_URL, MEN_PAGE_URL, GEAR_PAGE_URL, YOGA_URL
                             ]
                             )
    def test_check_link_create_account_is_visible_and_clickable(self, url):
        self.basic_elements.open_url(url)
        assert self.basic_elements.check_create_an_account_link_visibility(), \
            'Element is not visible'
        self.basic_elements.click_create_an_account_link()
        assert self.basic_elements.check_url_is_(CREATE_ACCOUNT_URL), \
            'Wrong URL'
        assert self.basic_elements.check_page_title_is_('Create New Customer Account'), \
            'Wrong title'
        assert self.create_account_page.check_btn_create_an_account_displays(), \
            'Button Create an Account is not displaying'
