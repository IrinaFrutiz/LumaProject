import allure

from base.base_page import BasePage
from data.links import LOGIN_URL

FIELD_EMAIL = ('id', 'email')
FIELD_PASSWORD = ('id', 'pass')
BTN_SING_IN = ('id', 'send2')


class LoginPage(BasePage):
    URL = LOGIN_URL

    @allure.step("User login to the system")
    def user_login(self):
        self.field_form(FIELD_EMAIL, "balblabla@email.com")
        self.field_form(FIELD_PASSWORD, "balblabla@email.com123!")
        self.click_button(BTN_SING_IN)
