import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from pages.basic_elements import BasicElements
from pages.footer_page import FooterPage
from pages.men_page import MenPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.product_page import ProductPage
from pages.corporation_list_page import CorporationListPage
from pages.cart_page import CartPage
from pages.wish_list_page import WishListPage
from pages.women_tops_trees_page import WomenTopsTreesPage
from pages.mini_cart_page import MiniCartPage


class BaseTest:
    main_page: MainPage
    login_page: LoginPage
    create_account_page: CreateAccountPage
    basic_elements: BasicElements
    footer_page: FooterPage
    privacy_policy_page: PrivacyPolicyPage
    product_page: ProductPage
    corporation_list_page: CorporationListPage
    cart_page: CartPage
    wish_list_page: WishListPage
    women_tops_trees_page: WomenTopsTreesPage
    men_page: MenPage
    mini_cart_page: MiniCartPage

    @pytest.fixture(autouse=True)
    def setup_method(self, request, browser):
        request.cls.browser = browser
        request.cls.main_page = MainPage(browser)
        request.cls.login_page = LoginPage(browser)
        request.cls.create_account_page = CreateAccountPage(browser)
        request.cls.basic_elements = BasicElements(browser)
        request.cls.footer_page = FooterPage(browser)
        request.cls.privacy_policy_page = PrivacyPolicyPage(browser)
        request.cls.product_page = ProductPage(browser)
        request.cls.corporation_list_page = CorporationListPage(browser)
        request.cls.cart_page = CartPage(browser)
        request.cls.wish_list_page = WishListPage(browser)
        request.cls.women_tops_trees_page = WomenTopsTreesPage(browser)
        request.cls.men_page = MenPage(browser)
        request.cls.mini_cart_page = MiniCartPage(browser)
