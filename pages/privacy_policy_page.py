import allure

from base.base_page import BasePage
from data.links import PRIVACY_POLICY_PAGE_URL, expected_anchor_urls

LUMA_SECURITY_ANCHOR_LINK = ("xpath", "//a[text()='Luma Security']")
LUMA_PRIVACY_POLICY_ANCHOR_LINK = ("xpath", "//a[text()='Luma Privacy Policy']")
THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = ("xpath", "//a[text()='The Information We Collect']")
HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = ("xpath", "//a[text()='How We Use The Information We Collect']")
SECURITY_ANCHOR_LINK = ("xpath", "//a[text()='Security']")
OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK = ("xpath",
                                                          "//a[text()='Others With Whom We Share Your Information.']")
YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = \
    ("xpath", "//a[text()='Your Choices Regarding Use Of The Information We Collect']")
YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK = ("xpath", "//a[text()='Your California Privacy Rights']")
COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK = ("xpath",
                                                       "//a[text()='Cookies, Web Beacons, and How We Use Them']")
LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK = ("xpath",
                                          "//li[@class='item']//a[contains(text(),'List of cookies we collect')]")
ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK = ("xpath", "//a[text()='Online Account Registration']")
EMAILS_ANCHOR_LINK = ("xpath", "//a[text()='Emails']")
ACCEPTANCE_ANCHOR_LINK = ("xpath", "//a[text()='Acceptance']")
QUESTIONS_FOR_LUMA_ANCHOR_LINK = ("xpath", "//a[text()='Questions for Luma?']")
LEFT_NAV_LINKS = ("xpath", "//*[@id='privacy-policy-nav-content']/ul/li")


