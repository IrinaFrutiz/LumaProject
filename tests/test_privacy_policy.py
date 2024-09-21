import allure

from base.base_test import BaseTest
from data.links import *


class TestPrivacyPolicyPage(BaseTest):
    @allure.feature('Privacy and Cookie Policy')
    @allure.title("All links in the block on the left are visible")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-18')
    def test_verify_left_nav_links(self):
        self.privacy_policy_page.open()
        assert self.privacy_policy_page.check_url_is_(PRIVACY_POLICY_PAGE_URL), \
            'Wrong URL'
        assert self.privacy_policy_page.check_page_title_is_('Privacy Policy'), \
            'Wrong title'
        assert self.privacy_policy_page.check_luma_security_anchor_link_visibility(), \
            'Luma Security anchor link is not visible'
        assert self.privacy_policy_page.check_luma_privacy_policy_anchor_link_visibility(), \
            'Luma Privacy Policy anchor link is not visible'
        assert self.privacy_policy_page.check_the_information_we_collect_anchor_link_visibility(), \
            'The Information We Collect anchor link is not visible'
        assert self.privacy_policy_page.check_how_we_use_the_information_we_collect_anchor_link_visibility(), \
            'How We Use The Information We Collect anchor link is not visible'
        assert self.privacy_policy_page.check_security_anchor_link_visibility(), \
            'Security anchor link is not visible'
        assert self.privacy_policy_page.check_others_with_whom_we_share_your_information_anchor_link_visibility(), \
            'Others With Whom We Share Your Information anchor link is not visible'
        assert self.privacy_policy_page.check_choices_regarding_information_anchor_link_visibility(), \
            'Your Choices Regarding Use Of The Information We Collect anchor link is not visible'
        assert self.privacy_policy_page.check_your_california_privacy_rights_anchor_link_visibility(), \
            'Your California Privacy Rights anchor link is not visible'
        assert self.privacy_policy_page.check_cookies_web_beacons_and_how_we_use_them_anchor_link_visibility(), \
            'Cookies, Web Beacons, and How We Use Them anchor link is not visible'
        assert self.privacy_policy_page.check_list_of_cookies_we_collect_anchor_link_visibility(), \
            'List Of Cookies We Collect anchor link is not visible'
        assert self.privacy_policy_page.check_online_account_registration_anchor_link_visibility(), \
            'Online Account Registration anchor link is not visible'
        assert self.privacy_policy_page.check_emails_anchor_link_visibility(), \
            'Emails anchor link is not visible'
        assert self.privacy_policy_page.check_acceptance_anchor_link_visibility(), \
            'Acceptance anchor link is not visible'
        assert self.privacy_policy_page.check_questions_for_luma_anchor_link_visibility(), \
            'Questions For Luma? anchor link is not visible'

    @allure.feature('Privacy and Cookie Policy')
    @allure.title("Verify link highlight after hovering in left-side navigation block")
    @allure.link('https://pola-gor.atlassian.net/browse/LUM-17')
    def test_verify_left_nav_links_highlighted_on_mouse_over(self):
        self.privacy_policy_page.open()
        assert self.privacy_policy_page.check_url_is_(PRIVACY_POLICY_PAGE_URL), \
            'Wrong URL'
        assert self.privacy_policy_page.check_page_title_is_('Privacy Policy'), \
            'Wrong title'
        assert self.privacy_policy_page.check_luma_security_anchor_link_is_highlighted_(), \
            'Luma Security anchor link is not highlighted'
        assert self.privacy_policy_page.check_luma_privacy_policy_anchor_link_is_highlighted_(), \
            'Luma Privacy Policy anchor link is not highlighted'
        assert self.privacy_policy_page.check_the_information_we_collect_anchor_link_is_highlighted_(), \
            'The Information We Collect anchor link is not highlighted'
        assert self.privacy_policy_page.check_how_we_use_the_information_we_collect_anchor_link_is_highlighted_(), \
            'How We Use The Information We Collect anchor link is not highlighted'
        assert self.privacy_policy_page.check_security_anchor_link_is_highlighted_(), \
            'Security anchor link is not highlighted'
        assert self.privacy_policy_page.check_others_with_whom_we_share_information_anchor_link_is_highlighted_(), \
            'Others With Whom We Share Your Information anchor link is not highlighted'
        assert (self.privacy_policy_page.check_choices_regarding_information_anchor_link_is_highlighted_()), \
            'Your Choices Regarding Use Of The Information We Collect anchor link is not highlighted'
        assert self.privacy_policy_page.check_your_california_privacy_rights_anchor_link_is_highlighted_(), \
            'Your California Privacy Rights anchor link is not highlighted'
        assert self.privacy_policy_page.check_cookies_web_beacons_and_how_we_use_them_anchor_link_is_highlighted_(), \
            'Cookies, Web Beacons, and How We Use Them anchor link is not highlighted'
        assert self.privacy_policy_page.check_list_of_cookies_we_collect_anchor_link_is_highlighted_(), \
            'List Of Cookies We Collect anchor link is not highlighted'
        assert self.privacy_policy_page.check_online_account_registration_anchor_link_is_highlighted_, \
            'Online Account Registration anchor link is not highlighted'
        assert self.privacy_policy_page.check_emails_anchor_link_is_highlighted_(), \
            'Emails anchor link is not highlighted'
        assert self.privacy_policy_page.check_acceptance_anchor_link_is_highlighted_(), \
            'Acceptance anchor link is not highlighted'
        assert self.privacy_policy_page.check_questions_for_luma_anchor_link_is_highlighted_(), \
            'Questions For Luma? anchor link is not highlighted'
