import allure

from base.base_page import BasePage
from data.links import PRIVACY_POLICY_PAGE_URL

LUMA_SECURITY_ANCHOR_LINK = ("xpath", "//a[text()='Luma Security']")
LUMA_PRIVACY_POLICY_ANCHOR_LINK = ("xpath", "//a[text()='Luma Privacy Policy']")
THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = ("xpath", "//a[text()='The Information We Collect']")
HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = ("xpath", "//a[text()='How We Use The Information We Collect']")
SECURITY_ANCHOR_LINK = ("xpath", "//a[text()='Security']")
OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK = ("xpath",
                                                          "//a[text()='Others With Whom We Share Your Information.']")
YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK = ("xpath",
                                                                        "//a[text()='Your Choices Regarding Use Of The Information We Collect']")
YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK = ("xpath", "//a[text()='Your California Privacy Rights']")
COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK = ("xpath",
                                                       "//a[text()='Cookies, Web Beacons, and How We Use Them']")
LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK = ("xpath", "//a[text()='List of cookies we collect']")
ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK = ("xpath", "//a[text()='Online Account Registration']")
EMAILS_ANCHOR_LINK = ("xpath", "//a[text()='Emails']")
ACCEPTANCE_ANCHOR_LINK = ("xpath", "//a[text()='Acceptance']")
QUESTIONS_FOR_LUMA_ANCHOR_LINK = ("xpath", "//a[text()='Questions for Luma?']")


class PrivacyPolicyPage(BasePage):
    URL = PRIVACY_POLICY_PAGE_URL

    @allure.step("Check Luma Security Anchor Link Visibility")
    def check_luma_security_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LUMA_SECURITY_ANCHOR_LINK))

    def check_luma_privacy_policy_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LUMA_PRIVACY_POLICY_ANCHOR_LINK))

    def check_the_information_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    def check_how_we_use_the_information_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(HOW_WE_USE_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    def check_security_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(SECURITY_ANCHOR_LINK))

    def check_others_with_whom_we_share_your_information_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION_ANCHOR_LINK))

    def check_your_choices_regarding_use_of_the_information_we_collect_anchor_link_visibility(self):
        return bool(
            self.check_element_visibility_(YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_ANCHOR_LINK))

    def check_your_california_privacy_rights_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(YOUR_CALIFORNIA_PRIVACY_RIGHTS_ANCHOR_LINK))

    def check_cookies_web_beacons_and_how_we_use_them_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM_ANCHOR_LINK))

    def check_list_of_cookies_we_collect_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(LIST_OF_COOKIES_WE_COLLECT_ANCHOR_LINK))

    def check_online_account_registration_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(ONLINE_ACCOUNT_REGISTRATION_ANCHOR_LINK))

    def check_emails_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(EMAILS_ANCHOR_LINK))

    def check_acceptance_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(ACCEPTANCE_ANCHOR_LINK))

    def check_questions_for_luma_anchor_link_visibility(self):
        return bool(self.check_element_visibility_(QUESTIONS_FOR_LUMA_ANCHOR_LINK))
