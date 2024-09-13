import allure
import pytest

from base.base_test import BaseTest
from data.links import *
from pages.footer_page import *


class TestFooter(BaseTest):
    @allure.feature('Footer')
    @allure.title("Verify the footer of every page on the website contains the list of links")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-49')
    @pytest.mark.parametrize('url',
                             [
                                 MAIN_PAGE_URL, WHATS_NEW_PAGE_URL, WOMEN_PAGE_URL, MEN_PAGE_URL,
                                 GEAR_PAGE_URL, TRAINING_URL, SALE_URL
                             ]
                             )
    def test_verify_footer_links(self, url):
        self.basic_elements.open_url(url)
        assert self.footer_page.check_notes_link(), \
            'Notes link not visible'
        assert self.footer_page.check_api_testing_link(), \
            'API Testing link not visible'
        assert self.footer_page.check_write_for_us_link(), \
            'Write for us link not visible'
        assert self.footer_page.check_subscribe_link(), \
            'Subscribe link not visible'
        assert self.footer_page.check_search_terms_link(), \
            'Search terms link not visible'
        assert self.footer_page.check_privacy_cookies_link(), \
            'Privacy policy and cookies link not visible'
        assert self.footer_page.check_advanced_search_link(), \
            'Advanced search link not visible'
        assert self.footer_page.check_orders_returns_link(), \
            'Orders and returns link not visible'
