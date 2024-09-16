import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from pages.basic_elements import BasicElements
from pages.footer_page import FooterPage
from pages.privacy_policy_page import PrivacyPolicyPage


class BaseTest:
    main_page: MainPage
    login_page: LoginPage
    create_account_page: CreateAccountPage
    basic_elements: BasicElements
    footer_page: FooterPage
    privacy_policy_page: PrivacyPolicyPage

    @pytest.fixture(autouse=True)
    def setup_method(self, request, browser):
        request.cls.browser = browser
        request.cls.main_page = MainPage(browser)
        request.cls.login_page = LoginPage(browser)
        request.cls.create_account_page = CreateAccountPage(browser)
        request.cls.basic_elements = BasicElements(browser)
        request.cls.footer_page = FooterPage(browser)
        request.cls.privacy_policy_page = PrivacyPolicyPage(browser)