class PrivacyPolicyPage(BasePage):
    URL = PRIVACY_POLICY_PAGE_URL

    @allure.step("Check 'Luma Security' Anchor Link Visibility")
    def check_luma_security_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LUMA_SECURITY_ANCHOR_LINK))

    @allure.step("Check 'Luma Privacy Policy' Anchor Link Visibility")
    def check_luma_privacy_policy_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LUMA_PRIVACY_POLICY_ANCHOR_LINK))

    @allure.step("Check 'The Information We Collect' Anchor Link Visibility")
    def check_the_information_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    @allure.step("Check 'How We Use The Information We Collect' Anchor Link Visibility")
    def check_how_we_use_the_information_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    @allure.step("Check 'Security' Anchor Link Visibility")
    def check_security_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(SECURITY_ANCHOR_LINK))

    @allure.step("Check 'Others With Whom We Share Your Information' Anchor Link Visibility")
    def check_others_with_whom_we_share_your_information_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK))

    @allure.step("Check 'Your choices regarding use of the information we collect' Anchor Link Visibility")
    def check_choices_regarding_information_anchor_link_visibility(self):
        return bool(
            self.check_element_visibility_(YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    @allure.step("Check 'Your California Privacy Rights' Anchor Link Visibility")
    def check_your_california_privacy_rights_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK))

    @allure.step("Check 'Cookies, Web Beacons, And How We Use Them' Anchor Link Visibility")
    def check_cookies_web_beacons_and_how_we_use_them_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK))

    @allure.step("Check 'List Of Cookies We Collect' Anchor Link Visibility")
    def check_list_of_cookies_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK))

    @allure.step("Check 'Online Account Registration' Anchor Link Visibility")
    def check_online_account_registration_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK))

    @allure.step("Check 'Emails' Anchor Link Visibility")
    def check_emails_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(EMAILS_ANCHOR_LINK))

    @allure.step("Check 'Acceptance' Anchor Link Visibility")
    def check_acceptance_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(ACCEPTANCE_ANCHOR_LINK))

    @allure.step("Check 'Questions For Luma?' Anchor Link Visibility")
    def check_questions_for_luma_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(QUESTIONS_FOR_LUMA_ANCHOR_LINK))

    @allure.step("Check if element is highlighted")
    def check_element_highlighted_(self, locator):
        background_color = self.find(locator).value_of_css_property('background-color')
        expected_color = 'rgba(232, 232, 232, 1)'
        return background_color == expected_color

    @allure.step("Check 'Luma Security' Anchor Link Is Highlighted")
    def check_luma_security_anchor_link_is_highlighted_(self):
        self.hover(LUMA_SECURITY_ANCHOR_LINK)
        return self.check_element_highlighted_(LUMA_SECURITY_ANCHOR_LINK)

    @allure.step("Check 'Luma Privacy Policy' Anchor Link Is Highlighted")
    def check_luma_privacy_policy_anchor_link_is_highlighted_(self):
        self.hover(LUMA_PRIVACY_POLICY_ANCHOR_LINK)
        return self.check_element_highlighted_(LUMA_PRIVACY_POLICY_ANCHOR_LINK)

    @allure.step("Check 'The Information We Collect' Anchor Link Is Highlighted")
    def check_the_information_we_collect_anchor_link_is_highlighted_(self):
        self.hover(THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)
        return self.check_element_highlighted_(THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)

    @allure.step("Check 'How We Use The Information We Collect' Anchor Link Is Highlighted")
    def check_how_we_use_the_information_we_collect_anchor_link_is_highlighted_(self):
        self.hover(HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)
        return self.check_element_highlighted_(HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)

    @allure.step("Check 'Security' Anchor Link Is Highlighted")
    def check_security_anchor_link_is_highlighted_(self):
        self.hover(SECURITY_ANCHOR_LINK)
        return self.check_element_highlighted_(SECURITY_ANCHOR_LINK)

    @allure.step("Check 'Others With Whom We Share Your Information' Anchor Link Is Highlighted")
    def check_others_with_whom_we_share_information_anchor_link_is_highlighted_(self):
        self.hover(OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK)
        return self.check_element_highlighted_(OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK)

    @allure.step("Check 'Your Choices Regarding Use Of The Information We Collect Anchor Link Is Highlighted")
    def check_choices_regarding_information_anchor_link_is_highlighted_(self):
        self.hover(YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)
        return self.check_element_highlighted_(YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK)

    @allure.step("Check 'Your California Privacy Rights Anchor Link Is Highlighted")
    def check_your_california_privacy_rights_anchor_link_is_highlighted_(self):
        self.hover(YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK)
        return self.check_element_highlighted_(YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK)

    @allure.step("Check 'Cookies, Web Beacons, and How We Use Them Anchor Link Is Highlighted")
    def check_cookies_web_beacons_and_how_we_use_them_anchor_link_is_highlighted_(self):
        self.hover(COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK)
        return self.check_element_highlighted_(COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK)

    @allure.step("Check 'List Of Cookies We Collect Anchor Link Is Highlighted")
    def check_list_of_cookies_we_collect_anchor_link_is_highlighted_(self):
        self.hover(LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK)
        return self.check_element_highlighted_(LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK)

    @allure.step("Check 'Online Account Registration Anchor Link Is Highlighted")
    def check_online_account_registration_anchor_link_is_highlighted_(self):
        self.hover(ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK)
        return self.check_element_highlighted_(ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK)

    @allure.step("Check 'Emails' Anchor Link Is Highlighted")
    def check_emails_anchor_link_is_highlighted_(self):
        self.hover(EMAILS_ANCHOR_LINK)
        return self.check_element_highlighted_(EMAILS_ANCHOR_LINK)

    @allure.step("Check 'Acceptance' Anchor Link Is Highlighted")
    def check_acceptance_anchor_link_is_highlighted_(self):
        self.hover(ACCEPTANCE_ANCHOR_LINK)
        return self.check_element_highlighted_(ACCEPTANCE_ANCHOR_LINK)

    @allure.step("Check 'Questions for Luma?' Anchor Link Is Highlighted")
    def check_questions_for_luma_anchor_link_is_highlighted_(self):
        self.hover(QUESTIONS_FOR_LUMA_ANCHOR_LINK)
        return self.check_element_highlighted_(QUESTIONS_FOR_LUMA_ANCHOR_LINK)

    @allure.step("Verify left nav anchor links on Privacy Policy page are working")
    def check_privacy_left_nav_anchor_links_work(self):
        for i, link in enumerate(self.find_all(LEFT_NAV_LINKS)):
            link.click()
            expected_url = expected_anchor_urls.get(f"link{i + 1}")
            if expected_url == self.browser.current_url:
                return self.check_url_is_(expected_url)
            else:
                return False
