from base.base_page import BasePage
from data.links import CREATE_ACCOUNT_URL
import allure

FIELD_FIRST_NAME = ('id', 'firstname')
FIELD_LAST_NAME = ('id', 'lastname')
FIELD_EMAIL = ('id', 'email_address')
FIELD_PASSWORD = ('id', 'password')
FIELD_PASSWORD_CONFIRMATION = ('id', 'password-confirmation')
BTN_CREATE_AN_ACCOUNT = ('xpath', '//button[@title="Create an Account"]')


class CreateAccountPage(BasePage):
    URL = CREATE_ACCOUNT_URL

    @allure.step("Create a new user")
    def field_user_info(self):
        self.field_form(FIELD_FIRST_NAME, "Name")
        self.field_form(FIELD_LAST_NAME, "Name")
        self.field_form(FIELD_EMAIL, "balblabla@email.com")
        self.field_form(FIELD_PASSWORD, "balblabla@email.com123!")
        self.field_form(FIELD_PASSWORD_CONFIRMATION, "balblabla@email.com123!")
        self.click_button(BTN_CREATE_AN_ACCOUNT)

    @allure.step("Check Create An Account Button Displays")
    def check_btn_create_an_account_displays(self):
        return bool(self.check_element_visibility_(BTN_CREATE_AN_ACCOUNT))
